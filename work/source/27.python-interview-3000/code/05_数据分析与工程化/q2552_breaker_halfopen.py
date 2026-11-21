"""熔断恢复: 半开探测成功才闭合, 失败退避翻倍"""

BASE_COOLDOWN = 30
FAIL_LIMIT = 3


class Breaker:
    def __init__(self, clock):
        self.clock = clock
        self.state = "closed"
        self.fails = 0
        self.cooldown = BASE_COOLDOWN
        self.opened_at = None

    def can_pass(self):
        if self.state == "closed":
            return True
        if self.state == "open" and self.clock() - self.opened_at >= self.cooldown:
            self.state = "half_open"      # 只放一个探测请求
            return True
        return False

    def on_result(self, ok):
        if ok:
            self.state, self.fails, self.cooldown = "closed", 0, BASE_COOLDOWN
        else:
            self.fails += 1
            if self.state == "half_open":
                self.cooldown *= 2        # 探测失败, 退避翻倍
            if self.fails >= FAIL_LIMIT or self.state == "half_open":
                self.state, self.opened_at = "open", self.clock()


now = [0]


def clock():
    return now[0]


def fail_n(bk, n):
    for _ in range(n):
        bk.on_result(False)


if __name__ == "__main__":
    bk = Breaker(clock)
    fail_n(bk, FAIL_LIMIT)
    print(f"t={now[0]} 连续失败 3 次 -> {bk.state}, 冷却 {bk.cooldown}s")
    now[0] = 29
    assert not bk.can_pass()
    now[0] = 31
    assert bk.state == "open" and bk.can_pass()
    print(f"t=31 冷却结束放行探测 -> {bk.state}")
    bk.on_result(True)
    print(f"探测成功 -> {bk.state}, 计数清零冷却复位 {bk.cooldown}s")
    fail_n(bk, FAIL_LIMIT)
    now[0] = 71
    assert bk.can_pass() and bk.state == "half_open"
    bk.on_result(False)
    print(f"t=71 探测失败 -> {bk.state}, 冷却翻倍到 {bk.cooldown}s")
    assert bk.cooldown == 60 and bk.state == "open"
    print("要点: 半开期只放一个探测, 成功闭合 失败退避翻倍, 避免恢复瞬间被重试洪峰再次打死")
