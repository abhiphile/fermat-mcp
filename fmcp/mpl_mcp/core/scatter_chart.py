from typing import List, Optional, Union
import matplotlib.pyplot as plt
import io
import numpy as np
from fastmcp.utilities.types import Image


def plot_scatter(
    x_data: List[float],
    y_data: List[float],
    labels: Optional[Union[str, List[str]]] = None,
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    color: Union[str, List[str]] = "blue",
    size: Union[int, float, List[float]] = 36,
    alpha: float = 0.7,
    marker: str = "o",
    edgecolors: Optional[str] = "face",
    linewidths: float = 1.0,
    save: bool = False,
    dpi: int = 200,
    figsize: Optional[List[int]] = None,
    grid: bool = True,
    legend: bool = False,
) -> Image:
    """
    Create a scatter plot with customizable appearance.

    Args:
        x_data: X-axis data points (1D or 2D sequence for multiple series)
        y_data: Y-axis data points (1D or 2D sequence for multiple series)
        labels: Label or list of labels for the data series
        title: Plot title
        xlabel: Label for the x-axis
        ylabel: Label for the y-axis
        color: Color or list of colors for the markers (default: "blue")
        size: Size or list of sizes for the markers (default: 36)
        alpha: Alpha transparency (0-1, default: 0.7)
        marker: Marker style (default: "o" for circle)
        edgecolors: Color of marker edges (default: "face")
        linewidths: Width of marker edges (default: 1.0)
        save: If True, save the figure to a buffer
        dpi: Output image resolution (dots per inch, default: 200)
        figsize: Figure size as (width, height) in inches
        grid: Whether to show grid lines (default: True)
        legend: Whether to show legend (default: False)

    Returns:
        FastMCP Image object with the plotted scatter chart
    """
    # Convert inputs to numpy arrays for processing
    x = np.asarray(x_data, dtype=float)
    y = np.asarray(y_data, dtype=float)

    # Ensure y is at least 2D
    if y.ndim == 1:
        y = y.reshape(-1, 1)

    # Ensure x is 1D and matches the number of data points in y
    x = np.asarray(x_data, dtype=float).flatten()
    if len(x) != y.shape[0]:
        x = np.tile(x, (y.shape[1], 1)).T.flatten()
        y = y.T.reshape(-1, y.shape[0]).T

    # Handle labels
    if labels is None:
        labels = [""] * y.shape[1]
    elif isinstance(labels, str):
        labels = [labels]

    # Handle colors
    if isinstance(color, str):
        color = [color] * y.shape[1]

    # Handle sizes
    if isinstance(size, (int, float)):
        size = [size] * y.shape[1]

    # Create figure with specified size
    fig, ax = plt.subplots(figsize=(figsize[0], figsize[1]), dpi=dpi)

    # Create the scatter plot for each series
    for i in range(y.shape[1]):
        current_label = labels[i] if i < len(labels) else f"Series {i+1}"
        current_color = color[i % len(color)]
        current_size = (
            size[i % len(size)] if isinstance(size, (list, np.ndarray)) else size
        )

        ax.scatter(
            x,
            y[:, i],
            label=current_label,
            c=current_color,
            s=current_size,
            alpha=alpha,
            marker=marker,
            edgecolors=edgecolors,
            linewidths=linewidths,
        )

    # Customize the plot
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if grid:
        ax.grid(True)

    if legend and any(labels):
        ax.legend()

    # Save to buffer and return
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return Image(data=buf.read(), format="png")
