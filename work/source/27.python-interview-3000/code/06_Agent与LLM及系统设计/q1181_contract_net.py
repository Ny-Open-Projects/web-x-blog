"""合同网协议:广播任务书 -> 承包商出价含负载 -> 择优签约 -> 验收。"""


class Contractor:
    def __init__(self, name, skills, queue_len):
        self.name, self.skills, self.queue = name, skills, queue_len
        self.reputation = 1.0

    def bid(self, task):
        if task["skill"] not in self.skills:
            return None
        base = task["estimated_cost"] * self.reputation
        load_penalty = 1 + self.queue * 0.15          # 越忙报价越高
        return {"contractor": self.name, "price": base * load_penalty}


class Manager:
    def __init__(self, contractors):
        self.contractors, self.assignments = contractors, {}

    def announce(self, task, timeout_rounds=2):
        for _ in range(timeout_rounds):               # 流拍重试
            bids = [c.bid(task) for c in self.contractors]
            bids = [b for b in bids if b]
            if bids:
                best = min(bids, key=lambda b: b["price"])
                c = next(c for c in self.contractors if c.name == best["contractor"])
                c.queue += 1                          # 签约后负载上升,下次报价自动变贵
                self.assignments[task["id"]] = c.name
                return best
        return None

    def deliver(self, task_id, quality):
        c = next(c for c in self.contractors if c.name == self.assignments[task_id])
        c.reputation = max(0.5, c.reputation + (0.02 if quality else -0.1))
        c.queue = max(0, c.queue - 1)


if __name__ == "__main__":
    cs = [Contractor("A", {"search"}, queue_len=3), Contractor("B", {"search", "write"}, queue_len=0)]
    m = Manager(cs)
    task = {"id": "t1", "skill": "search", "estimated_cost": 10}
    win = m.announce(task)
    print("中标:", win)
    assert win["contractor"] == "B", "空闲者应胜出,忙者报价被负载惩罚抬高"

    m.deliver("t1", quality=True)
    win2 = m.announce({"id": "t2", "skill": "write", "estimated_cost": 8})
    assert win2["contractor"] == "B", "能力独占者中标"

    # 无人能干的任务流拍
    none = m.announce({"id": "t3", "skill": "legal", "estimated_cost": 5})
    print("流拍:", none)
    assert none is None
    print("负载感知出价与流拍处理验证通过")
