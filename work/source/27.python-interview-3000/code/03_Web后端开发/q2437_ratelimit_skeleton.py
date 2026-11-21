"""框架无关的限流中间件骨架: 固定窗口与 429 语义(纯标准库)。"""
import time


class FixedWindowLimiter:
    """进程内固定窗口计数器, 生产分布式场景把 buckets 换成 Redis 即可。"""

    def __init__(self, limit, period):
        self.limit, self.period = limit, period
        self.buckets = {}                       # key -> (窗口起点, 已用次数)

    def take(self, key, now):
        cur = int(now // self.period)
        win, count = self.buckets.get(key, (cur, 0))
        if win != cur:
            win, count = cur, 0
        if count >= self.limit:
            retry_after = self.period - (now - win * self.period)
            return False, max(retry_after, 0.0)
        self.buckets[key] = (win, count + 1)
        return True, self.period - (now - win * self.period)


def ratelimit_middleware(app, limiter, get_key, clock=time.time):
    """通用装饰: 拿不到键就不限流; 超限回 429 与 Retry-After。"""
    def handler(environ, start_response):
        key = get_key(environ)
        if key is None:
            return app(environ, start_response)
        ok, retry_after = limiter.take(key, clock())
        if ok:
            return app(environ, start_response)
        start_response("429 Too Many Requests",
                       [("Content-Type", "application/json"),
                        ("Retry-After", str(int(retry_after) + 1))])
        return [b'{"error": "rate_limited"}']
    return handler


def dummy_app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [b"ok"]


def key_by_api(environ):
    return environ.get("HTTP_X_API_KEY")


limiter = FixedWindowLimiter(limit=3, period=60)
app = ratelimit_middleware(dummy_app, limiter, key_by_api, clock=lambda: 1000.0)

for i in range(1, 6):
    captured = {}
    environ = {"HTTP_X_API_KEY": "client-a"}

    def start_response(status, headers, _cap=captured):
        _cap["status"], _cap["headers"] = status, dict(headers)
    body = b"".join(app(environ, start_response))
    extra = captured["headers"].get("Retry-After", "-")
    print("client-a 第 {} 次 -> {} body={} Retry-After={}".format(
        i, captured["status"], body.decode(), extra))

captured = {}


def start_response_b(status, headers):
    captured["status"] = status
environ = {"HTTP_X_API_KEY": "client-b"}
body = b"".join(app(environ, start_response_b))
print("client-b 第 1 次 -> {} body={}".format(captured["status"], body.decode()))
assert captured["status"] == "200 OK"
print("要点: 限流中间件只关心 取键 计数 回 429 三件事, "
      "Retry-After 告诉客户端何时再试, 不同键互相隔离")
