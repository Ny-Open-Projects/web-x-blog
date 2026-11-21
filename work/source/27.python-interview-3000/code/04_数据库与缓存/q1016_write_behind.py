"""Write-Behind: 缓冲计数, 定时批量落库, 失败回滚缓冲"""
import time

class WriteBehindCounter:
    def __init__(self, db_value=0):
        self.buffer = 0                          # 未落库的增量
        self.db_value = db_value
        self.pending_batches = []

    def incr(self, n=1):
        self.buffer += n                         # 只写缓存, 立即返回

    def flush(self):
        if self.buffer == 0:
            return "无事可刷"
        batch, self.buffer = self.buffer, 0
        self.pending_batches.append(batch)       # 模拟写 DB
        self.db_value += batch
        return f"落库 +{batch}, DB={self.db_value}"

    def on_flush_fail(self, batch):
        self.buffer += batch                     # 失败回滚到缓冲, 等下轮
        return "缓冲恢复, 重试中"

if __name__ == "__main__":
    c = WriteBehindCounter()
    for _ in range(100):                         # 高频写只碰内存
        c.incr()
    print("100 次写后:", c.flush())
    print("丢失窗口: flush 前进程崩溃 -> 最多丢一个批次的增量")
    print("资金场景禁用; 计数/赞/浏览量可接受并配对账")
