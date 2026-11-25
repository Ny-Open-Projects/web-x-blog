---
title: "[Q5589] 并发 API 的代际演进：Thread → Executor → TaskGroup"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5589 · 并发 API 的代际演进：Thread → Executor → TaskGroup

难度：★★★☆☆ ｜ 标签：版本演进 / 结构化并发 / TaskGroup / concurrent.futures

**问**：从裸 `threading.Thread` 到 `concurrent.futures` 再到 3.11 的 `TaskGroup`，每一代解决了上一代什么问题？为什么说 TaskGroup 是"结构化并发"而不是又一个并发原语？

**答**：
- **结论**：三代演进的核心是**失败语义逐代收紧**。第一代裸 Thread：生命周期完全脱管——线程死了没人知道（Q5549 静默死亡）、异常被吞进 `threading.excepthook`、无返回值传递、无统一取消。第二代 Executor（3.2+）：补上返回值（Future）与异常传递（result() 时 re-raise）、统一线程/进程接口、池化复用；但**生命周期依然非结构化**——提交后与提交者解耦，进程退出时悬空任务照样丢（Q5545/Q5552 的那类事故）。第三代结构化并发（3.11 `TaskGroup`）：任务的生命周期被词法作用域约束——`async with TaskGroup()` 块内创建的任务**保证在块退出前全部结束**，任一失败 → 取消兄弟任务 → 聚合抛 `ExceptionGroup`，"逃逸的任务"从机制上不可能存在。
- **取舍**：结构化的代价：① 取消是全员波及，需要部分成功场景时要用 `shield`/手动收集（Q5516）；② ExceptionGroup 拆包要 `except*`（Q5012）；③ 只覆盖 asyncio——线程侧还没有官方结构化原语（3.14 的 free-threading/`ThreadGroup` 提案未落地前，线程侧用 Executor + 显式 join 或第三方 anyio）。跨代迁移建议：新代码 asyncio 全走 TaskGroup；线程池任务明确"提交者等待全部完成"（`wait(all)`）来模拟结构化。
- **实战**：能力对照记忆：Thread（无管理）→ Executor（结果与异常）→ TaskGroup（作用域 + 取消传播 + 异常聚合）。评审清单：`Thread(` 直接创建且无人 join → 红灯；`submit` 后不 `wait` → 红灯；`create_task` 后引用即丢 → 红灯。

```python
"""三代并发 API 同一任务的表现对比（Python 3.11+，TaskGroup 可用）"""
import threading, time, asyncio
from concurrent.futures import ThreadPoolExecutor, wait

TASKS = ["a", "b", "c"]

def job(name, fail=False):
    time.sleep(0.02)
    if fail:
        raise ValueError(f"{name} failed")
    return name.upper()

# ---- 第一代：裸 Thread（失败静默、无返回值）----
results = {}
def thread_job(name):
    try:
        results[name] = job(name, fail=(name == "b"))
    except Exception as e:                       # 不捕获则进 threading.excepthook 静默
        results[name] = f"swallowed: {e}"
threads = [threading.Thread(target=thread_job, args=(t,)) for t in TASKS]
for th in threads: th.start()
for th in threads: th.join()                     # 必须手动 join，忘了就泄漏
print("Gen1 Thread:", results, "（失败要自己兜底）")

# ---- 第二代：Executor（结果/异常可取，但生命周期非结构化）----
with ThreadPoolExecutor(max_workers=3) as ex:
    futs = {t: ex.submit(job, t, t == "b") for t in TASKS}
    wait(list(futs.values()))                    # 提交者必须主动收口
    for t, f in futs.items():
        try:
            print("Gen2", t, "->", f.result())
        except ValueError as e:
            print("Gen2", t, "->", f"raised: {e}")   # 异常在 result() 时 re-raise

# ---- 第三代：TaskGroup（结构化：作用域 + 取消传播 + ExceptionGroup）----
async def job_async(name, fail=False):
    await asyncio.sleep(0.02)                     # 同步逻辑换协程形态
    if fail:
        raise ValueError(f"{name} failed")
    return name.upper()

async def structured():
    async with asyncio.TaskGroup() as tg:
        tasks = {t: tg.create_task(job_async(t, t == "b")) for t in TASKS}
    return tasks                                  # 走到这里时所有任务必然已结束

try:
    asyncio.run(structured())
except* ValueError as eg:                         # ExceptionGroup 拆包（3.11+）
    print("Gen3 TaskGroup 聚合异常:", [str(e) for e in eg.exceptions],
          "—— b 失败时 a/c 被自动取消，任务不可能逃逸作用域")
```

**追问链**
1. TaskGroup 里一个任务失败，兄弟任务的取消时序是怎样的？
   1. 失败任务先完成并记录异常 → TaskGroup 立即向兄弟任务 `cancel()` → `async with` 退出前 gather 等待**取消操作本身完成**（清理代码跑完）→ 把所有异常聚合为 ExceptionGroup 抛出。"先取消再等清理再抛"保证退出时无残留。
   2. 追问：兄弟任务里 `except asyncio.CancelledError` 吞掉取消会怎样？——TaskGroup 会把"被取消却返回成功"视为异常情况重新取消/记录，阻塞退出；清理必须 re-raise CancelledError。
2. Executor 怎么模拟结构化并发？还差什么？
   1. 用 `with ThreadPoolExecutor()` + 在 with 块内 `wait(futs)` + 统一 `future.result()` 收异常，能近似"块退出时全部完成"；差的是**取消**——Executor 没有取消正在运行的线程的机制（Future.cancel 只对未开始的任务有效），线程无法被强制中断是根本缺口。
   2. 追问：anyio 的 TaskGroup 与 asyncio 原生的差异？——anyio 支持多后端（trio/asyncio）、提供 CancelScope 更细粒度的取消域；原生 TaskGroup 3.11+ 无外部依赖但粒度固定为整组。

## 背诵要点
- 三代能力：Thread（无管理、异常静默）→ Executor（Future 结果/异常传递）→ TaskGroup（3.11：词法作用域 + 取消传播 + ExceptionGroup 聚合）。
- TaskGroup 退出保证：先取消兄弟 → 等清理完成 → 聚合抛出；吞 CancelledError 会阻塞退出。
- 线程侧无取消能力是 Executor 结构化的根本缺口；3.14 前线程侧靠 wait+result 模拟或用 anyio。

## 复盘追问
- 存量代码里"submit 后不收口"的任务悬空点，用什么静态/运行时手段扫出来？
- 部分成功场景（N 个子任务允许一半失败）在 TaskGroup 下怎么组织才不与取消传播打架？
