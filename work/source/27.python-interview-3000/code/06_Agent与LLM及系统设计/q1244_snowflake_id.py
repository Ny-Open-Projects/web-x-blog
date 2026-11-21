"""雪花 ID:位布局 + 序列号溢出等待 + 时钟回拨处理 + 全局唯一验证。"""
import threading, time


class Snowflake:
    TS_BITS, MACHINE_BITS, SEQ_BITS = 41, 10, 12

    def __init__(self, machine_id, epoch=1700000000000):
        assert 0 <= machine_id < (1 << self.MACHINE_BITS), "机器位必须全局唯一"
        self.machine, self.epoch = machine_id, epoch
        self.seq, self.last_ts = 0, -1
        self.mu = threading.Lock()

    def _ts(self):
        return int(time.time() * 1000) - self.epoch

    def next_id(self):
        with self.mu:
            ts = self._ts()
            if ts < self.last_ts:                        # 时钟回拨
                if self.last_ts - ts <= 5:               # 小回拨:等待追上
                    while ts <= self.last_ts:
                        time.sleep(0.001)
                        ts = self._ts()
                else:
                    raise RuntimeError(f"时钟回拨 {self.last_ts - ts}ms,拒绝发号")
            if ts == self.last_ts:
                self.seq = (self.seq + 1) & ((1 << self.SEQ_BITS) - 1)
                if self.seq == 0:                        # 单毫秒 4096 用尽
                    while ts <= self.last_ts:
                        time.sleep(0.001)
                        ts = self._ts()
            else:
                self.seq = 0
            self.last_ts = ts
            return (ts << (self.MACHINE_BITS + self.SEQ_BITS)) | \
                   (self.machine << self.SEQ_BITS) | self.seq


if __name__ == "__main__":
    sf = Snowflake(machine_id=7)
    ids = [sf.next_id() for _ in range(100)]
    print("样例 ID:", ids[:3])
    assert len(set(ids)) == 100, "同机必须唯一"
    assert all(a < b for a, b in zip(ids, ids[1:])), "同线程趋势递增"

    # 位段解析验证
    sid = ids[0]
    seq = sid & ((1 << 12) - 1)
    machine = (sid >> 12) & ((1 << 10) - 1)
    assert machine == 7 and 0 <= seq < 4096
    print(f"位段解析: machine={machine} seq={seq}")

    # 双机不同 machine_id 不冲突
    sf2 = Snowflake(machine_id=8)
    s1, s2 = sf.next_id(), sf2.next_id()
    assert ((s1 >> 12) & 1023) != ((s2 >> 12) & 1023)
    print("多机 machine 位隔离,无协调器下不会撞号")

    # 重复 machine_id 会撞号(演示约定的重要性)
    sfa, sfb = Snowflake(7), Snowflake(7)
    pool = {sfa.next_id() for _ in range(50)} | {sfb.next_id() for _ in range(50)}
    print("同 machine_id 双实例 100 个 ID 去重后:", len(pool), "<= 100(撞号风险)")
    assert len(pool) < 100, "错误配置必然产生重复"
