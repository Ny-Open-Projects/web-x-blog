"""混沌实验框架:稳态假设 + 最小爆炸半径 + 指标守卫自动回滚 + 实验报告。"""
import random


class SteadyState:
    def __init__(self, success_rate_min, p95_max_ms):
        self.sr_min, self.p95_max = success_rate_min, p95_max_ms

    def verify(self, metrics):
        return (metrics["success_rate"] >= self.sr_min and
                metrics["p95_ms"] <= self.p95_max), metrics


class ChaosExperiment:
    def __init__(self, steady, abort_on_breach=True):
        self.steady, self.abort = steady, abort_on_breach
        self.events = []

    def run(self, injector, baseline_ok=True, steps=20):
        random.seed(9)
        for i in range(steps):
            if i == 5:
                self.events.append("inject: db latency 200ms")
                injector["fault"] = True
            metrics = self._sample(injector, baseline_ok)
            ok, m = self.steady.verify(metrics)
            self.events.append(f"step{i}: sr={m['success_rate']:.0%} p95={m['p95_ms']}ms pass={ok}")
            if not ok and self.abort:
                self.events.append("ABORT: 指标越界自动回滚注入")
                injector["fault"] = False
                break
        return self.events

    @staticmethod
    def _sample(injector, baseline_ok):
        if injector.get("fault") and baseline_ok:
            return {"success_rate": 0.985, "p95_ms": 520}   # 降级生效但仍越界 -> 暴露缺陷
        return {"success_rate": 0.999, "p95_ms": 120}


if __name__ == "__main__":
    exp = ChaosExperiment(SteadyState(0.995, 300))
    events = exp.run(injector={})
    for e in events:
        print(" ", e)
    assert any("inject" in e for e in events), "注入已执行"
    assert any("ABORT" in e for e in events), "稳态被打破必须自动回滚"
    assert events[-1].startswith("ABORT")
    print("实验结论: 注入 DB 延迟后 P95 越界 -> 发现降级预案缺口,记缺陷修复后重演")
