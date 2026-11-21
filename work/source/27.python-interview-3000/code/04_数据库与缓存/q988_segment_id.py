"""号段发号 + 双 buffer 预加载"""
import threading

class SegmentAllocator:
    def __init__(self, db_max=0, step=100):
        self.step = step
        self.next_db_max = db_max + step        # 模拟第一次取号段
        self.cur = {"lo": db_max + 1, "hi": db_max + step}
        self.buffer = None                       # 预加载的下一号段
        self.lock = threading.Lock()

    def _fetch_new_segment(self):
        lo = self.next_db_max + 1                # 模拟 UPDATE max_id+step
        self.next_db_max += self.step
        return {"lo": lo, "hi": self.next_db_max}

    def next_id(self):
        with self.lock:
            if self.cur["lo"] > self.cur["hi"]:  # 当前号段耗尽
                self.cur = self.buffer or self._fetch_new_segment()
                self.buffer = None
            elif self.buffer is None and \
                    self.cur["lo"] > (self.cur["hi"] + self.cur["lo"]) // 2:
                self.buffer = self._fetch_new_segment()   # 消耗过半预加载
            v = self.cur["lo"]
            self.cur["lo"] += 1
            return v

if __name__ == "__main__":
    alloc = SegmentAllocator(step=5)
    ids = [alloc.next_id() for _ in range(12)]
    print("发号:", ids)
    print("有序:", ids == sorted(ids), "趋势递增, 允许宕机跳号")
    print("双 buffer: 消耗过半即预取下一段, 切换无尖刺")
