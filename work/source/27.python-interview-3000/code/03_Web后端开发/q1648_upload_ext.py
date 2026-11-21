"""扩展名不可信: 同一个 .png 文件名可以装任何内容(纯标准库)。"""
import os

# 客户端提交的两个"图片", 名字都叫 .png
FILES = {
    "avatar.png": b"\x89PNG\r\n\x1a\n" + b"real-pixel-data",      # 真 PNG 魔数
    "shell.png": b"<?php system($_GET['c']); ?>" + b"\x00" * 8,   # 名字骗人
}

for name, data in FILES.items():
    ext = os.path.splitext(name)[1].lower()
    claimed = {"png": "图片", "jpg": "图片"}.get(ext, "未知")
    starts_png = data.startswith(b"\x89PNG")
    print(f"{name}: 扩展名说它是{claimed}, 内容是 PNG 吗 -> {starts_png}")
print("结论: 扩展名与 Content-Type 都由客户端控制, 只能当提示, 不能当依据")
print("上传存储目录必须不可执行, 提供下载时用固定 Content-Type, 防止服务端解析执行")
