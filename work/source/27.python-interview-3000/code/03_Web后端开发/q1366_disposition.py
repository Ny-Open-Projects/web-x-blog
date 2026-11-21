"""安全构造 Content-Disposition 文件名(纯标准库)。"""
from urllib.parse import quote


def content_disposition(name):
    # 剥离会造成头注入与结构破坏的字符
    cleaned = "".join(ch for ch in name if ch not in '\r\n"\\/')
    ascii_fallback = cleaned.encode("ascii", "ignore").decode() or "download"
    return (f'attachment; filename="{ascii_fallback}"; '
            f"filename*=UTF-8''{quote(cleaned)}")


print(content_disposition("月度报表 2026.xlsx"))
evil = 'a.txt"\r\nX-Injected: 1'
safe = content_disposition(evil)
print("恶意输入已消毒 ->", safe.replace("\r\n", "|"))
assert "\r" not in safe and "\n" not in safe
