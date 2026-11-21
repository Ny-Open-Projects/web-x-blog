"""慢查询采样器: 全量阈值记录加概率抽样"""
import random
import time

random.seed(3)

class SlowQuerySampler:
    def __init__(self, threshold_ms=20.0, sample_rate=0.1, max_per_window=5):
        self.threshold_ms = threshold_ms
        self.sample_rate = sample_rate
        self.window = 1.0
        self.window_start = time.monotonic()
        self.logged_in_window = 0
        self.max_per_window = max_per_window
        self.captured = []
        self.total = 0
        self.slow_total = 0
    def observe(self, sql, elapsed_ms):
        self.total += 1
        now = time.monotonic()
        if now - self.window_start > self.window:
            self.window_start = now
            self.logged_in_window = 0
        if elapsed_ms >= self.threshold_ms:
            self.slow_total += 1
            self.captured.append((sql, round(elapsed_ms, 1)))
            return True
        if random.random() < self.sample_rate and self.logged_in_window < self.max_per_window:
            self.captured.append((sql, round(elapsed_ms, 1)))
            self.logged_in_window += 1
            return True
        return False

sampler = SlowQuerySampler()
queries = []
for i in range(400):
    if i % 40 == 0:
        queries.append(("SELECT * FROM orders WHERE user_id = ? 慢", 35 + random.random() * 10))
    else:
        queries.append(("SELECT * FROM users WHERE id = ?", random.random() * 15))

kept = 0
for sql, ms in queries:
    if sampler.observe(sql, ms):
        kept += 1
print(f"总查询 {sampler.total}  慢查询 {sampler.slow_total} 全量捕获")
print(f"快速查询按 {sampler.sample_rate:.0%} 抽样 共记录 {kept} 条 日志量压到 {kept / sampler.total:.1%}")
print("捕获样例 ->", sampler.captured[:6])
print("结论: 慢查询全量记录 快查询低概率抽样加窗口限流 既保住长尾可见性又不把日志打爆")
