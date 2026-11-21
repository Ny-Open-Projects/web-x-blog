"""zset 延迟队列: 原子取到期任务 + 失败回队"""
import time

class DelayQueue:
    def __init__(self):
        self.zset = {}                          # task -> due_ts

    def offer(self, task, delay_sec):
        self.zset[task] = time.monotonic() + delay_sec

    def poll_due(self, now=None, limit=5):
        now = now if now is not None else time.monotonic()
        due = sorted((t for t, d in self.zset.items() if d <= now))[:limit]
        for t in due:                           # 原子语义: 取出即移除
            del self.zset[t]
        return due

    def nack(self, task, delay_sec, max_retry):
        retry = self.retry.get(task, 0) + 1 if hasattr(self, "retry") else 1
        self.retry = getattr(self, "retry", {})
        self.retry[task] = retry
        if retry <= max_retry:
            self.offer(task, delay_sec)
        return retry <= max_retry

if __name__ == "__main__":
    dq = DelayQueue()
    dq.offer("order:1", 0.2)                    # 0.2 秒后到期(模拟30分钟)
    dq.offer("order:2", 0.5)
    for _ in range(6):
        due = dq.poll_due()
        if due:
            print(f"{time.monotonic():.1f} 到期任务:", due)
            for t in due:
                if t == "order:2":
                    dq.nack(t, 0.3, max_retry=1)
                    print("  order:2 处理失败, 延后重试")
        time.sleep(0.2)
