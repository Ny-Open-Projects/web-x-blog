---
title: "[Q6092] yield 依赖的 finally 与请求取消时序"
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6092 · FastAPI yield 依赖的 finally 与客户端断开取消时序

难度：P7 | 标签：原理深挖 | FastAPI 依赖 | 取消语义

**问**：FastAPI 里用 `yield` 写依赖（yield 前建事务、yield 后提交/回滚）。当客户端在响应发送中途断开、请求协程被取消时，finally 段到底会不会执行、在什么时机执行？为什么"依赖里的事务没有回滚"会成为一个经典事故？

**答**：
结论：`yield` 依赖是一个包在 `contextmanager` 里的生成器：请求处理完成后框架在依赖栈（`AsyncExitStack`）上调用 `__aexit__`，即生成器的 finally 段。取消时序的关键点：① 客户端断开 → Starlette 收到 disconnect → 若是流式响应，处理协程被 `CancelledError` 取消 → 取消会在 await 点注入，`try/finally` 里的 finally **会被执行**（asyncio 取消语义保证 finally 段运行，但其中**不允许再 await 长操作**，否则要用 shield）；② 非流式请求下，FastAPI/Starlette 默认**不主动取消**处理协程（响应已写完就结束），依赖 finally 正常执行；③ 经典事故场景：finally 里做 `db.commit()`/`db.rollback()`，而取消导致 finally 里再 await 时抛 CancelledError，rollback 半途而废——事务悬挂直到连接池回收。
取舍：finally 内的清理要么是同步快操作（内存态），要么用 `asyncio.shield` 保护不可中断的关键段，代价是 shield 期间取消被吞，需要再等待 shield 任务结束。
实战：事务边界推荐"依赖 yield 前开启，业务侧显式提交，finally 只 rollback 未提交事务"；finally 里避免网络调用；把"客户端断开 → 取消 → finally 行为"写进集成测试（用 httpx 流式断开模拟）。

```python
import asyncio
from contextlib import asynccontextmanager

class FakeDB:
    def __init__(self): self.tx = None; self.log = []
    async def begin(self): self.tx = "open"; self.log.append("begin")
    async def commit(self): self.tx = None; self.log.append("commit")
    async def rollback(self):
        self.log.append("rollback-start")
        await asyncio.sleep(0.01)        # 清理也要 await：取消注入点！
        if self.tx: self.tx = None; self.log.append("rollback-done")

db = FakeDB()

@asynccontextmanager
async def tx_dependency():
    await db.begin()
    try:
        yield db                          # 业务在 yield 期间运行
    finally:
        # 请求取消（CancelledError）会在业务 await 点注入，
        # finally 会被执行，但其中再 await 时可能再次收到取消
        try:
            if db.tx:                     # 未提交 → 回滚
                await asyncio.shield(db.rollback())
        except asyncio.CancelledError:
            # shield 期间又被取消：回滚结果不确定 → 记录并交由连接池复位兜底
            db.log.append("rollback-interrupted, pool reset will fix")
            raise
        except Exception as e:
            db.log.append(f"rollback-failed {e}")

async def handle_request(cancel_at: float | None):
    async with tx_dependency() as tx:
        tx.log.append("business")
        await asyncio.sleep(0.2)          # 业务处理
        await tx.commit()

async def scenario(name, cancel):
    db.log.clear()
    task = asyncio.create_task(handle_request(None if cancel is None else cancel))
    if cancel is not None:
        await asyncio.sleep(cancel)
        task.cancel()                     # 模拟客户端断开导致的取消
    try:
        await task
    except asyncio.CancelledError:
        pass
    print(f"{name}: {db.log}")

async def main():
    await scenario("正常完成", None)
    await scenario("0.05s 时客户端断开", 0.05)
    print("事务悬挂判定: 取消发生在 commit 前 → finally 回滚；"
          "若 rollback 自身再被取消则靠连接池复位兜底")

if __name__ == "__main__":
    asyncio.run(main())
```

**追问 1**：为什么 finally 里裸 `await rollback()` 是危险的？
- 追问 2 层：取消会"重新注入"——finally 中第一个 await 点就可能再抛 CancelledError，清理半途而废；shield 让关键清理不可被取消，但要 await shield 完成才算完成。
- 追问 3 层：连接池的 `reset on return`（如 SQLAlchemy async 的 pool_reset_on_return）是最后一道防线，业务级 rollback 失败时依赖它兜底。

**追问 2**：`use_cache=False` 的依赖和取消有什么交互？
- 追问 2 层：默认依赖在请求内缓存（同一依赖只实例化一次）；取消时退出栈逆序执行各依赖 finally——多个依赖间的收尾顺序就是注册的逆序，跨依赖的资源顺序敏感时要显式分层。
- 追问 3 层：流式响应的取消传播比 JSON 响应更即时（disconnect 事件触发），断开敏感的依赖（限流/事务）要按流式路径单独测试。

## 背诵要点
1. yield 依赖的 finally 一定会执行（asyncio 取消保证 finally 运行），但 finally 内 await 可能再收 CancelledError。
2. 事务模式：begin 在 yield 前、commit 由业务显式做、finally 只 rollback，关键清理用 shield。
3. 非流式请求 Starlette 不主动取消处理协程；流式响应断开才即时取消——测试要分路径。

## 复盘追问
1. 为什么"回滚没生效"的事故难复现？——只在客户端断开+回滚自身被取消的窗口发生，重放需要精确断开时机。
2. 连接池复位能兜住什么、兜不住什么？——能兜住未提交事务回滚，兜不住业务已发出的副作用（如已发出的 MQ 消息）。
