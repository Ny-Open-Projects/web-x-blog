---
title: [Q5071] tracemalloc 快照对比定位内存增长事故
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5071 · tracemalloc 快照对比定位内存增长事故

> 难度:★★★☆ | 标签:事故复盘, 内存, tracemalloc

**问**：服务灰度新版本后 RSS 每天涨 200MB，`gc` 没有可见的对象环增长，怎么用 tracemalloc 的快照对比把泄漏点定位到代码行？快照对比的正确姿势和常见误判有哪些？

**答**：结论：tracemalloc 是唯一能把"分配调用栈"和"字节数"关联起来的标准库工具，用法是三步：`start()` 后在疑似泄漏阶段取 `take_snapshot()`，隔一段时间再取一次，`compare_to(old, key_type='lineno')` 看**增量**而不是绝对量，再用 `statistics.filter` 按文件名收敛。关键取舍：a) tracemalloc 开销约 2 倍分配耗时 + 每 1MB 实际内存约 2 倍追踪内存（存帧栈），生产只能低流量实例或压测环境开，用 `PYTRACEMALLOC` 环境变量或 `start(nframe)` 限制栈深（默认 1 帧，3 帧通常够定位）；b) **常见误判一**：只看 lineno 统计会把"分配点"当"泄漏点"——分配发生在缓存里、对象其实被复用，要配合 `gc.get_referrers` 确认对象是否真的存活（见既有 Q5021 的 referents 手法）；c) **误判二**：C 扩展/原生内存（比如带 Rust 核心的 Pydantic v2、numpy buffer）不经过 Python 分配器，tracemalloc 看不到，RSS 涨但快照平稳时要转向 malloc 级工具（valgrind massif / jemalloc profiling，参见既有 Q5030 PYTHONMALLOC）；d) 快照对比要保证"负载形态一致"，请求样本不同会把正常缓存预热误报为泄漏。实战：把"涨 200MB"翻译成代码行：先在压测环境重放同一批请求 1000 次，前后快照 diff 的 top3 行基本就是元凶。

```python
# file: code/01_语言核心与底层/q5071_tracemalloc_diff.py
import tracemalloc, gc, sys

tracemalloc.start(3)          # 记 3 层调用栈, 默认 1 帧不够定位

def leak_step(store):         # 模拟泄漏: 每步多留 1000 个未释放对象
    store.append([bytes(256) for _ in range(1000)])

store = []
for _ in range(5):
    leak_step(store)
snap1 = tracemalloc.take_snapshot()

for _ in range(5):
    leak_step(store)
snap2 = tracemalloc.take_snapshot()

diff = snap2.compare_to(snap1, key_type="lineno")
print("== 增量 Top3(按行) ==")
for s in diff[:3]:
    print(f"{s.size_diff/1024:8.1f} KB  {s.count_diff:6d} 块  {s}")

# 按文件过滤: 只看业务代码所在模块的增量
leaks = [s for s in diff if "q5071" in str(s.traceback)]
print("业务文件相关增量合计(KB):", sum(s.size_diff for s in leaks) / 1024)

# 误判校验: 增量对象是否真的存活? 用 gc 找 referrer
big = [o for o in gc.get_objects() if isinstance(o, list) and len(o) == 1000]
print("存活的 1000 元素 list 数:", len(big), "(>0 才是真泄漏, 0 说明只是复用)")

tracemalloc.stop()
cur, peak = tracemalloc.get_traced_memory() if tracemalloc.is_tracing() else (0, 0)
print("追踪内存在 stop 前应归零:", cur, peak, "| python:", sys.version.split()[0])
```

**追问**：1) `nframe` 取多少合适？——1 帧只能给"分配行"，无法回答"谁调用的"；3 帧一般够，但调用栈深的框架（asyncio 任务链）要 5+，且 nframe 越大追踪内存与 CPU 开销越大，生产压测建议先用 1 帧确认哪行涨、再开 5 帧看调用链。2) compare_to 用 lineno 还是 traceback 差别？——lineno 把同一行聚合，适合"哪一行在涨"；traceback 保留完整栈，适合"这条路径是谁触发的"；定位顺序是先 lineno 收敛行、再 traceback 定路径。3) 快照平稳但 RSS 仍涨怎么办？——两种可能：内存碎片/分配器 arena 不还（`PYTHONMALLOC=malloc` + jemalloc 验证，见 Q5030/Q6029），或原生内存泄漏（Pydantic-core、DB 驱动的 C 层），tracemalloc 的口径只覆盖 Python 对象。

## 背诵要点
- tracemalloc 三步：start(nframe) → 两次 take_snapshot() → compare_to(old, key_type="lineno") 看增量，top 行即嫌疑代码。
- 开销约 2 倍分配耗时 + 约 2 倍追踪内存；默认 1 帧，定位调用链用 3-5 帧；生产只在低流量实例或压测环境开。
- 两个盲区：分配点≠泄漏点（配 gc.get_referrers 验存活）；C 扩展原生内存不在口径内，转 malloc 级工具。

## 复盘追问
- 你们上一次内存事故是怎么定位的？有没有"快照涨了但对象其实被缓存复用"的误判经历？（提示：diff top 行 + get_referrers 验存活，两步都做再下结论）
- 如果涨的内存来自 pydantic-core / numpy 这类原生层，tracemalloc 会显示什么？你的下一板斧是什么？（提示：快照平稳但 RSS 涨 → PYTHONMALLOC=malloc + jemalloc profiling）
