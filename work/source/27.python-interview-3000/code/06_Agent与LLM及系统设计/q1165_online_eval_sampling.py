"""在线评估埋点:全量轻指标 + 按率抽样全文 + 负反馈必采,聚合质量大盘。"""
import json, random, statistics


class Telemetry:
    def __init__(self, sample_rate=0.2, seed=1):
        self.events, self.sample_rate = [], sample_rate
        random.seed(seed)

    def log(self, *, user_feedback=None, **fields):
        keep = user_feedback == "bad" or random.random() < self.sample_rate
        if not keep:
            self.events.append({"sampled": False, "latency": fields.get("latency")})
            return
        ev = {"sampled": True, **fields, "feedback": user_feedback}
        self.events.append(ev)

    def dashboard(self):
        full = [e for e in self.events if e["sampled"]]
        lat = [e["latency"] for e in self.events if e.get("latency")]
        lat.sort()
        p95 = lat[int(len(lat) * 0.95) - 1] if lat else 0
        bad = sum(1 for e in full if e.get("feedback") == "bad")
        return {"requests": len(self.events), "sampled_full": len(full),
                "p95_latency": p95, "bad_rate": bad / len(full) if full else 0}


if __name__ == "__main__":
    random.seed(7)
    tel = Telemetry(sample_rate=0.25)
    for i in range(100):
        fb = "bad" if i in {12, 40, 77} else ("good" if i % 17 == 0 else None)
        tel.log(request_id=i, model="v1", latency=200 + (i % 50) * 10,
                tokens=500, user_feedback=fb)
    d = tel.dashboard()
    print(json.dumps(d, ensure_ascii=False, indent=1))
    assert d["requests"] == 100
    assert any(e.get("feedback") == "bad" for e in tel.events), "负反馈必须全量保留"
    assert 0 < d["sampled_full"] < 100, "其余按率抽样,成本可控"
    print(f"全量 {d['requests']} 条,落全文 {d['sampled_full']} 条,P95={d['p95_latency']}ms")
