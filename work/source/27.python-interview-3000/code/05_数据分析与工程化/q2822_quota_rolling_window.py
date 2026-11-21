"""配额的滚动窗口结算: 只看最近 60 分钟, 老用量自动滑出"""

CAP = 100
WINDOW = 60  # 分钟


class RollingQuota:
    def __init__(self, cap, window):
        self.cap, self.window = cap, window
        self.log = []   # (ts, units)

    def _used(self, t):
        return sum(u for ts, u in self.log if t - self.window < ts <= t)

    def allow(self, t, units):
        used = self._used(t)
        if used + units <= self.cap:
            self.log.append((t, units))
            return True, f"窗口内已用 {used} + 本次 {units} = {used + units}, 放行"
        return False, f"窗口内已用 {used}, 再加 {units} 将超 {self.cap}, 拒绝"

    def state(self, t):
        return self._used(t)


if __name__ == "__main__":
    q = RollingQuota(CAP, WINDOW)
    cases = [(0, 50), (10, 60), (30, 30), (65, 60), (70, 30)]
    results = []
    for t, units in cases:
        ok, why = q.allow(t, units)
        results.append(ok)
        print(f"t={t:>2} 分钟请求 {units:>2}: {'OK ' if ok else 'REJ'} {why}")
        print(f"      当前窗口用量 {q.state(t)}")
    assert results == [True, False, True, True, False]
    # 老用量滑出: t=0 的 50 在 t=65 已不在窗口内
    assert q.state(65) == 90, "t=65 的窗口应只含 t=30 与 t=65 两次用量"
    assert q.state(95) == 60, "t=95 的窗口应只含 t=65 的用量"
    print("要点: 滚动窗口比固定窗口平滑, 判定只依赖最近一段用量, 老用量滑出的瞬间配额自然回血")
