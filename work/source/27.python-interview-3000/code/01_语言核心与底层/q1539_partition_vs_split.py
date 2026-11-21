

def parse_endpoint(text):
    """partition:返回形状恒定,解构不用判长度。"""
    host, sep, port = text.partition(":")
    return host, int(port) if sep and port.isdigit() else None


if __name__ == "__main__":
    for raw in ("db.internal:5432", "localhost", ":9999"):
        print(raw, "->", parse_endpoint(raw))

    # 扩展名要从右切:文件名里可能有多个点
    for path in ("archive.tar.gz", "README", ".hidden"):
        stem, dot, ext = path.rpartition(".")
        print(path, "-> stem:", stem or path, "ext:", ext if dot else "")

    # split 的两个细节:无分隔符 vs 空白压缩
    print("split ':' no sep :", "localhost".split(":"))
    print("split() 压缩空白 :", "a  b\tc\n d".split())
    print("split(' ') 不压缩:", "a  b".split(" "))
    print("maxsplit=1       :", "k=v=more".split("=", 1))
    print("partition 一刀   :", "k=v=more".partition("="))
