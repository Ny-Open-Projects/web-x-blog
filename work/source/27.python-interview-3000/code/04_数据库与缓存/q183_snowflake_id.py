"""雪花算法生成趋势递增的 64 位全局 ID(纯标准库)"""
import threading
import time


class Snowflake:
    TIMESTAMP_BITS, WORKER_BITS, SEQ_BITS = 41, 10, 12
    EPOCH = 1704038400000        # 2024-01-01 起始纪元, ms

    def __init__(self, worker_id: int):
        assert 0 <= worker_id < (1 << self.WORKER_BITS)
        self.worker_id = worker_id
        self._seq = 0
        self._last_ts = -1
        self._lock = threading.Lock()

    def _now_ms(self) -> int:
        return int(time.time() * 1000)

    def next_id(self) -> int:
        with self._lock:
            ts = self._now_ms()
            if ts == self._last_ts:
                self._seq = (self._seq + 1) & ((1 << self.SEQ_BITS) - 1)
                if self._seq == 0:              # 同毫秒序列用尽, 等下一毫秒
                    while ts <= self._last_ts:
                        ts = self._now_ms()
            else:
                self._seq = 0
            if ts < self._last_ts:
                raise RuntimeError("时钟回拨, 拒绝发号")
            self._last_ts = ts
            return (
                ((ts - self.EPOCH) << (self.WORKER_BITS + self.SEQ_BITS))
                | (self.worker_id << self.SEQ_BITS)
                | self._seq
            )


if __name__ == "__main__":
    sf = Snowflake(worker_id=1)
    ids = [sf.next_id() for _ in range(5)]
    print("生成 ID:", ids)
    print("严格递增:", all(a < b for a, b in zip(ids, ids[1:])))
