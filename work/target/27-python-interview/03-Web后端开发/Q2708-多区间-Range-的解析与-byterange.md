---
title: [Q2708] 多区间 Range 的解析与 byteranges 响应
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2708 · 多区间 Range 的解析与 byteranges 响应

> 难度:★★★★ | 标签:HTTP 协议, Range, 下载

**问**:视频客户端发来 bytes=0-4,10-19,-100,服务端怎么解析、怎么响应?

**答**:解析按 RFC 7233 落:逗号切分逐段处理,`a-b` 常规区间钳到 [0, total),`-N` 后缀区间取最后 N 字节,start>end 或起点越界的段丢弃;全部段不可满足才回 416 并带 `Content-Range: bytes */total`,部分可满足就只回可满足的那些。重叠与相邻区间要合并升序,避免冗余传输。响应形态分两路:单区间直接 206 加 Content-Range;多区间用 multipart/byteranges 封装,每段自带 Content-Range 与分隔边界,结尾补闭界。注意区间语义是双闭区间,end 是含在内的最后字节;Range 头整体非法(前缀都不是 bytes=)按无 Range 处理还是 416,各实现要固定一种并写进文档。

```python
# file: code/03_Web后端开发/q2708_multi_range.py
"""多区间 Range 的解析与 byteranges 响应(纯标准库)。"""
import re

TOTAL = 1000
BODY = bytes((i * 7) % 256 for i in range(TOTAL))


def parse_ranges(spec, total):
    """解析 bytes= 头: 返回 (合并后的区间列表, 是否可满足)。

    后缀写法 -N 取最后 N 字节; 起点越界或 start>end 的区间丢弃;
    全部区间不可满足返回 416, 部分可满足只回可满足的那些(RFC 7233)。
    """
    if not spec or not spec.strip().lower().startswith("bytes="):
        return None, False
    raw = []
    for part in spec.split("=", 1)[1].split(","):
        part = part.strip()
        m = re.match(r"^(\d*)-(\d*)$", part)
        if not m or (not m.group(1) and not m.group(2)):
            continue  # 非法段直接丢弃
        if m.group(1) == "":
            n = int(m.group(2))
            if n <= 0 or total == 0:
                continue
            raw.append((max(0, total - n), total - 1))
        else:
            start, end = int(m.group(1)), int(m.group(2) or total - 1)
            if start > end or start >= total:
                continue
            raw.append((start, min(end, total - 1)))
    if not raw:
        return [], False
    raw.sort()
    merged = [list(raw[0])]
    for s, e in raw[1:]:
        if s <= merged[-1][1] + 1:  # 相邻或重叠则并区间
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return [tuple(r) for r in merged], True


def build_response(body, ranges):
    """单区间走 Content-Range, 多区间走 multipart/byteranges。"""
    if len(ranges) == 1:
        s, e = ranges[0]
        return 206, body[s:e + 1], "bytes %d-%d/%d" % (s, e, len(body))
    boundary = "sep7f3d2a1c"
    chunks = []
    for s, e in ranges:
        chunks.append(("--%s\r\nContent-Range: bytes %d-%d/%d\r\n\r\n"
                       % (boundary, s, e, len(body))).encode("ascii") + body[s:e + 1] + b"\r\n")
    chunks.append(("--%s--\r\n" % boundary).encode("ascii"))
    return 206, b"".join(chunks), "multipart/byteranges; boundary=%s" % boundary


for spec in ("bytes=0-4,10-19", "bytes=0-499,250-749", "bytes=-100", "bytes=2000-3000", "bytes=2000-3000,5-9", "bytes=abc"):
    ranges, ok = parse_ranges(spec, TOTAL)
    if not ok:
        print("%-24s -> 416, Content-Range: bytes */%d" % (spec, TOTAL))
        continue
    status, payload, note = build_response(BODY, ranges)
    print("%-24s -> %d 区间%s" % (spec, status, ranges))

assert parse_ranges("bytes=0-4,10-19", TOTAL)[0] == [(0, 4), (10, 19)]
assert parse_ranges("bytes=0-499,250-749", TOTAL)[0] == [(0, 749)]
assert parse_ranges("bytes=-100", TOTAL)[0] == [(900, 999)]
assert parse_ranges("bytes=2000-3000", TOTAL) == ([], False)
assert parse_ranges("bytes=2000-3000,5-9", TOTAL)[0] == [(5, 9)]
s, payload, note = build_response(BODY, [(0, 4), (10, 19)])
head = payload.index(b"\r\n\r\n") + 4  # 第一段的正文起点
assert payload[head:head + 5] == BODY[0:5] and b"bytes 10-19/1000" in payload
print("multipart 首段正文与源字节一致, 边界与 Content-Range 齐全")
```

**追问**:
- 多区间响应的 ETag 怎么处理?——与单区间一致用同一个强 ETag,区间划分不影响资源版本,If-Range 校验逻辑不变。
- 区间数量要不要设上限?——要,区间数乘以平均收益不抵 multipart 开销时直接给全量或 416,几十段以上的请求基本是滥用。
