---
title: [Q5128] 切片拷贝峰值内存账与 islice 规避
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5128 · 切片拷贝的峰值内存账与 islice 规避

> 难度:★★★☆☆ | 标签:容量规划, 内存峰值, 迭代器

**问**:`data[100_0000:200_0000]` 这行"随手切片"在内存峰值账上等于多少？为什么"读 10GB 日志文件"用 `for line in f` 没事、用 `f.readlines()[1000:2000]` 会 OOM？三种规避手段（islice/内存视图/分页）各适合什么场景？

**答**:结论：切片是**浅拷贝容器**——`data[a:b]` 立刻分配一个新 list，把区间内所有元素引用复制进去：峰值 = 原容器 + 新容器引用数组（8B×长度 + 头部）+ 若元素被独占还有对象本体。对千万级 list，一次切片就是几十 MB 的瞬时峰值；对 `str`/`bytes` 切片更是**复制内容本体**，1GB bytes 切一刀瞬时峰值翻倍。`readlines()` 把整个文件物化成 list of str，10GB 文件就是 10GB+ 的对象数组，而 `for line in f` 逐行流式、常数内存。三种规避：a) **islice**：`itertools.islice(f, a, b)` 延迟窗口迭代，适合"只要一个窗口"且顺序可跳过（底层仍是顺序推进，随机窗口要扫过前 a 项）；b) **memoryview**：对 `bytes`/`array` 零拷贝切视图，适合二进制定长记录的随机访问；c) **分页/索引**：数据库游标 fetchmany、文件定长索引，适合真正随机访问。取舍核心：**峰值内存是容量事故的主因，"平均值正常"掩盖不了"峰值翻倍"**——评审时任何大容器上的切片都要问一句"这里多久被调用一次、并发下峰值乘几"。

```python
import sys, itertools, tracemalloc

N = 2_000_000
data = list(range(N))                      # 原容器：引用数组 + 共享小 int（含 -5~256 缓存）

# ---- 1) 切片的瞬时峰值：tracemalloc 实测 ----
tracemalloc.start()
slice_view = data[1_000_000:1_100_000]     # 10 万个引用 -> 新 list
cur, peak = tracemalloc.get_traced_memory()
print(f"list 切片 10 万元素: 峰值 +{peak/1e6:.2f} MB（约 8B/引用 + 头部）")
del slice_view
tracemalloc.stop()

# ---- 2) bytes 切片复制内容本体 vs memoryview 零拷贝 ----
blob = bytes(N)                            # 2 MB
tracemalloc.start()
copy_part = blob[500_000:1_500_000]        # 复制 1MB 内容
cur2, peak2 = tracemalloc.get_traced_memory()
tracemalloc.stop()
mv = memoryview(blob)[500_000:1_500_000]   # 零拷贝视图
print(f"bytes 切片峰值 +{peak2/1e6:.2f} MB；memoryview 视图 +{sys.getsizeof(mv)} B（零拷贝）")
del mv

# ---- 3) islice：流式窗口，不必物化整个 list ----
tracemalloc.start()
window = list(itertools.islice(data, 1_000_000, 1_100_000))   # 只物化窗口
cur3, peak3 = tracemalloc.get_traced_memory()
print(f"islice 取窗口: 峰值 +{peak3/1e6:.2f} MB（与切片同量级，但无需先有全量内存时可用流源）")
tracemalloc.stop()
del window

# ---- 4) 真正的流式来源：文件逐行 vs readlines 物化 ----
import tempfile, os
with tempfile.NamedTemporaryFile("w", delete=False) as f:
    f.writelines(f"line-{i}\n" for i in range(200_000))
    path = f.name
tracemalloc.start()
with open(path) as f:
    head = list(itertools.islice(f, 0, 100))            # 流式前 100 行
cur4, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.start()
with open(path) as f:
    all_lines = f.readlines()[0:100]                    # 先物化 20 万行再切
cur5, peak5 = tracemalloc.get_traced_memory()
print(f"islice(f) 取 100 行: 峰值 {cur4/1e6:.2f} MB vs readlines() 物化全部: 瞬时峰值 {peak5/1e6:.2f} MB")
os.unlink(path)
```

**追问一层**:为什么 list 切片只复制引用也要付"8B×长度"？（容器是引用数组，拷贝的是指针数组；峰值还叠加 list over-allocation 的 append 增长策略）。
**追问二层**:`memoryview` 的坑是什么？（视图持有原 buffer 引用、阻止其释放；`release()` 前原 bytes 不回收；str 无法做视图——文本流没有零拷贝通道，只能靠行迭代）。
**追问三层**:如何在 code review 里制度化防切片峰值事故？（对 >10 万元素的容器切片要求注释容量账；linter 规则标记 `readlines()`、`bytes[:N]` on 大对象；压测加 RSS 峰值断言）。

## 背诵要点
- 切片 = 立即分配新容器：list 峰值约 8B/引用，str/bytes 复制内容本体，峰值可翻倍。
- 规避三件套：islice 流式窗口（顺序访问）、memoryview 零拷贝（二进制）、游标分页（随机访问）。
- 容量事故看峰值不看均值：并发 × 单次峰值才是水位。

## 复盘追问
- 一个"导出接口"在 10 万并发下 OOMKill，代码里有 `readlines()[:1000]`，给出定位与重构步骤。
- `bytes` 用 memoryview 后内存不降，除了忘记 release 还有什么原因？（残留视图对象、cache 引用、引用环）
