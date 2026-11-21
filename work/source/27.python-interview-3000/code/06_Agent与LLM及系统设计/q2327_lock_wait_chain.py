"""行级锁等待链:谁持有什么 谁在等谁构成等待图,图上有环即死锁,选牺牲者解锁。"""
class RowLockManager:
    def __init__(self):
        self.holders = {}
        self.waits = {}
        self.victims = []

    def acquire(self, row, txn):
        holder = self.holders.get(row)
        if holder is None or holder == txn:
            self.holders[row] = txn
            self.waits.pop(txn, None)
            return True
        self.waits[txn] = holder
        return False

    def release(self, row, txn):
        if self.holders.get(row) == txn:
            del self.holders[row]

    def find_deadlock(self):
        for start in list(self.waits):
            seen, node = [], start
            while node in self.waits:
                if node in seen:
                    return seen[seen.index(node):]
                seen.append(node)
                node = self.waits[node]
        return None

    def resolve_deadlock(self, victim_policy=min):
        cycle = self.find_deadlock()
        if not cycle:
            return None
        victim = victim_policy(cycle)
        self.victims.append(victim)
        for row in [r for r, t in self.holders.items() if t == victim]:
            self.release(row, victim)
        self.waits.pop(victim, None)
        return victim


if __name__ == "__main__":
    lm = RowLockManager()
    assert lm.acquire("r1", "T1")
    assert lm.acquire("r2", "T2")
    assert not lm.acquire("r2", "T1"), "T1 等 T2"
    assert not lm.acquire("r1", "T2"), "T2 等 T1 成环"
    cycle = lm.find_deadlock()
    assert cycle == ["T1", "T2"], "等待图找到环"
    victim = lm.resolve_deadlock()
    assert victim == "T1", "选字典序最小为牺牲者"
    assert "r1" not in lm.holders, "牺牲者的锁被释放"
    assert lm.acquire("r1", "T2"), "T2 重试拿到 r1"
    assert lm.waits == {}, "等待链清空"
    lm2 = RowLockManager()
    lm2.acquire("r3", "T9")
    assert not lm2.acquire("r3", "T8")
    assert lm2.find_deadlock() is None, "单链等待不是死锁"
    print("等待链通过:等待图建边 成环即死锁 选牺牲者解锁")
