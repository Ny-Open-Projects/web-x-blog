---
title: [Q5127] 微基准 timeit 方法论与常见坑
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5127 · 微基准 timeit 方法论与常见坑

> 难度:★★★★☆ | 标签:成本工程, timeit, 基准方法

**问**:"我在 notebook 里 `%timeit` 测出 dict 比 list 快"——这句话可能错在哪几个环节？`timeit` 默认为什么关 GC？取平均值还是最小值？如何避免"基准测的是优化器"？

**答**:结论：微基准的正确姿势是**最小化方差来源 + 只报告可复现的数字**。四个常见坑：a) **GC 噪音**：`timeit` 默认 `gc.disable()`，而生产代码是开着 GC 的——比较两种数据结构时，若其中一种产生大量循环垃圾（如树、引用环），关 GC 的基准会系统性失真；要么显式 `gc.enable()` 对齐生产，要么单独做 GC 开销实验。b) **取值方法**：多次 `repeat` 后**取最小值**（variance 修正，docs 官方建议），不是平均——平均值被系统毛刺抬高，最小值代表"无干扰上限性能"。c) **测量对象漂移**：setup 里建好的对象会被特化/缓存（属性内联缓存、代码对象特化），首轮偏慢；全局变量访问比局部慢（LOAD_GLOBAL vs LOAD_FAST），把被测代码放进函数再测。d) **优化器吃掉被测代码**：纯计算且结果未消费的循环可能被常量折叠，必须把结果累加/传出。取舍：微基准只回答"实现 A vs 实现B"的常数差，回答不了"线上会不会快"——后者用生产画像（cProfile/perf 火焰图）确认热点再回来测，顺序不能反。

```python
import timeit, gc, sys

# ---- 被测代码必须放函数里（LOAD_FAST 局部变量），结果必须被消费 ----
def bench_join(n=1000):
    parts = ["a"] * n
    return "".join(parts)

def bench_concat(n=1000):
    s = ""
    for p in ["a"] * n:
        s += p                 # CPython 对 += 有_str 加速，但整体仍慢于 join
    return s

# ---- 1) repeat 多次取 min（官方建议），不是 mean ----
t_join = min(timeit.repeat(lambda: bench_join(1000), number=2000, repeat=5))
t_cat  = min(timeit.repeat(lambda: bench_concat(1000), number=2000, repeat=5))
print(f"join: {t_join:.4f}s | concat: {t_cat:.4f}s | join 快 {t_cat/t_join:.1f}x（取 min）")

# ---- 2) GC 开关的系统性影响：产生循环垃圾的结构 ----
class Node:
    def __init__(self):
        self.parent = None
def build_ring(n):
    prev = first = Node()
    for _ in range(n):
        cur = Node(); cur.parent = prev; prev = cur
    prev.parent = first        # 成环 -> 只能靠 GC 回收
    return prev

def with_gc(fn, n):
    gc.enable(); gc.collect()
    t = min(timeit.repeat(lambda: fn(n), number=20, repeat=3))
    gc.collect(); return t

def with_gc_off(fn, n):
    gc.disable()
    t = min(timeit.repeat(lambda: fn(n), number=20, repeat=3))
    gc.enable(); return t

g_on  = with_gc(build_ring, 2000)
g_off = with_gc_off(build_ring, 2000)
print(f"建环 + GC开: {g_on:.4f}s | GC关: {g_off:.4f}s —— 差值即分代回收的摊销成本")

# ---- 3) 常量折叠陷阱：未消费的纯计算被编译期折叠 ----
f_folded = timeit.timeit("sum(range(1000))", number=100_000)      # 正常
f_trap   = timeit.timeit("for _ in range(1000): pass", number=100_000)
print(f"消费结果 {f_folded:.3f}s vs 空循环 {f_trap:.3f}s —— 若后者'快得离谱'说明测的是空转")

# ---- 4) 报告规范：贴上 number/repeat/机器环境 ----
print(f"环境: {sys.version.split()[0]}, number=2000, repeat=5, 取 min")
```

**追问一层**:`timeit.repeat(number=N, repeat=5)` 和 `number=5N, repeat=1` 哪个更可信？（前者——方差来自外部干扰，短切片多次取 min 更抗毛刺；但也别太短，首轮特化开销要被 number 摊掉）。
**追问二层**:怎么测"分配成本"而不是"回收成本"？（`gc.disable` + `tracemalloc` 测分配路径；回收摊销用 gc callbacks/`gc.set_debug` 统计；两者分开报告）。
**追问三层**:为什么生产决策要用 macro-benchmark（压测端到端 P99）验证微基准结论？（特化/缓存行为随调用形态变化，常数级优势可能被 IO、锁、缓存未命中掩盖；微基准只筛掉明显差实现）。

## 背诵要点
- timeit 默认关 GC；比较含循环垃圾结构时必须 `gc.enable()` 对齐，否则系统性失真。
- repeat 多次取 min（官方建议），number 要够大摊掉首轮特化；被测代码放函数、结果必须消费。
- 微基准只比常数差，上线决策以压测 P99/生产火焰图为准。

## 复盘追问
- 有人说 notebook 里 join 比 concat 快 10 倍，你复测只有 1.2 倍，列出三个可能原因并给复现实验。
- 如何为团队制定"提交性能优化 PR 必须附基准"的规范模板？（number/repeat/环境/生产热点关联四要素）。
