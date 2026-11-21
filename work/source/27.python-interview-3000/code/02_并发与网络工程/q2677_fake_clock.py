# -*- coding: utf-8 -*-
"""假时钟测试: 把 sleep 变成瞬移, 重试逻辑毫秒级跑完。

- 把 sleep 作为依赖注入, 被测代码不直接调 asyncio.sleep;
- 假时钟虚拟时间瞬时推进, 真实时间只花在调度让步上;
- 同一参数下两种时钟的调度序列一致, 逻辑验证与耗时解耦。
"""
import asyncio
import time


class RealClock:
    """真时钟: 记账并真睡。"""

    def __init__(self):
        self.waits = []

    async def sleep(self, s):
        self.waits.append(s)
        await asyncio.sleep(s)


class FakeClock:
    """虚拟时钟: sleep 只记账不真等。"""

    def __init__(self):
        self.t = 0.0
        self.waits = []

    async def sleep(self, s):
        self.waits.append(s)
        self.t += s
        await asyncio.sleep(0)               # 让出调度, 保持协作式


async def retry_with_backoff(clock, should_fail):
    """指数退避重试: 时钟是注入的依赖, should_fail 决定前几次失败。"""
    delay = 0.1
    attempts = 0
    while True:
        attempts += 1
        if not should_fail(attempts):
            return attempts, list(clock.waits)
        await clock.sleep(delay)
        delay = min(delay * 2, 0.8)


async def main():
    fail_plan = lambda n: n <= 3             # 前 3 次失败

    real = RealClock()
    t0 = time.perf_counter()
    real_result = await retry_with_backoff(real, fail_plan)
    real_elapsed = time.perf_counter() - t0

    fake = FakeClock()
    t0 = time.perf_counter()
    fake_result = await retry_with_backoff(fake, fail_plan)
    fake_elapsed = time.perf_counter() - t0

    print("重试次数: 真钟 %s / 假钟 %s" % (real_result[0], fake_result[0]))
    print("退避序列: 真钟 %s / 假钟 %s" % (real_result[1], fake_result[1]))
    print("调度序列一致:", real_result[1] == fake_result[1])
    print("真实耗时: 真钟 %.3fs / 假钟 %.4fs (虚拟时间推进 %.1fs)"
          % (real_elapsed, fake_elapsed, fake.t))
    print("要点: 时间注入让退避逻辑的测试从秒级降到毫秒级")


if __name__ == "__main__":
    asyncio.run(main())
