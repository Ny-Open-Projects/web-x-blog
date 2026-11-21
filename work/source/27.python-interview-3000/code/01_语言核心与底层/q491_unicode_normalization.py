import unicodedata

s1 = "caf\u00e9"          # 预组合:é 是单个码点
s2 = "cafe\u0301"         # 分解:e + 组合重音两个码点

if __name__ == "__main__":
    print("codepoints s1:", [hex(ord(c)) for c in s1])
    print("codepoints s2:", [hex(ord(c)) for c in s2])
    print("direct equality:", s1 == s2)

    n1 = unicodedata.normalize("NFC", s1)
    n2 = unicodedata.normalize("NFC", s2)
    print("NFC equality:", n1 == n2, "len:", len(n1))

    print("NFD len:", len(unicodedata.normalize("NFD", s1)))
    print("already NFC:", unicodedata.is_normalized("NFC", n1))
    print("casefold:", "STRASSE".casefold() == "straße".casefold())
