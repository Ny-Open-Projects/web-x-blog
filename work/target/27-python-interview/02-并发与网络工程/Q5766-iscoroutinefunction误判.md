---
title: "[Q5766] iscoroutinefunction 的误判：装饰器、partial 与“协程未 await”"
date: 2026-11-25
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5766 · iscoroutinefunction 的误判：装饰器、partial 与“协程未 await”

难度：P6 ｜ 标签：inspect、iscoroutinefunction、装饰器、markcoroutinefunction、functools.wraps、FastAPI

基线：CPython 3.12.2，纯标准库；用同步装饰器包裹 `async def`，对比 `iscoroutinefunction`、`inspect.unwrap`、`markcoroutinefunction` 与 `isawaitable`。

**问**：给一个 FastAPI 的 `async def` 接口加了一个同步的耗时统计装饰器，内部用 `functools.wraps` 保留了原函数信息。上线后该接口全部 500，日志里只有一句 `coroutine 'handler' was never awaited`；把装饰器去掉就正常。另一个团队把 `async def __call__` 的类实例注册成路由，框架判断"不是协程函数"后直接调用，同样不 await。`functools.wraps` 不是保留了吗，为什么还判断错？`iscoroutinefunction` 到底看什么？有没有办法让同步 wrapper 被正确识别？

**答**：

- **结论**：`inspect.iscoroutinefunction(fn)` 看的是**函数对象的代码标志**（`CO_COROUTINE`），不是 `__name__`、`__doc__` 这些元数据。`functools.wraps` 只复制 `__module__/__name__/__qualname__/__doc__/__dict__/__wrapped__`，wrapper 本身是普通 `def`，代码标志不是协程，所以返回 `False`。`inspect.unwrap(fn)` 会沿 `__wrapped__` 链找到原始 `async def`，再判断就对了。3.12 新增 `inspect.markcoroutinefunction(fn)`，可以给"同步函数但返回协程"的 wrapper 打上标记，让 `iscoroutinefunction` 返回 `True`；这是给装饰器/适配器用的元数据，不改变调用行为。`functools.partial(async_fn)` 从 3.8 起能被正确识别；`functools.partialmethod` 同理；但**实例** `Handler()` 不是函数，`iscoroutinefunction(instance)` 为 `False`，要检查 `Handler.__call__` 或先调用再用 `inspect.isawaitable`。
- **取舍**：修 wrapper 有三条路：① 把 wrapper 写成 `async def` 并 `await f(...)`，最直观，但多一层协程、且同步函数被包时会变成协程；② 保留同步 wrapper，用 `inspect.markcoroutinefunction(wrapper)` 打标，零运行时开销，但静态类型检查器不认，且只对 3.12+ 生效；③ 让框架不要只信 `iscoroutinefunction`，而是"调用后看 `inspect.isawaitable(result)`"——这是最健壮的调度方式，能同时支持同步返回值、协程、自定义 awaitable。生产上的组合是②+③：库侧打标兼容旧框架，框架侧用 `isawaitable` 兜底。
- **实战**：事故的装饰器是同步的 `wrapper`，FastAPI 在注册时用 `iscoroutinefunction` 决定是否走 async 路径，看到 `False` 就按同步函数调用，拿到 coroutine 直接当返回值序列化，于是 `never awaited`。修复：① wrapper 改成 `async def`，内部 `return await func(*args, **kwargs)`（如果被装饰的是同步函数，则用 `markcoroutinefunction` 单独处理）；② 在装饰器工厂里加断言：`if inspect.iscoroutinefunction(func): ...`，避免以后再把同步/异步混包；③ 升级框架后确认它已改用 `isawaitable`。上线后 500 归零，`never awaited` 告警清零。

下面验证：直接函数、同步 wrapper、`unwrap`、`partial`、异步 `__call__` 实例、`markcoroutinefunction`，以及"按 `iscoroutinefunction` 调度"导致的未 await 警告。

