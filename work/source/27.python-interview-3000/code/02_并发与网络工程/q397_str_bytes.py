"""str 与 bytes 的转换与陷阱。"""
if __name__ == "__main__":
    s = "中文ABC"
    b = s.encode("utf-8")
    print("bytes:", b, "长度:", len(b), "(utf-8 中文 3 字节)")
    print("解码还原:", b.decode("utf-8"))

    # 陷阱 1: 索引类型不同
    print("b[0] =", b[0], type(b[0]).__name__, "| b[0:1] =", b[0:1])

    # 陷阱 2: GBK 与 UTF-8 互不兼容
    gbk = s.encode("gbk")
    print("gbk 字节:", gbk)
    try:
        gbk.decode("utf-8")
    except UnicodeDecodeError as e:
        print("乱码根因:", e)

    # 陷阱 3: errors 选项——strict 暴露问题, replace 保流程
    print("replace:", gbk.decode("utf-8", errors="replace"))
    print("十六进制:", b.hex())

    # 标准库 chardet 替代: 只能启发式判断, 生产用第三方 charset detection
    import codecs
    print("BOM 检测:", codecs.BOM_UTF8 == b"\xef\xbb\xbf")
