---
title: [Q687] 协议调试利器:hex dump 解析器
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q687 · 协议调试利器:hex dump 解析器

> 难度:★★☆ | 标签:hexdump, 调试, 二进制

**问**:线上只抓到一串十六进制,怎么快速判断帧结构对不对?

**答**:第一步是格式化 hexdump(每行 16 字节,offset+hex+ASCII 三列),ASCII 列让可读字段(如 JSON 体)直接跳出来;第二步按协议头逐字段 annotate——把 magic/ver/type/length 的期望值写在 dump 旁,偏移一眼对上;第三步验证长度字段与实际剩余字节是否一致(80% 的协议 bug 是长度算错,含/不含头、是否算 CRC)。把这三步写成一个调试函数,联调时"dump+annotate"一次输出,比日志盲猜快得多。

```python
# file: code/02_并发与网络工程/q687_hexdump.py
import struct


def hexdump(data: bytes, width: int = 16) -> str:
    lines = []
    for off in range(0, len(data), width):
        row = data[off:off + width]
        hex_part = " ".join(f"{b:02x}" for b in row)
        ascii_part = "".join(chr(b) if 32 <= b < 127 else "." for b in row)
        lines.append(f"{off:06x}  {hex_part:<{width * 3 - 1}}  |{ascii_part}|")
    return "\n".join(lines)


HEADER = struct.Struct("!2sBHI")
MAGIC = b"PY"


def annotate(data: bytes) -> str:
    lines = []
    try:
        magic, ver, mtype, length = HEADER.unpack_from(data)
        lines.append(f"  偏移 0-6  头部: magic={magic!r} ver={ver} type={mtype:#x} length={length}")
        ok_magic = magic == MAGIC
        body_end = HEADER.size + length
        actual = len(data) - HEADER.size
        lines.append(f"  长度字段={length}, 实际载荷={actual} → "
                     f"{'一致' if actual == length else '不一致 (典型 bug: 长度含头/含CRC)'}")
        lines.append(f"  magic 校验: {'通过' if ok_magic else '失败'}")
        lines.append(f"  预期帧总长 = 头{HEADER.size} + 体{length} = {body_end}, "
                     f"实际 {len(data)} 字节")
    except struct.error:
        lines.append("  数据不足以解析头部")
    return "\n".join(lines)


if __name__ == "__main__":
    # 构造一帧带 JSON 体的协议数据
    body = b'{"action":"reload","target":"config"}'
    frame = HEADER.pack(MAGIC, 1, 0x02, len(body)) + body
    print(hexdump(frame))
    print(annotate(frame))
    print()

    # 一个"长度算错"的坏帧: 长度多算了 4
    bad = HEADER.pack(MAGIC, 1, 0x02, len(body) + 4) + body
    print(hexdump(bad))
    print(annotate(bad))
```

**追问**:1) 二进制协议联调最快的排障顺序是什么?——先 hexdump 看长度字段与实际是否一致,再对 magic/ver/type 逐字节比对,最后才上抓包;90% 的联调问题在前两步就能定位。2) 长度字段的三种口径怎么排查?——「含头/不含头」「是否含 CRC」「是否含 padding」;验证:dump 里数实际剩余字节与声明值比对,差值恒等于头长或 CRC 长即是口径问题——80% 的联调 bug 在这一步现形。3) annotate 怎么自动化?——写 describe(bytes, 描述表) 函数:按字段偏移/格式逐项输出「字段名=值」,两端各 dump 一次对照;配合 struct.iter_unpack 快速定位第一个错位字段。4) 生产陷阱?——生产环境常开 hexdump 打日志(大 payload 打爆磁盘,要开关+截断);ASCII 列直接暴露敏感数据(要脱敏);用 repr 打整段 bytes,转义噪声淹没帧结构。

---
