"""bytes 与 str 的比较:永不相等、哈希不同、混排直接报错。"""

if __name__ == "__main__":
    text = "中文"
    data = text.encode("utf-8")
    print("bytes 形式:", data)
    print("与 str 比较:", data == text)
    print("decode 后相等:", data.decode("utf-8") == text)

    print("哈希不同:", hash(data) != hash(text))
    table = {text: "值"}
    try:
        table[data]
    except KeyError:
        print("bytes 键取不到 str 的值")

    print("b'abc' 索引得到:", b"abc"[0], type(b"abc"[0]).__name__)
    print("str 索引得到:", "abc"[0], type("abc"[0]).__name__)

    try:
        sorted(["a", b"a"])
    except TypeError as exc:
        print("混排:", exc)

    try:
        b"a" in "abc"
    except TypeError as exc:
        print("in 跨类型:", exc)
