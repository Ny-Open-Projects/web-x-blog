---
title: "[Q5648] asyncio.run 与 get_event_loop 弃用演进"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5648 · asyncio.run 与 get_event_loop 弃用演进

难度：P6 ｜ 标签：asyncio、事件循环、弃用演进、3.10-3.14

**问**：老代码在同步入口写 `loop = asyncio.get_event_loop(); loop.run_until_complete(...)`，升级 3.12 后开始打 DeprecationWarning，3.14 计划直接报错。`get_event_loop` 的语义演进是怎么走到今天的？同步代码调用协程的现在标准答案是什么？

**答**：
结论：这条演进线是"**隐式全局循环** → 显式循环"的迁移史：① 3.8 及以前 `get_event_loop()` 在主线程无循环时会**静默创建**一个并设为全局——方便但制造了"隐藏的循环状态"；② 3.10/3.12 起在"没有运行中循环"的线程里调用它发出 DeprecationWarning（3.12 强化为弃用事件循环创建），鼓励改用 `asyncio.run()` 或 `asyncio.new_event_loop()`；③ 3.14 移除"自动创建"行为，无循环即 RuntimeError。新标准：入口用 `asyncio.run(coro)`（每次新建循环、跑完关闭、隔离状态），库代码里用 `asyncio.get_running_loop()`（只在协程内有效，语义精确），非主线程同步调协程要先 `new_event_loop + set_event_loop` 或把协程 `run_coroutine_threadsafe` 投给已有循环。

取舍：`asyncio.run` 每次建循环有毫秒级成本，高频短任务不适合（应复用常驻循环/专用线程）；嵌套 `asyncio.run`（在已有循环内再 run）直接 RuntimeError，桥接需求用 `nest_asyncio` 只是 hack，正解是重构调用链。

实战：迁移清单——入口 `run_until_complete` → `asyncio.run`；库内 `get_event_loop` → `get_running_loop`；`ensure_future` → `create_task`；测试里 fixture 常驻循环的用 `event_loop` fixture 显式管理或 pytest-asyncio 的 loop scope。CI 在 3.12 上跑 `-W error::DeprecationWarning` 提前暴露。

```python
import asyncio
import warnings
import threading

async def job() -> str:
    loop = asyncio.get_running_loop()      # 协程内：语义精确，永远正确
    await asyncio.sleep(0.01)
    return f"job done on loop {id(loop) % 10000}"

# 标准入口：asyncio.run 新建循环、跑完关闭
print(asyncio.run(job()))

# 老写法在 3.12 的表现：DeprecationWarning（3.14 将 RuntimeError）
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    try:
        loop = asyncio.get_event_loop()    # 主线程无运行循环 -> 弃用告警
        loop.run_until_complete(job())
    except Exception as e:
        print("old-style error:", type(e).__name__, str(e)[:60])
    dep = [x for x in w if issubclass(x.category, DeprecationWarning)]
    print("deprecation warnings captured:", len(dep) > 0)

# 非主线程的同步桥接：线程内自建循环
def worker_thread() -> None:
    loop = asyncio.new_event_loop()        # 不再依赖隐式创建
    asyncio.set_event_loop(loop)
    try:
        print("thread result:", loop.run_until_complete(job()))
    finally:
        loop.close()
        asyncio.set_event_loop(None)

t = threading.Thread(target=worker_thread)
t.start()
t.join()

# 跨线程投递：外部线程用 run_coroutine_threadsafe 把协程交给主循环
async def main_bridge() -> None:
    loop = asyncio.get_running_loop()
    def from_worker():                     # 模拟另一线程发起调用
        fut = asyncio.run_coroutine_threadsafe(job(), loop)
        print("bridged result:", fut.result(timeout=1))
    await loop.run_in_executor(None, from_worker)   # 在线程池里执行 from_worker

asyncio.run(main_bridge())
```

**追问一**：为什么 3.14 敢删隐式创建？老代码怎么办？——生态迁移完成度足够（uvicorn/gunicorn 等都早已显式管理循环）；存量代码按"入口 run 化 + 库内 running 化"机械替换；真正需要"外部循环引用"的场景（扩展嵌入）走 `new_event_loop` 显式持有。

**追问二**：`get_running_loop` 与 `get_event_loop` 在协程内等价吗？——协程内二者返回同一循环，但 `get_running_loop` 无循环即 RuntimeError（fail-fast），`get_event_loop` 语义模糊（可能回退全局/弃用路径）；新代码一律 `get_running_loop`。

**追问三**：多循环并存（主循环 + 后台线程循环）如何避免状态泄漏？——每个循环有自己的 task/回调集合，跨循环传对象要 `call_soon_threadsafe`/`run_coroutine_threadsafe`；Future/Task 跨循环 await 会挂死，这也是 Q5621 事故的同类根因。

## 背诵要点
- 演进线：3.8 隐式建循环 → 3.10-3.12 弃用告警 → 3.14 移除自动创建（RuntimeError）。
- 新标准：入口 `asyncio.run`，协程内 `get_running_loop`，非主线程 `new_event_loop` + `set_event_loop`，跨线程 `run_coroutine_threadsafe`。
- CI 用 `-W error::DeprecationWarning` 在 3.12 提前暴露弃用路径。

## 复盘追问
- 大型同步 CLI 工具要在多处调协程，run 每次新建循环的性能账怎么算？（毫秒级×调用次数 vs 常驻循环线程方案，讨论复杂度收益比）
- pytest-asyncio 的 function/loop scope 选错会造成什么泄漏？（fixture 循环与任务残留、pooled 连接跨测试漂移，讨论 scope 决策依据）