```python
# iscoroutinefunction 看代码标志, 不看 __name__; markcoroutinefunction 可给 wrapper 打标
import asyncio
import functools
import gc
import inspect
import warnings


async def handler(x=1):
    return x * 2


print("[1] 直接 async def:", inspect.iscoroutinefunction(handler))
assert inspect.iscoroutinefunction(handler) is True


def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)      # 同步 wrapper, 返回 coroutine

    return wrapper


wrapped = timing(handler)
print("[2] wraps 后:", inspect.iscoroutinefunction(wrapped),
      "| unwrap 后:", inspect.iscoroutinefunction(inspect.unwrap(wrapped)))
assert inspect.iscoroutinefunction(wrapped) is False
assert inspect.iscoroutinefunction(inspect.unwrap(wrapped)) is True

partial_fn = functools.partial(handler, 3)
print("[3] partial:", inspect.iscoroutinefunction(partial_fn))
assert inspect.iscoroutinefunction(partial_fn) is True


class Handler:
    async def __call__(self, x=1):
        return x + 1


print("[4] 实例/方法:", inspect.iscoroutinefunction(Handler()),
      inspect.iscoroutinefunction(Handler.__call__))
assert inspect.iscoroutinefunction(Handler()) is False
assert inspect.iscoroutinefunction(Handler.__call__) is True

# 模拟"只看 iscoroutinefunction"的调度器: 同步 wrapper 被当成同步函数
def naive_dispatch(fn):
    if inspect.iscoroutinefunction(fn):
        return asyncio.run(fn())
    return fn()                            # 返回 coroutine, 没人 await


with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    leaked = naive_dispatch(wrapped)
    assert inspect.iscoroutine(leaked)
    del leaked
    gc.collect()
    messages = [str(item.message) for item in caught]
    print("[5] 未 await 警告:", messages)
    assert any("never awaited" in msg for msg in messages)

# 正确调用: 直接 await wrapper 返回的 coroutine
async def main():
    print("[6] 手动 await:", await wrapped(5))
    assert await wrapped(5) == 10

    # 3.12: 给同步 wrapper 打上协程函数标记
    inspect.markcoroutinefunction(wrapped)
    print("[7] mark 后 iscoroutinefunction:", inspect.iscoroutinefunction(wrapped))
    assert inspect.iscoroutinefunction(wrapped) is True
    print("[8] 标记后调度结果:", await wrapped(7))
    assert await wrapped(7) == 14

    # 最健壮的调度: 调用后看 isawaitable, 同时支持同步返回与协程
    async def robust_dispatch(fn):
        result = fn()
        if inspect.isawaitable(result):
            return await result
        return result

    assert await robust_dispatch(wrapped) == 2
    assert await robust_dispatch(lambda: 99) == 99
    print("[9] isawaitable 调度同时兼容同步/异步")


asyncio.run(main())
```

**追问一**：`asyncio.iscoroutinefunction` 和 `inspect.iscoroutinefunction` 有什么区别？—— 历史上 `asyncio` 版本先支持了 `partial` 和 `partialmethod`，`inspect` 版本在 3.8 跟进；3.12 两者对普通函数、`partial`、`markcoroutinefunction` 的行为基本一致。`asyncio.iscoroutinefunction` 在 3.14 起被弃用，新代码应使用 `inspect.iscoroutinefunction`。真正稳的判断是"调用后 `inspect.isawaitable(result)`"，因为它不关心函数怎么定义，只关心返回对象能不能 `await`。

**追问二**：为什么 `functools.wraps` 要复制 `__wrapped__`？—— 主要是给 `inspect.signature`、`inspect.unwrap`、文档工具、类型检查器用的：它们可以沿 `__wrapped__` 找到原函数，恢复签名和注解。但 `iscoroutinefunction` 不沿 `__wrapped__` 走（否则一个同步 wrapper 会被误判成协程，反而危险），所以需要显式 `unwrap` 或 `markcoroutinefunction`。这也解释了"签名对了但调度错了"的割裂。

## 背诵要点

- `iscoroutinefunction` 看 `CO_COROUTINE` 代码标志，`functools.wraps` 只复制元数据，不改变标志。
- `inspect.unwrap` 沿 `__wrapped__` 找原函数；`partial` 可识别；实例的异步 `__call__` 要查 `__call__`。
- 3.12 `inspect.markcoroutinefunction` 给同步 wrapper 打标；最健壮的调度是调用后 `inspect.isawaitable(result)`。

## 复盘追问

- 为什么给同步 wrapper 打 `markcoroutinefunction` 后，调用它仍然返回 coroutine 而不是结果？（标记只影响判断，不改变函数体；仍需 `await` 返回值）
- 框架在注册时判断一次 `iscoroutinefunction` 有什么风险？（运行时可被 `markcoroutinefunction`/monkey patch 改变，最好每次调用后用 `isawaitable` 兜底）
