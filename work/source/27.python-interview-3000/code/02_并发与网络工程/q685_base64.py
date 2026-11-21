import base64
import json


def json_with_binary(obj: dict, binary_fields: set) -> bytes:
    """约定: binary_fields 中的字段以 base64 字符串承载。"""
    payload = {}
    for k, v in obj.items():
        payload[k] = base64.b64encode(v).decode() if k in binary_fields else v
    return json.dumps(payload).encode()


def parse_json_with_binary(raw: bytes, binary_fields: set) -> dict:
    payload = json.loads(raw)
    return {k: (base64.b64decode(v) if k in binary_fields else v)
            for k, v in payload.items()}


if __name__ == "__main__":
    blob = bytes(range(256))  # 含所有"非法"字符的二进制
    encoded = base64.b64encode(blob)
    assert base64.b64decode(encoded) == blob
    print(f"256 字节 → base64 {len(encoded)} 字节 (膨胀 {len(encoded) / 256:.2f}x)")

    # JSON 承载: 不编码则 json.dumps 直接报错
    try:
        json.dumps({"data": blob})
    except TypeError as e:
        print("裸二进制进 JSON:", e)

    framed = json_with_binary({"name": "cert", "data": blob}, {"data"})
    back = parse_json_with_binary(framed, {"data"})
    assert back["data"] == blob
    print(f"base64 承载往返: {len(framed)} 字节 JSON, 数据无损")

    # URL-safe 变体: +/ 会破坏 URL 与文件名
    raw = bytes([0xFB, 0xEF, 0xBE])
    std = base64.b64encode(raw)
    url = base64.urlsafe_b64encode(raw)
    print(f"标准: {std.decode()}  URL-safe: {url.decode()} (+ 与 / 被替换)")

    # Base64 不是加密: 一眼可逆
    secret = base64.b64encode(b"password=123456")
    print(f"'编码'的密码 {secret.decode()} → 解码 {base64.b64decode(secret).decode()}")
    print("结论: 保密用加密 (Q375), base64 只解决'穿过文本通道'")
