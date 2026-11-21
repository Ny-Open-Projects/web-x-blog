"""端到端演示的确定性:注入随机种子 假时钟 固定桩数据,两次运行指纹一致。"""
import random, hashlib


class FakeClock:
    def __init__(self, start=0.0, step=0.5):
        self.now = start
        self.step = step

    def __call__(self):
        self.now += self.step
        return self.now


class DemoPipeline:
    def __init__(self, seed, clock):
        self.rng = random.Random(seed)
        self.clock = clock

    def run(self, query):
        picks = [self.rng.choice(["a", "b", "c"]) for _ in range(3)]
        ts = self.clock()
        body = "%s|%s|%.2f" % (query, ",".join(picks), ts)
        return {"picks": picks, "ts": round(ts, 2),
                "fingerprint": hashlib.sha256(body.encode("utf-8")).hexdigest()[:12]}


if __name__ == "__main__":
    r1 = DemoPipeline(seed=42, clock=FakeClock()).run("退货政策")
    r2 = DemoPipeline(seed=42, clock=FakeClock()).run("退货政策")
    assert r1 == r2, "同种子同输入两次运行完全一致"
    assert r1["ts"] == 0.5 and r1["ts"] == r2["ts"], "假时钟推进确定"
    random.seed(1)
    random.choice(["x", "y", "z"])
    r3 = DemoPipeline(seed=42, clock=FakeClock()).run("退货政策")
    assert r3 == r1, "管道只用自带 Random 实例 全局随机被污染也不影响"
    picks_set = {DemoPipeline(seed=s, clock=FakeClock()).run("x")["picks"][0] for s in range(20)}
    assert len(picks_set) > 1, "不同种子应产生不同序列"
    print("确定性演示通过:种子注入 假时钟 全局随机隔离 指纹可复现")
