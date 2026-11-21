---
title: [Q5538] asyncio.TimeoutError 与 TimeoutError 合并（3.11）的陷阱
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5538 · asyncio.TimeoutError 与 TimeoutError 合并（3.11）的 except 顺序陷阱

> 难度:★★★★ | 标签:版本演进, TimeoutError, 异常处理, asyncio

**问**：3.11 把 `asyncio.TimeoutError` 和内置 `TimeoutError` 合并了，这改变什么？为什么 `except (socket.timeout, asyncio.TimeoutError, TimeoutError)` 这样的写法有历史兼容坑？超时后的清理路径有什么新要求？

**答**：历史包袱：内置 `TimeoutError`（OSError 子类，EAGAIN 语义，socket.timeout 是它的别名）与 `asyncio.TimeoutError`（早期继承 Exception）本是两个类，`except TimeoutError` 抓不到 asyncio 的超时——于是代码里长出 `except (asyncio.TimeoutError, socket.timeout)` 的三连组合。3.11 统一：**`asyncio.TimeoutError = TimeoutError` 内置类的别名**（concurrent.futures.TimeoutError 也改继承自它，3.11+），`socket.timeout` 早已是内置 TimeoutError 别名。收益与陷阱并存：1) **陷阱一：OSError 遮蔽**——TimeoutError 是 OSError 子类，`except OSError` 写在前面会**吞掉 asyncio 超时**（3.11 前它俩不相干），升级后旧代码语义悄然改变；2) **陷阱二：超时后任务仍在跑**——`asyncio.wait_for`/`timeout`（Q5505）触发时内部任务被取消，但取消是协作式的，捕获 CancelledError 里"再 await 一点"的清理代码会拖长超时生效时间；3) 正确顺序：`except (TimeoutError, OSError)` 中 TimeoutError 在前（虽然 MRO 上超时也是 OSError，顺序影响可读性），并把"应用层超时"与"传输层 EAGAIN"分开归因（用 `task.cancelled()` 或异常来源区分）。迁移建议：删掉三连 except 直接写 `except TimeoutError`，但**审计所有 `except OSError` 分支**——这是本次合并最大的隐性行为变化。

```python
# file: code/02_并发与网络工程/q5538_timeout_merge.py
"""3.11 TimeoutError 合并的语义探测与 except 顺序陷阱."""
import asyncio
import socket
import sys

# 1) 类同一性: 三个历史名字现在是同一个类
print("asyncio.TimeoutError is TimeoutError:",
      asyncio.TimeoutError is TimeoutError)
print("socket.timeout is TimeoutError:", socket.timeout is TimeoutError)
try:
    import concurrent.futures as cf
    print("futures.TimeoutError 是 TimeoutError 子类:",
          issubclass(cf.TimeoutError, TimeoutError))
except ImportError:
    pass

# 2) except 顺序陷阱: OSError 在前会吞掉 asyncio 超时
async def slow() -> None:
    await asyncio.sleep(5)

async def trap() -> str:
    try:
        async with asyncio.timeout(0.05):            # 3.11+ 结构化超时(Q5505)
            await slow()
        return "completed"
    except OSError:                                  # 写在前: TimeoutError 也是 OSError!
        return "被 OSError 吞掉(陷阱)"
    except TimeoutError:
        return "应用层超时(正确分支)"

print("顺序陷阱演示:", asyncio.run(trap()))

# 3) 正确写法: 超时在前, 并区分归因
async def correct() -> str:
    try:
        async with asyncio.timeout(0.05):
            await slow()
        return "completed"
    except TimeoutError:
        return "应用层超时"
    except OSError as e:
        return f"传输层错误 errno={getattr(e, 'errno', None)}"

print("正确顺序:", asyncio.run(correct()))

# 4) 超时与取消的联动: wait_for 超时后内部任务被取消
async def inner() -> str:
    try:
        await asyncio.sleep(5)
        return "done"
    except asyncio.CancelledError:
        print("inner 收到取消(超时触发) -> 清理后重抛")
        raise

async def outer() -> None:
    t = asyncio.create_task(inner())
    try:
        await asyncio.wait_for(t, timeout=0.05)
    except TimeoutError:
        print("outer 捕获 TimeoutError; inner.cancelled =", t.cancelled())

asyncio.run(outer())
print("python:", sys.version_info[:3])
```

**追问**：1) 为什么合并进 OSError 家族？——内置 TimeoutError 本就是 OSError 子类（系统调用超时语义），asyncio 超时统一进来后"一个 except 抓两类"成为可能，但也带来遮蔽风险，这是设计取舍的两面。2) 怎么在 except 里区分"应用层超时"与"系统调用超时"？——应用层用 `asyncio.timeout`/`wait_for` 的调用点包裹判定（上下文管理器自己抛的就是应用层）；系统层看 errno（EAGAIN/ETIMEDOUT）与调用栈来源。3) `asyncio.timeout` 与 `wait_for` 在超时传播上的差异？——timeout 是上下文管理器，覆盖块内**所有** await 点的取消时机更可控（进入/退出精确），wait_for 只包一个 awaitable；嵌套预算见 Q5505。

## 背诵要点
- 3.11 起 `asyncio.TimeoutError is TimeoutError`，socket.timeout 是同一别名；futures.TimeoutError 变其子类。
- 最大隐性陷阱：TimeoutError 属于 OSError 家族，前面的 `except OSError` 会吞掉超时，升级必审计。
- 超时触发=内部任务被取消（协作式），清理路径在 CancelledError 里仍要快进快出。

## 复盘追问
- 全库 grep `except OSError` 后发现 40 处，怎么排序审计优先级（调用链上有无 asyncio/网络）？
- 3.10 环境还要兼容两年，你写"双语义安全"的 except 的方案是什么（版本判断还是显式元组）？
