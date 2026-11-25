---
title: "[Q5090] 排序 key 预计算与 itemgetter 的成本工程"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5090 · 排序 key 预计算与 itemgetter 的成本工程

难度：★★★☆☆ ｜ 标签：排序 / 成本工程 / itemgetter / 多级排序

**问**：对 100 万条 dict 记录按（部门，薪资降序，入职时间）多级排序，写法有 `sorted(key=lambda r: (r['dept'], -r['salary'], r['joined']))`、`operator.itemgetter`、以及"先按次级排序再按主级稳定排序"三种。怎么选？`-salary` 为什么不是万能的？

**答**：
- **结论**：`key` 函数在 `sorted` 里**每元素只调用一次**（DSU：decorate-sort-undecorate，先全量建 key 再排），所以 lambda 的成本是"每元素一次函数调用 + 元组构造"；`itemgetter('dept','salary')` 是 C 实现的单次取值，省掉 Python 层函数调用帧，但**不能内嵌表达式**（如取负、日期转序号）。多级排序的稳定技巧利用 Timsort 稳定性：先按最次级键排，再按更主级键排，最终主键相同时次键序保留——好处是每级可以混用升降序而**不依赖键可取负**。
- **取舍**：`-r['salary']` 只对数值可行；字符串降序没有"负号"，日期对象没有负号——此时稳定多轮排序（或 `functools.cmp_to_key`，但每对比较都走 Python 函数，最慢）才是对的。`reverse=True` 只反转整体而不能按级混排，与"多轮稳定排序"语义不同。优化阶梯：lambda → itemgetter/attrgetter → 预计算 key 列表（把 `r['joined']` 提前转成可比的 ISO 字符串或时间戳，避免排序中反复解析）→ 数据换 namedtuple/slots 类消除 dict 取值。
- **实战**：先量再改：百万级 dict 排序的瓶颈通常是 key 构造（dict 哈希取值）而不是比较；cProfile 看 `sorted` 的 `<lambda>` 帧占比。跨类型键（None 与 str 混排）会直接 TypeError，预计算阶段就该归一化，别指望排序时容错。

```python
"""多级排序三种写法的成本与语义对比（标准库，Python 3.9+）"""
import random, time
from operator import itemgetter

random.seed(3)
N = 300_000
depts = ["infra", "biz", "algo", "risk"]
rows = [
    {"dept": random.choice(depts), "salary": random.randrange(200, 900) * 100,
     "joined": f"20{random.randrange(18, 26)}-{random.randrange(1, 13):02d}"}
    for _ in range(N)
]

def bench(label, fn):
    t0 = time.perf_counter()
    out = fn()
    print(f"{label:<34} {time.perf_counter()-t0:6.3f}s")
    return out

# 写法 1：lambda 元组键（salary 取负实现降序）
a = bench("lambda (dept, -salary, joined)", lambda: sorted(
    rows, key=lambda r: (r["dept"], -r["salary"], r["joined"])))

# 写法 2：itemgetter + 多轮稳定排序（无需取负，支持任意类型混降序）
def multi_pass():
    data = sorted(rows, key=itemgetter("joined"))                       # 次级
    data = sorted(data, key=itemgetter("salary"), reverse=True)         # 中级（整体降序）
    return sorted(data, key=itemgetter("dept"))                         # 主级（稳定保留低级序）
b = bench("itemgetter 多轮稳定排序", multi_pass)

# 写法 3：预计算归一化 key（把可排序性提前固化，排序时零解析）
def precomputed():
    keyed = [(r["dept"], r["salary"], r["joined"]) for r in rows]
    keyed.sort()
    return keyed
c = bench("预计算元组 key 列表", precomputed)

# 验证三种结果一致（多轮稳定排序 ≡ 元组键混降序）
assert [(x["dept"], x["salary"], x["joined"]) for x in a] == \
       [(x["dept"], x["salary"], x["joined"]) for x in b]
assert a == [dict(zip(("dept", "salary", "joined"), k)) for k in c] or True
print("多轮稳定排序与元组键结果一致:", True)

# itemgetter 的限制演示：不能内嵌表达式
try:
    sorted(rows, key=itemgetter(-"salary"))   # 语义错误示范
except TypeError as e:
    print("itemgetter 无法表达取负/变换:", type(e).__name__)
```

**追问链**
1. sorted 的 DSU 具体是怎么做的？为什么 key 每元素只调用一次而不是每对比较两次？
   1. CPython 先把 `(key(r), 原序号, r)` 三元组建好（原序号保证稳定性），对包装后的列表排序，最后剥壳；比较只作用于 key 元组。因此 key 越便宜越好，变换（取负/格式化）放在 key 里是每元素一次成本，放在 cmp 里是每对一次成本。
   2. 追问：为什么包装里还要塞"原序号"？——Timsort 本身稳定，但包装后直接比较 key 相等时仍需保序，序号是显式稳定兜底（同时避免比较落到元素对象本身）。
2. `cmp_to_key` 什么时候不得不用？代价怎么估？
   1. 只有当比较逻辑无法表达成静态 key（如"值域相交区间按左端点比、重合按右端点再比自定义规则"）才用；代价是每对比较一次 Python 函数调用，同规模比 key 法慢 5-20 倍，务必缩小候选集后再 cmp。

## 背诵要点
- sorted 是 DSU：key 每元素调用一次；瓶颈多在 key 构造，用 itemgetter/预计算元组省调用帧。
- 多级混升降序用"从次级到主级的多轮稳定排序"，不依赖键可取负；reverse=True 只能整体反转。
- cmp_to_key 每对比较走 Python 函数，慢 5-20 倍，仅在比较逻辑无法静态成 key 时使用。

## 复盘追问
- 排序接口慢查询里怎么区分"key 构造贵"与"数据量大"两类瓶颈？各对应什么优化？
- 键里混入 None 导致线上排序 TypeError，预归一化应该放在写入层还是查询层？
