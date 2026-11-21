# -*- coding: utf-8 -*-
"""as_completed 的异常传递: 谁先完成谁先出队, 异常也不例外。

- as_completed 把异常当结果递送: fut.result() 在循环体内抛出原异常;
- 单个任务失败不中断整批, catch 之后循环继续消费剩余 Future;
- 调用方负责逐个区分成败, 这正是 as_completed 与 gather 的分工差异。
"""
import asyncio


async def ok_task(name, s):
    await asyncio.sleep(s)
    return name + "-ok"


async def bad_task(msg, s):
    await asyncio.sleep(s)
    raise ValueError(msg)


async def main():
    fs = [asyncio.ensure_future(ok_task("A", 0.05)),
          asyncio.ensure_future(bad_task("B 爆了", 0.10)),
          asyncio.ensure_future(ok_task("C", 0.15)),
          asyncio.ensure_future(bad_task("D 爆了", 0.20))]
    outcomes = []
    for fut in asyncio.as_completed(fs):
        try:
            outcomes.append(("ok", await fut))
        except ValueError as e:
            outcomes.append(("err", str(e)))
    print("按完成顺序的结局:")
    for kind, payload in outcomes:
        print("  ", kind, payload)
    kinds = [k for k, _ in outcomes]
    assert kinds == ["ok", "err", "ok", "err"], "顺序与成败都应如实递送"
    assert len(outcomes) == 4, "一个任务失败不能打断整批消费"


if __name__ == "__main__":
    asyncio.run(main())
