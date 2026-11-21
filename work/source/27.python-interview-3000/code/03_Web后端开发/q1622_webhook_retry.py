"""Webhook 投递重试: 指数退避 + 全抖动 + Retry-After 优先(纯标准库)。"""
import random

random.seed(7)                                   # 固定种子让演示可复现


def next_delay(attempt, retry_after=None, base=1.0, cap=60.0):
    if retry_after is not None:
        return float(retry_after)                # 对端明确指示就听对端的
    ceiling = min(cap, base * 2 ** (attempt - 1))
    return random.uniform(0, ceiling)            # full jitter 把重试打散


def deliver_schedule(statuses):
    """statuses: 每次投递的模拟状态码, None 表示成功。"""
    timeline, t = [], 0.0
    for attempt, status in enumerate(statuses, 1):
        timeline.append((attempt, round(t, 1), status if status else 200))
        if status is None:
            break
        retry_after = 30 if status == 429 else None
        t += next_delay(attempt, retry_after)
    return timeline


statuses = [503, 429, 500, None]
for attempt, at, status in deliver_schedule(statuses):
    print(f"第 {attempt} 次  t={at:>5}s  -> {status}")
print("要点: 退避防打爆对端, 抖动防同一时刻重放, Retry-After 是对端明确意图, 优先级最高")
