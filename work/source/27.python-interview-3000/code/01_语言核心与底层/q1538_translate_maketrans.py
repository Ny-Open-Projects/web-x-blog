import string
import timeit

SANITIZE = str.maketrans("aeiou", "43107", string.punctuation)
SENSITIVE = str.maketrans({c: "*" for c in "password0123456789"})


def rot13_table():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    return str.maketrans(lower + upper,
                         lower[13:] + lower[:13] + upper[13:] + upper[:13])


def clean_with_replace(text):
    """反模式:一串 replace,每个替换都全文扫描一遍。"""
    for ch in string.punctuation:
        text = text.replace(ch, "")
    return text.translate(str.maketrans("aeiou", "43107"))


if __name__ == "__main__":
    raw = "Hello, World! Email: user@example.com 2026-11-05"
    print("sanitize :", raw.translate(SANITIZE))
    print("mask     :", "password: 42".translate(SENSITIVE))
    print("rot13    :", "The Quick Brown Fox".translate(rot13_table()))

    text = raw * 400
    n = 30
    t_translate = timeit.timeit(lambda: text.translate(SANITIZE), number=n)
    t_replace = timeit.timeit(lambda: clean_with_replace(text), number=n)
    print("translate    :", round(t_translate * 1000 / n, 3), "ms per run")
    print("replace chain:", round(t_replace * 1000 / n, 3), "ms per run")

    # bytes.translate:256 字节映射表,协议清洗的常用工具
    b = b"hello\x00world"
    print("bytes    :", b.translate(bytes.maketrans(b"lo", b"10"),
                                   delete=b"\x00"))
