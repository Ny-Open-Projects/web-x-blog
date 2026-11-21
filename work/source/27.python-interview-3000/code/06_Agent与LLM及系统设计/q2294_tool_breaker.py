"""工具级熔断:每个工具独立计数,连续失败达阈值即熔断,半开探测成功才恢复。"""


class ToolBreaker:
    def __init__(self, threshold=3, cooldown=5.0):
        self.threshold = threshold
        self.cooldown = cooldown
        self.fails = {}
        self.opened_at = {}
        self.half_open = set()
        self.clock = [0.0]

    def call(self, tool, func, *args, **kwargs):
        if tool in self.opened_at:
            if self.clock[0] - self.opened_at[tool] < self.cooldown:
                raise RuntimeError("工具 %s 熔断中 请改走其他路径" % tool)
            self.half_open.add(tool)
        try:
            out = func(*args, **kwargs)
        except Exception:
            self.fails[tool] = self.fails.get(tool, 0) + 1
            if tool in self.half_open or self.fails[tool] >= self.threshold:
                self.opened_at[tool] = self.clock[0]
                self.half_open.discard(tool)
            raise
        self.fails[tool] = 0
        self.opened_at.pop(tool, None)
        self.half_open.discard(tool)
        return out


if __name__ == "__main__":
    br = ToolBreaker(threshold=3, cooldown=5.0)

    def flaky():
        raise ConnectionError("下游超时")

    for i in range(3):
        try:
            br.call("search_api", flaky)
        except ConnectionError:
            pass
    assert br.opened_at["search_api"] == 0.0, "连续三次失败即熔断"
    try:
        br.call("search_api", flaky)
        raise SystemExit("熔断后不应再触达下游")
    except RuntimeError as e:
        assert "熔断" in str(e)
    ok = {"n": 0}

    def good():
        ok["n"] += 1
        return "ok"

    assert br.call("mail_api", good) == "ok", "熔断按工具隔离 不牵连其他工具"
    br.clock[0] = 10.0
    try:
        br.call("search_api", flaky)
    except ConnectionError:
        pass
    assert br.opened_at["search_api"] == 10.0, "半开探测失败重新计时熔断"
    br.clock[0] = 20.0
    assert br.call("search_api", good) == "ok" and br.fails["search_api"] == 0, "半开成功即恢复并清零"
    assert "search_api" not in br.opened_at
    print("工具级熔断通过:独立计数 熔断隔离 半开探测恢复")
