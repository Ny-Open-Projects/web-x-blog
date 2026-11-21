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
