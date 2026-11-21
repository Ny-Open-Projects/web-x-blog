"""追踪的尾部采样: 错误与慢请求全保, 正常按比例(纯标准库)。"""
import random

random.seed(21)

# 模拟 200 个请求的 span: duration 秒, error 标志
spans = []
for i in range(200):
    roll = random.random()
    if roll < 0.05:
        spans.append({"id": i, "duration": random.uniform(0.8, 2.5), "error": True})
    elif roll < 0.15:
        spans.append({"id": i, "duration": random.uniform(1.1, 1.6), "error": False})
    else:
        spans.append({"id": i, "duration": random.uniform(0.02, 0.3), "error": False})

SLOW_MS = 1000          # 慢阈值
NORMAL_KEEP = 0.05      # 正常请求保留 5%


def tail_sample(span_list, slow_threshold, normal_keep):
    """尾部采样: 采样决策在请求结束后作出, 三类必留: 错误、慢、随机正常。"""
    kept, reasons = [], {}
    for s in span_list:
        if s["error"]:
            reasons[s["id"]] = "error"
            kept.append(s)
        elif s["duration"] > slow_threshold:
            reasons[s["id"]] = "slow"
            kept.append(s)
        elif random.random() < normal_keep:
            reasons[s["id"]] = "baseline"
            kept.append(s)
    return kept, reasons


kept, reasons = tail_sample(spans, SLOW_MS / 1000.0, NORMAL_KEEP)
from collections import Counter
stat = Counter(reasons.values())
print("总数 {} 保留 {} 原因分布: {}".format(len(spans), len(kept), dict(stat)))
assert stat["error"] == sum(1 for s in spans if s["error"])
assert stat["slow"] == sum(1 for s in spans
                           if not s["error"] and s["duration"] > 1.0)

# 全错场景: 错误保留率 100%, 正常请求大幅丢弃降低存储成本
normal_total = sum(1 for s in spans if not s["error"] and s["duration"] <= 1.0)
print("正常请求 {}/{} 保留率 {:.0%}".format(
    stat["baseline"], normal_total, stat["baseline"] / float(normal_total)))
assert stat["baseline"] < normal_total * 0.15
print("要点: 头部采样省的是采集成本, 尾部采样保的是诊断价值, 错误与慢请求必须 100% 留存")
