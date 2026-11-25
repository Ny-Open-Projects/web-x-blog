---
title: "[Q5099] gzip/bz2/lzma 压缩家族选型演进"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5099 · gzip/bz2/lzma 压缩家族选型演进

难度：P6 | 标签：版本演进 | gzip/bz2/lzma | 选型

**问**：归档平台要压测样本数据：当前用 gzip，审计想换 bz2，有人提议 lzma。三者的压缩比/吞吐/内存/解压成本矩阵是什么？选型如何随数据形态（单大文件 vs 海量小文件）变化？

**答**：
结论：标准库三代压缩家族的坐标：gzip（DEFLATE，zlib 内核）吞吐高、压缩比中、内存占用小（64KB×2 级别），生态兼容性最强；bz2（BWT+MTF）压缩比高于 gzip 但压缩吞吐慢数倍、内存较高（几百 KB-数 MB），解压快；lzma（LZMA2/xz）压缩比最高、解压快、但压缩最慢且内存最大（preset 6 默认字典 8MB，可达几十 MB），擅长"一次压缩、多次解压"的冷归档。演进趋势上，行业标准已从 bz2 转向 zstd/lzma：bz2 的生态位基本被 zstd（第三方 `pyzstd`/`zstandard`）取代，标准库里 bz2 主要剩历史包袱。
取舍：海量小文件独立压缩时 lzma 每文件 8MB 字典纯属浪费（压缩后比原文件还大），必须分块或打包合并；lzma 解压内存也要计入读取方容量账。
实战：选型公式 = 压缩次数 × 压缩 CPU + 读取次数 × 解压 CPU + 存储成本 × 压缩比；高频读用 gzip/level 3，冷归档单大文件用 lzma，网络传输热路径推荐 zstd（标准库外的降级路径要写明版本基线）。

```python
import gzip, bz2, lzma, time, os

sample = (b'{"user":"u1","action":"click","ts":"2026-11-21","meta":{"ab":"b"}}\n') * 120_000
MB = len(sample) / 1e6

def profile(name, comp, decomp):
    t0 = time.perf_counter(); blob = comp(); t1 = time.perf_counter()
    out = decomp(blob); t2 = time.perf_counter()
    assert out == sample
    print(f"{name:6s} | 压缩 {t1-t0:5.2f}s | 解压 {t2-t1:5.2f}s | "
          f"压缩比 {len(blob)/len(sample):.3f} | 输出 {len(blob)/1e6:.1f}MB")

profile("gzip6", lambda: gzip.compress(sample, 6), lambda b: gzip.decompress(b))
profile("bz2-9", lambda: bz2.compress(sample, 9), lambda b: bz2.decompress(b))
profile("xz-6", lambda: lzma.compress(sample, preset=6), lambda b: lzma.decompress(b))
profile("xz-0", lambda: lzma.compress(sample, preset=0), lambda b: lzma.decompress(b))

# 小文件场景：lzma 的字典开销让小样本"越压越大"
tiny = b'log line ' * 30  # 270B
for name, c in (("gzip", gzip.compress), ("bz2", bz2.compress),
                ("xz", lambda d: lzma.compress(d, preset=6))):
    blob = c(tiny)
    print(f"小样本({len(tiny)}B) {name}: {len(blob)}B {('膨胀' if len(blob)>len(tiny) else '缩小')}")

# 内存账：xz preset 与字典大小
for p in (0, 3, 6, 9):
    f = lzma.LZMACompressor(preset=p)
    f.compress(b"x" * 1000); f.flush()
    # preset 6 默认字典 8MB：可从 format/filter 链显式看到
print("xz preset 6 字典 8MiB —— 小文件或内存受限容器要显式 preset 降级")

# 解压端内存限制（防止解压炸弹）：LZMADecompressor 支持 max_length
d = lzma.LZMADecompressor()
blob = lzma.compress(sample, preset=0)
first = d.decompress(blob, max_length=1 << 20)
print("xz 解压限流首块:", len(first), "≤", 1 << 20)
```

**追问 1**：为什么海量小文件不适合 lzma？
- 追问 2 层：LZMA 靠字典捕捉长程重复，小输入撑不满字典，压缩比优势消失甚至负收益，且每文件固定启动开销（头+字典初始化）占比过高。
- 追问 3 层：正确做法是先 tar/合并成大流再压缩（tar.xz），或用带分块字典的 zstd skew 大小可调。

**追问 2**：zstd 为什么成了事实标准？
- 追问 2 层：压缩吞吐与解压吞吐都高于 gzip，压缩比接近 lzma，且支持字典训练与多级 preset；但它在标准库之外（pyzstd/zstandard），引入要有降级路径。
- 追问 3 层：跨语言/跨平台交付仍建议 gzip（兼容性保险），内部管道可自由选 zstd。

## 背诵要点
1. gzip 快而省内存、bz2 高压但压缩慢、lzma 压缩比最高但压缩慢+字典 8MB 内存大。
2. 小文件单独 lzma 会膨胀，先合并再压；解压内存也要进读取方容量账。
3. 选型公式：压缩次数×压 CPU + 读次数×解 CPU + 存储成本；热路径倾向 zstd（第三方需降级路径）。

## 复盘追问
1. 审计为什么点名 bz2？——历史合规清单残留；应推动把"算法白名单"从 bz2 更新到 SHA 校验+gzip/xz 组合。
2. 解压端内存怎么监控？——容器 limit + 解压 max_length 双闸，观察 peak RSS 与解压吞吐曲线。
