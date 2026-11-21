"""Q2837 任务队列的提交幂等:同键复用任务号与参数冲突拒收。

用户双击提交 网络重发 上游重试,都会把同一个任务投两遍。提交层幂等:
同一个幂等键在窗口内重复提交,直接返回原任务号而不是再建一个任务;
键相同但参数指纹不同,说明是业务冲突,宁可报错也不能悄悄新开任务。
"""

import hashlib
import json


def fingerprint(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    ).hexdigest()[:12]


class TaskQueue:
    def __init__(self, window_s):
        self.window = window_s
        self.store = {}
        self.counter = 0

    def submit(self, key, payload, now):
        fp = fingerprint(payload)
        hit = self.store.get(key)
        if hit is not None and now - hit["ts"] < self.window:
            if hit["fp"] != fp:
                return None, "conflict"
            return hit["id"], "replayed"
        self.counter += 1
        tid = "task_%03d" % self.counter
        self.store[key] = {"id": tid, "fp": fp, "ts": now}
        return tid, "created"


def main():
    q = TaskQueue(window_s=60)
    payload = {"account": "a1", "amount": 100}
    t1, r1 = q.submit("order_9", payload, now=1000)
    assert r1 == "created" and t1 == "task_001", (t1, r1)
    # 三秒后同键同参重发:拿到同一个任务号,不再新建
    t2, r2 = q.submit("order_9", payload, now=1003)
    assert t2 == t1 and r2 == "replayed", (t2, r2)
    # 同键不同参:业务冲突,拒收
    t3, r3 = q.submit("order_9", {"account": "a1", "amount": 999}, now=1005)
    assert t3 is None and r3 == "conflict", (t3, r3)
    # 窗口过后同键再来:允许新任务(业务上的新一轮)
    t4, r4 = q.submit("order_9", payload, now=1100)
    assert r4 == "created" and t4 == "task_002", (t4, r4)
    assert q.counter == 2, q.counter  # 五次提交只建了两个任务
    print("提交1:", t1, r1, "| 提交2:", t2, r2)
    print("冲突提交:", r3, "| 窗口后:", t4, r4, "| 实际建任务数:", q.counter)


if __name__ == "__main__":
    main()
