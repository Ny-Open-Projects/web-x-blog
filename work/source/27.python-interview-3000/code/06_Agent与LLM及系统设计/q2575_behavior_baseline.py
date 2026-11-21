"""Q2575 Agent 行为的回归基线:统计画像与偏差评分。

金样本指纹只能抓可复现场景;统计画像基线记录步数分布与工具调用
频次的均值方差,新版本跑一批种子,任一指标偏离超阈值就告警,
能抓住"没坏但行为漂移"的隐性回归。
"""
import random
import statistics


def run_agent(seed):
    rng = random.Random(seed)
    steps = rng.randint(6, 9)
    tools = {}
    for _ in range(steps):
        t = rng.choice(["search", "calc", "sum"])
        tools[t] = tools.get(t, 0) + 1
    return {"steps": steps, "tools": tools}


def build_baseline(seeds):
    runs = [run_agent(s) for s in seeds]
    steps = [r["steps"] for r in runs]
    tool_total = {}
    for r in runs:
        for t, c in r["tools"].items():
            tool_total[t] = tool_total.get(t, 0) + c
    n = len(runs)
    return {"steps_mean": statistics.mean(steps),
            "steps_std": max(statistics.pstdev(steps), 1.0),
            "tool_mean": {t: c / n for t, c in tool_total.items()}}


def deviation(profile, run):
    worst = abs(run["steps"] - profile["steps_mean"]) / profile["steps_std"]
    for t, m in profile["tool_mean"].items():
        worst = max(worst, abs(run["tools"].get(t, 0) - m) / max(m, 1.0))
    return worst


def main():
    profile = build_baseline([1, 2, 3, 4, 5])
    normal = run_agent(6)
    weird = {"steps": 30, "tools": {"search": 30}}
    d1, d2 = deviation(profile, normal), deviation(profile, weird)
    assert d1 < 2.0, d1
    assert d2 > 2.0, d2
    print("基线:步数均值", round(profile["steps_mean"], 2),
          "标准差", round(profile["steps_std"], 2))
    print("正常新样本偏差:", round(d1, 2), "通过")
    print("异常新样本偏差:", round(d2, 2), "触发回归告警")


if __name__ == "__main__":
    main()
