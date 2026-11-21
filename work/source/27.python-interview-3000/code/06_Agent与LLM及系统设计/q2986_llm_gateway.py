"""Q2986 LLM 网关的完整路由:健康检查+限流+降级+请求日志。

网关是所有模型调用的唯一出口,职责四件套:按优先级维护供应商
列表;每个供应商有熔断健康状态(连续失败达阈值就熔断,冷却后
半开放行探测);令牌桶限流防突发把配额打穿;每次路由写结构化
日志,包含最终落在哪一家、是否降级,出问题才有得查。
"""

import time


class TokenBucket:
    """令牌桶:注入时钟,容量 capacity,每秒补充 rate。"""

    def __init__(self, capacity, rate, clock=time.time):
        self.capacity = capacity
        self.rate = rate
        self.tokens = float(capacity)
        self.clock = clock
        self.last = clock()

    def allow(self, cost=1.0):
        now = self.clock()
        self.tokens = min(self.capacity,
                          self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False


class Provider:
    def __init__(self, name, priority, fail_threshold=2, cooldown=10):
        self.name = name
        self.priority = priority
        self.fail_threshold = fail_threshold
        self.cooldown = cooldown
        self.fail_streak = 0
        self.open_until = 0.0          # 熔断截止时刻

    def available(self, now):
        return now >= self.open_until

    def record(self, ok, now):
        if ok:
            self.fail_streak = 0
        else:
            self.fail_streak += 1
            if self.fail_streak >= self.fail_threshold:
                self.open_until = now + self.cooldown   # 熔断


class Gateway:
    def __init__(self, providers, bucket, clock):
        self.providers = sorted(providers, key=lambda p: p.priority)
        self.bucket = bucket
        self.clock = clock
        self.logs = []

    def route(self, call):
        """call: fn(name)->text,失败抛异常。返回 (text, provider)。"""
        now = self.clock()
        if not self.bucket.allow():
            self.logs.append({"event": "rate_limited", "ts": now})
            raise RuntimeError("rate_limited")
        for p in self.providers:
            if not p.available(now):
                self.logs.append({"event": "skip_circuit_open",
                                  "provider": p.name})
                continue
            try:
                text = call(p.name)
            except Exception:
                p.record(False, now)
                self.logs.append({"event": "failover_from",
                                  "provider": p.name})
                continue
            p.record(True, now)
            self.logs.append({"event": "served", "provider": p.name})
            return text, p.name
        raise RuntimeError("all_providers_down")


def main():
    now = [1000.0]
    clock = lambda: now[0]
    bucket = TokenBucket(capacity=10, rate=5.0, clock=clock)
    calls = {"counter": 0}

    def call(name):
        if name == "primary":
            calls["counter"] += 1
            raise ConnectionError("primary down")
        return "回答来自 " + name

    gw = Gateway([Provider("primary", 1), Provider("backup", 2)], bucket,
                 clock)
    text, used = gw.route(call)
    assert used == "backup" and text == "回答来自 backup", (text, used)

    # 熔断:首调已让 primary 带一次失败,再来一次即连续两次熔断
    calls["counter"] = 0
    now[0] += 1
    gw.route(call)                           # primary 失败,熔断开闸
    assert gw.providers[0].open_until == 1011.0, gw.providers[0].open_until
    now[0] += 1
    gw.route(call)                           # 冷却期内 primary 被跳过
    assert calls["counter"] == 1, calls["counter"]   # 熔断前只再试了一次

    # 限流:清空令牌后拒绝而不是排队堵死
    now[0] = 2000.0
    bucket.tokens = 0.0
    bucket.last = now[0]
    gw3 = Gateway([Provider("a", 1)], bucket, clock)
    try:
        gw3.route(lambda n: "ok")
        raise AssertionError("应当被限流")
    except RuntimeError as exc:
        assert "rate_limited" in str(exc)

    events = [l["event"] for l in gw.logs]
    assert "served" in events and "failover_from" in events, gw.logs
    assert "rate_limited" in [l["event"] for l in gw3.logs]
    print("降级命中:", used)
    print("日志事件:", events[:5])


if __name__ == "__main__":
    main()
