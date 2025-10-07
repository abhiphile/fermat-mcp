from typing import List, Optional, Literal
import matplotlib.pyplot as plt
import io
from fastmcp.utilities.types import Image
from typing import Union


def plot_barchart(
    values: List[Union[float, int]],
    labels: Optional[List[str]] = None,
    title: str = "",
    xlabel: str = "",
    ylabel: str = "",
    color: str = "skyblue",
    save: bool = False,
    dpi: int = 200,
    orientation: Literal["vertical", "horizontal"] = "vertical",
) -> Image:
    """
    Plot a bar chart (vertical or horizontal) with optional labels (defaults to empty strings).

    Args:
        values: List of bar heights (values: float or int)
        labels: List of bar labels (categories) or None for empty labels
        title: Plot title
        xlabel: Label for the x-axis
        ylabel: Label for the y-axis
        color: Color for the bars (default: "skyblue")
        save: If True, save the figure to a buffer
        dpi: Output image resolution (dots per inch, default: 100)
        orientation: "vertical" or "horizontal" (default: "vertical")
    Returns:
        FastMCP Image object with the plotted chart
    """
    plt.figure(dpi=dpi)
    if labels is None:
        labels = [""] * len(values)

    if orientation == "vertical":
        plt.bar(labels, values, color=color)
    else:
        plt.barh(labels, values, color=color)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=dpi)
    plt.close()
    buf.seek(0)
    return Image(data=buf.read(), format="png")
