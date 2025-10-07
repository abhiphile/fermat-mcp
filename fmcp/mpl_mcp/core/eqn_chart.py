import numpy as np
import matplotlib.pyplot as plt
from typing import Union, List
import re
import io
from pydantic import BaseModel, ConfigDict
from fastmcp.utilities.types import Image


class PlotConfig(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    # This allows NumPy arrays and other arbitrary types


def eqn_chart(
    equations: Union[str, List[str]],
    x_min: Union[float, int] = -10.0,
    x_max: Union[float, int] = 10.0,
    num_points: Union[int, float] = 1000,
    title: str = "Equation Plot",
    xlabel: str = "x",
    ylabel: str = "y",
    grid: bool = True,
    legend: bool = True,
    figsize: List[Union[int, float]] = [10, 6],
    linewidth: Union[float, int] = 2.0,
    linestyle: str = "-",
    alpha: Union[float, int] = 1.0,
    dpi: Union[int, float] = 200,
    save: bool = False,
) -> Image:
    """
    Plot one or more mathematical equations on the same chart.

    Args:
        equations: Single equation string or list of equation strings (e.g., "x**2" or ["x**2", "sin(x)"])
        x_min: Minimum x-value for the plot
        x_max: Maximum x-value for the plot
        num_points: Number of points to generate for the plot
        title: Title of the plot
        xlabel: Label for the x-axis
        ylabel: Label for the y-axis
        grid: Whether to show grid lines
        legend: Whether to show legend
        figsize: Figure size (width, height) in inches
        linewidth: Width of the plot lines
        linestyle: Style of the plot lines
        alpha: Transparency of the plot lines
        dpi: Dots per inch for the output image
        save: If True, save the figure to a buffer

    Returns:
        Image: The image object containing the plot
    """
    # Create a config instance to allow arbitrary types
    _ = PlotConfig()

    # Rest of your function remains the same
    if isinstance(equations, str):
        equations = [equations]

    fig, ax = plt.subplots(figsize=(float(figsize[0]), float(figsize[1])), dpi=int(dpi))
    x = np.linspace(float(x_min), float(x_max), int(num_points))

    for eq in equations:
        eq_py = eq.replace("^", "**")
        eq_py = re.sub(r"(\W|^)([a-z]+)\(", r"\1np.\2(", eq_py)

        try:
            y = eval(
                eq_py,
                {
                    "x": x,
                    "np": np,
                    "sin": np.sin,
                    "cos": np.cos,
                    "tan": np.tan,
                    "exp": np.exp,
                    "log": np.log,
                    "sqrt": np.sqrt,
                    "pi": np.pi,
                    "e": np.e,
                },
            )

            # Convert numpy arrays to lists for Pydantic compatibility
            if isinstance(y, np.ndarray):
                y = y.tolist()

            ax.plot(
                x,
                y,
                label=f"y = {eq}",
                linewidth=float(linewidth),
                linestyle=linestyle,
                alpha=float(alpha),
            )

        except Exception as e:
            print(f"Error plotting equation '{eq}': {str(e)}")
            continue

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid)

    if (len(equations) > 1 or legend) and any(ax.lines):
        ax.legend()

    plt.tight_layout()

    # Always save to buffer for the return value
    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=int(dpi))
    plt.close()
    buf.seek(0)

    # If save is True, also save to a file
    if save:
        with open("equation_plot.png", "wb") as f:
            f.write(buf.getvalue())
        buf.seek(0)  # Reset buffer position after reading

    return Image(data=buf.read(), format="png")
