---
title: "[Q5662] TaskGroup fail-fast 取消风暴与清理竞态"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5662 · TaskGroup fail-fast 取消风暴与清理竞态

难度：P7 ｜ 标签：asyncio、TaskGroup、取消传播、清理竞态、结构化并发

**问**：TaskGroup 里一个子任务失败，其它子任务会收到几次 `CancelledError`？被取消的任务在 `except CancelledError` 里 `await` 做清理安全吗，还是会被二次取消打断？如果清理任务**吞掉**取消（`return` 而不重抛）会怎样——TaskGroup 会当成成功、把主异常吞了吗？`asyncio.shield` 在这里到底防的是什么？

**答**：
结论：TaskGroup 是 fail-fast 的：任一子任务抛非取消异常，它立即**取消组内所有其它任务**，然后等全部任务结束，最后把"主异常 + 期间其它非取消异常"聚合成 `ExceptionGroup` 抛出。取消默认只投递**一次**：兄弟任务收到 `CancelledError` 后，在 `except` 里再 `await` 做清理是允许的（不会再被 TaskGroup 二次取消），但清理本身若耗时，会拖慢整个 TaskGroup 的退出（它要等所有任务结束）；若清理中又抛了新异常，这个新异常会**作为附加异常进入同一个 ExceptionGroup**。两条红线：① 清理完必须**重抛 `CancelledError`**——吞掉它（`return`）会让该任务"正常完成"，虽然主异常仍会抛出，但任务做完了"本不该做完"的副作用（如已提交事务、已扣款），破坏一致性；② 兄弟任务被取消产生的 `CancelledError` 是**预期行为**，TaskGroup 不会把它当第二个错误抛给你——`except* CancelledError` 通常抓不到东西，别指望用它做"谁被取消了"的统计。

取舍：`shield` 防的不是"第一次取消"（那已经发生），而是**外来的后续取消**——比如整组又套了一层 `asyncio.timeout`，超时二次取消到来时，`await asyncio.shield(cleanup())` 能让清理继续跑完（shield 把内部任务挂到独立 Task 上，取消只打到外壳）。代价是超时语义被"拖延"：TaskGroup 的退出会被 shield 住的清理时长卡住，所以清理必须有自己的超时上限。设计上要用"**取消即放弃业务、清理走不可取消通道但有硬超时**"的两段式。

实战：事故形态是"批量任务一条失败触发全组取消，某个 worker 的 finally 已把款项提交"——根因是吞掉取消让清理段跑成了"成功完成"。下面跑出三种情形：正常重抛（主异常单独抛出）、吞掉取消（副作用完成但主异常仍在）、清理中抛新异常（聚合进 ExceptionGroup）。

```python
import asyncio

async def failing():
    await asyncio.sleep(0.01)
    raise ValueError("primary failure")

async def worker(name, mode):
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print(f"  {name}: got cancel -> cleanup")
        await asyncio.sleep(0.02)              # 单次取消后，清理 await 可完成
        print(f"  {name}: cleanup done")
        if mode == "swallow":
            return                             # 危险：吞掉取消，副作用算"成功"
        if mode == "raise_new":
            raise RuntimeError(f"{name} cleanup failed")
        raise                                  # 正确：重抛，宣告自己是被取消的

async def main(mode):
    print(f"=== mode={mode} ===")
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(failing())
            tg.create_task(worker("w1", mode))
    except* ValueError as e:
        print("  VE branch:", [str(x) for x in e.exceptions])
    except* RuntimeError as e:
        print("  RE branch:", [str(x) for x in e.exceptions])
    except* asyncio.CancelledError as e:
        print("  CE branch:", [str(x) for x in e.exceptions])

for m in ("rethrow", "swallow", "raise_new"):
    asyncio.run(main(m))
```

**追问一**：为什么 `except* asyncio.CancelledError` 在 TaskGroup 里通常抓不到兄弟任务的取消？——TaskGroup 把"因组内失败而被取消"的任务视为**正常收尾**，不把它们的取消异常计入要抛出的 ExceptionGroup；只有"任务主动抛出 CancelledError 且并非来自组内取消"这种少数情况才可能出现。所以统计"谁被取消"要在任务内部用 `task.cancelling()` 或自己的状态记录，不能靠外层 `except* CancelledError`。

**追问二**：`shield` 住的清理被外层 timeout 二次取消时，TaskGroup 会怎样？——`shield` 让内部清理任务继续跑，但外层 `await` 外壳会立即抛 `CancelledError`，TaskGroup 收到这个取消后会继续它的取消流程；清理任务跑完后结果被丢弃（没人 await 它），但副作用已生效。治理：给 shield 的清理也套一个独立 `asyncio.timeout`，并让它写自己的审计日志，确保"即使外壳被取消，清理也有确定结局与可观测记录"。

## 背诵要点
- TaskGroup fail-fast：一失败就取消所有兄弟，等全部结束，聚合成 ExceptionGroup（主异常 + 期间新异常）。
- 取消只投递一次，`except CancelledError` 里可 await 清理；清理中抛的新异常会并入组；兄弟的 CancelledError 不算错误。
- 红线：清理后必须重抛 CancelledError，吞掉会让"不该完成的副作用"算成功；shield 只防后续取消、需配硬超时。

## 复盘追问
- 批量任务失败触发全组取消后，某 worker 的 finally 已提交款项，如何用"吞掉取消"解释并给出两段式修复？（重抛 CancelledError / shield 清理 + 硬超时 / 审计日志，讨论一致性边界）
- 为什么不能靠外层 `except* CancelledError` 统计哪些兄弟被取消？（组内取消被视作正常收尾不抛出，讨论用 task.cancelling() 自记录）
