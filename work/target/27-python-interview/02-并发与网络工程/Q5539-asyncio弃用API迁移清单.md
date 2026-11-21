---
title: [Q5539] asyncio 弃用 API 迁移清单：从 loop 参数到显式生命周期
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5539 · asyncio 弃用 API 迁移清单：从 loop 参数到显式生命周期

> 难度:★★★★ | 标签:版本演进, asyncio, 弃用迁移

**问**：3.8-3.14 之间 asyncio 一路弃用了哪些常用 API？"loop 参数全线下架"影响哪些代码？迁移到新写法的对照表长什么样？

**答**：asyncio 的演进主线是**从隐式全局 loop 转向显式生命周期**。迁移对照清单（按踩坑频率排序）：1) `loop=` 参数全线移除——`asyncio.sleep(d, loop=)`、`asyncio.gather(loop=)`、`asyncio.wait(loop=)` 等 3.8 弃用、3.10 移除，改为"在运行中的 loop 里调用，自动取 running loop"；2) `asyncio.get_event_loop` 隐式创建（Q5531）→ `get_running_loop()` / `asyncio.run`；3) `asyncio.coroutine` 装饰器 3.8 移除 → `async def`；4) `asyncio.async()` 3.8 移除 → `create_task`；5) **3.12**：`asyncio.wait_for` 对外语义收敛（超时即 TimeoutError，内部一律取消）与 `asyncio.timeout`/`timeout_at` 引入（结构化超时，Q5505）；`eager_task_factory` 提供低延迟 Task 创建（Q5502）；6) **3.13**：TaskGroup 成为官方推荐的任务编排（替代裸 gather 的异常处理困境，Q5503）；7) **3.14**：隐式 loop 创建移除、`asyncio.iscoroutinefunction` → `inspect.iscoroutinefunction`（行为统一）。迁移纪律：a) **一次只迁一层**——先消 loop 参数（机械替换），再改 get_event_loop（语义审查），最后上 TaskGroup/timeout（结构重排）；b) 弃用期开 `-W error::DeprecationWarning` 进 CI，把警告当门禁；c) 三方库版本锁死在迁移分支里，避免"库还在用旧 API、应用先升级"的断层。

```python
# file: code/02_并发与网络工程/q5539_deprecation_map.py
"""asyncio 弃用 API 的新旧写法对照与自检清单."""
import asyncio
import inspect
import sys

OLD_NEW = [
    ("asyncio.sleep(d, loop=lp)",      "asyncio.sleep(d)  # loop 参数 3.10 移除"),
    ("asyncio.coroutine f",            "async def f       # 3.8 移除"),
    ("asyncio.async(coro)",            "asyncio.create_task(coro)  # 3.8 移除"),
    ("asyncio.get_event_loop()",       "asyncio.get_running_loop() / asyncio.run()"),
    ("asyncio.wait_for(c, t)",         "async with asyncio.timeout(t)   # 3.11+"),
    ("loop.create_task + 裸 gather",    "async with asyncio.TaskGroup()  # 3.11+"),
    ("asyncio.iscoroutinefunction",    "inspect.iscoroutinefunction     # 3.14 收敛"),
]
for o, n in OLD_NEW:
    print(f"  {o:34s} -> {n}")

# 1) TaskGroup 替代裸 gather + 手工异常分拣 (3.11+)
async def fetch(i: int) -> int:
    await asyncio.sleep(0.01 * i)
    if i == 2:
        raise ValueError(f"downstream-{i}")
    return i * 10

async def modern_gather() -> dict:
    ok, errs = {}, []
    try:
        async with asyncio.TaskGroup() as tg:          # 结构化并发(Q5503)
            for i in range(4):
                tg.create_task(fetch(i))
    except* ValueError as eg:                          # except* 拆包(Q5012)
        errs = [str(e) for e in eg.exceptions]
    return {"errs": errs, "note": "TaskGroup 失败即整组取消"}

print(asyncio.run(modern_gather()))

# 2) inspect.iscoroutinefunction: 统一后的判定
async def a() -> None: ...
def s() -> None: ...
print("async 判定:", inspect.iscoroutinefunction(a),
      "| sync 判定:", not inspect.iscoroutinefunction(s))

# 3) 自检: 代码库里还残留哪些旧写法(简化示意)
LEGACY_TOKENS = ("loop=", "get_event_loop()", "asyncio.coroutine", "asyncio.async(")
def audit(source: str) -> list[str]:
    return [t for t in LEGACY_TOKENS if t in source]

demo_src = "asyncio.gather(x, loop=lp); lp=asyncio.get_event_loop()"
print("audit 命中:", audit(demo_src))
print("python:", sys.version_info[:3])
```

**追问**：1) 为什么 loop 参数要整体移除而不是保留可选？——运行中任务拿 running loop 是唯一正确来源，显式传 loop 反而支持了"跨 loop 调度"这类错误用法（Q2674 双循环嵌套），API 设计上把错误用法变成不可能比文档警告有效。2) `asyncio.wait` 的 3.12 签名变化之外还有什么坑？——`asyncio.wait` 不再接受协程集合（必须 Task/Future），`return_when` 语义配合 TaskGroup 时代基本只剩特殊场景；日常编排优先 TaskGroup。3) 三方库（旧 aiohttp 等）还没迁移就升 3.10+ 会怎样？——运行时传 loop= 直接 TypeError；对策是依赖矩阵先行、用兼容 shim 分支或锁旧版本直到库适配。

## 背诵要点
- 演进主线：隐式全局 loop → 显式生命周期；loop 参数 3.10 移除、get_event_loop 3.14 收口。
- 新写法四件套：get_running_loop / asyncio.run / asyncio.timeout / TaskGroup。
- 迁移纪律：分层推进（机械替换→语义审查→结构重排），CI 用 -W error::DeprecationWarning 当门禁。

## 复盘追问
- 你的 CI 现在会把 DeprecationWarning 当失败吗？如果不是，第一批该对哪个目录开？
- "库未适配、应用想升级"的窗口期，shim 层放在应用侧还是 fork 库？决策依据是什么？
