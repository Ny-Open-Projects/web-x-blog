---
title: [Q5516] 结构化并发的取消风暴与 cleanup 幂等
date: 2026-11-19
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5516 · 取消风暴与 cleanup 幂等

> 难度:★★★ | 标签:结构化并发, 取消传播

**问**：TaskGroup 里一个子任务失败，其余任务的「取消风暴」是怎么传播的？为什么 cleanup 代码（finally / `__aexit__`）必须幂等——举出取消打断 cleanup 导致资源泄漏的具体时序，正确写法长什么样？

**答**：传播时序：子任务 A 抛异常 → TaskGroup **先取消其余全部子任务**（向它们注入 CancelledError）→ 等所有子任务结束 → 把真实异常与取消期间的异常**聚合**成 ExceptionGroup 抛出。cleanup 的三重风险：① 取消会打断正在执行的 cleanup（`await cleanup()` 途中再被注入取消 → 资源没清完）；② 外层取消与内部异常**同时发生**时，`except CancelledError` 分支和 `except* ValueError` 分支都要走清理；③ cleanup 自己 await 的子调用又可能抛取消——必须**屏蔽取消**（`asyncio.shield` 或 3.11+ `uncancel` 配合的受保护段）或把清理设计成**幂等可重试**。正确姿势：资源申请与释放配对封装成 async context manager，`__aexit__` 里用 `asyncio.shield` 包清理动作并吞掉二次取消，重试式清理保证「清多少次结果一样」。

```python
# 全部标准库；基线 3.11+（TaskGroup）
import asyncio, random

class Resource:
    def __init__(self, name):
        self.name, self.closed = name, False
    async def close(self):
        await asyncio.sleep(0.01)          # 清理动作本身要 await
        self.closed = True
        print(f"{self.name} closed")

class ResGroup:
    """cleanup 幂等模板：shield 保护清理，重复调用结果一致。"""
    def __init__(self):
        self.res: Resource | None = None
    async def __aenter__(self):
        self.res = Resource("conn")
        await asyncio.sleep(0.01)
        return self.res
    async def __aexit__(self, *exc):
        if self.res and not self.res.closed:       # 幂等闸门①：已关不再关
            try:
                await asyncio.shield(self.res.close())   # 闸门②：防清理被打断
            except asyncio.CancelledError:
                # 屏蔽不代表吞掉外层取消：清理完成后继续传播取消
                await self.res.close() if not self.res.closed else None
                raise
        return False

async def worker(rg, fail: bool):
    async with rg:
        await asyncio.sleep(0.02)
        if fail:
            raise ValueError("worker boom")
        return "ok"

async def main():
    rg = ResGroup()
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(worker(rg, fail=True))      # 一个失败
            t2 = tg.create_task(worker(rg, fail=False))  # 其余被取消
    except* ValueError as eg:
        print("聚合异常:", [str(e) for e in eg.exceptions])
        assert t2.cancelled() or t2.done()
        print("其余子任务已取消:", t2.cancelled())
    assert rg.res.closed, "取消风暴后资源必须已清理"
    print("cleanup 幂等：资源最终 closed ✅")

if __name__ == "__main__":
    asyncio.run(main())
```

**追问**：1) 取消风暴里子任务能「拒绝取消」吗？——能，捕获 CancelledError 不再抛即可赖着不退，但 TaskGroup 会等它——所以超时兜底（`asyncio.timeout`）必须套在 TaskGroup 外层，否则一个赖皮任务拖死整组。2) 聚合组里 CancelledError 会和 ValueError 一起出现吗？——顶层取消的 CancelledError 不入组（保证取消语义可被外层识别），只有子任务自身抛的异常才聚合。3) cleanup 幂等的工程检验标准？——重复调用不报错、状态最终一致、可被「半途取消后重放」；写完 cleanup 自测一遍「连续 close 两次」是廉价有效的习惯。

## 背诵要点
1. 取消风暴时序：子任务失败 → 组内其余任务注入 CancelledError → 全员结束后聚合 ExceptionGroup。
2. cleanup 三重风险：清理被打断、双路径（取消+异常）、清理自身再被取消——shield + 幂等闸门双保。
3. 顶层 CancelledError 不入聚合组；超时兜底必须套在 TaskGroup 外层防赖皮任务。

## 复盘追问
1. shield 保护清理时，外层取消在 shield 完成前到达会怎样？（提示：清理完成后 CancelledError 继续传播——shield 只保护被包操作，不吞取消）
2. 数据库事务在取消风暴里怎么保证不出现半提交？（提示：事务回滚天然幂等 + 连接归还前 reset，参考 Q102 幂等设计）
