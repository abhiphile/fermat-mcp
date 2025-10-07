from typing import List, Optional, Union
import matplotlib.pyplot as plt
import numpy as np
import io
from fastmcp.utilities.types import Image


def plot_stem(
    x_data: Union[List[Union[float, int]], List[List[Union[float, int]]]],
    y_data: Union[List[Union[float, int]], List[List[Union[float, int]]]],
    labels: Optional[Union[str, List[str]]] = None,
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    colors: Union[str, List[str]] = "blue",
    linefmt: str = "-",
    markerfmt: str = "o",
    basefmt: str = "k-",
    bottom: float = 0.0,
    orientation: str = "vertical",  # "vertical" or "horizontal"
    dpi: int = 200,
    figsize: Optional[List[Union[int, float]]] = None,
    grid: bool = True,
    legend: bool = False,
) -> Image:
    """
    Create a stem plot (vertical or horizontal) with customizable appearance.

    Args:
        x_data: X-axis data points (1D array-like)
        y_data: Y-axis data points (1D or 2D array-like for multiple series)
        labels: Label or list of labels for the data series
        title: Plot title
        xlabel: Label for the x-axis
        ylabel: Label for the y-axis
        colors: Color or list of colors for the stems and markers
        linefmt: Line style for the stems (default: "-" for solid line)
        markerfmt: Marker style for the points (default: "o" for circles)
        basefmt: Format of the baseline (default: "k-" for black line)
        bottom: Position of the baseline (default: 0.0)
        orientation: "vertical" or "horizontal" (default: "vertical")
        dpi: Output image resolution (dots per inch, default: 200)
        figsize: Figure size as (width, height) in inches.
        grid: Whether to show grid lines (default: True)
        legend: Whether to show legend (default: False)

    Returns:
        FastMCP Image object with the plotted stem chart
    """
    # Convert inputs to numpy arrays with explicit float type
    x = np.asarray(x_data, dtype=float)
    y = np.asarray(y_data, dtype=float)

    # Handle 1D y_data case by adding an extra dimension
    if y.ndim == 1:
        y = y.reshape(1, -1)

    # Ensure x matches the number of data points in y
    if x.ndim == 1 and len(x) != y.shape[1]:
        x = np.tile(x, (y.shape[0], 1))

    # Handle labels — normalize to a list
    if labels is None:
        labels_list: List[str] = [""] * y.shape[0]
    elif isinstance(labels, str):
        labels_list = [labels]
    else:
        labels_list = list(labels)

    # Handle colors — normalize to a list
    if isinstance(colors, str):
        colors_list = [colors] * y.shape[0]
    else:
        colors_list = list(colors)

    # Create figure with specified size using OO interface
    # Normalize figsize
    if figsize and len(figsize) >= 2:
        figsize_vals = (float(figsize[0]), float(figsize[1]))
    else:
        figsize_vals = (6.0, 4.0)

    fig, ax = plt.subplots(figsize=figsize_vals, dpi=dpi)

    # Create the stem plot for each series
    # Create the stem plot for each series
    for i in range(y.shape[0]):
        current_label = labels_list[i] if i < len(labels_list) else f"Series {i+1}"
        current_color = colors_list[i % len(colors_list)]

        # Create the stem plot
        if orientation == "vertical":
            markerline, stemlines, baseline = ax.stem(
                x[i] if x.ndim > 1 else x,
                y[i],
                linefmt=linefmt,
                markerfmt=markerfmt,
                basefmt=basefmt,
                bottom=bottom,
                label=current_label,
            )
        else:  # horizontal
            markerline, stemlines, baseline = ax.stem(
                y[i],
                x[i] if x.ndim > 1 else x,
                linefmt=linefmt,
                markerfmt=markerfmt,
                basefmt=basefmt,
                bottom=bottom,
                label=current_label,
                orientation="horizontal",
            )

        # Set the color for this series
        plt.setp(stemlines, "color", current_color)
        plt.setp(markerline, "color", current_color)
        plt.setp(baseline, "color", "black")

    # Customize the plot
    ax.set_title(title)
    ax.set_xlabel(xlabel if orientation == "vertical" else ylabel)
    ax.set_ylabel(ylabel if orientation == "vertical" else xlabel)

    if grid:
        ax.grid(True, linestyle="--", alpha=0.7)

    if legend and any(labels_list):
        ax.legend()

    # Save the plot to a buffer and close the figure
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)

    return Image(data=buf.read(), format="png")
