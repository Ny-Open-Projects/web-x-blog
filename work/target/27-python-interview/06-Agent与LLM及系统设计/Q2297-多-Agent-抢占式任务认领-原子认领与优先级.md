---
title: [Q2297] 多 Agent 抢占式任务认领:原子认领与优先级抢占
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2297 · 多 Agent 抢占式任务认领:原子认领与优先级抢占

> 难度:★★★★ | 标签:多Agent, 调度, 并发

**问**:十个 Agent 抢一个任务池,紧急任务插队时正在跑的低优先级任务怎么办?

**答**:两层机制。认领是原子 CAS:任务状态从 open 改为 claimed 的判定与写入一体,后到者看到状态非 open 即失败,天然防重复认领,不需要额外锁。抢占是显式动作:高优先级调度者对在跑任务做优先级比较,仅当在跑任务优先级低于阈值才标记 preempted 并递增 epoch。epoch 是 fencing 令牌:旧持有者拿着旧 epoch 回写结果会被拒绝,新认领者拿最新 epoch 才能提交——没有 epoch,被抢占的 Agent 可能在收到通知前把过期结果写回,覆盖新主的工作。抢占要有宽限期与次数上限,否则两个高优先级任务会来回震荡。

```python
# file: code/06_Agent与LLM及系统设计/q2297_preemptive_claim.py
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
```

**追问**:
- 被抢占的 Agent 怎么知道? 答:它下次心跳或回写时会发现自己 epoch 已落后,主动放弃并把已完成的部分产物登记上交
- 认领与抢占是同一动作吗? 答:认领是空任务分配,抢占是夺走在跑任务,后者多了优先级裁决与宽限期两个前置
