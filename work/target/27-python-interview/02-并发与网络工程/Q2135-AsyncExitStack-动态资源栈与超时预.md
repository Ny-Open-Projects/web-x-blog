---
title: [Q2135] AsyncExitStack:动态资源栈与超时预算继承
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2135 · AsyncExitStack:动态资源栈与超时预算继承

> 难度:★★★★ | 标签:AsyncExitStack, 超时预算, 资源管理

**问**:资源数量运行期才知道,或者要把一摞清理动作整体交给下游,怎么办?嵌套超时又怎么不失控?

**答**:AsyncExitStack 把任意数量的异步上下文与回调压栈,aclose 时 LIFO 逆序收尾;超时预算继承则要求内层申请被外层剩余预算钳制,谁也活不过总预算。

- 实测外层预算 0.4s,内层申请 2.0s,被 wait_for 在 0.4s 砍断;

- TimeoutError 上浮的同时,conn-2、conn-1 与同步回调逆序清理;

- pop_all 可以把清理权整体移交,适合"建好后交给主循环"的场景;

- deadline 用 time.monotonic 计算剩余,单调钟不怕中途改表。

```python
# file: code/02_并发与网络工程/q2135_asyncexitstack_timeout.py
# -*- coding: utf-8 -*-
"""AsyncExitStack: 动态资源栈与超时预算继承。

- AsyncExitStack 把不定数量的异步上下文压栈, aclose 时按 LIFO 逆序收尾;
- 超时预算继承: 内层申请的超时被外层剩余预算钳制, 谁也不能活得比总预算长;
- 实测: 内层申请 2.0s, 外层只剩 0.4s, 内层在 0.4s 被砍且清理逆序执行。
"""
import asyncio
import contextlib
import time


class TracedResource:
    def __init__(self, name):
        self.name = name

    async def __aenter__(self):
        print("  进入", self.name)
        return self

    async def __aexit__(self, et, ev, tb):
        print("  清理", self.name)
        return False


@contextlib.asynccontextmanager
async def bounded_stage(name, want, deadline):
    """想睡 want 秒, 但永远被外层预算 deadline 钳制。"""
    remaining = deadline - time.monotonic()
    eff = min(want, remaining)
    print("  %s 申请 %.2fs, 预算剩 %.2fs, 有效 %.2fs" %
          (name, want, remaining, eff))
    try:
        await asyncio.wait_for(asyncio.sleep(want), timeout=eff)
        yield "slept"
    except asyncio.TimeoutError:
        print("  %s 被预算砍断" % name)
        raise


async def main():
    deadline = time.monotonic() + 0.4          # 总预算 0.4s
    stack = contextlib.AsyncExitStack()
    try:
        await stack.enter_async_context(TracedResource("conn-1"))
        await stack.enter_async_context(TracedResource("conn-2"))
        stack.callback(print, "  同步清理也支持")   # 非异步资源同样入栈
        try:
            async with bounded_stage("stage-A", 2.0, deadline) as r:
                print("  stage-A 完成:", r)
        except asyncio.TimeoutError:
            print("  预算被守住, TimeoutError 上浮")
    finally:
        await stack.aclose()
        print("外层栈收尾完毕, 上面三行清理是 LIFO 逆序")

    # 动态资源栈的正经用法: 资源数量运行期才知道
    async with contextlib.AsyncExitStack() as dynamic:
        hosts = ["db-a", "db-b", "db-c"]
        conns = [await dynamic.enter_async_context(TracedResource(h))
                 for h in hosts]
        print("动态压栈:", [c.name for c in conns])
    print("动态栈 aclose: 三个资源逆序清理完成")


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) 为什么用 wait_for 而不是 asyncio.timeout?——3.9 还没有 timeout 上下文(3.11+),wait_for 是当时的标准件,预算思想一致。2) 多个内层都申请 2 秒会怎样?——各自被剩余预算钳制,先来者先耗,后来者拿到的 remaining 更小甚至为 0,预算天然防超卖。3) 超时预算继承的钳制公式与边界?——内层超时=min(申请值, 外层剩余预算);remaining=deadline-monotonic(),deadline 沿调用链传递(Q1338);剩余≤0 直接失败(不发起);「谁也活不过总预算」是递归定义,AsyncExitStack 让多资源共享同一个 deadline。4) pop_all 的移交语义怎么用?——建好资源栈后整体交给主循环,清理责任随栈移交;移交后原代码 aclose 不再清这些资源(所有权转移);与「finally 清理」的组合:先 pop_all 再 finally,避免双重关闭。5) 生产陷阱?——内层申请超预算被砍时资源清理次序错(LIFO 保证,别手动逆序);monotonic 换成 time.time(改表跳变);stack 在异常路径没 aclose(泄漏);把同步资源混进异步栈(回调注册用 callback 而不是 exit);嵌套 stack 的预算不继承(各自为政,Q1338 的加法灾难)。

---
