"""过期时间的业务语义分层: 不同数据不同 TTL 策略"""
import random

POLICY = {
    "cfg":  {"ttl": 86400, "jitter": 0.0, "mode": "fixed",   "why": "配置类 变更走主动失效 TTL 兜底"},
    "rank": {"ttl": 60,    "jitter": 0.1, "mode": "fixed",   "why": "榜单 短 TTL 加抖动防雪崩"},
    "sess": {"ttl": 1800,  "jitter": 0.0, "mode": "sliding", "why": "会话 活跃就续期 闲置即失效"},
    "idem": {"ttl": 600,   "jitter": 0.0, "mode": "fixed",   "why": "幂等键 覆盖上游最大重试窗口"},
    "neg":  {"ttl": 60,    "jitter": 0.2, "mode": "fixed",   "why": "负缓存 短命 防止固化缺失"},
}

def resolve(kind, rnd=random.random):
    p = POLICY[kind]
    ttl = int(p["ttl"] * (1 + rnd() * p["jitter"])) if p["jitter"] else p["ttl"]
    return ttl, p["mode"]

random.seed(7)
print("kind   ttl秒  模式       说明")
for kind in POLICY:
    ttl, mode = resolve(kind)
    print("%-5s %6d  %-8s  %s" % (kind, ttl, mode, POLICY[kind]["why"]))

now, expire = 1000, 1000 + POLICY["sess"]["ttl"]
for access in (1100, 1400, 2000):
    if access >= expire:
        print("t=%d 会话已过期" % access)
    else:
        expire = access + POLICY["sess"]["ttl"]
        print("t=%d 访问, 会话滑动续期到 t=%d" % (access, expire))
print("TTL 定错的症状能反推语义: 负缓存过长是复活慢, 幂等键过短是重试被放行")
