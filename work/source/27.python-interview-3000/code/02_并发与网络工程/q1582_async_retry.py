"""异步重试装饰器: 可重试分类 + 绝不吞 CancelledError。

- 只对声明的瞬时异常(网络抖动、5xx)重试, 业务异常直接抛;
- 指数退避 + 抖动, 上限 cap;
- 取消(CancelledError)是协程世界的硬中断: 重试装饰器必须让它穿透,
  否则"取消一个卡死的重试"会变成"再等一轮退避"。
"""
import asyncio
import random


class TransientError(Exception):
    pass


def async_retry(attempts=4, base=0.05, cap=0.15, retry_on=(TransientError,)):
    def deco(fn):
        async def wrapper(*args, **kwargs):
            delay = base
            for attempt in range(1, attempts + 1):
                try:
                    return await fn(*args, **kwargs)
                except asyncio.CancelledError:
                    raise                    # 取消永远不重试
                except retry_on:
                    if attempt == attempts:
                        raise
                    pause = min(cap, delay * random.uniform(0.5, 1.5))
                    print("第 %d 次失败, %.0fms 后重试" % (attempt, pause * 1000))
                    await asyncio.sleep(pause)
                    delay *= 2
        return wrapper
    return deco


calls = {"n": 0}


@async_retry()
async def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise TransientError("网络抖动")
    return "ok"


@async_retry()
async def always_fail():
    raise TransientError("一直失败")


async def main():
    r = await flaky()
    print("flaky 最终返回:", r, "| 尝试次数:", calls["n"])
    assert r == "ok" and calls["n"] == 3, "前两次失败第三次应成功"

    # 重试中的任务被取消: CancelledError 必须穿透, 而不是再等一轮退避
    task = asyncio.create_task(always_fail())
    await asyncio.sleep(0.08)            # 让它先失败一两次进入退避
    task.cancel()
    try:
        await task
        raise AssertionError("不应正常返回")
    except asyncio.CancelledError:
        print("取消正确穿透重试装饰器, 任务被取消")
    assert task.cancelled(), "任务应以取消收场"

    print("结论: 重试清单解决'该不该重', CancelledError 通道解决'停得下来'")


if __name__ == "__main__":
    asyncio.run(main())
