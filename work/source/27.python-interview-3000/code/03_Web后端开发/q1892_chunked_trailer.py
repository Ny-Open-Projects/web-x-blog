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
