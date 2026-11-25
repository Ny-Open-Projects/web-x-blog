---
title: "[Q5241] async with 与 __aenter__/__aexit__：异步上下文协议与取消路径"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5241 · async with 与 __aenter__/__aexit__：异步上下文协议与取消路径

难度：P6 ｜ 标签：async with、__aenter__、__aexit__、异步上下文管理器、asynccontextmanager、取消安全、AsyncExitStack、资源清理

**问**：`async with` 与 `with` 的协议差异是什么——`__aenter__`/`__aexit__` 各在什么时机被 await？异常与取消（CancelledError）进入 `__aexit__` 后会发生什么？"退出阶段可 await"为什么既是能力也是陷阱？`contextlib.asynccontextmanager` 装饰异步生成器与手写类如何选择，清理代码里再 await 时的取消安全怎么保证？

**答**：
结论：`async with` 是同步 `with` 协议的异步镜像：进入时 await `obj.__aenter__()` 并把返回值绑定给 `as` 变量；无论正常结束、异常还是任务被取消，退出时都 await `obj.__aexit__(exc_type, exc, tb)`——三个参数与同步协议完全一致，返回 True 吞异常、None/False 放行的语义也一致（Q024）。与同步版的本质差异在**两点**：①**进入与退出都是挂起点**——连接握手（`__aenter__` 里 connect/auth）和清理动作（`__aexit__` 里发 FIN、事务回滚、asyncio 锁的 release 唤醒等待者）都可以 await，这是同步协议做不到的；②**异常路径更宽**——除了业务异常，`CancelledError` 也会进入 `__aexit__`（任务在 `async with` 体内被 cancel 时，await 点抛出 CancelledError，栈展开先跑 `__aexit__`），所以异步资源的清理代码必须把"取消也算一种退出"当常态设计。陷阱面：`__aexit__` 里的 await 如果自身被取消，新 CancelledError 会**替换**正在传播的原异常（原异常丢失，只剩 traceback 链上的 __context__ 可追），所以清理动作要写幂等、快、且关键的收尾（如 finally 里的 unlock）尽量不依赖可被取消的 await；`contextlib.AsyncExitStack`（Q2135）提供注册式回滚栈与 exit 回调，把"动态数量的异步资源"变成一次 `async with`。选择口径：一次性固定资源手写类或 `@asynccontextmanager`；`@asynccontextmanager` 要求 yield 只有一个且 try/finally 包住 yield（yield 后的代码就是 `__aexit__`），适合轻量场景；复杂生命周期（条件进入、多资源、需要复用实例）手写类更清晰。

取舍：a) `__aexit__` 里要不要吞异常：只有"异常是预期分支"（如连接断开自动重连的上游）才返回 True，且必须留痕（日志/计数），否则永远 None——吞掉 CancelledError 是重罪，会把任务退出伪装成正常完成；b) 清理中的 await：用 `asyncio.shield` 保护不可中断的收尾（但要清楚 shield 后原任务仍会被取消、只是内层协程跑完），或者把收尾改成不 await 的同步动作；c) 超时嵌套：`async with asyncio.timeout(...)` 包住的整个块取消时，`__aexit__` 是在超时异常传播前执行的——把"释放资源"放进 CM 而不是裸 try/finally，才不会被超时路径跳过；d) 每请求建连接 vs 连接池：`async with pool.acquire()` 是标准形态，`__aexit__` 只做归还（快、不可失败），真正的关闭由池统一管理——把慢清理从退出路径挪走是取消安全的第一原则；e) 生成器形态的坑：`@asynccontextmanager` 里在 yield 前抛异常，进入阶段就失败、调用方根本拿不到 CM 实例，错误归因要在"进入失败"与"体内异常"之间分清。

实战：事故形态是"网关 handler 里 `async with conn.transaction()` 包住下游调用，下游超时触发请求取消，`__aexit__` 里的 ROLLBACK 是慢 await，又被二次取消——事务连接带着半截状态回到池里，下一个请求复用时读到脏快照。修复为：回滚改成 `shield(rollback())` + 回滚幂等（重复 ROLLBACK 安全），池归还前做状态断言，坏连接直接销毁重建"。下面实测协议时机、异常/取消路径与 asynccontextmanager 模板。

