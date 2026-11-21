"""幂等键中间件: 重放回缓存响应, 并发重复回 409(纯标准库)。"""


class IdempotencyStore:
    def __init__(self):
        self.done = {}                           # key -> (status, body)
        self.inflight = set()


def idempotency_middleware(app, store, get_key):
    def handler(environ, start_response):
        key = get_key(environ)
        if key is None:                          # 没带幂等键则不去重
            return app(environ, start_response)
        if key in store.done:
            status, body = store.done[key]
            start_response(status, [("Idempotency-Replayed", "true"),
                                    ("Content-Type", "text/plain")])
            return [body]
        if key in store.inflight:
            start_response("409 Conflict", [("Content-Type", "text/plain")])
            return [b"duplicate in-flight request"]
        store.inflight.add(key)
        try:
            captured = {}

            def sr(status, headers):
                captured["status"] = status
                start_response(status, headers)
            body_parts = app(environ, sr)
            body = b"".join(body_parts)
            store.done[key] = (captured["status"], body)
            return [body]
        finally:
            store.inflight.discard(key)
    return handler


def payment_app(environ, start_response):
    payment_app.calls += 1
    start_response("201 Created", [("Content-Type", "text/plain")])
    return ["payment-{}".format(payment_app.calls).encode()]


payment_app.calls = 0
store = IdempotencyStore()


def get_key(environ):
    return environ.get("HTTP_IDEMPOTENCY_KEY")


app = idempotency_middleware(payment_app, store, get_key)


def post(key):
    captured = {}
    environ = {"HTTP_IDEMPOTENCY_KEY": key} if key else {}

    def sr(status, headers):
        captured["status"] = status
        captured["headers"] = dict(headers)
    body = b"".join(app(environ, sr))
    return captured["status"], body, captured["headers"]


s1, b1, h1 = post("order-77")
print("首次提交  key=order-77 -> {} {} calls={}".format(s1, b1.decode(), payment_app.calls))
s2, b2, h2 = post("order-77")
print("网络重试  key=order-77 -> {} {} calls={} replay={}".format(
    s2, b2.decode(), payment_app.calls, h2.get("Idempotency-Replayed")))
s3, b3, h3 = post("order-78")
print("新键提交  key=order-78 -> {} {} calls={}".format(s3, b3.decode(), payment_app.calls))

store.inflight.add("order-79")
s4, b4, h4 = post("order-79")
print("并发重复  key=order-79 -> {} {}".format(s4, b4.decode()))
assert s1 == s3 == "201 Created"
assert s2 == "201 Created" and b2 == b1 and payment_app.calls == 2
assert h2.get("Idempotency-Replayed") == "true"
assert s4 == "409 Conflict"
print("要点: 幂等键中间件三分支 已完成回缓存 在途回 409 未完成才执行; "
      "finally 里清在途标记是防卡死的关键")
