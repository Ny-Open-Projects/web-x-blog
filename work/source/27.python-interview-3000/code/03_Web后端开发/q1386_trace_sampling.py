"""跨服务一致性采样:上游决策加传播头,下游跟随(纯标准库)。"""
import hashlib


def sample_decision(trace_id, rate):
    return int(hashlib.sha256(("sampling:" + trace_id).encode()).hexdigest(), 16) % 100 < rate * 100


def upstream(trace_id, rate=0.5):
    keep = sample_decision(trace_id, rate)
    return keep, {"x-trace-id": trace_id, "x-sampled": "1" if keep else "0"}


def downstream(headers):
    if "x-sampled" in headers:
        return headers["x-sampled"] == "1"     # 尊重上游决定
    return False                               # 无头时按自身策略兜底


for tid in ("t-aaa", "t-bbb", "t-ccc"):
    keep, headers = upstream(tid)
    print(tid, "上游决策:", keep, "下游跟随:", downstream(headers),
          "一致:", keep == downstream(headers))
