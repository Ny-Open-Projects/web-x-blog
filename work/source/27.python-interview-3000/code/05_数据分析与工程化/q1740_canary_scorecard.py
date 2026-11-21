"""灰度放量评分卡:多指标加权打分,红线一票否决,总分不足同样拦下"""

BASELINE = {"error_rate": 0.004, "p99_ms": 320, "cvr": 0.052}
CANARY = {"error_rate": 0.006, "p99_ms": 410, "cvr": 0.049}
RULES = [
    # 指标, 方向, 劣化红线(相对), 权重
    ("error_rate", "lower", 0.50, 0.4),
    ("p99_ms", "lower", 0.25, 0.3),
    ("cvr", "higher", 0.10, 0.3),
]
PASS_SCORE = 0.8


def score_metric(b, c, good_when, redline):
    rel = (c - b) / b
    bad = max(rel, 0.0) if good_when == "lower" else max(-rel, 0.0)
    return max(0.0, 1.0 - bad / redline), rel


def decision(baseline, canary, rules, pass_score):
    total, veto, detail = 0.0, False, []
    for name, good, redline, w in rules:
        s, rel = score_metric(baseline[name], canary[name], good, redline)
        total += s * w
        detail.append(f"{name}: 变化 {rel:+.1%} 得分 {s:.2f} 权重 {w}")
        if s == 0.0:
            veto = True
    verdict = "HOLD" if veto or total < pass_score else "PROMOTE"
    return verdict, total, detail


if __name__ == "__main__":
    verdict, total, detail = decision(BASELINE, CANARY, RULES, PASS_SCORE)
    for d in detail:
        print(" ", d)
    print(f"总分 {total:.2f},门槛 {PASS_SCORE} -> {verdict}")
    print("要点:评分卡让放量决策可解释可审计;红线指标一票否决,总分不足也 HOLD;阈值权重由稳定性评审定,发布当天不许现场改")
