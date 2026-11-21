"""依赖时钟的注入模式: Clock 抽象与冻结测试"""

from datetime import datetime, timedelta


class SystemClock:
    def now(self):
        return datetime.now()


class FrozenClock:
    """测试专用: 冻结起点, 可手动推进, 永不真实等待"""

    def __init__(self, fixed):
        self.fixed = fixed

    def now(self):
        return self.fixed

    def advance(self, **kwargs):
        self.fixed += timedelta(**kwargs)


def trial_expired(clock, started_at, days=14):
    """业务逻辑只认 clock, 不认全局时间"""
    return clock.now() > started_at + timedelta(days=days)


if __name__ == "__main__":
    started = datetime(2026, 3, 1)
    fc = FrozenClock(datetime(2026, 3, 10))
    assert not trial_expired(fc, started), "第 10 天试用未到期"
    print("冻结在 03-10: 试用未到期, 测试零等待")
    fc.advance(days=6)
    assert trial_expired(fc, started), "推进 6 天越过边界后应判定到期"
    print(f"手动推进到 {fc.now():%m-%d}: 越过 14 天边界判定翻转, 无需 sleep")
    sc = SystemClock()
    print(f"生产注入 SystemClock: now={sc.now():%Y-%m-%d %H:%M} (演示用 naive 时间, 3.9 兼容)")
    print("要点: 时间是隐式依赖, 把 now() 注入进来, 过期 续费 重试间隔才可测, 测试也不再真睡")
