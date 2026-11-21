import re


def mask_phone(s: str) -> str:
    return s[:3] + "****" + s[-4:] if len(s) == 11 else s


def mask_id_card(s: str) -> str:
    return s[:4] + "*" * (len(s) - 8) + s[-4:]


def mask_email(s: str) -> str:
    if "@" not in s:
        return s
    name, domain = s.split("@", 1)
    return (name[:1] + "***" + "@" + domain) if name else s


PHONE_RE = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
ID_RE = re.compile(r"(?<!\d)\d{17}[\dXx](?!\d)")


def sanitize_log(text: str) -> str:
    """日志框架全局兜底:正则自动打码。"""
    text = PHONE_RE.sub(lambda m: mask_phone(m.group()), text)
    text = ID_RE.sub(lambda m: mask_id_card(m.group()), text)
    return text


if __name__ == "__main__":
    print(mask_email("zhangsan@example.com"))
    print(sanitize_log("user 13812345678 paid, id 11010119900307867X"))
