# -*- coding: utf-8 -*-
"""基于 awaitable 的重试组合子: 单次尝试限时与总预算是两种不同的超时。

- 每次尝试用 wait_for 包住: 慢尝试会被掐断, 不至于拖垮整个重试序列;
- 总预算在尝试之间检查: 不管还剩几次尝试, 预算烧完就收手;
- 指数退避封顶, 可重试异常集合显式分类, 不吞 CancelledError。
"""
import asyncio

RETRYABLE = (RuntimeError, OSError, asyncio.TimeoutError)


class FlakyOp:
    """前两次报错, 第三次太慢, 第四次成功。"""

    def __init__(self):
        self.tries = 0

    async def __call__(self, i):
        self.tries += 1
        if i == 0:
            raise RuntimeError("瞬态故障一")
        if i == 1:
            raise OSError("瞬态故障二")
        if i == 2:
            await asyncio.sleep(0.5)
            return "slow-ok"
        return "ok"


async def retry(op, attempts=5, per_attempt_timeout=0.3, total_timeout=None,
                base_delay=0.05, factor=2.0, max_delay=0.4):
    loop = asyncio.get_running_loop()
    start = loop.time()
    last = None
    for i in range(attempts):
        if total_timeout is not None and (loop.time() - start) >= total_timeout:
            raise TimeoutError("总预算耗尽, 停止于第 %d 次尝试之前" % (i + 1))
        try:
            return await asyncio.wait_for(op(i), per_attempt_timeout)
        except RETRYABLE as e:
            last = e
            print("  第 %d 次尝试失败: %r" % (i + 1, e))
        await asyncio.sleep(min(base_delay * (factor ** i), max_delay))
    raise RuntimeError("重试 %d 次后仍失败: %r" % (attempts, last))


async def main():
    op = FlakyOp()
    r = await retry(op)
    print("场景A 单次限时 0.3s: 慢尝试被掐断, 结果=%r 共尝试 %d 次" % (r, op.tries))
    assert r == "ok" and op.tries == 4, "第三次太慢被掐断, 第四次应成功"

    op2 = FlakyOp()
    try:
        await retry(op2, total_timeout=0.6)
        raise AssertionError("总预算应耗尽")
    except TimeoutError as e:
        print("场景B 总预算 0.6s: 提前收手 ->", e, "共尝试 %d 次" % op2.tries)
        assert op2.tries < 4, "总预算烧完必须停止, 不许把尝试次数用完"

    print("结论: 单次限时保护一次调用, 总预算保护整个策略, 组合次序就是语义")


if __name__ == "__main__":
    asyncio.run(main())
