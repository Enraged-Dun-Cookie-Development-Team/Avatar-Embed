from pathlib import Path
from PIL import Image
from PIL.Image import Image as PILImage

TEST_ASSET_PATH = Path(__file__).parent / "assets"

def load_pic_file(mock_pic_name: str) -> PILImage:
    """加载图片文件

    Args:
        path: 图片文件的路径

    Returns:
        PIL.Image.Image
    """
    return Image.open(TEST_ASSET_PATH / mock_pic_name).convert("RGBA")
