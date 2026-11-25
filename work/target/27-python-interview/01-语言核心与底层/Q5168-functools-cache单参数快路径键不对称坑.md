---
title: "[Q5168] functools.cache 单参数快路径的键不对称坑"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5168 · functools.cache 单参数快路径的键不对称坑

难度：P7 ｜ 标签：functools.cache、缓存键、CPython 快路径、bool/int/float、NaN

**问**：`@cache` 的单参数调用有一个 CPython 实现级快路径——它并不是把参数一律包成元组。请根据 `f(True)`、`f(1)`、`f(1.0)` 的实际命中情况反推：为什么 `True` 和 `1` **不合并**，而 `True` 和 `1.0` 却会合并、`1` 和 `1.0` 又不合并？传 `list`/`dict` 为什么直接 `TypeError`、`float('nan')` 为什么永不命中？这些语义对"用缓存做幂等/去重"意味着什么，如何用 `cache_info()` 做容量账？

**答**：
结论：CPython 的 `lru_cache`/`cache` 对"恰好一个位置参数、无关键字"走快路径，但**只有参数是 exact `str` 或 exact `int` 时才用裸对象当键**；其他类型（包括 `bool`——它是 `int` 子类但**不是** exact int、`float`、`Decimal`…）统一回退到**元组键 `(arg,)`**。于是出现反直觉的不对称：`f(1)` 的键是裸 `1`（哈希 1），`f(True)` 的键是 `(True,)`（元组哈希，与整数 1 的哈希不同），两者**不同槽位**；`f(1.0)` 的键是 `(1.0,)`，它与 `(True,)` 按 `==` 判同且哈希相同，就会**命中 `True` 槽位**——因为 `1.0 == True`。这就是"值相等却因表示形态不同而不合并、形态相同（都是元组）则因值相等而合并"的根源。不可哈希的 `list`/`dict` 在构造元组键时直接 `TypeError`；`float('nan')` 因 `nan != nan` 破坏判同自反性，**永不命中**，缓存随调用无限增长。

取舍：`@cache` 的键语义是**实现细节 + Python 相等协议的混合产物**，绝不能当"可靠的业务去重器"。用之前审三件事：① 参数类型是否齐全一（把 bool/int/float 归一到同一类型或用 `(type_tag, value)` 元组显式编码，绕开快路径歧义）；② 是否存在 NaN 或自定义 `__eq__` 这种自反性失效的值；③ 键基数是否有界——枚举/状态码适合 `@cache`，用户 ID/请求 ID 必须换有界 `lru_cache(maxsize=N)` 或外部缓存并监控 `currsize`/命中率。

实战：事故形态是"给一个收 `user_id` 的函数加 `@cache` 做优化，内存随 UV 线性上涨"——`cache_info().currsize` 是最直接的证据；另一个隐蔽事故是"开关/状态码混用 bool 与 int，缓存按形态分叉导致同一逻辑参数走两条分支"。下面用 `gc.get_referents` 内省内部字典键，把快路径的不对称直接暴露出来。

```python
from functools import cache
import gc

calls = []
@cache
def f(x):
    calls.append(x)
    return repr(x)

for v in (True, 1, 1.0, True, 1, 1.0):
    print(f"f({v!r:>6}) -> {f(v)!r:>6}  currsize={f.cache_info().currsize} hits={f.cache_info().hits}")
print("calls:", calls)   # 只有两次真实计算：True 与 1 各自成键

# 1) 内省内部字典：看 "裸 int 键" 与 "元组键" 的形态差异
for obj in gc.get_referents(f):
    if isinstance(obj, dict) and any(isinstance(k, tuple) for k in obj):
        print("internal keys:", [(type(k).__name__, repr(k)) for k in obj.keys()])
        break

g = cache(lambda y: y)          # 对照：单 int 参数走裸键快路径
g(1)
for obj in gc.get_referents(g):
    if isinstance(obj, dict) and obj:
        print("int-fast-path keys:", [(type(k).__name__, repr(k)) for k in obj.keys()])
        break

# 2) 不可哈希参数 -> 构造元组键时 TypeError
try:
    f([1, 2])
except TypeError as e:
    print("unhashable:", type(e).__name__, "->", str(e)[:50])

# 3) NaN 自反性失效 -> 永不命中
n = float("nan")
before = f.cache_info().currsize
f(n); f(n); f(n)
print("nan added:", f.cache_info().currsize - before, "(三次调用都是 miss)")

# 4) 容量账与归一化防线
print("cache_info:", f.cache_info())
@cache
def normalized(kind, value):
    calls.append((kind, value))
    return (kind, value)
for k, v in (("bool", True), ("int", 1), ("float", 1.0)):
    normalized(k, v)
print("normalized keys:", calls[-3:], "(三个独立槽位，语义清晰)")
```

**追问一**：为什么快路径只对 exact `str`/`int` 用裸对象当键、对 `bool` 却回退到元组？——这是 CPython 的性能优化：exact 类型是常见情形，裸对象做键省掉一次元组分配；但用 `PyLong_CheckExact` 这类精确判定，`bool`（`int` 子类）不通过，于是走通用路径 `(args,)`。收益是常见路径更快，代价是键形态敏感——`True` 与 `1` 因为"一个是元组键、一个是裸键"而分道扬镳。这是实现细节泄漏到语义的典型例子，所以文档从不承诺 `True`/`1` 的合并行为。

**追问二**：这种"同值不同键"什么时候会造成真实 bug 而不是仅仅多算一次？——当函数对参数类型有分支时：`def f(x): return "bool" if isinstance(x, bool) else "num"`，`f(True)` 缓存的是 "bool"，`f(1.0)` 命中的是 `(True,)` 槽位却拿到 "bool"（因为 `1.0 == True`），而语义上它该是 "num"——**跨类型同键串了分支结果**。反过来 `f(1)` 独立成键又是对的。结论：带类型分支的纯函数不能用 `@cache` 裸缓存，必须先归一化参数。

## 背诵要点
- `cache` 单参数快路径：exact `str`/`int` 用裸对象作键，其他类型（含 `bool`、`float`）用 `(arg,)` 元组键。
- 后果：`True` 与 `1` 不同键，但 `True` 与 `1.0` 合并（`(True,)==(1.0,)`）、`1` 与 `1.0` 不合并；未文档化的实现细节。
- 不可哈希参数 → TypeError；NaN 自反性失效 → 永不命中；`cache_info().currsize` 做容量账，高基数换有界缓存，类型分支先归一化。

## 复盘追问
- 开关参数有时传 bool 有时传 1，缓存结果串了分支，如何用快路径键形态解释并修复？（裸键 vs 元组键的不对称、`1.0==True` 合并，讨论归一化 `(type_tag, value)`）
- 为什么 `functools.cache` 不能当请求去重器？（键基数无界、不可哈希载荷报错、相等但不同业务请求会被错误合并；显式幂等键 + 存储约束 + TTL 才是正解）
