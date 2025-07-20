from typing import Union, Literal, get_args, Dict, Any
from sympy import (
    Interval as _Interval,
    FiniteSet as _FiniteSet,
    Union as _Union,
    Intersection as _Intersection,
    sympify,
    S,
    Basic,
)
from sympy.sets import Set

# Define operation types for type hints
SetOperation = Literal[
    "finiteset",
    "interval",
    "union",
    "intersection",
    "issubset",
    "issuperset",
    "contains",
    "cardinality",
]


def _parse_set_elements(elements):
    """Parse elements for finite sets."""
    if isinstance(elements, (list, tuple)):
        return [sympify(x) for x in elements]
    elif isinstance(elements, str):
        if elements.startswith("{") and elements.endswith("}"):
            elements = elements[1:-1]
        return [sympify(x.strip()) for x in elements.split(",") if x.strip()]
    return [sympify(elements)]


def _parse_interval_args(args: Dict[str, Any]) -> Dict[str, Any]:
    """Parse arguments for interval creation."""
    parsed = {}
    for key in ["start", "end", "left_open", "right_open"]:
        if key in args:
            parsed[key] = sympify(args[key]) if key in ["start", "end"] else args[key]
    return parsed


def set_operation(operation: SetOperation, *args, **kwargs) -> Union[Set, bool, int]:
    """
    Unified interface for set operations.

    Args:
        operation: The set operation to perform. One of:
            - 'finiteset': Create a finite set
            - 'interval': Create an interval
            - 'union': Compute union of sets
            - 'intersection': Compute intersection of sets
            - 'issubset': Check if set is a subset
            - 'issuperset': Check if set is a superset
            - 'contains': Check if element is in set
            - 'cardinality': Get the cardinality of a set
        *args: Positional arguments for the operation
        **kwargs: Keyword arguments for the operation

    Returns:
        The result of the set operation, which could be a Set, bool, or int
        depending on the operation.

    Examples:
        >>> set_operation('finiteset', [1, 2, 3, 4])
        {1, 2, 3, 4}
        >>> set_operation('interval', start=0, end=1, left_open=True)
        Interval.open(0, 1)
        >>> A = set_operation('finiteset', [1, 2, 3])
        >>> B = set_operation('finiteset', [3, 4, 5])
        >>> set_operation('union', A, B)
        {1, 2, 3, 4, 5}
        >>> set_operation('contains', A, 2)
        True
        >>> set_operation('cardinality', A)
        3
    """
    # Handle finite set creation
    if operation == "finiteset":
        if not args and "elements" in kwargs:
            elements = kwargs["elements"]
        elif len(args) == 1 and not kwargs:
            elements = args[0]
        else:
            elements = list(args) + list(kwargs.values())

        return _FiniteSet(*_parse_set_elements(elements))

    # Handle interval creation
    elif operation == "interval":
        if args and len(args) == 2 and not kwargs:
            # Handle interval(0, 1) syntax
            start, end = map(sympify, args)
            left_open = kwargs.get("left_open", False)
            right_open = kwargs.get("right_open", False)
        else:
            # Handle keyword arguments
            params = _parse_interval_args(kwargs)
            start = params.get("start", S.NegativeInfinity)
            end = params.get("end", S.Infinity)
            left_open = params.get("left_open", False)
            right_open = params.get("right_open", False)

        if left_open and right_open:
            return _Interval.open(start, end)
        elif left_open:
            return _Interval.Lopen(start, end)
        elif right_open:
            return _Interval.Ropen(start, end)
        else:
            return _Interval(start, end)

    # Handle set operations
    elif operation in ("union", "intersection", "issubset", "issuperset"):
        if len(args) < 2:
            raise ValueError(f"At least two sets required for {operation}")

        # Convert args to SymPy sets if they aren't already
        sets = []
        for arg in args:
            if isinstance(arg, (list, tuple, str)):
                sets.append(set_operation("finiteset", arg))
            elif isinstance(arg, dict) and "start" in arg and "end" in arg:
                sets.append(set_operation("interval", **arg))
            elif isinstance(arg, (Set, Basic)):
                sets.append(arg)
            else:
                raise ValueError(f"Cannot convert {arg} to a set")

        if operation == "union":
            return _Union(*sets)
        elif operation == "intersection":
            return _Intersection(*sets)
        elif operation == "issubset":
            return sets[0].is_subset(*sets[1:])
        elif operation == "issuperset":
            return sets[0].is_superset(*sets[1:])

    # Handle element operations
    elif operation == "contains":
        if len(args) != 2:
            raise ValueError(
                "'contains' operation requires exactly 2 arguments (set, element)"
            )

        # First argument is the set, second is the element
        set_arg, element = args

        # Convert set_arg to a SymPy set if it isn't already
        if not isinstance(set_arg, (Set, Basic)):
            if isinstance(set_arg, (list, tuple, str)):
                set_obj = set_operation("finiteset", set_arg)
            elif isinstance(set_arg, dict) and "start" in set_arg and "end" in set_arg:
                set_obj = set_operation("interval", **set_arg)
            else:
                raise ValueError("First argument must be a set or convertible to a set")
        else:
            set_obj = set_arg

        # Convert element to a SymPy object if it isn't already
        if not isinstance(element, Basic):
            element = sympify(element)

        return element in set_obj

    # Handle cardinality
    elif operation == "cardinality":
        if not args:
            raise ValueError("No set provided for cardinality operation")

        set_arg = args[0]

        # Convert set_arg to a SymPy set if it isn't already
        if not isinstance(set_arg, (Set, Basic)):
            if isinstance(set_arg, (list, tuple, str)):
                set_obj = set_operation("finiteset", set_arg)
            elif isinstance(set_arg, dict) and "start" in set_arg and "end" in set_arg:
                set_obj = set_operation("interval", **set_arg)
            else:
                raise ValueError("Argument must be a set or convertible to a set")
        else:
            set_obj = set_arg

        return len(set_obj) if hasattr(set_obj, "__len__") else float("inf")

    else:
        valid_ops = get_args(SetOperation)
        raise ValueError(f"Invalid operation. Must be one of: {valid_ops}")


# Add type hints for better IDE support
set_operation.__annotations__["return"] = Union[Set, bool, int]
