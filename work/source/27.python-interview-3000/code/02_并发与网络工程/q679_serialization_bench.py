import json
import struct
import timeit
from datetime import datetime

RECORD = {
    "id": 12345678,
    "name": "device-42",
    "active": True,
    "score": 98.6,
    "tags": ["edge", "beta"],
    "ts": "2026-11-01T12:00:00",
}


def encode_binary(rec: dict) -> bytes:
    """手工二进制编码: 定长头 + 字段, 模拟 msgpack/protobuf 思路。"""
    body = b"".join([
        struct.pack("!I", rec["id"]),
        struct.pack("!B", len(rec["name"])) + rec["name"].encode(),
        struct.pack("!B", 1 if rec["active"] else 0),
        struct.pack("!f", rec["score"]),
        struct.pack("!B", len(rec["tags"])) + b"".join(
            struct.pack("!B", len(t)) + t.encode() for t in rec["tags"]),
    ])
    return struct.pack("!H", len(body)) + body


if __name__ == "__main__":
    j = json.dumps(RECORD).encode()
    b = encode_binary(RECORD)
    print(f"JSON  体积: {len(j)} 字节")
    print(f"二进制体积: {len(b)} 字节 (约省 {(1 - len(b) / len(j)) * 100:.0f}%)")

    n = 20000
    t_json = timeit.timeit(lambda: json.loads(json.dumps(RECORD)), number=n)
    t_bin_enc = timeit.timeit(lambda: encode_binary(RECORD), number=n)

    def decode_binary(raw: bytes):
        blen = struct.unpack("!H", raw[:2])[0]
        body = raw[2:2 + blen]
        off = 0
        id_ = struct.unpack_from("!I", body, off)[0]; off += 4
        nlen = body[off]; off += 1
        name = body[off:off + nlen].decode(); off += nlen
        active = bool(body[off]); off += 1
        score = struct.unpack_from("!f", body, off)[0]; off += 4
        ntags = body[off]; off += 1
        tags = []
        for _ in range(ntags):
            tl = body[off]; off += 1
            tags.append(body[off:off + tl].decode()); off += tl
        return {"id": id_, "name": name, "active": active, "score": score, "tags": tags}

    t_bin_dec = timeit.timeit(lambda: decode_binary(encode_binary(RECORD)), number=n)
    print(f"json roundtrip  {n} 次: {t_json * 1000:.0f}ms")
    print(f"binary 编码     {n} 次: {t_bin_enc * 1000:.0f}ms")
    print(f"binary 编解码   {n} 次: {t_bin_dec * 1000:.0f}ms")

    rt = decode_binary(b)
    print("二进制解码结果:", rt)
    print("注意 float 精度: 98.6 → struct 单精度 →", rt["score"],
          "(cbor/msgpack 用 double 可避免)")

    # pickle 的能力与危险演示
    import pickle
    p = pickle.dumps({"ts": datetime(2026, 11, 1)})
    print(f"pickle 能原生携带 datetime ({len(p)} 字节), 但 loads 不可信数据 = 任意代码执行")
