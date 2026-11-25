---
title: "[Q5189] lru_cache 装饰实例方法：self 进键导致对象永不释放"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5189 · lru_cache 装饰实例方法：self 进键导致对象永不释放

难度：P7 ｜ 标签：functools、lru_cache、内存泄漏、weakref、缓存作用域

**问**：给 `Service.fetch()` 加了 `@lru_cache(maxsize=None)`，压测两小时后内存单调上涨，实例数量只增不减。缓存不是挂在类上的吗，怎么会拽着实例不放？`cache_clear()` 为什么会影响所有租户？正确做法有哪几种，各自代价是什么？

**答**：
结论：装饰器作用在**函数对象**上，缓存字典的键是 `(self, *args)`。只要缓存里还有条目，键里那个 `self` 就是强引用，实例永远进不了 GC——即使业务代码早就把引用丢了。缓存本身挂在类的函数对象上（所有实例共享一份），所以 `cache_info()` 是全局统计、`cache_clear()` 是全局清空；在多租户/多实例场景里，"清一个实例的缓存"这个操作根本不存在。`maxsize=None` 会让它变成无界字典，等于把泄漏放大到"每个被缓存过的实例都无法回收"。

取舍：三条路。a) 每实例缓存：`__init__` 里 `self._cache = lru_cache(maxsize=8)(self._load)`，闭包绑定实例，实例没了缓存跟着走，代价是每实例一个缓存对象、无法全局统计；b) `WeakKeyDictionary` 或 weakref 键，实例可回收但需要自己实现淘汰；c) 干脆别缓存方法——把需要的纯数据作为参数，缓存模块级纯函数（最容易测、最容易失效）。经验法则：缓存键里只要出现 self，就要回答"谁负责让它失效"。

实战：事故形态是"报表服务每小时新建一个 TenantReporter，缓存命中率很高、内存稳步上涨，重启后恢复"。排查：`Service.fetch.cache_info()` 看到 currsize 等于历史实例数；用 `weakref` 统计存活实例就能确认。下面 200 个实例各调一次方法，标准写法全部存活，自持缓存版本全部释放。

```python
import functools
import gc
import weakref


class User:
    def __init__(self, uid):
        self.uid = uid

    @functools.lru_cache(maxsize=None)  # 键是 (self, arg)：self 被强引用常驻
    def profile(self, section):
        return f"u{self.uid}:{section}"


refs = []
for i in range(200):
    u = User(i)
    u.profile("basic")
    refs.append(weakref.ref(u))
del u
gc.collect()

alive = sum(1 for r in refs if r() is not None)
print("[1] 200 个实例、各调一次方法后仍存活:", alive, "| 缓存条目:", User.profile.cache_info().currsize)


class Fixed:
    def __init__(self, uid):
        self.uid = uid
        self._cache = functools.lru_cache(maxsize=8)(self._load)  # 每实例一份，随实例释放

    def _load(self, section):
        return f"u{self.uid}:{section}"

    def profile(self, section):
        return self._cache(section)


r2 = []
for i in range(200):
    f = Fixed(i)
    f.profile("basic")
    r2.append(weakref.ref(f))
del f
gc.collect()
print("[2] 同规模自持缓存后仍存活:", sum(1 for r in r2 if r() is not None))

User.profile.cache_clear()  # 全局清空：所有实例的缓存一起失效
print("[3] cache_clear 后条目:", User.profile.cache_info().currsize)
print("[4] 命中率统计是全局的:", User.profile.cache_info())
```

**追问一**：为什么 `@cached_property` 没有这个问题？—— 它把结果写进实例自己的 `__dict__`（或 `__slots__` 指定的槽），生命周期与实例完全一致，不做任何全局注册，也不会因为缓存而阻止回收。代价是"失效"要靠 `del obj.__dict__["name"]` 或重新赋值，没有统一的 `cache_clear()`。

**追问二**：多线程下 lru_cache 会重复计算吗？—— 命中/未命中的字典操作是加锁的，但锁不覆盖你的函数体：两个线程同时未命中同一个 key 时，函数会被执行两次，只是最后写入一条。要"只算一次"得自己在外面加 single-flight 锁（按 key 的 `threading.Lock`）或用 `functools.cache` + 幂等函数。

## 背诵要点
- 方法级 `@lru_cache` 的键含 `self`（强引用），条目未清就永不回收；缓存挂在类上，`cache_clear()`/`cache_info()` 是全局的。
- 正解：每实例缓存（`__init__` 里包一层）、weakref 键、或缓存不含 self 的纯函数。
- `maxsize=None` + 长生命周期对象 = 无界泄漏；`cached_property` 随实例走，无此问题。

## 复盘追问
- 压测后内存只涨不降、`cache_info().currsize` 等于历史实例数，如何解释并重构？（self 进键、全局缓存、每实例缓存/weakref）
- 为什么"清某个用户的缓存"用 `cache_clear()` 做不到？多租户下缓存键该怎么设计？（全局清空、按租户分桶或键前缀）
