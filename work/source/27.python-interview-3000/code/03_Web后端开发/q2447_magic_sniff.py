"""上传文件魔数嗅探: 以内容而非扩展名判定真身(纯标准库)。"""

MAGIC = [
    (b"\x89PNG\r\n\x1a\n", "image/png"),
    (b"\xff\xd8\xff", "image/jpeg"),
    (b"GIF87a", "image/gif"),
    (b"GIF89a", "image/gif"),
    (b"%PDF-", "application/pdf"),
    (b"PK\x03\x04", "application/zip"),
]

# 扩展名 -> 允许的真实类型集合
EXT_WHITELIST = {
    ".pdf": {"application/pdf"},
    ".png": {"image/png"},
    ".jpg": {"image/jpeg"},
    ".zip": {"application/zip"},
}

SNIFF_LEN = 16


def sniff(head):
    """读文件头前若干字节比对魔数表。"""
    for magic, mime in MAGIC:
        if head.startswith(magic):
            return mime
    return "application/octet-stream"


def check_upload(filename, head, sniff_len=SNIFF_LEN):
    """扩展名白名单 + 魔数校验双重关卡。"""
    dot = filename.rfind(".")
    ext = filename[dot:].lower() if dot >= 0 else ""
    if ext not in EXT_WHITELIST:
        return False, "扩展名 {} 不在白名单".format(ext or "(无)")
    real = sniff(head[:sniff_len])
    if real not in EXT_WHITELIST[ext]:
        return False, "内容魔数是 {}, 与扩展名 {} 不符".format(real, ext)
    return True, "类型 {} 与扩展名匹配".format(real)


png_head = b"\x89PNG\r\n\x1a\n" + b"rest-of-png"
pdf_head = b"%PDF-1.7\n%fake"
exe_head = b"MZ\x90\x00\x03pe-payload"
zip_head = b"PK\x03\x04zip-entry"

cases = [
    ("report.pdf", pdf_head, True),
    ("chart.png", png_head, True),
    ("photo.jpg", png_head, False),        # 内容与扩展名不符
    ("evil.png", exe_head, False),         # 可执行内容伪装 png
    ("doc.pdf", zip_head, False),          # zip 伪装 pdf
    ("x.exe", exe_head, False),            # 扩展名直接不在白名单
    ("noext", pdf_head, False),
]
for filename, head, expect in cases:
    ok, why = check_upload(filename, head)
    print("{:12s} {:16s} -> {:<5} {}".format(filename, repr(head[:8]), ok, why))
    assert ok == expect, (filename, ok, why)

assert sniff(png_head) == "image/png"
assert sniff(exe_head) == "application/octet-stream"
print("要点: 扩展名是用户自报的, 魔数才是文件自己的话; "
      "两道关卡都要过, ZIP 魔数还会覆盖 docx 等容器格式, 校验后建议再重命名为服务端文件名")
