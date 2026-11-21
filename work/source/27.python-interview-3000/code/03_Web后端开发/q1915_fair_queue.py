"""请求队列公平性: 按用户轮转调度防止单一大户饿死他人(纯标准库)。"""
from collections import deque, OrderedDict


class FairQueue:
    """每键独立队列 + 轮转出队; 键可以是用户、租户或 API key。

    FIFO 全局队列下大户的 100 个请求会排在别人前面; 轮转保证按人公平。
    """

    def __init__(self, weights=None):
        self.queues = OrderedDict()       # key -> deque, 保持插入顺序轮转
        self.weights = weights or {}
        self.credits = {}                 # 每轮次的剩余信用

    def push(self, key, item):
        self.queues.setdefault(key, deque()).append(item)

    def _round_robin(self):
        """依次扫每个非空键, 按权重取走对应数量, 模拟加权轮转。"""
        while any(self.queues.values()):
            for key in list(self.queues):
                q = self.queues.get(key)
                if not q:
                    continue
                weight = self.weights.get(key, 1)
                for _ in range(weight):
                    if q:
                        yield q.popleft()
                if not q:
                    self.queues.pop(key, None)

    def drain(self):
        return list(self._round_robin())


# 大户 alice 连发 4 个, 小户 bob carol 各 1 个
fair = FairQueue()
for i in range(4):
    fair.push("alice", "alice-%d" % i)
fair.push("bob", "bob-0")
fair.push("carol", "carol-0")
print("公平调度顺序:", fair.drain())
fair2 = FairQueue()
for i in range(4):
    fair2.push("alice", "alice-%d" % i)
fair2.push("bob", "bob-0")
fair2.push("carol", "carol-0")
naive = [x for q in fair2.queues.values() for x in q]
print("朴素 FIFO 顺序:", naive)
assert naive[:4] == ["alice-0", "alice-1", "alice-2", "alice-3"]

# VIP 加权: 权重 2 的用户每轮拿 2 个名额
vip = FairQueue(weights={"alice": 2})
vip.push("alice", "a1")
vip.push("alice", "a2")
vip.push("bob", "b1")
vip.push("carol", "c1")
order = vip.drain()
print("加权轮转顺序:", order)
assert order[:2] == ["a1", "a2"] and order[2:4] == ["b1", "c1"]
print("要点: 公平性按键轮转而不是按到达时间, 权重表达付费等级, 队头阻塞不会跨越用户边界")
