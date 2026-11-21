---
title: [Q2442] multipart/form-data 的边界解析器
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2442 · multipart/form-data 的边界解析器

> 难度:★★★★ | 标签:multipart, 上传, 解析器

**问**:multipart 报文的边界解析到底在做什么?文件内容为什么必须按字节保真?

**答**:解析器只做两件事:按"两个连字符加边界"做分片切分,再对每个分片做头体二分(空行 CRLF CRLF 分隔)。细节都藏在边角:正文以边界行开始、以"--边界--"结束;每个分片紧邻边界行后的 CRLF 与结束前的 CRLF 都属于分隔符,要精确剥掉,但不能多剥——这就是为什么演示里用定长切片而不是盲目 strip;头部的 Content-Disposition 用参数形式携带 name 与 filename,文件部件多一个 filename 参数。文件内容必须按字节保真,因为上传的可能是任意二进制,按字符串解码再编码会毁掉内容——字段值与文件体要分开处理,前者解码为文本,后者保持 bytes。生产解析器还要加边界出现于数据中的防御、头大小上限与部件数上限,示波器式的健壮性来自这些上限。

```python
# file: code/03_Web后端开发/q2442_multipart_parser.py
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
```

**追问**:
- 边界为什么能保证不与内容冲突?——不能绝对保证,规范要求客户端选择不会出现在数据里的边界,服务端仍要防恶意构造。
- boundary 从哪来?——Content-Type 头的 boundary 参数,可能带引号,解析时要去引号并用它构造分片分隔符。
