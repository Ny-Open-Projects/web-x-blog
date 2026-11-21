import hashlib
import os
import re

ALLOWED_EXT = {".png", ".jpg", ".pdf"}
MAGIC = {b"\x89PNG\r\n\x1a\n": "png", b"%PDF-": "pdf", b"\xff\xd8\xff": "jpg"}

def safe_name(filename: str) -> str:
    base = os.path.basename(filename)               # 防路径穿越
    base = re.sub(r"[^A-Za-z0-9._-]", "_", base)
    return base[:64] or "upload.bin"

def sniff_and_check(data: bytes, filename: str) -> str:
    ext = os.path.splitext(safe_name(filename))[1].lower()
    if ext not in ALLOWED_EXT:
        raise ValueError("扩展名不允许")
    for magic, kind in MAGIC.items():
        if data.startswith(magic):
            if kind != ext.lstrip("."):
                raise ValueError("魔数与扩展名不符")
            digest = hashlib.sha256(data).hexdigest()[:12]
            return f"/store/{digest}.{kind}"        # 内容寻址的随机存储名
    raise ValueError("文件内容不是允许的类型")

print(sniff_and_check(b"\x89PNG\r\n\x1a\nxxxx", "../../etc/passwd.png"))
print(safe_name("../../etc/passwd.png"))
try:
    sniff_and_check(b"MZ fake exe", "evil.png")
except ValueError as e:
    print("拦截:", e)
