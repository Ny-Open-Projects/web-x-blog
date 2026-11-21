"""文件名规范化攻击: Unicode 归一化、控制字符与保留名(纯标准库)。"""
import re
import unicodedata

RESERVED_WIN = ({"CON", "PRN", "AUX", "NUL"}
                | {"COM{}".format(i) for i in range(1, 10)}
                | {"LPT{}".format(i) for i in range(1, 10)})
CONTROL_RE = re.compile(r"[\x00-\x1f\x7f]")


def sanitize_filename(raw):
    problems = []
    name = unicodedata.normalize("NFKC", raw)
    if name != raw:
        problems.append("unicode 归一化改变了文件名")
    if CONTROL_RE.search(name):
        problems.append("含控制字符")
        name = CONTROL_RE.sub("", name)
    if "/" in name or "\\" in name:
        problems.append("含路径分隔符")
        name = name.replace("/", "_").replace("\\", "_")
    base = name.split(".")[0].upper()
    if base in RESERVED_WIN:
        problems.append("命中保留设备名 " + base)
    if name != name.rstrip(". "):
        problems.append("清理了尾随点与空格")
        name = name.rstrip(". ")
    if name in ("", ".", ".."):
        problems.append("规范化后为空或为路径分量")
        name = "upload.bin"
    if len(name) > 255:
        problems.append("超长已截断")
        name = name[:255]
    return name, problems


attacks = ["ｒｅｐｏｒｔ.pdf", "CON.txt", "invoice.pdf...   ", "a\x00b.png",
           "../../etc/passwd", "..  ", "LPT1.log"]
for raw in attacks:
    safe, probs = sanitize_filename(raw)
    print("{!r:24s} -> {!r:18s} {}".format(raw, safe, probs or "通过"))
assert sanitize_filename("CON.txt")[1]
assert sanitize_filename("ｒｅｐｏｒｔ.pdf")[0] == "report.pdf"
print("要点: 落盘前一次性做 NFKC 归一加清洗, 同形字符、控制字符、保留名与尾随点空格是组合攻击面")
