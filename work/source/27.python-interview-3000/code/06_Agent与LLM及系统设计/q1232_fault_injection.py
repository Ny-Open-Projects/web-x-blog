"""故障注入框架:错误/延迟/分区三类注入 + 比例控制 + 一键熔停 + 注入打标。"""
import random, time


class FaultInjector:
    def __init__(self, seed=1):
        self.rules, self.enabled = [], True
        random.seed(seed)

    def add_rule(self, service, kind, prob, arg=None):
        self.rules.append({"service": service, "kind": kind, "prob": prob, "arg": arg})

    def kill_all(self):
        self.enabled = False

    def wrap(self, service, fn):
        def call(*a, **kw):
            if not self.enabled:
                return fn(*a, **kw), {}
            for r in self.rules:
                if r["service"] == service and random.random() < r["prob"]:
                    if r["kind"] == "error":
                        return None, {"fault": "error", "detail": r["arg"]}
                    if r["kind"] == "latency":
                        time.sleep(r["arg"] * 0.01)     # 演示缩小 100 倍
                        out = fn(*a, **kw)
                        return out, {"fault": "latency"}
                    if r["kind"] == "partition":
                        raise ConnectionError("partition injected")
            return fn(*a, **kw), {}
        return call


class Downstream:
    @staticmethod
    def query():
        return {"data": "ok"}


if __name__ == "__main__":
    inj = FaultInjector()
    inj.add_rule("order-db", "error", prob=0.4, arg="synthetic 500")
    inj.add_rule("order-db", "latency", prob=0.2, arg=8)
    call = inj.wrap("order-db", Downstream.query)

    faults = {"error": 0, "latency": 0, "clean": 0}
    for _ in range(20):
        out, meta = call()
        faults[meta.get("fault", "clean")] += 1
        if meta.get("fault") == "error":
            assert out is None
    print("注入统计:", faults)
    assert faults["clean"] + faults["error"] + faults["latency"] == 20
    assert faults["error"] >= 1, "错误注入生效"

    # 分区注入抛异常,上层熔断捕获
    inj.add_rule("inventory", "partition", prob=1.0)
    p_call = inj.wrap("inventory", Downstream.query)
    try:
        p_call()
    except ConnectionError as e:
        print("分区注入:", e)

    inj.kill_all()
    out, meta = call()
    print("熔停演练后恢复:", out, meta)
    assert meta == {}, "熔停后不再注入"
