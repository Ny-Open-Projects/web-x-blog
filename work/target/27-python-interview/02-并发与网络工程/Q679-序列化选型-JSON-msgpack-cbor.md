---
title: [Q679] 序列化选型:JSON / msgpack / cbor / protobuf
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q679 · 序列化选型:JSON / msgpack / cbor / protobuf

> 难度:★★★☆ | 标签:序列化, 选型, 性能

**问**:给内部服务间通信选序列化格式,你的决策树是什么?

**答**:按四个轴权衡:可读性/调试性、体积、编解码 CPU、跨语言类型保真。JSON:人类可读、生态无敌,体积与解析开销大,数字只有 double 精度语义;msgpack/cbor:二进制 JSON,体积小 30-50%、解析快,cbor 是 IETF 标准(带类型语义,时间/bigfloat),适合日志管道与边缘设备;protobuf/flatbuffer:强 schema、最小体积、生成代码,适合高频 RPC 与存储格式。决策路径:对外 API 与人看的数据用 JSON;内部高频通道上 protobuf(有 schema 评审需求)或 msgpack(无 schema 痛点);绝不用 pickle 跨信任边界(反序列化即代码执行)。

```python
# file: code/02_并发与网络工程/q679_serialization_bench.py
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
```

**追问**:1) 序列化升级(加字段)时格式迁移怎么做?——二进制格式靠字段号/版本位保证双读(新旧共存期两版都能解析);JSON 靠"只加不删不改语义"+容忍未知字段;切忌同字段切换类型。2) 数字精度在各格式里的差异?——JSON 数字语义弱(解析器自由决定 int/float,到 JS 超 2^53 丢精度);msgpack 有整数/浮点类型但默认映射仍有坑;protobuf 字段类型显式(int64/fixed64)跨语言保真最强——选型要把消费端的数字处理能力算进去(Q686)。3) 体积与 CPU 怎么实测?——用真实 payload 对各格式做 dumps+loads 基准(体积、编码耗时、解码耗时),别背百分比结论;开启压缩后格式间体积差距收窄,瓶颈会移到 CPU 侧。4) 生产陷阱?——pickle 跨信任边界(反序列化即代码执行,只限进程内可信数据);schema 演进不守纪律(reserved/只加不删);把大对象序列化放进热路径日志,序列化本身成为瓶颈。

---
