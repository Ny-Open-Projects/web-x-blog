---
title: [Q1338] 超时预算传递:整条调用链共享一个 deadline
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1338 · 超时预算传递:整条调用链共享一个 deadline

> 难度:★★★★ | 标签:deadline 传播, contextvars, 超时

**问**:上游给请求 500ms,下游每级 RPC 各自设 200ms 超时,为什么还是可能全线超时?正确做法是什么?

**答**:各自为政的超时是加法灾难:三级调用每级 200ms,最坏 600ms,早就超出上游的 500ms 预算,而且每一级都在"白等一个注定失败的下级"。正确做法是把 deadline 当请求上下文传播:入口设定绝对截止时刻,每一级执行前先看"剩余预算还够不够我这一步",不够就直接放弃(快速失败),够则带着"min(父级剩余, 本级预算)"继续往下传。Python 里用 contextvars 承载,天然随调用链流动且线程安全;跨线程池时用 copy_context().run 显式传递。下面的演示一条三级调用链,总预算 300ms,前两级真实耗时,第三级发现剩余不足直接放弃。

```python
# file: code/02_并发与网络工程/q1338_deadline_propagation.py
import contextvars
import time

current_deadline = contextvars.ContextVar("deadline", default=None)


def remaining_ms() -> float:
    dl = current_deadline.get()
    return (dl - time.monotonic()) * 1000 if dl is not None else float("inf")


def enter_budget(own_ms: float):
    """子级预算 = min(父级剩余, 本级声明), 返回可恢复的 token。"""
    parent = remaining_ms()
    child = min(parent, own_ms)
    token = current_deadline.set(time.monotonic() + child / 1000)
    return token, parent, child


class DeadlineExceeded(Exception):
    pass


def stage(name: str, work_s: float, own_ms: float) -> str:
    token, parent, child = enter_budget(own_ms)
    try:
        rem = remaining_ms()
        need = work_s * 1000
        if rem < need:
            raise DeadlineExceeded(
                f"{name}: 剩余 {rem:.0f}ms < 需要 {need:.0f}ms, 快速放弃")
        time.sleep(work_s)
        return f"{name}: 耗时 {need:.0f}ms, 链上剩余 {remaining_ms():.0f}ms"
    finally:
        current_deadline.reset(token)


def main() -> None:
    token = current_deadline.set(time.monotonic() + 0.300)   # 入口: 总预算 300ms
    try:
        print("入口预算 300ms")
        print(stage("网关鉴权", 0.02, 100))
        print(stage("查用户服务", 0.08, 200))
        try:
            stage("查推荐服务", 0.25, 250)      # 剩余约 200ms < 需要 250ms
            print("推荐服务: 完成")
        except DeadlineExceeded as exc:
            print(f"第三级快速失败: {exc}")
            print("上游拿到部分结果 + 明确降级, 而不是 300ms 整体超时")
    finally:
        current_deadline.reset(token)

    start = time.monotonic()
    time.sleep(0.25)
    print(f"无预算传递对照: 白等 {(time.monotonic()-start)*1000:.0f}ms 才得到同样的失败")


if __name__ == "__main__":
    main()
```

**追问**:1) deadline 在线程池里怎么不丢?——contextvars 不会自动跨线程,提交任务时用 ctx = contextvars.copy_context(),然后 executor.submit(ctx.run, fn) 在任务线程里恢复同一份上下文。2) contextvars 为什么是正确的载体?——它是 Python 官方为「上下文随调用链流动」设计的机制:协程间自动传播、线程内隔离;相比 thread local,它正确处理异步任务边界——这是 async 时代传上下文的标准答案。3) 剩余预算不足时「直接放弃」的判据怎么写?——「本级最小耗时估算 > 剩余预算」就放弃(连尝试都别试);这个估算要按 P50 而不是 P99(否则大量正常请求被误杀);放弃时的错误要带「在哪一级、剩多少预算」,排障价值极大。4) 生产陷阱?——各级 timeout 各自为政(见原问的加法灾难);deadline 在线程池/进程边界丢失(contextvars 不自动跨线程,要 copy_context,Q1338 原问);预算传递到了但下游不检查(白传);把 deadline 当重试依据(超时后立刻重试,预算已尽,重试必然失败)。

---
