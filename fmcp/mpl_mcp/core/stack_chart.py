from typing import List, Optional, Union
import matplotlib.pyplot as plt
import numpy as np
import io
from fastmcp.utilities.types import Image


def plot_stack(
    x_data: Union[List[Union[float, int]], List[List[Union[float, int]]]],
    y_data: Union[List[List[Union[float, int]]], List[Union[float, int]]],
    chart_type: str = "area",  # "area" or "bar"
    labels: Optional[List[str]] = None,
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    colors: Optional[Union[str, List[str]]] = None,
    alpha: float = 0.7,
    dpi: int = 200,
    figsize: Optional[List[Union[int, float]]] = None,
    grid: bool = True,
    legend: bool = True,
) -> Image:
    """
    Create a stacked area or bar chart.

    Args:
        x_data: X-axis data points (1D array-like)
        y_data: 2D array-like where each row represents a series to be stacked
        chart_type: Type of chart to create ("area" or "bar")
        labels: List of labels for the data series
        title: Plot title
        xlabel: Label for the x-axis
        ylabel: Label for the y-axis
        colors: Color or list of colors for the areas/bars
        alpha: Alpha transparency (0-1, default: 0.7)
        dpi: Output image resolution (dots per inch, default: 200)
        figsize: Figure size as (width, height) in inches
        grid: Whether to show grid lines (default: True)
        legend: Whether to show legend (default: True)

    Returns:
        FastMCP Image object with the plotted stack chart
    """
    # Convert inputs to numpy arrays with explicit float type
    x = np.asarray(x_data, dtype=float)
    y = np.asarray(y_data, dtype=float)

    # Ensure y_data is 2D
    if y.ndim == 1:
        y = y.reshape(1, -1)

    # Handle labels
    if labels is None:
        labels_list = [f"Series {i+1}" for i in range(y.shape[0])]
    elif isinstance(labels, str):
        labels_list = [labels]
    else:
        labels_list = list(labels)

    # Handle colors
    if colors is None:
        # Default color cycle
        default_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
        colors = [default_colors[i % len(default_colors)] for i in range(y.shape[0])]
    elif isinstance(colors, str):
        colors = [str(colors)] * y.shape[0]
    elif isinstance(colors, list):
        # If the list is empty or contains None, use default colors
        if not colors or all(c is None for c in colors):
            default_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
            colors = [default_colors[i % len(default_colors)] for i in range(y.shape[0])]
        else:
            # Filter out None values and ensure all elements are strings
            default_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
            colors = [str(c) if c is not None else default_colors[i % len(default_colors)] for i, c in enumerate(colors)]
            # If colors list is shorter than y.shape[0], repeat colors
            if len(colors) < y.shape[0]:
                colors += [default_colors[i % len(default_colors)] for i in range(len(colors), y.shape[0])]
    else:
        colors = [str(colors)] * y.shape[0]

    # Ensure colors is always a list for safe usage of len(colors)
    if not isinstance(colors, list):
        colors = [str(colors)] * y.shape[0]
    # If colors is still None (edge case), set to default colors
    if colors is None:
        default_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
        colors = [default_colors[i % len(default_colors)] for i in range(y.shape[0])]

    # Create figure with specified size using OO interface
    # Normalize figsize
    if figsize and len(figsize) >= 2:
        figsize_vals = (float(figsize[0]), float(figsize[1]))
    else:
        figsize_vals = (8.0, 6.0)

    fig, ax = plt.subplots(figsize=figsize_vals, dpi=dpi)

    # Calculate the cumulative sum for stacking
    y_stack = np.cumsum(y, axis=0)

    # Create the stacked chart
    for i in range(y.shape[0] - 1, -1, -1):
        if i == 0:
            y_plot = y_stack[i]
            y_bottom = np.zeros_like(x)
        else:
            y_plot = y_stack[i] - y_stack[i - 1]
            y_bottom = y_stack[i - 1]

        if chart_type == "area":
            ax.fill_between(
                x,
                y_bottom,
                y_stack[i],
                label=labels_list[i] if i < len(labels_list) else f"Series {i+1}",
                color=colors[i % len(colors)],
                alpha=alpha,
                edgecolor="none",
            )
        elif chart_type == "bar":
            ax.bar(
                x,
                y_plot,
                bottom=y_bottom,
                label=labels_list[i] if i < len(labels_list) else f"Series {i+1}",
                color=colors[i % len(colors)],
                alpha=alpha,
                edgecolor="none",
                width=0.8 if len(x) > 1 else 0.8 * (x[1] - x[0]) if len(x) > 1 else 0.8,
            )

    # Customize the plot
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if grid:
        ax.grid(True, linestyle="--", alpha=0.7)

    if legend:
        ax.legend()

    plt.tight_layout()

    # Save the plot to a buffer and close the figure
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)

    return Image(data=buf.read(), format="png")
