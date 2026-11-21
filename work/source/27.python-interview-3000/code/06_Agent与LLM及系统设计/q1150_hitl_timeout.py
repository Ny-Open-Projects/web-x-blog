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
