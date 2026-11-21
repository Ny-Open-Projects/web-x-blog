"""阈值扫描: 分类分数的操作点选择与 F1 最优阈值"""

# 确定性的打分样本: 8 正 12 负, 分数有重叠制造权衡
SAMPLES = [
    (0.92, 1), (0.88, 1), (0.83, 1), (0.79, 0), (0.74, 1), (0.71, 1),
    (0.66, 0), (0.62, 1), (0.58, 1), (0.55, 0), (0.52, 0), (0.49, 1),
    (0.45, 0), (0.41, 0), (0.38, 0), (0.34, 0), (0.30, 0), (0.26, 0),
    (0.21, 0), (0.15, 0),
]


def evaluate(samples, thr):
    tp = sum(1 for s, y in samples if s >= thr and y == 1)
    fp = sum(1 for s, y in samples if s >= thr and y == 0)
    fn = sum(1 for s, y in samples if s < thr and y == 1)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return precision, recall, f1


if __name__ == "__main__":
    rows = []
    for i in range(1, 20):
        thr = i * 0.05
        p, r, f1 = evaluate(SAMPLES, thr)
        rows.append((thr, p, r, f1))
    print(" thr   precision  recall   f1")
    for thr, p, r, f1 in rows[::2]:
        print(f" {thr:.2f}   {p:.3f}      {r:.3f}    {f1:.3f}")
    best = max(rows, key=lambda x: x[3])
    at_half = next(row for row in rows if abs(row[0] - 0.5) < 1e-9)
    print(f"F1 最优阈值 {best[0]:.2f}: precision {best[1]:.3f}, recall {best[2]:.3f}, F1 {best[3]:.3f}")
    print(f"默认阈值 0.50: precision {at_half[1]:.3f}, recall {at_half[2]:.3f}, F1 {at_half[3]:.3f}")
    assert best[3] >= at_half[3], "扫描出的最优 F1 不应低于默认阈值"
    assert best[1] >= at_half[1] and best[2] <= at_half[2] + 1e-9, "高阈值应换取精度让出召回"
    # 单调性检查: 阈值升高, 召回不增, 精度不必然但本例应大体上升
    recalls = [r for _, _, r, _ in rows]
    assert all(a >= b - 1e-9 for a, b in zip(recalls, recalls[1:])), "召回应随阈值单调不增"
    print("要点: 阈值是业务参数不是模型参数, 风控取高精度, 营销取高召回, 用扫描表谈判")
