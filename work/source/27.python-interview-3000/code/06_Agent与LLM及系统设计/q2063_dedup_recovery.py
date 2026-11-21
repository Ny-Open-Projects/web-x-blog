"""去重窗口的崩溃恢复:定期快照去重表,重启后窗口内重复仍被挡,快照后的会重放。"""
import json


class PersistentDedup:
    def __init__(self, ttl):
        self.ttl = ttl
        self.table = {}          # msg_id -> expire_at
        self.snapshot = {}
        self.processed = []

    def process(self, msg_id, now):
        self._evict(now)
        if msg_id in self.table:
            return False         # 去重命中,不重复处理
        self.table[msg_id] = now + self.ttl
        self.processed.append(msg_id)
        return True

    def snapshot_now(self, now):
        self._evict(now)
        self.snapshot = dict(self.table)
        return json.dumps(sorted(self.snapshot.items()))

    def crash_and_recover(self, now):
        """模拟崩溃:活表全丢,从最近快照恢复,并清掉已过期的快照项。"""
        self.table = dict(self.snapshot)
        self._evict(now)
        return len(self.table)

    def _evict(self, now):
        for k in [k for k, e in self.table.items() if e <= now]:
            del self.table[k]


if __name__ == "__main__":
    pd = PersistentDedup(ttl=100)
    assert pd.process("m1", 0) is True
    assert pd.process("m2", 10) is True
    assert pd.process("m1", 20) is False, "崩溃前去重正常工作"
    pd.snapshot_now(20)                  # 快照时点:T=20,含 m1 m2

    # 崩溃后恢复:m1 m2 仍在窗口内,重复投递照样被挡
    assert pd.crash_and_recover(30) == 2
    assert pd.process("m1", 30) is False, "快照恢复后窗口内重复仍被挡"

    # 快照后才处理的 m3 不在快照里:恢复后重复投递会被再处理一次
    assert pd.process("m3", 40) is True
    pd.crash_and_recover(50)
    assert pd.process("m3", 50) is True, "快照缺口的 m3 会被重放,下游必须幂等"
    assert pd.processed.count("m3") == 2

    # 快照本身也过 TTL:恢复后窗口全空
    pd2 = PersistentDedup(ttl=50)
    pd2.process("x", 0)
    pd2.snapshot_now(0)
    pd2.crash_and_recover(100)
    assert pd2.table == {}, "过期快照恢复出空窗,宁重放不误挡"
    print("崩溃恢复通过:快照内重复照挡,快照缺口重放一次,TTL 过后窗口归零")
