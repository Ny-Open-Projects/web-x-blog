"""AB 实验护栏:SRM 校验、样本污染检测与护栏指标突变"""

import math
from statistics import NormalDist


def srm_check(observed, expected_ratio, z=1.96):
    """样本比完整性校验:实际分桶比偏离配置比过大说明分流有 bug"""
    total = sum(observed.values())
    ratios = list(expected_ratio.values())
    base = sum(ratios)
    worst = None
    for name, n in observed.items():
        expect = total * ratios[list(observed).index(name)] / base
        sigma = math.sqrt(total * (expect / total) * (1 - expect / total))
        zz = (n - expect) / sigma if sigma else 0.0
        if worst is None or abs(zz) > abs(worst[1]):
            worst = (name, zz)
    name, zz = worst
    return {"worst_bucket": name, "z": round(zz, 2),
            "srm_violated": abs(zz) > z}


def pollution_check(assignments):
    """同一用户出现在多个实验组,分流服务粘性失效的典型信号"""
    seen = {}
    polluted = set()
    for user, group in assignments:
        if user in seen and seen[user] != group:
            polluted.add(user)
        seen[user] = group
    return polluted


GUARD_BASELINE = {"p99_latency_ms": 200, "error_rate": 0.01}


def guardrail_check(current):
    alerts = []
    if current["p99_latency_ms"] > GUARD_BASELINE["p99_latency_ms"] * 1.1:
        alerts.append("p99 延迟涨幅超 10%")
    if current["error_rate"] > GUARD_BASELINE["error_rate"] * 1.5:
        alerts.append("错误率涨幅超 50%")
    return alerts


if __name__ == "__main__":
    print("SRM:", srm_check({"control": 5210, "treatment": 4790},
                            {"control": 1, "treatment": 1}))
    polluted = pollution_check([("u1", "control"), ("u1", "treatment"), ("u2", "treatment")])
    print("污染用户:", polluted or "无")
    print("护栏:", guardrail_check({"p99_latency_ms": 260, "error_rate": 0.008}) or "全部正常")
    print("三条护栏任一失败都应先停实验再分析业务指标")
