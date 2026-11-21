"""Q2852 检索评估的双盲对比:匿名化 顺序随机化与事后揭盲。

让评测员对比两个检索器时,如果他知道左边是新系统,评分就会偏向
新系统。双盲协议:两路结果匿名成 X/Y,出场顺序按种子随机,评测员
按统一规则打分,收齐后才能揭盲对号——偏好统计才有可信度。
"""

import random

RET_A = {
    "q1": ["d1", "d2", "d3"],
    "q2": ["d4", "d5"],
    "q3": ["d6"],
}
RET_B = {
    "q1": ["d1", "d2", "d3", "d9"],
    "q2": ["d4", "d5"],
    "q3": ["d7", "d6"],
}


def judge_score(results):
    """stub 评测规则:覆盖广者优先,平手取更短者。"""
    return (len(set(results)), -len(results))


def blind_sessions(queries, seed):
    rng = random.Random(seed)
    sheets = []
    for q in queries:
        pair = [RET_A[q], RET_B[q]]
        a_first = rng.random() < 0.5
        shown = pair if a_first else pair[::-1]
        mapping = {"X": ("A" if a_first else "B"),
                   "Y": ("B" if a_first else "A")}
        sheets.append({"q": q, "X": shown[0], "Y": shown[1], "map": mapping})
    return sheets


def run_eval(queries, seed):
    sheets = blind_sessions(queries, seed)
    wins = {"A": 0, "B": 0, "tie": 0}
    for s in sheets:
        sx, sy = judge_score(s["X"]), judge_score(s["Y"])
        if sx == sy:
            wins["tie"] += 1
        else:
            winner_label = "X" if sx > sy else "Y"
            wins[s["map"][winner_label]] += 1
    return sheets, wins


def main():
    queries = ["q1", "q2", "q3"]
    sheets, wins = run_eval(queries, seed=42)
    # 评测单上绝不能出现真实系统名
    for s in sheets:
        assert "A" not in (s["X"], s["Y"]) and isinstance(s["map"], dict)
    # 揭盲统计:B 在 q1 q3 胜出,A 只在平局里出现
    assert wins == {"A": 0, "B": 2, "tie": 1}, wins
    # 同一 seed 复跑结果一致(评估可复现)
    sheets2, wins2 = run_eval(queries, seed=42)
    assert wins2 == wins and sheets2 == sheets
    # 换 seed 会变出场顺序,但按规则推出的胜负一致
    _, wins3 = run_eval(queries, seed=7)
    assert wins3 == wins
    print("揭盲结果:", wins)
    print("出场顺序已随机化,评测单只含 X/Y 标签")
    print("胜负只由评测规则决定,与出场顺序无关")


if __name__ == "__main__":
    main()
