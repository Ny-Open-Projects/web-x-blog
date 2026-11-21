---
title: [Q5503] TaskGroup 异常聚合的 ExceptionGroup 拆包与部分失败回滚
date: 2026-11-18
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5503 · TaskGroup 异常聚合的 ExceptionGroup 拆包与部分失败回滚

> 难度:★★★ | 标签:TaskGroup, ExceptionGroup, 回滚

**问**：TaskGroup 里 3 个子任务成功 1 个失败，发生什么？怎么在 `except*` 里拆出「哪些输入失败了」并只对成功的部分做回滚？部分失败回滚和「全组取消」怎么区分设计？嵌套 TaskGroup 的异常组会怎样？

**答**：结论：TaskGroup 遵循结构化并发——任一子任务异常时**取消其余全部**，退出 `async with` 时抛 `ExceptionGroup`，其 `.exceptions` 按完成顺序携带全部异常（含「取消前已完成但失败」的）。处理分四步：1) `except* ValueError as eg` 按异常类型切片（except* 不许混 except）；2) 拆包取上下文：异常对象自己携带输入（抛出前把 input 塞进异常属性），或在外层维护 `results: dict[seq, ok/fail]` 映射，组的元信息比异常类型更有用；3) **回滚只针对已成功的**——失败的没有副作用，回滚对象是 `succeeded` 集合；回滚本身要幂等且容忍「回滚中再失败」（记日志进补偿队列，不在 except* 里再抛嵌套异常组）；4) 与「全组取消」区分：`asyncio.CancelledError` 是外部取消，不该被回滚逻辑误伤——except* 不会捕获 CancelledError（它是 BaseException），这正是结构设计的妙处。嵌套 TaskGroup：内层抛出会被外层包装成嵌套 ExceptionGroup（`.exceptions` 里是子组），拆包要递归展平（写个 `flatten(eg)` 生成器）。取舍：需要「部分失败不取消全组」的场景不该用 TaskGroup 的单组语义——要么拆成多个组，要么换 `asyncio.wait` 收集 FIRST_EXCEPTION/MODE 结果再自己编排回滚。

```python
# 基线:Python 3.11+。标准库可直接运行。
import asyncio

class JobError(Exception):
    def __init__(self, seq: int):
        super().__init__(f"job {seq} failed")
        self.seq = seq                    # 关键:异常自带输入上下文

async def job(seq: int) -> int:
    await asyncio.sleep(0.01)
    if seq % 2 == 0:
        raise JobError(seq)
    return seq * 10

async def run_batch(n: int) -> tuple[list[int], list[int]]:
    succeeded: list[int] = []
    failed: list[int] = []

    async def guarded(seq: int) -> None:
        try:
            succeeded.append(await job(seq))
        except JobError as e:
            failed.append(e.seq)
            raise                          # 继续抛给 TaskGroup 聚合

    try:
        async with asyncio.TaskGroup() as tg:
            for i in range(n):
                tg.create_task(guarded(i))
    except* JobError as eg:                # 拆包:每个失败都带 seq
        print("group:", [e.seq for e in eg.exceptions],
              "| succeeded:", sorted(succeeded), "| failed:", sorted(failed))
        # 实战:此处对 succeeded 做补偿回滚(幂等),失败集不回滚
    return succeeded, failed

asyncio.run(run_batch(6))
```

**追问**：
1) 为什么第一个失败后其它任务还在跑完才抛组？——取消是异步的：TaskGroup 先 cancel 其余任务、等所有任务终结（含各自的 CancelledError 处理），保证退出 `async with` 时没有任务存活——这是结构化并发的核心承诺，代价是「失败后的尾巴延迟」等于最慢的取消耗时。
2) except* 里再 raise 会怎样？——包装成新的 ExceptionGroup 抛给上层（原组作为 `__context__` 链）；回滚代码抛错要显式收集成新的业务异常（如 RollbackError 附失败清单），不要让原始失败信息被组嵌套淹没。
3) 怎么让失败不触发全组取消？——把异常吞在 guarded 包装层（像本例 append 后可改为不 raise），组永不异常、天然全部跑完；或降级用 `asyncio.wait(tasks, return_when=FIRST_EXCEPTION)` 手工编排。取舍：吞异常损失「结构化并发保证无泄漏任务」的自动性，需要自己确保清理——两难的本质是「强一致取消 vs 尽力而为批量」。
