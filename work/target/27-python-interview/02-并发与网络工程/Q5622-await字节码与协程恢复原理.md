---
title: [Q5622] await 的字节码产物与协程恢复原理
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5622 · await 的字节码产物（GET_AWAITABLE/SEND）与协程恢复原理

> 难度:★★★★★ | 标签:原理深挖, asyncio, 字节码

**问**:`await obj` 编译成哪些字节码？协程和生成器在"暂停-恢复"机制上是同一套东西吗？`coro.send(None)` 驱动一个协程到结束，值怎么传进来、`StopIteration` 怎么携带返回值？

**答**:结论：**协程就是约束更严的生成器**。`await x` 在 3.11+ 编译为 `GET_AWAITABLE`（解析 `__await__`，禁止把普通可迭代当 awaitable）→ `LOAD_CONST None` + `SEND`（挂起点跳转，恢复时把 yield 的值放栈顶）→ `END_SEND`/`RESUME`（恢复点标记）。运行时机制与生成器完全同构：帧对象的 `f_lasti` 记录挂起的指令偏移，`send()` 恢复执行、yield/await 的值成为 `send` 的入参；协程结束时 `StopIteration` 被 `__Pyx`…准确说被 `Task.__step` 捕获，`StopIteration.value` 就是协程返回值——这也是 `Task` 把协程包装成 Future 的底层原理。了解这条链的价值：a) 能解释"coroutine never awaited"警告（协程对象被创建但没人 send）、"cannot reuse already awaited coroutine"（帧已耗尽）；b) `TaskGroup`/`gather` 的取消本质是对子 Task 调 `coro.throw(CancelledError)`，在当前挂起点抛出；c) 自研调度器（自定义 Task 步进）完全可以用 `send/throw` 手写驱动。

```python
import dis, types

# ---- 1) await 的字节码 ----
async def demo():
    r = await sub()
    return r + 1

async def sub():
    return 42

print(dis.Bytecode(demo).dis())

# ---- 2) 手写驱动器：send/throw 驱动协程（Task.__step 的极简版） ----
def drive(coro, *args):
    """把协程跑完，返回 (返回值, 经过的挂起点数)。"""
    try:
        coro.send(None)               # 首次必须 send(None) 启动
        assert False, "demo 协程应一次性完成"
    except StopIteration as e:
        return e.value                # StopIteration.value 即协程返回值

coro = demo()
print("手写驱动返回值:", drive(coro))

# ---- 3) 挂起-恢复与值的双向流动（生成器视角同一机制） ----
def echo():
    got = yield "first"               # 挂起，交出 "first"
    yield f"echo: {got}"

g = echo()
print("第一次 send(None) ->", g.send(None))
print("send('hi') ->", g.send("hi"))   # 恢复时，'hi' 成为上一个 yield 的表达式的值
try:
    g.send(None)
except StopIteration:
    print("耗尽 -> StopIteration（协程同理，value 带返回值）")

# ---- 4) 错误状态观测 ----
c1 = demo()
try:
    c1.send(None); c1.send(None)
except Exception as e:
    print("已耗尽协程再 send:", type(e).__name__)

async def never(): ...
c2 = never()
print("未 await 的协程:", type(c2).__name__, "直接 send 才会执行；仅创建会触发 never-awaited 警告")
c2.close()
```

**追问一层**:`SEND` 与旧版 `YIELD_FROM` 的差别是什么，3.10 为什么拆开？（YIELD_FROM 把"解 awaitable + 转发"揉在一条指令里，deopt 多、特化难；3.10/3.11 拆成 GET_AWAITABLE + SEND 后每步可特化、可被调试器单步）。
**追问二层**:`Task.__step` 里 `send` 与 `throw` 两个分支各自处理什么？（正常步进用 send；取消/异常注入用 throw——CancelledError 在协程当前挂起点抛出，若协程吞掉取消，Task 记录"取消失败"并在 await 时再抛）。
**追问三层**:如何在协程里实现"可重入的检查点"？（挂起即可检查：在长循环里周期 `await asyncio.sleep(0)` 让出控制权，本质上就是一次 send 驱动的暂停）。

## 背诵要点
- await 编译为 GET_AWAITABLE → SEND → END_SEND；协程与生成器同构：f_lasti 记挂起点、send 传值、StopIteration.value 带返回值。
- Task.__step 用 send 驱动正常步进、throw 注入取消；"never awaited"/"already awaited" 警告都源于帧生命周期。
- 手写调度器 = send/throw 循环；长循环用 `await asyncio.sleep(0)` 造检查点。

## 复盘追问
- 团队自研的"简易 task runner"偶发返回 None，如何用 StopIteration.value 语义定位？
- 解释为什么在同步函数里直接调 `async def` 函数只会得到协程对象——从字节码与帧生命周期两层作答。
