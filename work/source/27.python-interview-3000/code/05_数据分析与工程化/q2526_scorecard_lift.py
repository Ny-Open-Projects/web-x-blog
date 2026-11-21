"""评分卡校验: 十分位 lift 曲线与分数漂移的口径修正"""

USERS = []
for i in range(40):
    USERS.append({"id": f"u{i:02d}", "score": 10 + (i * 37) % 90})
USERS.sort(key=lambda u: -u["score"])
for j, u in enumerate(USERS):          # 分数越高流失概率越高, 用排序位造标签
    u["churn"] = j < 14

RAW_THRESHOLD = 60
DRIFT_DELTA = 25                        # 次月全员行为变化, 分数整体抬升


def decile_lift(users, parts=10):
    n = len(users)
    size = n // parts
    base = sum(u["churn"] for u in users) / n
    lifts = []
    for d in range(parts):
        grp = users[d * size:(d + 1) * size]
        rate = sum(u["churn"] for u in grp) / size
        lifts.append(rate / base)
    return base, lifts


if __name__ == "__main__":
    base, lifts = decile_lift(USERS)
    print("十分位 lift(第1组=分数最高): " + ", ".join(f"D{i + 1} {l:.2f}" for i, l in enumerate(lifts)))
    assert lifts[0] > 2 * lifts[-1], "头部组 lift 应显著高于尾部组"
    print(f"整体流失率 {base:.0%}, 头部十分位 lift {lifts[0]:.2f}")
    month1 = [u["score"] for u in USERS]
    month2 = [min(s + DRIFT_DELTA, 100) for s in month1]
    raw1 = sum(1 for s in month1 if s >= RAW_THRESHOLD)
    raw2 = sum(1 for s in month2 if s >= RAW_THRESHOLD)
    print(f"固定阈值 {RAW_THRESHOLD} 分: 本月命中 {raw1} 人, 次月命中 {raw2} 人 -> 行为漂移导致误报膨胀")
    assert raw2 > raw1 * 1.5, "次月原始阈值命中数应显著膨胀"
    k = len(USERS) // 4
    print(f"改为分位数口径(取分数最高 25%): 本月 {k} 人, 次月 {k} 人 -> 名单规模稳定")
    assert k == 10
    print("要点: 阈值用绝对分解读业务含义, 拿名单看相对分位, 二者并行才扛得住分布漂移")
