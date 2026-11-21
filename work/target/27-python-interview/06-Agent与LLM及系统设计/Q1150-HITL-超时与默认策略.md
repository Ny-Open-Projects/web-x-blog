---
title: [Q1150] HITL 超时与默认策略
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1150 · HITL 超时与默认策略

> 难度:★★★☆ | 标签:HITL, 可靠性

**问**:审批流挂起后一直没人响应,任务卡死怎么解?

**答**:每个审批单必须带截止时间与超时默认策略(deny-by-default 或 safe-default)。deny 模式超时自动驳回任务转 FAILED 或 CANCELLED;safe-default 模式执行预定义的安全替代动作(如"转账失败则先冻结订单并通知人工")。实现上用定时扫描器扫 `PAUSED + 超时` 的单子统一处理,并给审批人发提醒与二次升级。所有超时决策要留痕,因为"系统替人做的决定"在审计上等同于人的决定。

```python
# file: code/06_Agent与LLM及系统设计/q1150_hitl_timeout.py
"""审批超时处理:定时扫描挂起审批单,按策略执行 deny 或 safe-default。"""
import time


class TimeoutScanner:
    def __init__(self):
        self.orders = []                      # {id, deadline, policy, task}

    def create(self, oid, ttl_sec, policy, task):
        assert policy in ("deny", "safe_default")
        self.orders.append({"id": oid, "deadline": time.monotonic() + ttl_sec,
                            "policy": policy, "task": task, "notified": False})

    def scan(self, now=None):
        now = time.monotonic() if now is None else now
        actions = []
        for o in self.orders:
            if o["task"]["state"] != "PAUSED":
                continue
            remain = o["deadline"] - now
            if 0 < remain <= 0.05 and not o["notified"]:
                o["notified"] = True
                actions.append(f"提醒审批人处理 {o['id']}")
            elif remain <= 0:
                if o["policy"] == "deny":
                    o["task"]["state"] = "CANCELLED"
                    actions.append(f"{o['id']} 超时自动驳回,任务取消")
                else:
                    o["task"]["state"] = "RUNNING"
                    o["task"]["fallback"] = "order_frozen_and_notified"
                    actions.append(f"{o['id']} 超时执行安全默认动作,任务继续")
        return actions


if __name__ == "__main__":
    scanner = TimeoutScanner()
    t1 = {"id": "t1", "state": "PAUSED"}
    t2 = {"id": "t2", "state": "PAUSED"}
    scanner.create("a1", ttl_sec=0.1, policy="deny", task=t1)
    scanner.create("a2", ttl_sec=0.2, policy="safe_default", task=t2)
    print("扫描1:", scanner.scan())            # 未到期,无动作
    time.sleep(0.12)
    print("扫描2:", scanner.scan())            # a1 超时驳回
    time.sleep(0.12)
    print("扫描3:", scanner.scan())            # a2 超时安全默认
    assert t1["state"] == "CANCELLED"
    assert t2["state"] == "RUNNING" and t2["fallback"]
    print("deny 与 safe_default 两种超时策略均生效")
```

**追问**:
- 超时默认策略怎么选?答:看动作可逆性——可逆动作可 safe-default,不可逆动作(转账/删除)必须 deny,原则是"超时的代价小于错误执行的代价"。
- 提醒风暴怎么防?答:同一审批单提醒幂等(notified 标志),按升级阶梯限频,超期转人工队列而不是反复催。
