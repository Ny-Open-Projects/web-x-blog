"""后台任务注册表: fire-and-forget 的收编。

裸 create_task 不持引用会被 GC 吞掉(Q603 的陷阱); 放进注册表:
- 强引用: 注册表替你持有任务;
- done callback: 完成即移出并回收结果/异常;
- shutdown: 主流程结束时统一排空, 剩下的收编任务一个不漏。
"""
import asyncio


class BackgroundRegistry:
    def __init__(self):
        self.tasks = {}
        self.outcomes = {}

    def spawn(self, name, coro):
        task = asyncio.create_task(coro, name=name)
        self.tasks[name] = task                    # 强引用, 防 GC
        task.add_done_callback(lambda t, n=name: self._collect(n, t))
        return task

    def _collect(self, name, task):
        self.tasks.pop(name, None)
        if task.cancelled():
            self.outcomes[name] = "cancelled"
            return
        try:
            self.outcomes[name] = task.result()
        except Exception as e:
            self.outcomes[name] = e                # 异常在这里回收, 不变孤儿

    async def shutdown(self, timeout=2.0):
        pending = [t for t in list(self.tasks.values()) if not t.done()]
        if not pending:
            return []
        _, still = await asyncio.wait(pending, timeout=timeout)
        return list(still)


async def job(name, delay, fail=False):
    await asyncio.sleep(delay)
    if fail:
        raise ValueError(name + " 失败")
    return name + " 完成"


async def main():
    reg = BackgroundRegistry()
    reg.spawn("flush", job("flush", 0.05))
    reg.spawn("metrics", job("metrics", 0.3))
    reg.spawn("report", job("report", 0.02, fail=True))
    print("主流程干完活, 注册表里还有:", sorted(reg.tasks))

    still = await reg.shutdown(timeout=1.0)
    print("shutdown 后未完成:", [t.get_name() for t in still])
    for name, outcome in sorted(reg.outcomes.items()):
        print("后台 %-8s -> %s" % (name, outcome))

    assert not still, "超时足够时后台应全部收尾"
    assert not reg.tasks, "done callback 应清空注册表"
    assert isinstance(reg.outcomes["report"], ValueError), "失败任务的异常应被回收"
    assert reg.outcomes["flush"] == "flush 完成"
    print("结论: 注册表 = 强引用 + 完成回收 + 关闭排空, 三件套缺一不可")


if __name__ == "__main__":
    asyncio.run(main())
