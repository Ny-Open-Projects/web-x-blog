"""供应商限流退避适配:有 Retry-After 就按它的来,没有则用该供应商的退避曲线,退避有上限。"""
PROFILES = {
    "vendorA": {"base": 1.0, "factor": 2.0, "max": 30.0},
    "vendorB": {"base": 2.0, "factor": 1.5, "max": 10.0},
}


class BackoffPlanner:
    def __init__(self, profiles):
        self.profiles = profiles
        self.attempts = {}

    def next_delay(self, vendor, key, retry_after=None):
        k = (vendor, key)
        self.attempts[k] = self.attempts.get(k, 0) + 1
        if retry_after is not None:
            return min(float(retry_after), self.profiles[vendor]["max"]), "respect-retry-after"
        p = self.profiles[vendor]
        d = min(p["base"] * (p["factor"] ** (self.attempts[k] - 1)), p["max"])
        return d, "profile"

    def reset(self, vendor, key):
        self.attempts.pop((vendor, key), None)


if __name__ == "__main__":
    planner = BackoffPlanner(PROFILES)
    d1, s1 = planner.next_delay("vendorA", "chat")
    d2, _ = planner.next_delay("vendorA", "chat")
    d3, _ = planner.next_delay("vendorA", "chat")
    assert (d1, d2, d3) == (1.0, 2.0, 4.0) and s1 == "profile", "vendorA 指数退避"
    d4, s4 = planner.next_delay("vendorA", "chat", retry_after=120)
    assert d4 == 30.0 and s4 == "respect-retry-after", "Retry-After 也受自家上限保护"
    d5, s5 = planner.next_delay("vendorB", "chat", retry_after=5)
    assert d5 == 5.0 and s5 == "respect-retry-after", "合理 Retry-After 照单全收"
    d6, _ = planner.next_delay("vendorB", "mail")
    assert d6 == 2.0, "vendorB 曲线不同 base 2.0"
    planner.reset("vendorA", "chat")
    assert planner.next_delay("vendorA", "chat")[0] == 1.0, "成功后计数清零"
    print("退避差异通过:按供应商曲线 Retry-After 适配 上限保护 成功清零")
