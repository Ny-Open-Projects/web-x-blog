"""影子流量:打标透传 + 写隔离到影子存储 + 外呼拦截 + 护栏自动停止。"""


class ShadowContext:
    def __init__(self, shadow=False):
        self.shadow = shadow

    def headers(self):
        return {"x-shadow": "1"} if self.shadow else {}


class Storage:
    def __init__(self):
        self.prod, self.shadow_rows = [], []

    def write(self, row, ctx):
        if ctx.shadow:
            self.shadow_rows.append({**row, "shadow": True})
            return "shadow_write"
        self.prod.append(row)
        return "prod_write"


class SMSClient:
    def __init__(self):
        self.sent, self.blocked = [], 0

    def send(self, phone, text, ctx):
        if ctx.shadow:
            self.blocked += 1
            return "blocked_double_guard"      # 框架层拦截
        self.sent.append((phone, text))
        return "sent"


def business_write(storage, sms, ctx, order):
    storage.write({"order": order}, ctx)
    assert ctx.headers().get("x-shadow") == "1" or not ctx.shadow, "标记必须透传"
    sms.send("13800001111", f"订单 {order} 已创建", ctx)
    return "ok"


class LoadTest:
    def __init__(self, guard):
        self.guard, self.stopped = guard, False

    def fire(self, n, sampler):
        for i in range(n):
            if self.stopped:
                break
            m = sampler()
            if m["p95_ms"] > 800 or m["err_rate"] > 0.05:   # 护栏越界
                self.stopped = True
        return not self.stopped


if __name__ == "__main__":
    storage, sms = Storage(), SMSClient()
    prod_ctx, shadow_ctx = ShadowContext(False), ShadowContext(True)
    business_write(storage, sms, prod_ctx, "o1")
    business_write(storage, sms, shadow_ctx, "o1-shadow")
    print("生产写:", storage.prod, "影子写:", storage.shadow_rows)
    assert storage.prod and not storage.shadow_rows in ([], None) and storage.shadow_rows[0]["shadow"]
    assert len(sms.sent) == 1 and sms.blocked == 1, "影子请求外呼被双重拦截"

    lt = LoadTest(guard=True)
    ok = lt.fire(100, lambda: {"p95_ms": 120, "err_rate": 0.001})
    print("压测护栏: 正常指标放行 =", ok)
    assert ok
    ok2 = lt.fire(100, lambda: {"p95_ms": 900, "err_rate": 0.001})
    print("指标越界自动停止 =", not ok2)
    assert not ok2
    print("影子隔离与护栏熔停机制验证通过")
