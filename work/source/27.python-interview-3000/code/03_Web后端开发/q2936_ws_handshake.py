"""WebSocket 握手的完整服务端: 升级校验、Accept 计算与首帧掩码解析(纯标准库)。"""
import base64
import hashlib

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"  # RFC 6455 固定魔串


class HandshakeError(Exception):
    def __init__(self, status, reason):
        self.status = status
        self.reason = reason


def parse_request(raw):
    try:
        lines = raw.decode("latin-1").split("\r\n")
        method, target, _version = lines[0].split(" ", 2)
    except (ValueError, IndexError):
        raise HandshakeError(400, "请求行非法")
    headers = {}
    for line in lines[1:]:
        if not line:
            continue
        key, _, value = line.partition(":")
        headers[key.strip().lower()] = value.strip()
    return method, target, headers


def handshake(raw):
    """校验升级请求并产出 101 响应字节; 任何不合规格直接拒绝。"""
    method, target, h = parse_request(raw)
    if method != "GET":
        raise HandshakeError(405, "握手必须是 GET")
    if h.get("upgrade", "").lower() != "websocket":
        raise HandshakeError(400, "缺少 Upgrade: websocket")
    if "upgrade" not in h.get("connection", "").lower():
        raise HandshakeError(400, "Connection 头必须含 upgrade")
    key = h.get("sec-websocket-key")
    if not key:
        raise HandshakeError(400, "缺少 Sec-WebSocket-Key")
    try:
        if len(base64.b64decode(key)) != 16:
            raise ValueError
    except Exception:
        raise HandshakeError(400, "Sec-WebSocket-Key 不是 16 字节的 base64")
    accept = base64.b64encode(hashlib.sha1((key + GUID).encode("ascii")).digest()).decode("ascii")
    response = (
        "HTTP/1.1 101 Switching Protocols\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "Sec-WebSocket-Accept: " + accept + "\r\n"
        "\r\n"
    )
    return response.encode("ascii"), target


def decode_client_frame(frame):
    """解析客户端首帧; RFC 6455 规定客户端帧必须掩码, 服务端帧绝不掩码。"""
    if len(frame) < 2:
        raise HandshakeError(400, "帧过短")
    b0, b1 = frame[0], frame[1]
    opcode = b0 & 0x0F
    length = b1 & 0x7F
    masked = bool(b1 & 0x80)
    offset = 2
    if length == 126:
        length = int.from_bytes(frame[2:4], "big")
        offset = 4
    elif length == 127:
        length = int.from_bytes(frame[2:10], "big")
        offset = 10
    if not masked:
        raise HandshakeError(400, "客户端帧必须带掩码")
    mask = frame[offset:offset + 4]
    payload = bytes(b ^ mask[i % 4] for i, b in enumerate(frame[offset + 4:offset + 4 + length]))
    return opcode, payload


def encode_client_frame(payload, mask=b"\x01\x02\x03\x04"):
    """构造测试用的带掩码文本帧 opcode=0x1。"""
    masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
    header = bytes([0x81, 0x80 | len(payload)])
    return header + mask + masked


# 1. 标准握手: RFC 6455 示例密钥, 期望 Accept 值固定
raw = (
    b"GET /chat HTTP/1.1\r\n"
    b"Host: server.example.com\r\n"
    b"Upgrade: websocket\r\n"
    b"Connection: Upgrade\r\n"
    b"Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
    b"Sec-WebSocket-Version: 13\r\n"
    b"\r\n"
)
resp, target = handshake(raw)
print(resp.decode().strip())
assert b"101 Switching Protocols" in resp
assert b"s3pPLMBiTxaQ9kYGzzhZRbK+xOo=" in resp, "RFC 6455 附录的黄金值"
assert target == "/chat"

# 2. 非法握手逐个拒绝
bad_cases = [
    (raw.replace(b"Upgrade: websocket\r\n", b"Upgrade: h2c\r\n"), 400, "Upgrade 不是 websocket"),
    (raw.replace(b"Connection: Upgrade\r\n", b"Connection: keep-alive\r\n"), 400, "Connection 缺 upgrade"),
    (raw.replace(b"Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n", b""), 400, "缺 Key"),
    (raw.replace(b"Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n",
                 b"Sec-WebSocket-Key: tooshort\r\n"), 400, "Key 不是 16 字节"),
    (raw.replace(b"GET /chat HTTP/1.1", b"POST /chat HTTP/1.1"), 405, "非 GET"),
]
for bad, status, why in bad_cases:
    try:
        handshake(bad)
        raise AssertionError("应当拒绝: %s" % why)
    except HandshakeError as e:
        print("拒绝 [%s] -> %s" % (why, e.status))
        assert e.status == status

# 3. 握手后收发帧: 掩码解码还原客户端消息
frame = encode_client_frame(b"hello ws")
opcode, payload = decode_client_frame(frame)
print("首帧解码 opcode=%s payload=%r" % (opcode, payload))
assert (opcode, payload) == (0x1, b"hello ws")

unmasked = bytes([0x81, len(b"hello ws")]) + b"hello ws"  # 掩码位清零的违规帧
try:
    decode_client_frame(unmasked)
    raise AssertionError("未掩码帧应当被拒")
except HandshakeError as e:
    print("未掩码客户端帧 ->", e.status, e.reason)
    assert e.status == 400
print("WebSocket 握手服务端演示通过")
