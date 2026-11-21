"""请求优先级调度:高优插队,等待老化防饿死,公平性可用模拟验证。"""


class AgingScheduler:
    def __init__(self, aging_gain=1.0):
        self.queue = []                          # [{id, pri, arrival}]
        self.now = 0
        self.served = []
        self.aging_gain = aging_gain

    def submit(self, req_id, pri):
        self.queue.append({"id": req_id, "pri": pri, "arrival": self.now})

    def effective(self, item):
        return item["pri"] + (self.now - item["arrival"]) * self.aging_gain

    def tick(self, capacity=1):
        """每拍按有效优先级服务 capacity 个,服务耗时 1 拍。"""
        picked = sorted(self.queue, key=lambda it: -self.effective(it))[:capacity]
        served_ids = []
        for it in picked:
            self.queue.remove(it)
            served_ids.append(it["id"])
            self.served.append({"id": it["id"], "pri": it["pri"],
                                "wait": self.now - it["arrival"]})
        self.now += 1
        return served_ids


if __name__ == "__main__":
    sched = AgingScheduler(aging_gain=2.0)
    sched.submit("L", 1)                         # 低优请求先到
    sched.submit("H1", 10)
    order = []
    for i in range(6):
        order += sched.tick()
        sched.submit("H%d" % (i + 2), 10)        # 高优请求持续到达
    assert order == ["H1", "H2", "H3", "H4", "H5", "L"], "老化让低优在 6 拍内被服务"
    assert sched.served[-1] == {"id": "L", "pri": 1, "wait": 5}, "低优等待有上界"

    starve = AgingScheduler(aging_gain=0.0)
    starve.submit("L", 1)
    starve.submit("H1", 10)
    got = []
    for i in range(8):
        got += starve.tick()
        starve.submit("H%d" % (i + 2), 10)
    assert "L" not in got, "无老化时低优被持续饿死"
    print("优先级调度通过:增益 2 时低优 6 拍内服务,增益 0 时可复现饿死")
