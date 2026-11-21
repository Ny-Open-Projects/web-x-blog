"""反压队列:有界容量,队满按策略阻塞 丢新 丢旧,压力可观测。"""
from collections import deque


class BackpressureQueue:
    def __init__(self, capacity, policy="block"):
        assert policy in ("block", "drop_newest", "drop_oldest")
        self.q = deque(maxlen=capacity if policy == "drop_oldest" else None)
        self.capacity = capacity
        self.policy = policy
        self.metrics = {"put": 0, "blocked": 0, "dropped": 0}

    def put(self, item):
        """返回 True 表示入队;block 策略演示中返回 False 表示向上游施压。"""
        self.metrics["put"] += 1
        if self.policy == "drop_oldest":
            if len(self.q) == self.capacity:
                self.metrics["dropped"] += 1     # 挤掉最旧
            self.q.append(item)
            return True
        if len(self.q) >= self.capacity:
            if self.policy == "drop_newest":
                self.metrics["dropped"] += 1
                return False
            self.metrics["blocked"] += 1         # 真实实现为阻塞等待,这里标记施压
            return False
        self.q.append(item)
        return True

    def get(self):
        return self.q.popleft() if self.q else None

    def __len__(self):
        return len(self.q)


if __name__ == "__main__":
    q1 = BackpressureQueue(capacity=3, policy="block")
    assert [q1.put(i) for i in range(5)] == [True, True, True, False, False]
    assert q1.metrics["blocked"] == 2 and len(q1) == 3
    assert [q1.get() for _ in range(3)] == [0, 1, 2], "施压不丢数据"

    q2 = BackpressureQueue(capacity=3, policy="drop_newest")
    assert [q2.put(i) for i in range(5)] == [True, True, True, False, False]
    assert q2.metrics["dropped"] == 2
    assert [q2.get() for _ in range(3)] == [0, 1, 2], "保旧弃新"

    q3 = BackpressureQueue(capacity=3, policy="drop_oldest")
    assert [q3.put(i) for i in range(5)] == [True] * 5
    assert q3.metrics["dropped"] == 2
    assert list(q3.q) == [2, 3, 4], "保新弃旧"
    print("反压队列通过:block 施压不丢数 drop_newest 保旧 drop_oldest 保新,容量恒有界")
