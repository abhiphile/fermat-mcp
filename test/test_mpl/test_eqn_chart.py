import matplotlib

matplotlib.use("Agg")
from fastmcp.utilities.types import Image as FastImage

from fmcp.mpl_mcp.core.eqn_chart import eqn_chart


def test_eqn_chart_single_and_multiple():
    img1 = eqn_chart("x**2", x_min=0, x_max=2, num_points=50, dpi=80)
    assert isinstance(img1, FastImage)
    assert img1.data is not None, "eqn_chart returned FastImage with None data"
    assert img1.data[:8] == b"\x89PNG\r\n\x1a\n"

    img2 = eqn_chart(["x", "x**2"], x_min=0, x_max=3, num_points=30, dpi=80)
    assert isinstance(img2, FastImage)
    assert img2.data is not None, "eqn_chart returned FastImage with None data for multiple equations"
    assert img2.data[:8] == b"\x89PNG\r\n\x1a\n"
