from typing import Literal, cast
from pathlib import Path
import re
import click

from avatar_embed.load import load_pic_file, load_pic_url
from avatar_embed.save import save_file
from avatar_embed.embed import embed as _embed

PosType = Literal["top-left", "top-right", "bottom-left", "bottom-right"]

pos_map: dict[str, PosType] = {
    "tl": "top-left",
    "tr": "top-right",
    "bl": "bottom-left",
    "br": "bottom-right",
}

SIZE_PATTERN = re.compile(r"(\d+)x(\d+)")
URL_PATTERN = re.compile(r"https?://")

# avaemb <avatar_path> --embed <label_path> --pos <label_pos> --size <label_size> --output <output_size> --save <save_path> # noqa: E501
@click.command("avaemb")
@click.argument("avatar_path", type=str)
@click.option(
    "--embed", "-e", type=click.Path(exists=True), required=True, help="角标文件/URL"
)
@click.option(
    "--pos",
    "-p",
    type=click.Choice(["tl", "tr", "bl", "br"]),
    default="br",
    help="角标位置, tl: 左上, tr: 右上, bl: 左下, br: 右下",
)
@click.option(
    "--size", "-s", type=float, default=0.25, help="角标大小, 相对于头像的比例"
)
@click.option(
    "--output",
    "-o",
    type=str,
    default="64x64",
    help="输出图片的大小, 格式:宽x高",
)
@click.option(
    "--save",
    "-S",
    type=click.Path(),
    required=False,
    help="保存图片的路径, 默认为当前目录的同名.embed.png",
)
def avaemb(
    avatar_path: str,
    embed: str,
    pos: str,
    size: float,
    output: str,
    save: Path,
):
    is_url_avatar = False

    if URL_PATTERN.match(avatar_path):
        is_url_avatar = True
        avatar = load_pic_url(avatar_path)
    else:
        if (ap := Path(avatar_path)).exists():
            avatar = load_pic_file(ap)
        else:
            click.Abort(f"头像文件不存在: {avatar_path}")
            return

    if URL_PATTERN.match(embed):
        label = load_pic_file(embed)
    else:
        if (ep := Path(embed)).exists():
            label = load_pic_file(ep)
        else:
            click.Abort(f"角标文件不存在: {embed}")
            return

    size_tuple = SIZE_PATTERN.match(output)
    if not size_tuple:
        raise ValueError(f"无效的输出图片大小: {output}")
    size_tuple = tuple(map(int, size_tuple.groups()))
    size_tuple = cast(tuple[int, int], size_tuple)
    avatar = _embed(avatar, label, pos_map[pos], size, size_tuple)

    if save:
        save_file(avatar, save)
    else:
        if is_url_avatar:
            save_file(avatar, Path.cwd() / f"{id(avatar_path)}.embed.png")
        else:
            save_file(
                avatar, Path.cwd() / Path(avatar_path).with_suffix(".embed.png").name
            )
