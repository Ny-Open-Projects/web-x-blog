---
title: [Q6002] yield 依赖的 finally 与请求取消时序
date: 2026-11-18
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6002 · yield 依赖的 finally 与请求取消时序

> 难度:★★★ | 标签:FastAPI 0.106+, 依赖注入, 取消传播

**问**：yield 依赖里 `finally` 写的清理，客户端断开或请求超时被取消时一定执行吗？Cancel 到达时 finally 内部再 `await` 会怎样？teardown 发生在响应发送前还是发送后？

**答**：一定执行。yield 依赖由 AsyncExitStack 管理，无论路由正常返回、抛 HTTPException 还是 handler 被 cancel，依赖的 `yield` 语句处都会恢复执行并把清理走完（底层是 anyio 的 cancel scope，清理在取消路径上运行）。三个时序要点：1) **取消是 Exception 路径**：cleanup 在 CancelledError 传播链上执行，finally 里再做 `await` 会再次被取消注入打断，涉及不能中断的收尾（如发离开心跳、flush）要用 `asyncio.shield` 保护；2) **teardown 在响应发送之后**：FastAPI 0.106 起语义明确——yield 依赖的退出等到响应体发送完成才执行，避免「响应头已写出、依赖提前关闭」的撕裂状态（旧版本行为有歧义，是经典坑）；3) cleanup 里禁止阻塞调用：它跑在事件循环上，同步 sleep/IO 会拖住整个 worker。反过来面试官也爱问「cleanup 能拿到响应吗」——不能可靠拿到，请求上下文在 teardown 阶段已收尾，别依赖。

```python
# 基线:FastAPI 0.106+/Python 3.9+。标准库 asyncio 模拟 yield 依赖的取消时序,可直接运行。
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def fake_yield_dependency():
    print("dep: 进入,资源已获取")
    try:
        yield "resource"
        print("dep: 正常 teardown(响应发送完成后)")
    except asyncio.CancelledError:
        print("dep: 在取消路径上 teardown —— finally 语义等价,一定执行")
        # 不能被中断的收尾用 shield 保护:取消再次注入时只杀外围,不杀收尾
        try:
            await asyncio.shield(asyncio.sleep(0.01))  # 模拟 flush/离开心跳
            print("dep: 关键收尾完成")
        except asyncio.CancelledError:
            print("dep: shield 内收尾仍在继续/已完成,外围取消不影响它")
            raise
        raise   # 继续向上传播取消,别吞
    finally:
        print("dep: finally 兜底 —— 无论如何都执行")

async def handler(dep):
    await asyncio.sleep(10)     # 模拟慢接口,等不到就整体超时

async def request_with_timeout():
    async with asyncio.timeout(0.05):          # 模拟请求级超时注入取消
        async with fake_yield_dependency() as dep:
            await handler(dep)

try:
    asyncio.run(request_with_timeout(), debug=False)
except TimeoutError:
    print("外层: TimeoutError 如实上抛(清理已全部完成,取消未被吞)")
# 预期输出顺序:进入 → 在取消路径上 teardown → shield 收尾 → finally 兜底 → 外层 TimeoutError
```

**追问**：
1) 为什么 cleanup 里的 `await` 会被再次取消？——任务已处于取消状态时，任何 await 点都可能被再次注入 CancelledError；shield 把内层协程隔离成独立任务，外围被取消只表现为「等待被中断」，内层继续跑完。所以 shield 之后必须重新 raise，否则取消被吞、任务可能永远收不了尾。
2) 0.106 前后 teardown 时序差异的实际影响？——旧版本清理可能在响应发送前触发：比如 yield 依赖持有一个 DB 会话，路由里流式返回的生成器还在迭代时依赖已关，查询报错；新语义下流式响应也被完整覆盖。迁移老代码要重查「依赖清理顺序 vs 响应完成」的隐含假设。
3) handler 里 try/except 捕获了 CancelledError 会怎样？——除非重新 raise，否则取消被吞，超时语义失效，任务进入「应该死了还活着」状态；依赖的 teardown 也会延后。这是 asyncio 3.8+ 的通用红线：CancelledError 是 BaseException，捕获必须有条件、必须重抛。
