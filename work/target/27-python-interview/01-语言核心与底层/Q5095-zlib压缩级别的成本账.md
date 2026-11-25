---
title: "[Q5095] zlib 压缩级别的 CPU/内存成本账"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5095 · zlib 压缩级别的 CPU/内存成本账

难度：P6 | 标签：成本工程 | zlib | 选型

**问**：一个导出服务把响应体 zlib 压缩后再入库，level 用了默认值但高峰 CPU 打满。压缩级别怎么量化成本？`compressobj` 流式压缩在内存上比一次性 `compress` 省多少？

**答**：
结论：zlib level 1-9 的成本曲线是典型的"边际递减"：level 1→6 压缩比提升明显，CPU 近线性增长；6→9 压缩比只多几个百分点，CPU 可能翻倍（level 9 还会启用更贵的匹配策略）。选型的正确动作是拿**真实样本**测三条曲线：压缩比、吞吐（MB/s）、CPU 秒/GB，而不是拍脑袋上 level 9。内存维度：`zlib.compress(data, level)` 需要同时持有原数据+压缩结果；`compressobj` 可以 `compress(chunk)` 分块喂入、`flush()` 收尾，峰值内存 = chunk 大小 + 输出缓冲，与文档总大小解耦；解压端 `decompressobj.decompress(chunk, max_length)` 还能限制单次输出防解压炸弹。
取舍：字典压缩（`zdict`）对同构小报文（日志行、JSON）收益巨大——3.12 起 `zlib.compressobj(zdict=...)` 直接支持；代价是解压端必须持同一字典。
实战：库内归档用 level 6 或 `compresslevel` 可配置化；热路径（RPC 压缩）用 level 1-3；跨服务带宽紧张时优先上字典而不是拉高 level。

```python
import zlib, time, os

def bench(data: bytes, level: int, n=3):
    t0 = time.perf_counter()
    blob = zlib.compress(data, level)
    dt = time.perf_counter() - t0
    ratio = len(blob) / len(data)
    mbs = len(data) / 1e6 / dt
    return ratio, mbs, len(blob)

# 重复结构样本（贴近日志/JSON 报文）
sample = (b'{"user":"u1","action":"click","ts":"2026-11-21T00:00:00Z","meta":{"ab":"b"}}\n') * 200_000
print(f"样本 {len(sample)/1e6:.1f} MB")
print("level | 压缩比 | 压缩吞吐(MB/s) | 压缩后大小(MB)")
for lv in (1, 3, 6, 9):
    r, m, size = bench(sample, lv)
    print(f"{lv:5d} | {r:.3f}  | {m:8.0f}      | {size/1e6:.2f}")

# 流式压缩：峰值内存与总大小解耦
def streaming_size(data, level=6, chunk=1 << 20):
    co = zlib.compressobj(level)
    out = bytearray()
    for i in range(0, len(data), chunk):
        out += co.compress(data[i:i+chunk])
    out += co.flush()
    return bytes(out)

one_shot = zlib.compress(sample, 6)
streamed = streaming_size(sample)
print("一次性=流式结果一致:", one_shot == streamed, f"| 输出 {len(streamed)/1e6:.2f} MB，但流式峰值内存=1MB chunk")

# 分块解压 + max_length 限流（防解压炸弹）
d = zlib.decompressobj()
first = d.decompress(streamed, max_length=1 << 20)
print("解压首块上限 1MB:", len(first) <= 1 << 20, "| 尚未耗尽:", d.unconsumed_tail != b"" or d.unused_data == b"")

# 3.12+ 字典压缩
zdict = (b'{"user":"","action":"","ts":"","meta":{}}\n')
try:
    co = zlib.compressobj(6, zdict=zdict)
    blob = co.compress(sample[:1_000_000]) + co.flush()
    do = zlib.decompressobj(zdict=zdict)
    assert do.decompress(blob) == sample[:1_000_000]
    print(f"zdict 压缩 {len(blob)/1e6:.2f} MB vs 无字典 {len(zlib.compress(sample[:1_000_000],6))/1e6:.2f} MB")
except TypeError:
    print("当前 Python <3.12：zlib.compressobj 不支持 zdict，请用 pyzstd/lzma 降级")
```

**追问 1**：为什么 level 9 常常"又慢又没小多少"？
- 追问 2 层：level 主要控制惰性匹配与搜索深度，重复结构的数据在 level 6 就基本找齐最长匹配；9 的额外搜索是纯 CPU 税。
- 追问 3 层：真正要再压小应该换算法层级（zstd/lzma）或加 zdict，而不是在 zlib 内卷 level。

**追问 2**：解压炸弹在容量账里怎么防？
- 追问 2 层：`decompressobj.decompress(chunk, max_length)` 限制单次输出，配合累计输出上限总闸；`zlib` 自身无总量上限，防线在应用层。
- 追问 3 层：多成员 gzip 流（`unused_data`）与 concat 攻击要用循环消耗 unused_data 并累计计数。

## 背诵要点
1. level 1→6 收益明显、6→9 纯 CPU 税；选型用真实样本测"压缩比/吞吐/CPU 秒"三曲线。
2. compressobj 分块流式把峰值内存降到 chunk 级；解压端 max_length + 总量闸防炸弹。
3. 3.12+ compressobj 支持 zdict，同构报文优先上字典而不是拉高 level。

## 复盘追问
1. 高峰 CPU 打满后第一步是什么？——先降 level 到 3 观察，再做可配置化，而不是直接换算法。
2. 流式压缩输出如何边压边写盘？——compress 返回值即块，直接写文件对象，不要 accumulate 进 bytearray。
