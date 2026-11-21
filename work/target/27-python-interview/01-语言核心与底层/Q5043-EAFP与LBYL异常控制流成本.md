---
title: [Q5043] EAFP vs LBYL：异常控制流的成本账
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5043 · EAFP vs LBYL：异常控制流的成本账

> 难度:★★★ | 标签:EAFP, LBYL, 异常, 成本工程, timeit

**问**：团队规范争论：热路径里该用 `try/except KeyError`（EAFP）还是 `if key in d`（LBYL）？3.11 的零开销异常（Q1260）改变了什么？除了性能，还有哪些正确性维度要一起权衡？

**答**：成本结论分三段：1) **3.11+ 零开销异常后，try 块本身几乎免费**（编译成异常表，不进 try 就没有成本）；2) **成本全部在"真的抛出"**：抛异常要走 unwind、构造 traceback、查异常表，单次微秒级（对照 LBYL 的 `in` 检查是几十 ns）；3) 所以选择只取决于**命中率**：key 几乎总存在 → EAFP 更快（省掉每次的 in 检查）；经常缺失（如缓存 miss 率高）→ LBYL/`.get()` 更快。**正确性维度比性能更重要**：a) EAFP 的 except 可能把你不想捕的异常也捕了（try 块里其他行的 KeyError），必须缩窄 try 范围；b) LBYL 的 check-then-act 有 TOCTOU 竞态（`in` 之后、取值之前被并发删除）——多线程下 EAFP 天然原子性更强；c) `.get()`/`setdefault` 是两态合一，无竞态也无异常，但"缺失"与"值本身为 None"无法区分时要用哨兵（Q1282）。3.12 起 `except*`/异常表继续演进，但选择逻辑不变。实战规范：单线程纯内存查找看命中率选；跨线程/跨进程边界一律 EAFP 或原子 API；异常不应做常规控制流（每秒百万次 miss 的场景用哨兵/特殊返回值）。

```python
# file: code/01_语言核心与底层/q5043_eafp_cost.py
import timeit
import sys

d = {f"key{i}": i for i in range(1000)}
HIT, MISS = "key500", "nokey"          # 高命中场景 / 高缺失场景

def eafp(k):
    try:
        return d[k]
    except KeyError:
        return -1

def lbyl(k):
    if k in d:
        return d[k]
    return -1

def via_get(k):
    v = d.get(k, _SENT)                # 哨兵区分"缺失"与 None
    return -1 if v is _SENT else v

_SENT = object()

def bench(fn, arg, n=200_000):
    t = timeit.timeit(lambda: fn(arg), number=n)
    return t / n * 1e9

print(f"{'场景':<10}{'EAFP ns':>10}{'LBYL ns':>10}{'.get ns':>10}")
for name, arg in (("高命中", HIT), ("高缺失", MISS)):
    print(f"{name:<10}{bench(eafp, arg):>10.0f}{bench(lbyl, arg):>10.0f}{bench(via_get, arg):>10.0f}")

# 正确性维度1: except 范围过宽会误伤
def fragile(items):
    total = 0
    try:
        for it in items:               # 这里的 KeyError 可能来自 it["x"]
            total += d[it]             # 也可能来自 d[it] —— 分不清
    except KeyError:
        return -1
    return total
print("宽 try 误伤示例:", fragile(["key1", "bad"]))   # 内层 key 错误也被吞

# 正确性维度2: LBYL 的 TOCTOU —— 单线程下无害, 并发下 check 与 act 之间可被删
# 正确性维度3: .get() + 哨兵 一次完成, 无竞态无异常
print("哨兵 get:", via_get(MISS), "| python:", sys.version_info[:2])
```

**追问**：1) 3.11 之前（如 3.8 服务仍在维护）EAFP 的成本结构有什么不同？——3.10- SETUP_FINALLY/POP_BLOCK 是真实字节码开销，try 块本身有成本，但抛出路径成本量级相同；结论方向不变、差距缩小。2) 为什么"异常不应做常规控制流"除了性能还有可观测性原因？——抛异常会创建 traceback（持有帧引用，Q424 的内存滞留），高频异常让错误监控噪声化，真故障被淹没；用哨兵/Optional 把"预期缺失"从异常通道剥离。3) `d.get(k)` 返回 None 的坑在什么业务里最容易爆？——值本身可能为 None/0/"" 的场景（falsy 判断），必须用哨兵或 `k in d` 显式区分缺失。

## 背诵要点
- 3.11+ try 块零开销，成本集中在抛出路径（微秒级 vs in 检查几十 ns）。
- 命中率高选 EAFP、缺失率高选 LBYL/get；并发边界选 EAFP 或原子 API（TOCTOU）。
- "缺失"与 None 值区分用哨兵对象；预期内缺失走哨兵不走异常通道。

## 复盘追问
- 你如何用一次基准测试结束团队的 EAFP/LBYL 争论？（提示：先统计线上真实命中率，再按命中率分档跑 bench，用数据落规范）
- 高频 miss 的缓存层改哨兵返回后，哪些监控指标应该同步调整？（提示：异常率指标含义变化、traceback 内存滞留消失）
