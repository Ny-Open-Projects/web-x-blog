---
title: [Q1892] Trailer 头与分块传输的完整性校验
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1892 · Trailer 头与分块传输的完整性校验

> 难度:★★★☆ | 标签:HTTP, 流式处理

**问**:响应都结束了 Trailer 才到,它有什么用?

**答**:chunked 传输编码允许把头拆两半:先发普通头,末尾零长块之后再跟 trailer 头。Trailer: X-Content-Digest 先声明"末帧会带这个头",接收方提前知道要等它。核心价值是流式完整性:生成方边产数据边算 sha256,全部发完在 trailer 里给出摘要,接收方同样边收边算,收完一比即可发现中途篡改或损坏——而 Content-Length 方案要求先缓冲全量才能算长度,与流式目标冲突。约束:trailer 不能放路由必需的头(Host、Content-Type 这类),因为接收方处理时早已用不上;客户端必须读到最后才能确认完整性。日志导出、大文件下载、分片合并校验都是典型场景,HTTP/2 里语义相同(END_STREAM 后的 HEADERS 帧)。

```python
# file: code/03_Web后端开发/q1892_chunked_trailer.py
"""分块传输与 Trailer 校验: 边发边算摘要, 末帧带 Trailer(纯标准库)。"""
import hashlib


def encode_chunked(pieces, trailer_headers):
    """把若干数据块编码为 chunked 体; Trailer 声明属于响应头, 不进分块体。"""
    out = []
    for piece in pieces:
        data = piece.encode("utf-8")
        out.append("{:x}\r\n".format(len(data)) + data.decode("utf-8") + "\r\n")
    tail = "".join("{}: {}\r\n".format(k, v) for k, v in trailer_headers.items())
    out.append("0\r\n" + tail + "\r\n")
    return "".join(out).encode("utf-8")


def decode_chunked(raw):
    """解码 chunked 体, 返回 (body_bytes, trailers dict); 必须按字节处理帧长度。"""
    body, trailers, i = bytearray(), {}, 0
    while True:
        j = raw.index(b"\r\n", i)
        size = int(raw[i:j], 16)
        if size == 0:                      # 终止块之后是 trailer 区
            rest = raw[j + 2:].decode("utf-8")
            for line in rest.strip().split("\r\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    trailers[k.strip()] = v.strip()
            return bytes(body), trailers
        body.extend(raw[j + 2:j + 2 + size])
        i = j + 2 + size + 2               # 跳过块数据与块尾 CRLF


def verify(body, trailers):
    """用 trailer 里的摘要校验体完整性; 接收方可以边收边算。"""
    expect = trailers.get("X-Content-Digest")
    actual = hashlib.sha256(body).hexdigest()
    return actual == expect, actual


pieces = ["第一批日志行\n", "第二批日志行\n", "第三批日志行\n"]
digest = hashlib.sha256("".join(pieces).encode("utf-8")).hexdigest()
raw = encode_chunked(pieces, {"X-Content-Digest": digest})
print("响应头应声明: Trailer: X-Content-Digest (让接收方知道末帧带摘要)")
body, trailers = decode_chunked(raw)
print("解码体:", body.decode("utf-8").strip().replace("\n", " | "))
print("trailer:", trailers)
ok, actual = verify(body, trailers)
print("摘要校验:", ok)
assert ok and body.decode("utf-8") == "".join(pieces)

# 篡改场景: 中途改一块, 末帧摘要对不上, 接收方当场发现
tampered = raw.replace("第二批".encode("utf-8"), "篡改后".encode("utf-8"))
body2, trailers2 = decode_chunked(tampered)
ok2, actual2 = verify(body2, trailers2)
print("篡改后校验:", ok2, "(接收方拒收)")
assert not ok2
print("要点: Trailer 让完整性校验能覆盖流式响应, 对生成方不必先缓冲全量才能带 Content-Length")
```

**追问**:
- 为什么不能把摘要放普通头?——放普通头就得先算完全部数据才能发头,流式生成被迫全量缓冲。
- trailer 头被中间代理剥掉怎么办?——接收方发现声明了 Trailer 却没收到对应头,按完整性失败拒收并告警。
