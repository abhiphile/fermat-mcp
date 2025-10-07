import matplotlib

matplotlib.use("Agg")
import pytest
from collections.abc import Sequence
from fastmcp.utilities.types import Image as FastImage

from fmcp.mpl_mcp.core.plot_chart import plot_chart


def test_plot_chart_line_and_png():
    x = [0.0, 1.0, 2.0, 3.0]
    y = [0.0, 1.0, 4.0, 9.0]
    img = plot_chart(x, y, plot_type="line", title="test", figsize=[6, 4])
    assert isinstance(img, FastImage)
    assert isinstance(img.data, (bytes, bytearray))
    assert img.data[:8] == b"\x89PNG\r\n\x1a\n"


def test_plot_chart_scatter_and_bar_and_invalid():
    x = [0.0, 1.0, 2.0, 3.0]
    y = [1.0, 3.0, 2.0, 5.0]

    img_scatter = plot_chart(x, y, plot_type="scatter", figsize=[6, 4])
    assert isinstance(img_scatter, FastImage)
    assert img_scatter.data is not None
    assert img_scatter.data[:8] == b"\x89PNG\r\n\x1a\n"

    img_bar = plot_chart(x, y, plot_type="bar", figsize=[6, 4])
    assert isinstance(img_bar, FastImage)
    assert img_bar.data is not None
    assert img_bar.data[:8] == b"\x89PNG\r\n\x1a\n"

    with pytest.raises(ValueError):
        plot_chart([float(val) for val in x], [float(val) for val in y], plot_type="unknown", figsize=[6, 4])
