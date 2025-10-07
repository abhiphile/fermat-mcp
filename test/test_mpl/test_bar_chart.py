import matplotlib

matplotlib.use("Agg")
from fastmcp.utilities.types import Image as FastImage

from fmcp.mpl_mcp.core.bar_chart import plot_barchart


def test_bar_chart_vertical_and_horizontal():
    values = [1.0, 3.0, 2.0]
    labels = ["a", "b", "c"]

    img_v = plot_barchart(
        values, labels=labels, orientation="vertical", title="v", dpi=100
    )
    assert isinstance(img_v, FastImage)
    assert img_v.data is not None
    assert img_v.data[:8] == b"\x89PNG\r\n\x1a\n"

    img_h = plot_barchart(
        values, labels=labels, orientation="horizontal", title="h", dpi=100
    )
    assert isinstance(img_h, FastImage)
    assert img_h.data is not None
    assert img_h.data[:8] == b"\x89PNG\r\n\x1a\n"
