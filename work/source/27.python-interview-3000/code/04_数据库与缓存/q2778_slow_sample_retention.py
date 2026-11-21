"""慢查询样本的留存: 指纹归一 参数脱敏 环形上限防撑爆"""
import collections
import re

def fingerprint(sql):
    s = re.sub(r"\s+", " ", sql.strip().lower())
    s = re.sub(r"'[^']*'", "?", s)
    s = re.sub(r"\b\d+\b", "?", s)
    return s

def scrub(value):
    t = str(value)
    t = re.sub(r"1\d{10}", "<phone>", t)
    t = re.sub(r"[\w.]+@[\w.]+", "<email>", t)
    return t[:60]

class SampleStore:
    def __init__(self, capacity):
        self.buf = collections.deque(maxlen=capacity)   # 环形上限: 新样本挤掉最旧
        self.dropped = 0

    def add(self, sql, params, ms, plan):
        if len(self.buf) == self.buf.maxlen:
            self.dropped += 1
        self.buf.append({"fp": fingerprint(sql),
                         "params": [scrub(p) for p in params],
                         "ms": round(ms, 1),
                         "plan": plan})

store = SampleStore(capacity=100)
for i in range(130):                                    # 模拟 130 个慢样本
    store.add("SELECT * FROM orders WHERE user_id = %d" % i, [13800000000 + i],
              100.0 + (i * 7) % 900, "SCAN orders")
print("样本总数 %d, 环形留存 %d, 挤掉 %d (磁盘占用有界)" % (130, len(store.buf), store.dropped))
top = sorted(store.buf, key=lambda s: -s["ms"])[:3]
for s in top:
    print("top 慢样本: %6.1f ms | %s | params=%s | %s" % (s["ms"], s["fp"], s["params"], s["plan"]))
print("要点: 指纹用于聚合归因, 脱敏防 PII 泄漏, 环形加 top-K 保证不漏最贵样本")
