"""魔数白名单 + 扩展名白名单的双校验落地(纯标准库)。"""

MAGIC = [
    (b"\x89PNG\r\n\x1a\n", "png"),
    (b"\xff\xd8\xff", "jpg"),
    (b"%PDF-", "pdf"),
    (b"PK\x03\x04", "zip"),
]
EXT_WHITELIST = {"png", "jpg"}


def sniff(data):
    for magic, kind in MAGIC:
        if data.startswith(magic):
            return kind
    return None


def accept(filename, data):
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in EXT_WHITELIST:
        return False, f"扩展名 {ext or '缺失'} 不在白名单"
    kind = sniff(data)
    if kind is None:
        return False, "魔数不认识, 拒绝"
    if ext != kind:
        return False, f"扩展名 {ext} 与魔数 {kind} 不一致"
    return True, f"{kind} 双校验通过"


samples = [
    ("a.png", b"\x89PNG\r\n\x1a\n" + b"x" * 10),
    ("b.jpg", b"\xff\xd8\xff" + b"y" * 10),
    ("c.png", b"PK\x03\x04" + b"z" * 10),          # zip 改名 png
    ("d.svg", b"<svg xmlns='x'>"),                  # 扩展名不在白名单
    ("e.png", b"GIF89a" + b"w" * 10),               # GIF 冒充 png
]
for name, data in samples:
    ok, why = accept(name, data)
    print(f"{name}: {'收' if ok else '拒'} - {why}")
print("要点: 双校验只看文件头仍不完美, 多合 polyglot 文件要靠存储隔离与固定 Content-Type 兜底")
