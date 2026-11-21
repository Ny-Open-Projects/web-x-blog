"""雪花 ID 最小实现: 趋势递增 + 时钟回拨保护"""
import threading
import time

class Snowflake:
    def __init__(self, worker: int, ts_bits=41, worker_bits=10, seq_bits=12):
        self.worker = worker
        self.seq = 0
        self.last = -1
        self.ts_bits, self.worker_bits, self.seq_bits = ts_bits, worker_bits, seq_bits
        self.epoch = 1700000000000
        self.lock = threading.Lock()

    def next_id(self) -> int:
        with self.lock:
            ts = int(time.time() * 1000)
            if ts < self.last:                       # 时钟回拨: 等待追平
                ts = self.last
            if ts == self.last:
                self.seq = (self.seq + 1) & ((1 << self.seq_bits) - 1)
                if self.seq == 0:                    # 本毫秒序列耗尽
                    while int(time.time() * 1000) <= self.last:
                        pass
            else:
                self.seq = 0
            self.last = ts
            return ((ts - self.epoch) << (self.worker_bits + self.seq_bits)
                    | (self.worker << self.seq_bits) | self.seq)

if __name__ == "__main__":
    sf = Snowflake(worker=1)
    ids = [sf.next_id() for _ in range(5)]
    print(ids)
    print("趋势递增:", ids == sorted(ids))
    print(f"41 位时间戳可用约 {(1 << 41) / 1000 / 86400 / 365:.0f} 年")
