"""multipart/form-data 边界解析器(纯标准库)。"""
import re


def parse_content_disposition(value):
    """从 Content-Disposition 取 name 与 filename 参数。"""
    return dict(re.findall(r'(\w+)="([^"]*)"', value))


def parse_multipart(body, boundary):
    """按 RFC 2046 切分, 返回 (字段字典, 文件列表)。"""
    delim = b"--" + boundary.encode("ascii")
    fields, files = {}, []
    for raw in body.split(delim)[1:]:            # 首段是边界前的前导, 丢弃
        if raw.startswith(b"--"):                # 结束标记 --boundary--
            break
        if raw.startswith(b"\r\n"):
            raw = raw[2:]                        # 边界行后的 CRLF
        if raw.endswith(b"\r\n"):
            raw = raw[:-2]                       # 分隔符前的 CRLF 属于分隔符
        head, sep, content = raw.partition(b"\r\n\r\n")
        if not sep:
            continue
        meta = {}
        for line in head.decode("utf-8", "replace").split("\r\n"):
            key, _, value = line.partition(":")
            meta[key.strip().lower()] = value.strip()
        disp = parse_content_disposition(meta.get("content-disposition", ""))
        name = disp.get("name")
        if name is None:
            continue
        if "filename" in disp:
            files.append({"name": name, "filename": disp["filename"],
                          "content_type": meta.get("content-type", "application/octet-stream"),
                          "content": content})
        else:
            fields[name] = content.decode("utf-8")
    return fields, files


title_bytes = "季度总结".encode("utf-8")
boundary = "XyZZyDemo42"
body = (b"--XyZZyDemo42\r\n"
        b'Content-Disposition: form-data; name="title"\r\n\r\n'
        + title_bytes + b"\r\n"
        b"--XyZZyDemo42\r\n"
        b'Content-Disposition: form-data; name="tag"\r\n\r\n'
        b"q3\r\n"
        b"--XyZZyDemo42\r\n"
        b'Content-Disposition: form-data; name="doc"; filename="a.pdf"\r\n'
        b"Content-Type: application/pdf\r\n\r\n"
        b"%PDF-1.4 fake-binary-\x00\x01\x02\r\n"
        b"--XyZZyDemo42--\r\n")

fields, files = parse_multipart(body, boundary)
print("字段:", fields)
for f in files:
    print("文件: name={} filename={} type={} bytes={}".format(
        f["name"], f["filename"], f["content_type"], len(f["content"])))
assert fields == {"title": "季度总结", "tag": "q3"}
assert len(files) == 1
assert files[0]["filename"] == "a.pdf"
assert files[0]["content"].startswith(b"%PDF-1.4")
assert files[0]["content"].endswith(b"\x00\x01\x02"), "二进制内容必须逐字节保真"

# 缺失结束标记的残包: 解析器不应崩溃, 已完整部分照常产出
fields2, files2 = parse_multipart(body[:-4], boundary)
assert fields2 == fields and len(files2) == 1
print("要点: 解析就是按边界 split 加头体二分, 文件内容按字节保真; "
      "真实实现还要处理边界出现在数据里的极端情形与 header 大小上限")
