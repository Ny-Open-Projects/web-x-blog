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
