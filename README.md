# Avatar Embed

Usage: python -m avatar_embed [OPTIONS] AVATAR_PATH

Options:
  -e, --embed PATH         角标文件  [required]
  -p, --pos [tl|tr|bl|br]  角标位置, tl: 左上, tr: 右上, bl: 左下, br: 右下
  -s, --size FLOAT         角标大小, 相对于头像的比例
  -o, --output TEXT        输出图片的大小, 格式:宽x高
  -S, --save PATH          保存图片的路径, 默认为当前目录的同名.embed.png
  --help                   Show this message and exit.
