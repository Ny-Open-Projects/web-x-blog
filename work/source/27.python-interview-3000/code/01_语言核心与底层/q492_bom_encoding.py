import os
import tempfile

if __name__ == "__main__":
    text = "héllo"
    path = os.path.join(tempfile.mkdtemp(), "bom.txt")
    with open(path, "w", encoding="utf-8-sig") as f:   # 写入 BOM
        f.write(text)

    with open(path, "rb") as f:
        raw = f.read(10)
        print("raw head:", raw)                        # 开头是 ef bb bf

    with open(path, encoding="utf-8") as f:            # 忘记 -sig:BOM 留在内容里
        print("utf-8 sees:", repr(f.read()))

    with open(path, encoding="utf-8-sig") as f:        # 正确:BOM 被剥掉
        print("utf-8-sig sees:", repr(f.read()))
