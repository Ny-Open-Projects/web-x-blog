"""限流下的排队策略:优先级加截止时间的队,同级按截止早先走,过期即弃不占额度。"""
import heapq


class QueueFull(Exception):
    pass


class DeadlineQueue:
    def __init__(self, max_size=100):
        self.heap = []
        self.seq = 0
        self.expired = 0
        self.max_size = max_size

    def push(self, priority, deadline, payload):
        if len(self.heap) >= self.max_size:
            raise QueueFull("队列已满,快速拒绝胜过无界排队")
        self.seq += 1
        # 键:高优先在前;同级截止早在前;再按入队序保公平
        heapq.heappush(self.heap, (-priority, deadline, self.seq, payload))

    def pop(self, now):
        """取下一个未过期任务,跳过并计数过期项,空则 None。"""
        while self.heap:
            negp, deadline, seq, payload = heapq.heappop(self.heap)
            if deadline < now:
                self.expired += 1
                continue
            return payload
        return None

    def __len__(self):
        return len(self.heap)


if __name__ == "__main__":
    q = DeadlineQueue(max_size=3)
    # 同优先级:截止早的先走
    q.push(5, 100, "job-a")
    q.push(5, 50, "job-b")
    assert q.pop(now=0) == "job-b", "同级按截止时间早先出队"

    # 高优先级压过截止更早的低优先级
    q.push(9, 40, "vip")
    q.push(1, 10, "batch")
    assert q.pop(now=0) == "vip"

    # 过期即弃:出队时已过截止的任务被丢弃并计数
    q2 = DeadlineQueue()
    q2.push(3, 10, "stale")
    q2.push(3, 100, "fresh")
    assert q2.pop(now=50) == "fresh", "过期项被跳过"
    assert q2.expired == 1
    q2.push(3, 60, "late")                  # 入队即已临近过期
    assert q2.pop(now=200) is None and q2.expired == 2, "全部过期返回 None"

    # 满员快速拒绝
    q3 = DeadlineQueue(max_size=2)
    q3.push(1, 10, "a")
    q3.push(1, 20, "b")
    try:
        q3.push(1, 30, "c")
        raise AssertionError("满员必须快速拒绝")
    except QueueFull:
        pass
    print("排队策略通过:同级 EDF 高优先走,过期即弃计数,满员快速拒绝")
