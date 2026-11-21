"""按用户维度限流: 身份键解析链与 429 响应语义(纯标准库)。"""
import time


def resolve_key(request):
    """身份键解析链: API key > 登录用户 > 客户端 IP, 越靠前越精确。

    键选择是限流的第一设计题: 用 IP 会误伤 NAT 出口, 不登录的爬虫又必须靠 IP。
    """
    if request.get("api_key"):
        return "key:" + request["api_key"]
    if request.get("user_id"):
        return "user:" + request["user_id"]
    return "ip:" + request["ip"]


class UserLimiter:
    """每键固定窗口计数; 429 时回 Retry-After, 正常时回剩余额度。"""

    def __init__(self, limit=3, window=60):
        self.limit = limit
        self.window = window
        self.counters = {}

    def take(self, request, now):
        key = resolve_key(request)
        bucket = self.counters.setdefault(key, [0, now + self.window])
        if now >= bucket[1]:
            bucket[0], bucket[1] = 0, now + self.window
        bucket[0] += 1
        reset_in = max(1, bucket[1] - now)
        if bucket[0] > self.limit:
            return 429, {"Retry-After": str(reset_in), "X-Limit-Key": key}
        return 200, {"X-RateLimit-Remaining": str(self.limit - bucket[0]),
                     "X-RateLimit-Reset": str(reset_in), "X-Limit-Key": key}


limiter = UserLimiter(limit=3, window=60)
now = 1000
req = {"api_key": "ak-77", "user_id": "u1", "ip": "1.2.3.4"}
for i in range(3):
    status, h = limiter.take(req, now)
    print("第{}次 -> {} Remaining={}".format(i + 1, status, h["X-RateLimit-Remaining"]))
    assert status == 200
status, h = limiter.take(req, now)
print("第4次 -> {} Retry-After={}".format(status, h["Retry-After"]))
assert status == 429

# 同一 NAT 出口下两个不同 API key 互不影响, 证明键隔离
status, _ = limiter.take({"api_key": "ak-88", "ip": "1.2.3.4"}, now)
print("另一把 API key ->", status)
assert status == 200
status, _ = limiter.take({"ip": "9.9.9.9"}, now)
print("无凭证按 IP ->", status)
assert status == 200
print("要点: 键解析链决定限流的粒度与误伤面, 429 必须带 Retry-After, 每键独立桶避免互相牵连")