```python
# async with: __aenter__/__aexit__ 协议与取消路径
import asyncio
from contextlib import asynccontextmanager

class AsyncConn:
    def __init__(self, name: str, slow_exit: bool = False) -> None:
        self.name = name
        self.slow_exit = slow_exit
        self.closed = False

    async def __aenter__(self) -> "AsyncConn":
        await asyncio.sleep(0)              # 进入阶段可挂起: 握手/鉴权
        print(f"[enter] {self.name}")
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await asyncio.sleep(0)              # 退出阶段可挂起: FIN/回滚/归还
        self.closed = True
        label = exc_type.__name__ if exc_type else "None"
        print(f"[exit ] {self.name}, exc={label}, closed={self.closed}")
        return None                          # 不吞异常

async def normal() -> None:
    c = AsyncConn("db-1")
    async with c as got:                     # as 绑定 __aenter__ 返回值
        print("[body ] inside, closed =", got.closed)
    print("[after] closed =", c.closed)

async def with_error() -> None:
    try:
        async with AsyncConn("db-2") as c:
            raise RuntimeError("boom")
    except RuntimeError as e:
        print("[error] 捕获:", e, "| 连接已清理:", c.closed)

async def with_cancel() -> None:
    async def work() -> None:
        async with AsyncConn("db-3"):
            await asyncio.sleep(10)          # 在这里被取消
    t = asyncio.create_task(work())
    await asyncio.sleep(0.05)
    t.cancel()
    try:
        await t
    except asyncio.CancelledError:
        print("[cancel] CancelledError 也走 __aexit__ 后才向上传播")

@asynccontextmanager
async def managed(name: str) -> "AsyncConn":       # asynccontextmanager 模板
    conn = AsyncConn(name)
    await conn.__aenter__()
    try:
        yield conn                                  # yield 之前= __aenter__, 之后= __aexit__
    finally:
        await conn.__aexit__(None, None, None)

async def main() -> None:
    await normal()
    await with_error()
    await with_cancel()
    async with managed("db-4") as c:
        print("[gen  ] asynccontextmanager 形态, closed =", c.closed)

asyncio.run(main())
print("[rule ] __aexit__ 返回 True 才吞异常; 清理要幂等且快, 慢收尾用 shield")
```

**追问一**：任务在 `async with` 体内被取消，`__aexit__` 里的 await 又被二次取消，原异常去哪了？怎么写取消安全的清理？—— 取消传到体内 await 点抛出第一个 CancelledError，栈展开进入 `__aexit__`；此时如果 `__aexit__` 里的清理 await 也被取消（同一任务的取消标志仍未消费完，或外部 cancel 再来），会抛出**第二个** CancelledError，它直接替换正在传播的第一个——原异常只能从新异常的 `__context__` 隐式链里看到，且外层 `except CancelledError` 拿不到原始取消点。取消安全三原则：①清理动作**幂等且小**（归还连接、release 锁是同步级动作，不要在 `__aexit__` 里做重 IO）；②必须完成的收尾用 `asyncio.shield(cleanup())` 包住——shield 保证内层不被取消跑完，但要明白任务本身仍会尽快返回取消，shield 只是让清理在后台完成（配合 `await asyncio.shield(...)` 则会等它）；③绝不 `return True` 吞 CancelledError——吞掉等于告诉 asyncio"任务正常结束"，await 才能正确感知取消。面试要点：取消不是异常路径的特例，是异步资源管理的**第一公民**。

**追问二**：`@asynccontextmanager` 的生成器里 yield 写在 try 外面会怎样？多个 yield、或在 yield 前抛异常分别是什么行为？—— 机制：装饰器把异步生成器包成 CM，`__aenter__` 推进到 yield、`__aexit__` 用 `athrow(exc)`/`asend(None)` 推进剩余部分——所以 yield 前的代码=进入阶段、yield 后=退出阶段。三个经典坑：①**yield 不在 try/finally 里**：体内异常 athrow 进来后，yield 之后的清理代码若因异常跳过（未捕获），清理丢失——标准模板永远是 `try: yield ... finally: 清理`；②**多个 yield**：`__aexit__` 只能推进一次，第二个 yield 会触发 RuntimeError("async generator ignored GeneratorExit"类错误)——一个 CM 只允许一个 yield；③**yield 前抛异常**：进入阶段失败，`async with` 语句在 `__aenter__` 就炸，body 根本不执行，finally 也没得跑——这类"进入失败"要与"体内异常"分开归因（前者是建连失败，后者是业务异常）。另外它复用的是生成器的状态机，**同一个装饰后的 CM 对象不能二次 enter**（生成器已耗尽），每次使用要重新调用工厂函数——手写类可以设计成可重入，这是两者的能力差异之一。

## 背诵要点
- async with = await __aenter__（as 绑定返回值）→ 退出必 await __aexit__(exc_type, exc, tb)：异常与 CancelledError 都走退出，返回 True 才吞异常。
- 退出阶段可 await 是能力（回滚/归还/FIN）也是陷阱：二次取消会替换原异常；清理要幂等、快，慢收尾用 shield，绝不吞 CancelledError。
- @asynccontextmanager：yield 前=进入、后=退出，必须 try/finally 包 yield，只允许一个 yield，实例不可重入；动态多资源用 AsyncExitStack（Q2135）。

## 复盘追问
- 任务在 async with 体内被取消时清理代码的执行顺序和风险点？（取消在 await 点抛 CancelledError → 先跑 __aexit__ → 清理中的 await 可能被二次取消并替换原异常；shield + 幂等收尾）
- asynccontextmanager 和手写异步 CM 类怎么选？（轻量一次性用装饰器且 try/finally 包 yield；复杂/可重入/多资源手写类或 AsyncExitStack）
