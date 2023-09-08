from .utils import load_pic_file


def test_embed():
    from avatar_embed.embed import embed

    avatar = load_pic_file("avatar.png")
    label = load_pic_file("label.png")

    res = embed(
        avatar, label, label_size=0.25, pos="bottom-right", output_size=(64, 64)
    )

    res.show()
