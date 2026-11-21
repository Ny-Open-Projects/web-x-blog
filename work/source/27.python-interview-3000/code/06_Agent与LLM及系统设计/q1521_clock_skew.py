"""时钟偏移检测:节点相对参考时钟采样偏移,漂移估计与告警,单调护栏防回拨。"""


class ClockSim:
    """可漂移的节点时钟:以固定速率偏离真实时间。"""

    def __init__(self, skew_ppm=0.0):
        self.skew_ppm = skew_ppm           # 每秒偏移微秒数换算的系数
        self.t = 0.0

    def now(self, real):
        return self.t + real * (1 + self.skew_ppm * 1e-6)

    def set(self, t):
        self.t = t


class SkewMonitor:
    """偏移监视器:周期采样 节点时间-参考时间,滑动窗口估计漂移速率并告警。"""

    def __init__(self, warn_ms=50.0):
        self.warn_ms = warn_ms
        self.samples = []                  # (real_s, offset_ms)

    def sample(self, real_s, node_clock, reference):
        offset_ms = (node_clock - reference) * 1000
        self.samples.append((real_s, offset_ms))
        return offset_ms

    def drift_ppm(self):
        """用首尾样本估计漂移速率:百万分之几。"""
        if len(self.samples) < 2:
            return 0.0
        (t0, o0), (t1, o1) = self.samples[0], self.samples[-1]
        dt = t1 - t0
        if dt <= 0:
            return 0.0
        return round((o1 - o0) / dt * 1000, 1)   # ms/s → ppm

    def alarm(self):
        return [s for s in self.samples if abs(s[1]) > self.warn_ms]


class MonotonicGuard:
    """单调护栏:业务序号下发时拒绝墙钟回拨,必要时等待追平。"""

    def __init__(self):
        self.last = 0.0

    def issue(self, wall_now):
        if wall_now < self.last:
            return None, self.last          # 回拨 拒绝并返回上次合法值
        self.last = wall_now
        return wall_now, None


if __name__ == "__main__":
    ref = {"now": 0.0}
    node = ClockSim(skew_ppm=100)          # 每秒快 100 微秒 → 每百秒偏 10ms
    mon = SkewMonitor(warn_ms=50.0)
    offsets = []
    for sec in range(0, 1001, 100):         # 采样 11 次 共 1000 秒
        ref["now"] = sec
        off = mon.sample(sec, node.now(sec), sec)
        offsets.append(off)
    assert offsets[0] == 0.0
    assert abs(offsets[-1] - 100.0) < 0.01, "1000 秒 x 100ppm = 100ms"
    assert mon.drift_ppm() == 100.0
    assert len(mon.alarm()) == 6, "偏移超 50ms 的样本从 500 秒起共 6 个"

    fast = ClockSim(skew_ppm=0)
    mon2 = SkewMonitor()
    mon2.sample(0, 10.0, 10.0)
    mon2.sample(1, 11.0002, 11.0)
    assert mon2.drift_ppm() == 200.0 and mon2.alarm() == [], "小偏移不告警"

    guard = MonotonicGuard()
    t1, _ = guard.issue(1000.0)
    back, hold = guard.issue(999.5)         # NTP 回拨场景
    assert t1 == 1000.0 and back is None and hold == 1000.0, "回拨被拒绝 返回保持值"
    t3, _ = guard.issue(1000.5)
    assert t3 == 1000.5
    print("时钟偏移通过:100ppm 千秒偏 100ms 漂移率 200ppm 估计正确 回拨被单调护栏拦截")
