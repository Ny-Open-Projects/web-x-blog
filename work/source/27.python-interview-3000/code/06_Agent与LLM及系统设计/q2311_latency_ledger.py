"""检索链路分段计时:召回 重排 生成各段记账,超标定位到段,预算超支传导。"""


class LatencyLedger:
    def __init__(self, budget_ms=100.0):
        self.budget = budget_ms
        self.spans = {}

    def record(self, stage, ms):
        self.spans[stage] = self.spans.get(stage, 0.0) + ms

    def total(self):
        return round(sum(self.spans.values()), 2)

    def report(self):
        total = self.total()
        worst = max(self.spans.items(), key=lambda kv: kv[1])[0] if self.spans else None
        return {"total": total, "budget": self.budget, "over": total > self.budget,
                "bottleneck": worst,
                "share": {k: round(v / total, 2) for k, v in self.spans.items()} if total else {}}


if __name__ == "__main__":
    led = LatencyLedger(budget_ms=100.0)
    led.record("recall", 30.0)
    led.record("rerank", 20.0)
    led.record("generate", 60.0)
    rep = led.report()
    assert rep["total"] == 110.0 and rep["over"]
    assert rep["bottleneck"] == "generate" and rep["share"]["generate"] == 0.55
    led.record("generate", 5.0)
    assert led.spans["generate"] == 65.0, "同段多次记账累加"
    ok = LatencyLedger(budget_ms=100.0)
    ok.record("recall", 25.0)
    ok.record("rerank", 15.0)
    ok.record("generate", 45.0)
    rep2 = ok.report()
    assert not rep2["over"] and rep2["share"]["recall"] == 0.29
    print("延迟分段通过:三段记账 超标定位瓶颈 份额归一")
