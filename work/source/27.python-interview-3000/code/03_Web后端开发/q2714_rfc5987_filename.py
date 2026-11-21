"""非 ASCII 文件名的 Content-Disposition 编码: RFC 5987 filename*(纯标准库)。"""
import re
from urllib.parse import quote, unquote


def content_disposition(filename, disposition="attachment"):
    """ASCII 安全名直接进 filename 引号串; 含非 ASCII 或特殊字符时补 filename*。

    filename* 按 RFC 5987 编码: charset''percent-encoded, 空格斜杠引号都不进 safe;
    filename 仍带一个 ASCII 兜底名, 给不认识 filename* 的老客户端。
    """
    if any(c in filename for c in "\r\n"):
        raise ValueError("非法文件名")
    if all(32 <= ord(c) < 127 for c in filename) and '"' not in filename and "\\" not in filename:
        return '%s; filename="%s"' % (disposition, filename)
    return '%s; filename="download"; filename*=UTF-8\'\'%s' % (disposition, quote(filename, safe=""))


def parse_filename(header):
    """优先解析 filename*, 拿不到再退 filename; 返回 (名字, 来源)。"""
    m = re.search(r"filename\*=([^']*)''([^;\s]+)", header)
    if m:
        return unquote(m.group(2)), m.group(1) or "UTF-8"
    m = re.search(r'filename="([^"]*)"', header)
    return (m.group(1), "ASCII") if m else (None, None)


h1 = content_disposition("report.pdf")
h2 = content_disposition("季度报告.pdf")
h3 = content_disposition('we"ird name.txt')
assert h1 == 'attachment; filename="report.pdf"', h1
assert parse_filename(h1) == ("report.pdf", "ASCII")
name, enc = parse_filename(h2)
assert name == "季度报告.pdf" and enc == "UTF-8", (name, enc)
name3, enc3 = parse_filename(h3)
assert name3 == 'we"ird name.txt' and enc3 == "UTF-8"
print("ASCII   :", h1)
print("中文    :", h2)
print("含引号  :", h3)
try:
    content_disposition("a\r\nb")
except ValueError as e:
    print("头注入拒绝:", e)
