"""len 是字符数不是显示宽度:东亚宽度与组合字符。"""
import unicodedata


def display_width(s):
    """宽字符记 2、组合字符记 0、其余记 1 的终端列宽估算。"""
    total = 0
    for ch in s:
        if unicodedata.combining(ch):
            continue
        total += 2 if unicodedata.east_asian_width(ch) in ("F", "W") else 1
    return total


if __name__ == "__main__":
    samples = ["abc", "中文", "ａｂｃ", "naïve", "éclair"]
    for s in samples:
        print(f"{s!r:<12} len={len(s)} 显示宽={display_width(s)}")

    nfc = "é"
    nfd = "e\u0301"
    print("NFC len:", len(nfc), "| NFD len:", len(nfd))
    print("显示宽相同:", display_width(nfc) == display_width(nfd))
    print("归一化后相等:", unicodedata.normalize("NFC", nfd) == nfc)

    rows = [("名称", "值"), ("name", "value")]
    width = max(display_width(r[0]) for r in rows)
    for name, val in rows:
        print(name + " " * (width - display_width(name)) + " | " + val)
