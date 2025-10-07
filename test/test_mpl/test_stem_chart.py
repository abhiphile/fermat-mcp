import matplotlib

matplotlib.use("Agg")
from fastmcp.utilities.types import Image as FastImage

from fmcp.mpl_mcp.core.stem_chart import plot_stem


def test_stem_vertical_and_horizontal():
    x = [0, 1, 2]
    y = [1, 3, 2]
    img_v = plot_stem(x, y, orientation="vertical", figsize=[5, 4])
    assert isinstance(img_v, FastImage)
    assert img_v.data[:8] == b"\x89PNG\r\n\x1a\n"

    img_h = plot_stem(x, y, orientation="horizontal", figsize=[5, 4])
    assert isinstance(img_h, FastImage)
    assert img_h.data[:8] == b"\x89PNG\r\n\x1a\n"
