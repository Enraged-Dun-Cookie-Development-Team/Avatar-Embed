from pathlib import Path
from PIL.Image import Image

def save_file(image: Image, path: Path | str):
    image.save(path)
