"""供应商健康度探测:连续失败摘除流量,连续恢复才重新接入,切换对调用方无感。"""


class HealthMonitor:
    def __init__(self, providers, dead_after=2, alive_after=2):
        self.health = {p: {"fail": 0, "ok": 0, "alive": True} for p in providers}
        self.dead_after = dead_after
        self.alive_after = alive_after
        self.events = []

    def probe(self, provider, ok):
        h = self.health[provider]
        if ok:
            h["ok"] += 1
            h["fail"] = 0
            if not h["alive"] and h["ok"] >= self.alive_after:
                h["alive"] = True
                h["ok"] = 0
                self.events.append(("recover", provider))
        else:
            h["fail"] += 1
            h["ok"] = 0
            if h["alive"] and h["fail"] >= self.dead_after:
                h["alive"] = False
                self.events.append(("dead", provider))

    def route(self):
        alive = [p for p, h in self.health.items() if h["alive"]]
        if not alive:
            raise RuntimeError("全部供应商被摘除")
        return alive[0]


if __name__ == "__main__":
    m = HealthMonitor(["vendor-a", "vendor-b"])
    assert m.route() == "vendor-a"
    m.probe("vendor-a", True)
    m.probe("vendor-a", False)
    assert m.route() == "vendor-a", "单次失败只观察不摘除"
    m.probe("vendor-a", False)
    assert ("dead", "vendor-a") in m.events, "连续 2 次失败摘除"
    assert m.route() == "vendor-b", "流量切到健康供应商"

    m.probe("vendor-a", True)
    assert m.route() == "vendor-b", "恢复 1 次不够,保持摘除"
    m.probe("vendor-a", True)
    assert ("recover", "vendor-a") in m.events, "连续 2 次成功重新接入"
    assert m.route() == "vendor-a"

    solo = HealthMonitor(["solo"], dead_after=1)
    solo.probe("solo", False)
    blew = False
    try:
        solo.route()
    except RuntimeError:
        blew = True
    assert blew, "全摘除必须显式失败而不是假装健康"
    print("健康探测通过:连续失败摘除 连续恢复接入,切换对调用方无感")
