---
title: "[Q5588] asyncio.Runner 与事件循环生命周期管理的版本演进"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5588 · asyncio.Runner 与事件循环生命周期管理的版本演进

难度：★★★☆☆ ｜ 标签：asyncio / 版本演进 / asyncio.Runner / 生命周期

**问**：`asyncio.run()` 3.10 才转正，`get_event_loop` 3.12 开始弃用，3.11 又冒出 `asyncio.Runner`。事件循环的生命周期 API 这几年到底怎么变的？一个库要同时兼容三种环境怎么写？

**答**：
- **结论**：演进主线是"**从隐式全局 loop 走向显式实例**"：3.8 前 `get_event_loop()` 在主线程隐式创建全局 loop（副作用魔法）；3.10 `asyncio.run()` 成为官方入口（临时 loop + 优雅关闭 + 取消残留任务）；3.10 起 `get_event_loop` 在无运行 loop 时发 DeprecationWarning，3.12 起更严（无运行 loop 直接报错的方向）；3.11 引入 **`asyncio.Runner`**：把 run 的能力做成可复用对象——支持在同一个 loop 上**顺序执行多个顶层协程**（共享 loop 状态，不必反复建拆），contextvars 传播更可控。库侧的兼容规则始终一条：**协程代码只依赖"运行中的 loop"（`asyncio.get_running_loop()`），绝不触碰事件循环的创建**。
- **取舍**：`Runner` 的适用面：测试夹具（一个 loop 跑多个用例，夹具间共享连接池）、嵌入宿主事件循环的应用（桌面/插件体系）。普通服务入口用 `asyncio.run` 就够；两者都不该出现在"库"里。兼容降级：库代码用 `get_running_loop()`（3.7+，无版本分歧），需要 loop 对象时 `try: loop = get_running_loop() except RuntimeError: loop = asyncio.new_event_loop() + 显式管理`；`typing_extensions` 无关此题，重点是不用已弃用的 `get_event_loop` 默认创建行为。
- **实战**：迁移检查：1）grep `get_event_loop`，主线程隐式创建点全部改 `asyncio.run` / `get_running_loop`；2）测试里 `pytest-asyncio` 的 loop scope 用 Runner 语义；3）`asyncio.run` 会 `shutdown_asyncgens` + `shutdown_default_executor` + 取消残留 task——依赖"进程退出时 loop 还活着"的 hack 全部要改。

```python
"""事件循环生命周期三代 API 对比（Python 3.11+：Runner 可用）"""
import asyncio

async def work(name, n):
    loop = asyncio.get_running_loop()          # 唯一推荐的取 loop 方式
    print(f"{name}: running loop id={id(loop) % 10000}, sleep {n}")
    await asyncio.sleep(n)
    return f"{name} done"

# 一代：asyncio.run —— 每次建/拆临时 loop（服务入口的标准答案）
r1 = asyncio.run(work("run", 0.01))

# 二代：asyncio.Runner（3.11+）—— 同一 loop 顺序跑多个顶层协程
with asyncio.Runner() as runner:
    r2 = runner.run(work("runner-a", 0.01))
    r3 = runner.run(work("runner-b", 0.01))
    # Runner 内 run 之间 loop 存活：可共享 loop 级资源（如连接池、timer）
print("asyncio.run:", r1, "| Runner 两次:", r2, r3)

# 兼容层：库代码只依赖 get_running_loop，不创建 loop
def library_api():
    try:
        loop = asyncio.get_running_loop()
        return f"in-loop path ({id(loop) % 10000})"
    except RuntimeError:
        return "sync path（无 loop，调用方决定是否 asyncio.run）"

print("库内调用（同步上下文）:", library_api())
print("库内调用（线程上下文）:", asyncio.run(asyncio.to_thread(library_api)))

# 三代对比结论（打印而非断言，方便背诵）
print("演进线: 隐式 get_event_loop(≤3.9) → asyncio.run(3.10) → Runner(3.11) → get_event_loop 严格弃用(3.12+)")
```

**追问链**
1. `asyncio.run` 退出时具体做了哪些清理？漏了哪个会出什么事故？
   1. 顺序：cancel 当前任务外的所有 task → gather 等待 → `shutdown_asyncgens`（强制 aclose 生成器）→ `shutdown_default_executor`（等线程池）。若旧代码用 `loop.run_until_complete` 手动管理，漏 `shutdown_asyncgens` 会让异步生成器的 finally（资源释放）不执行——连接/文件泄漏。
   2. 追问：为什么 Runner 里连续 run 不互相取消？——Runner 显式管理 loop 生命周期，run 结束只清理该次创建的 task，loop 本身留给上下文退出时关闭。
2. `get_event_loop` 在 3.10/3.12 的行为差异到底是哪条线？
   1. 3.10 起"主线程无运行 loop 时隐式创建"发弃用警告；3.12 起在**没有运行 loop** 时抛 RuntimeError（只有协程内 get_running_loop 语义），子线程从未支持隐式创建。迁移本质：把"谁来创建 loop"从库还给学生命的拥有者（入口/框架）。
   2. 追问：三方库必须在"无 loop 的同步上下文"里跑协程怎么办？——文档要求调用方 asyncio.run；库内提供 `if hasattr(asyncio, "Runner")` 分支用 Runner 自管，否则 `new_event_loop + run_until_complete + close` 全手动并保证异常时 close。

## 背诵要点
- 演进线：get_event_loop 隐式全局（≤3.9）→ asyncio.run 临时 loop（3.10）→ Runner 可复用 loop（3.11）→ get_event_loop 弃用加严（3.12+）。
- 库代码铁律：只用 get_running_loop，不创建 loop；loop 的创建权归入口（asyncio.run / Runner / 框架）。
- asyncio.run 退出做三件清理：取消残留 task、shutdown_asyncgens、shutdown_default_executor；漏了会资源泄漏。

## 复盘追问
- 老服务从 run_until_complete 迁到 asyncio.run 后出现"连接没释放"，按哪条清理链排查？
- 测试夹具想跨用例共享 loop 级连接池，用 Runner 还是 pytest-asyncio 的 loop scope？各自边界？
