from pathlib import Path
from httpx import Client
from PIL import Image

def load_pic_file(path: Path | str) -> Image.Image:
    """加载图片文件

    Args:
        path: 图片文件的路径

    Returns:
        图片
    """
    return Image.open(path).convert("RGBA")

def load_pic_url(url: str) -> Image.Image:
    """加载图片 URL

    Args:
        url: 图片 URL

    Returns:
        图片
    """
    with Client() as client:
        resp = client.get(url)
        return Image.open(resp.content).convert("RGBA")
