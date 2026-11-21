"""分群迁移矩阵:昨日分群 x 今日分群,输出漂移率并报警"""

PREV = {"u1": "high", "u2": "high", "u3": "high", "u4": "high",
        "u5": "mid", "u6": "mid", "u7": "mid", "u8": "mid",
        "u9": "low", "u10": "low", "u11": "low", "u12": "low"}
CURR = {"u1": "high", "u2": "high", "u3": "high", "u4": "high",
        "u5": "mid", "u6": "mid", "u7": "mid", "u8": "low",
        "u9": "low", "u10": "low", "u11": "low", "u12": "low"}
LABELS = ["high", "mid", "low"]
DRIFT_ALARM = 0.20  # 单群漂移超过 20% 触发报警


def migration_matrix(prev, curr, labels):
    matrix = {a: {b: 0 for b in labels} for a in labels}
    missing = 0
    for uid, a in prev.items():
        b = curr.get(uid)
        if b in matrix:
            matrix[a][b] += 1
        else:
            missing += 1
    return matrix, missing


def drift_rates(matrix):
    rates = {}
    for a, row in matrix.items():
        total = sum(row.values())
        moved = total - row[a]
        rates[a] = moved / total if total else 0.0
    return rates


if __name__ == "__main__":
    matrix, missing = migration_matrix(PREV, CURR, LABELS)
    print("迁移矩阵 行=昨日 列=今日:")
    print("      " + "  ".join(f"{b:>5}" for b in LABELS))
    for a in LABELS:
        print(f"{a:>5} " + "  ".join(f"{matrix[a][b]:>5}" for b in LABELS))
    if missing:
        print("昨日存在但今日找不到的用户:", missing, "需排查数据缺失")

    rates = drift_rates(matrix)
    for a, r in rates.items():
        flag = " <-- 超阈值,排查规则或数据源" if r > DRIFT_ALARM else ""
        print(f"{a} 群漂移率 {r:.1%}{flag}")
