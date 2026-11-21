"""TTFT 劣化归因:首 token 时延拆成排队段与上游段,p95 劣化定位到具体段。"""


def p95(xs):
    if not xs:
        return 0.0
    xs = sorted(xs)
    return xs[max(0, min(len(xs) - 1, int(round(0.95 * len(xs))) - 1))]


def attribute(samples):
    """samples: [{ttft, queue, upstream}] 返回分段 p95 与劣化主导段。"""
    seg = {}
    for k in ("queue", "upstream"):
        seg[k] = round(p95([s[k] for s in samples]), 1)
    base_upstream = round(p95([s["upstream"] for s in samples if not s.get("anomaly")]), 1)
    if seg["queue"] >= base_upstream * 1.5:
        dominant = "queue"
    elif seg["upstream"] >= base_upstream * 1.5:
        dominant = "upstream"
    else:
        dominant = "none"
    for s in samples:
        assert abs(s["queue"] + s["upstream"] - s["ttft"]) < 0.01, "分段必须能拼回总时延"
    return {"queue_p95": seg["queue"], "upstream_p95": seg["upstream"],
            "baseline_upstream_p95": base_upstream, "dominant": dominant}


if __name__ == "__main__":
    # 基线:上游稳定 200ms,排队 20ms
    normal = [{"ttft": 220, "queue": 20, "upstream": 200}] * 20

    # 场景一:10% 样本撞上限流,排队飙到 900ms,上游不变
    queued = normal[:]
    for _ in range(2):
        queued.append({"ttft": 1100, "queue": 900, "upstream": 200})
    a1 = attribute(queued)
    assert a1["dominant"] == "queue", a1
    assert a1["queue_p95"] == 900 and a1["upstream_p95"] == 200

    # 场景二:上游供应商变慢,排队正常
    slow = normal[:10] + [{"ttft": 1200, "queue": 20, "upstream": 1180, "anomaly": True}
                          for _ in range(12)]
    a2 = attribute(slow)
    assert a2["dominant"] == "upstream", a2
    assert a2["upstream_p95"] > a2["baseline_upstream_p95"] * 1.5

    # 场景三:都正常
    a3 = attribute(normal)
    assert a3["dominant"] == "none"
    print("归因通过:排队型劣化指认 queue,上游型指认 upstream,分段可拼回总时延")
