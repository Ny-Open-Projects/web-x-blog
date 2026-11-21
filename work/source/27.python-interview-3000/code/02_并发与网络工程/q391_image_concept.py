"""纯标准库:解析 PNG 头、魔数校验、缩略草图概念。"""
import struct
from typing import Optional


MAGIC = {
    "png": b"\x89PNG\r\n\x1a\n",
    "jpeg": b"\xff\xd8\xff",
    "gif": b"GIF8",
}


def detect_format(data: bytes) -> Optional[str]:
    """按魔数识别格式, 而不是相信扩展名。

    注: 返回类型若写成 str | None(PEP 604)在 3.10 以下运行时会
    TypeError, 纯注解场景可用 from __future__ import annotations 规避。
    """
    for name, magic in MAGIC.items():
        if data.startswith(magic):
            return name
    return None


def png_size(data: bytes):
    """PNG 第一个 chunk 是 IHDR: 8字节签名 + 4长度 + 4类型 + 宽高各4字节。"""
    if detect_format(data) != "png":
        raise ValueError("not a png")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


if __name__ == "__main__":
    # 手工构造一个 3x2 的最小合法 PNG 头片段用于演示
    ihdr = struct.pack(">IIBBBBB", 3, 2, 8, 2, 0, 0, 0)
    fake_png = MAGIC["png"] + struct.pack(">I", 13) + b"IHDR" + ihdr
    print("格式:", detect_format(fake_png))
    print("尺寸:", png_size(fake_png))
    # 把图片转 base64 嵌入 HTML/JSON 的做法(概念演示)
    import base64
    data_url = "data:image/png;base64," + base64.b64encode(fake_png).decode()
    print("data url:", data_url[:50], "...")
