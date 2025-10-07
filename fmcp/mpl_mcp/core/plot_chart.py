from typing import List, Optional, Union
import matplotlib.pyplot as plt
import io
import numpy as np
from fastmcp.utilities.types import Image


def plot_chart(
    x_data: List[Union[float, int]],
    y_data: Union[List[Union[float, int]], List[List[Union[float, int]]]],
    plot_type: str = "line",  # "line", "scatter", or "bar"
    labels: Optional[Union[str, List[str]]] = None,
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    color: Union[str, List[str]] = "skyblue",
    save: bool = False,
    dpi: int = 200,
    figsize: Optional[List[Union[int, float]]] = None,
    grid: bool = True,
    legend: bool = False,
) -> Image:
    """
    Create a customizable plot with support for multiple plot types.

    Args:
        x_data: X-axis data points (1D array-like)
        y_data: Y-axis data points (1D or 2D array-like for multiple series)
        plot_type: Type of plot to create ("line", "scatter", or "bar")
        labels: Label or list of labels for the data series
        title: Plot title
        xlabel: Label for the x-axis
        ylabel: Label for the y-axis
        color: Color or list of colors for the plot elements
        save: If True, save the figure to a buffer
        dpi: Output image resolution (dots per inch, default: 200)
        figsize: List of width and height in inches
        grid: Whether to show grid lines
        legend: Whether to show legend


    Returns:
        FastMCP Image object with the plotted chart
    """
    # Convert inputs to numpy arrays for processing
    x = np.asarray(x_data, dtype=float)
    y = np.asarray(y_data, dtype=float)

    # Handle 1D y_data case by adding an extra dimension
    if y.ndim == 1:
        y = y.reshape(-1, 1)

    # Ensure x matches the number of data points in y
    if x.ndim == 1 and len(x) != y.shape[0]:
        x = np.tile(x, (y.shape[1], 1)).T

    # Handle labels — normalize to a list of strings
    if labels is None:
        labels_list: List[str] = [""] * y.shape[1]
    elif isinstance(labels, str):
        labels_list = [labels]
    else:
        labels_list = list(labels)

    # Handle colors
    if isinstance(color, str):
        color = [color] * y.shape[1]

    # Create figure with specified size using OO interface
    # Normalize figsize to a tuple of floats (matplotlib accepts floats or ints)
    if figsize and len(figsize) >= 2:
        figsize_vals = (float(figsize[0]), float(figsize[1]))
    else:
        figsize_vals = (6.0, 4.0)

    fig, ax = plt.subplots(figsize=figsize_vals, dpi=dpi)

    # Create the appropriate plot type
    for i in range(y.shape[1]):
        current_label = labels_list[i] if i < len(labels_list) else f"Series {i+1}"
        current_color = color[i % len(color)]

        if plot_type == "line":
            ax.plot(x, y[:, i], label=current_label, color=current_color)
        elif plot_type == "scatter":
            ax.scatter(x, y[:, i], label=current_label, color=current_color)
        elif plot_type == "bar":
            ax.bar(x, y[:, i], label=current_label, color=current_color)
        else:
            plt.close(fig)
            raise ValueError(f"Unsupported plot type: {plot_type}")

    # Customize the plot
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

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
