if __name__ == "__main__":
    s = "你好, Python"
    b = s.encode("utf-8")
    print(b, len(b), len(s))     # 字节数不等于字符数
    print(b.decode("utf-8"))

    try:
        b.decode("ascii")
    except UnicodeDecodeError as e:
        print("decode error:", e)

    print("emoji".encode("ascii", errors="replace"))
    raw = b"caf\xe9"
    print(raw.decode("latin-1"), "|", raw.decode("utf-8", errors="replace"))

    with open("/tmp/enc_demo.txt", "w", encoding="utf-8") as f:
        f.write(s)
    with open("/tmp/enc_demo.txt", "r", encoding="utf-8") as f:
        print(f.read())
