from typing import Literal
from PIL.Image import Image


def embed(
    avatar: Image,
    label: Image,
    pos: Literal[
        "top-left", "top-right","bottom-left", "bottom-right"
    ] = "bottom-right",
    label_size: float = 0.25,
    output_size: tuple[int, int] = (128, 128),
) -> Image:
    """将角标嵌入头像中的某个角落

    Args:
        avatar: 需要嵌入角标的头像
        label: 角标
        pos: 角标嵌入的位置
            可选值为 "top-left", "top-right", "bottom-left", "bottom-right"
            默认为 "bottom-right"
        label_size: 角标的大小，相对于头像的比例

    Returns:
        镶嵌了角标的头像
    """
    avatar_width, avatar_height = avatar.size
    label_ratio = label.width / label.height
    label_width, label_height = (
        int(avatar_width * label_size * label_ratio),
        int(avatar_height * label_size),
    )
    label = label.resize((label_width, label_height))
    match pos:
        case "top-left":
            avatar.paste(label, (0, 0), label)
        case "top-right":
            avatar.paste(label, (avatar_width - label_width, 0), label)
        case "bottom-left":
            avatar.paste(label, (0, avatar_height - label_height), label)
        case "bottom-right":
            avatar.paste(
                label,
                (avatar_width - label_width, avatar_height - label_height),
                label
            )

    return avatar.resize(output_size)
