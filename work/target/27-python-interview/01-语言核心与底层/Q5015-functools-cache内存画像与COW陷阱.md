---
title: [Q5015] functools.cache vs lru_cache：内存画像与可变参数陷阱
date: 2026-11-19
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5015 · functools.cache vs lru_cache

> 难度:★★☆ | 标签:缓存, 内存治理

**问**：`functools.cache` 和 `lru_cache(maxsize=None)` 有什么区别？为什么说它们缓存**参数元组**而不缓存「逻辑参数」——`lru_cache` 装饰的方法里 `self` 会造成什么事故？怎么给缓存画像和设限？

**答**：`cache` 就是 `lru_cache(maxsize=None)` 的快捷写法，但语义定位不同：`cache` 声明「结果集有限」（如读配置、解析固定正则），永不淘汰；`lru_cache` 声明「热点局部性」，可淘汰。核心陷阱是**键的构成**：装饰器把**每次调用的全部实参**打包成键（含 `self`/`cls`、默认值差异、位置 vs 关键字形式都算不同键）：① 缓存实例方法 = 每个对象一份结果 + 对象生命周期内永不释放（self 被键引用，`lru_cache` 还会阻止对象被 GC）——生产事故高发；解法：模块级函数带显式 key、或 `@functools.lru_cache` 放在 `__init__` 外的方法上时手动 `cache_clear`，或用 `methodcaller` 风格拆分。② 可变默认值：`f(x=[])` 与 `f(x=())` 键不同但都安全；真正的坑是调用时传的**同一个可变对象**被原地修改后，键里的内容变了而缓存还在——所以可变对象作参数时先转 tuple/frozenset。③ 画像：`cache_info()` 看 hits/misses/c currsize，命中率低+currsize 高 = 键空间过大，直接判死刑。

```python
# 全部标准库，任何 3.x 版本可跑
import functools, sys, gc

@functools.lru_cache(maxsize=128)
def slow_query(sql: str, params: tuple) -> tuple:
    return (sql, params, "result")

@functools.cache                      # 等价 lru_cache(maxsize=None)
def compile_pattern(p: str):
    import re
    return re.compile(p)

for _ in range(3):
    compile_pattern(r"\d+")           # 命中 2 次
print(compile_pattern.cache_info())   # hits=2, currsize=1 —— 结果集有限场景用 cache

# 事故现场：缓存实例方法 → self 进键 → 对象无法回收
class Report:
    @functools.lru_cache(maxsize=None)
    def build(self, n: int) -> str:
        return f"report{n}"
reports = [Report() for _ in range(100)]
for r in reports:
    r.build(1)
print("cache_info:", Report.build.cache_info())   # currsize=100：每个实例一份
ids_before = {id(r) for r in reports}
del reports
gc.collect()
print("实例是否被缓存钉死:", Report.build.cache_info().currsize, "个键仍持有 self")
# currsize 仍=100 → 100 个 Report 对象全部无法 GC（内存泄漏）
Report.build.cache_clear()            # 修复：清空或改用模块级函数 + 显式 key

# 画像 → 判死刑示例：键空间爆炸
@functools.lru_cache(maxsize=256)
def bad_key(x: int, ts: float) -> int:
    return x
for i in range(500):
    bad_key(i, i * 0.001)             # ts 每次不同 → 键几乎不重复
info = bad_key.cache_info()
print("bad_key:", info)
assert info.hits == 0 and info.currsize == 256   # 命中率 0，缓存纯开销
```

**追问**：1) 为什么 `f(1)` 和 `f(x=1)` 是两个键？——键用 `self._make_key(args, kwds, typed)`：位置参数与关键字参数分别记录，`typed=True` 时还区分 `1`/`1.0`；这让键构造有成本（所以热路径缓存要先算收益）。2) maxsize 怎么定？——键空间的帕累托分布：用 `cache_info()` 观测 misses 递减斜率，斜率趋平时 currsize 即合理 maxsize；never-expire 的 cache 只许用于「可枚举有限键」。3) 线程安全吗？——`lru_cache` 内部有锁（Rlock），并发安全但高争用下锁是热点；3.12+ 对常用路径做了无锁快路径优化。

## 背诵要点
1. cache = lru_cache(maxsize=None)，语义分工：有限结果集用 cache、热点局部性用 lru_cache。
2. 缓存键 = 全部实参打包（含 self）：实例方法缓存 = 对象泄漏 + 每实例一份结果。
3. 画像口径：cache_info() 命中率 0 + currsize 满 = 键空间爆炸，缓存是负收益。

## 复盘追问
1. 缓存方法上带 `self` 的正确改造方案有哪些，各有什么代价？（提示：拆模块级函数/显式 key 参数/weakref 键/生命周期挂钩 cache_clear）
2. lru_cache 的锁在 no-GIL 构建下会变成什么瓶颈？（提示：全局锁争用放大，考虑 per-key 分片锁或换成外部缓存）
