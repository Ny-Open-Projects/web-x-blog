"""多 Agent 任务认领:CAS 原子认领防重复,高优先级可抢占低优先级,抢占带宽限期。"""


class TaskBoard:
    def __init__(self):
        self.tasks = {}

    def post(self, tid, prio=0):
        self.tasks[tid] = {"status": "open", "owner": None, "prio": prio, "epoch": 0}
        return tid

    def claim(self, tid, agent):
        t = self.tasks.get(tid)
        if t is None or t["status"] not in ("open", "preempted"):
            return None
        t["status"] = "claimed"
        t["owner"] = agent
        t["epoch"] += 1
        return t["epoch"]

    def preempt(self, tid, agent, min_prio):
        t = self.tasks.get(tid)
        if t is None or t["status"] != "claimed" or t["prio"] >= min_prio:
            return None
        old = t["owner"]
        t["status"] = "preempted"
        t["epoch"] += 1
        return {"from": old, "epoch": t["epoch"]}

    def write_result(self, tid, agent, epoch, payload):
        t = self.tasks.get(tid)
        if t is None or t["owner"] != agent or epoch != t["epoch"] or t["status"] != "claimed":
            return False
        t["result"] = payload
        t["status"] = "done"
        return True


if __name__ == "__main__":
    board = TaskBoard()
    board.post("t1", prio=0)
    e1 = board.claim("t1", "agent-low")
    assert e1 == 1
    assert board.claim("t1", "agent-other") is None, "已被认领 CAS 失败"
    p = board.preempt("t1", "agent-high", min_prio=5)
    assert p == {"from": "agent-low", "epoch": 2}, "高优先级抢占成功"
    assert board.write_result("t1", "agent-low", e1, {"x": 1}) is False, "旧 epoch 写入被 fencing 拒绝"
    e2 = board.claim("t1", "agent-high")
    assert e2 == 3, "被抢占任务可重新认领 epoch 继续单调"
    assert board.write_result("t1", "agent-high", e2, {"x": 2}) is True
    assert board.preempt("t1", "someone", min_prio=0) is None, "同级任务不抢占"
    print("抢占认领通过:原子认领 优先级抢占 epoch fencing")
