# -*- coding: utf-8 -*-
"""错误率的滑动窗口: 分桶计数与告警滞回。

- 滑动窗口由 N 个小桶组成, 每桶一个时间片, 过期即滚动丢弃;
- 错误率 = 窗口内错误总和 / 请求总和, 分桶让"最近"可计算;
- 告警带滞回: 超过 30% 拉响, 低于 10% 才解除, 阈值间抖动不 flap。
"""
from collections import deque

BUCKET_SEC = 0.2
N_BUCKETS = 10                            # 窗口 2 秒
CALLS_PER_TICK = 10
ALARM_ON = 0.30
ALARM_OFF = 0.10


class ErrorWindow:
    def __init__(self):
        self.buckets = deque()            # (start, ok, err)

    def advance(self, t):
        """滚动: 丢弃窗口外的桶, 补足到当前时间片。"""
        while self.buckets and t - self.buckets[0][0] >= N_BUCKETS * BUCKET_SEC:
            self.buckets.popleft()
        if not self.buckets or t - self.buckets[-1][0] >= BUCKET_SEC:
            self.buckets.append((t, 0, 0))

    def record(self, ok):
        start, o, e = self.buckets[-1]
        self.buckets[-1] = (start, o + (1 if ok else 0),
                            e + (0 if ok else 1))

    def rate(self):
        ok = sum(b[1] for b in self.buckets)
        err = sum(b[2] for b in self.buckets)
        total = ok + err
        return err / total if total else 0.0


def feed_pattern(tick):
    """确定性故障剧本: 0-2s 健康, 2-5s 故障风暴, 5s 后恢复。"""
    t = tick * BUCKET_SEC
    if t < 2.0:
        return 1                          # 每拍 1 个错误
    if t < 5.0:
        return 8                          # 风暴: 每拍 8 个错误
    return 0


if __name__ == "__main__":
    win = ErrorWindow()
    alarm = False
    transitions = []
    TICKS = 35
    for tick in range(TICKS):
        t = tick * BUCKET_SEC
        win.advance(t)
        errs = feed_pattern(tick)
        for i in range(CALLS_PER_TICK):
            win.record(i >= errs)            # 前 errs 个失败, 其余成功
        rate = win.rate()
        if not alarm and rate > ALARM_ON:
            alarm = True
            transitions.append((t, "ALARM", rate))
        elif alarm and rate < ALARM_OFF:
            alarm = False
            transitions.append((t, "RECOVER", rate))
        if tick % 5 == 0:
            print("t=%.1fs 窗口错误率 %.0f%% 告警=%s"
                  % (t, rate * 100, alarm))

    print("告警状态转移:")
    for t, kind, rate in transitions:
        print("  t=%.1fs %s (当时错误率 %.0f%%)" % (t, kind, rate * 100))
    print("要点: 滞回让告警在阈值附近不再抖动, 分桶让窗口滚动起来")
