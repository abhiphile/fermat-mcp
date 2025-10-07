import matplotlib

matplotlib.use("Agg")
from fastmcp.utilities.types import Image as FastImage

from fmcp.mpl_mcp.core.stack_chart import plot_stack


def test_stack_area_and_bar():
    x = [0.0, 1.0, 2.0]
    y = [[1.0, 2.0, 3.0], [2.0, 1.0, 0.0]]
    img_area = plot_stack(x, y, chart_type="area", figsize=[6, 4])
    assert isinstance(img_area, FastImage)
    assert img_area.data is not None, "img_area.data is None"
    assert img_area.data[:8] == b"\x89PNG\r\n\x1a\n"

    img_bar = plot_stack(x, y, chart_type="bar", figsize=[6, 4])
    assert isinstance(img_bar, FastImage)
    assert img_bar.data is not None, "img_bar.data is None"
    assert img_bar.data[:8] == b"\x89PNG\r\n\x1a\n"
