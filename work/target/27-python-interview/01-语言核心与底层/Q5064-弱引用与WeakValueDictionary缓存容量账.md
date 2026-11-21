---
title: [Q5064] 弱引用与 WeakValueDictionary 缓存的容量账
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5064 · 弱引用与 WeakValueDictionary 缓存的容量账

> 难度:★★★★ | 标签:容量规划, weakref, 缓存, 生命周期

**问**：用全局 dict 做对象缓存，对象明明没人用了 RSS 却不降。为什么 dict 持有强引用会导致"永不回收"？`weakref.WeakValueDictionary` 怎么解决？它能缓存所有对象吗？容量上限又该怎么控？

**答**：结论：强引用缓存 = 缓存条目数 × 单对象内存，没有淘汰策略就是**只增不减的内存水位**。`WeakValueDictionary` 的 value 侧持弱引用：外部没有别的强引用时，对象被 GC，条目自动消失——它解决的是"**生命周期跟随使用者**"的缓存语义（调用方还活着就命中，死了自动清），但注意它解决的是"不泄漏"，不是"限容量"：**没有 TTL、没有 LRU、没有大小上限**，只要对象活着它就都在。三个限制：a) 不是所有对象可弱引用——list/dict/set/int/str 等内置容器和基础类型直接 `weakref.ref` 会 TypeError（要么子类化，要么用 `__slots__ = ('__weakref__',)` 补槽，slots 类默认不可弱引用）；b) WeakKeyDictionary 对 key 做弱引用，key 必须可哈希且弱引用对象比较稳定（eq 与 hash 不随生命期变的对象）；c) 弱引用回调 `callback` 在解释器关闭阶段不可靠。容量规划：要上限就用 `functools.lru_cache(maxsize)`（见既有 Q5015 内存画像）或带 TTL 的容器；WeakValueDictionary 适合"元数据/共享句柄表"这类由业务方持有主引用的场景。实战：给弱引用缓存加监控——`sys.getrefcount` 采样 + `len(wd)` 曲线，条目数随流量波动说明语义正确，只涨不跌说明有隐藏强引用（典型：注册到类属性/闭包/日志对象里）。

```python
# file: code/01_语言核心与底层/q5064_weakref_cache.py
import gc, weakref, sys

class Big:
    __slots__ = ("payload", "__weakref__")   # 补 __weakref__ 槽才可弱引用
    def __init__(self, n=100_000):
        self.payload = bytearray(n)      # ~100KB/个

# 1) 强引用缓存: 只增不减
strong = {}
for i in range(5):
    strong[i] = Big()
print("强引用缓存 RSS 占用(对象字节):", sum(sys.getsizeof(o.payload) for o in strong.values()))
strong.clear()
gc.collect()
print("clear 后无可达强引用 -> 可回收")

# 2) WeakValueDictionary: 外部引用死, 条目自动消失
wd = weakref.WeakValueDictionary()
obj = Big()
wd["a"] = obj
print("有外部引用: 条目数 =", len(wd))
del obj
gc.collect()
print("删除外部引用: 条目数 =", len(wd))   # 0, 自动清理

# 3) 不可弱引用的类型: 直接炸
try:
    weakref.ref([1, 2, 3])
except TypeError as e:
    print("list 不可弱引用:", e)

class Slots:
    __slots__ = ()          # 默认无 __weakref__ 槽
try:
    weakref.ref(Slots())
except TypeError as e:
    print("slots 类默认不可弱引用:", e)

class WeakOk:
    __slots__ = ("__weakref__",)
print("补 __weakref__ 槽后:", weakref.ref(WeakOk()) is not None)

class NoWeak:
    __slots__ = ()          # 未补槽: 仍不可弱引用
try:
    weakref.ref(NoWeak())
except TypeError as e:
    print("未补槽仍不可弱引用:", e)

# 4) 弱引用缓存命中语义: 活着命中, 死了 miss
cache = weakref.WeakValueDictionary()
user = Big(1_000)
cache["k"] = user
print("命中:", cache.get("k") is user)
del user; gc.collect()
print("外部死了:", cache.get("k"))
```

**追问**：1) WeakValueDictionary 与 lru_cache 的本质区别？——语义相反：lru_cache 是"缓存持有主引用、使用者借走"（maxsize 控容量）；WeakValueDictionary 是"使用者持主引用、缓存只记账"（无上限但随主引用消亡）。选错语义就会要么泄漏要么永远 miss。2) 为什么 int/str 不可弱引用？——小对象走驻留/缓存池，弱引用管理器（C 层回调链）需要稳定的对象头布局，基础类型为性能不做弱引用槽；需要弱引用语义就包一层对象（例如存包装类的实例）。3) 弱引用回调里再创建对原对象的引用会怎样？——callback 收到的只是 ref，若在回调里复活对象（危险操作），依赖解释器状态，CPython 不保证语义，禁止这样做。

## 背诵要点
- 强引用缓存只增不减；WeakValueDictionary value 弱引用：外部引用消失条目自动清理，语义是"跟随使用者"，无 TTL/上限。
- list/dict/int/str 与默认 slots 类不可弱引用；slots 类补 `__weakref__` 槽可解。
- 只涨不跌的 len(wd) 曲线 = 有隐藏强引用；要上限选 lru_cache(maxsize)/TTL 容器，选错语义就泄漏或永远 miss。

## 复盘追问
- 你们的全局缓存 dict 有没有 maxsize/TTL？RSS 水位曲线和缓存条目数是否同步上涨？（提示：tracemalloc 定位持有者，grep 类属性/闭包/单例里的隐藏引用）
- 有没有 WeakValueDictionary 语义选错的情况——该"缓存持主引用"的场景用了弱引用导致命中率崩零？（提示：对照两容器语义矩阵与命中率监控）
