import matplotlib

matplotlib.use("Agg")
from fastmcp.utilities.types import Image as FastImage

from fmcp.mpl_mcp.core.scatter_chart import plot_scatter


def test_scatter_basic_png():
    x = [0.0, 1.0, 2.0]
    y = [0.0, 1.0, 4.0]
    img = plot_scatter(x, y, title="s", figsize=[4, 3])
    assert isinstance(img, FastImage)
    assert img.data is not None
    assert img.data[:8] == b"\x89PNG\r\n\x1a\n"
