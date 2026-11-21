"""样本不平衡演示:99:1 下全预测多数类准确率 99% 但召回 0,重采样与评估纪律"""

from collections import Counter
import random

# (编号, 标签) 标签 1 为少数类
DATA = [(i, 1 if i % 100 == 0 else 0) for i in range(1, 1001)]  # 10 正 990 负


def always_majority(data):
    """退化基线:全预测多数类,用混淆矩阵看穿准确率假象"""
    tp = fp = fn = tn = 0
    for _, y in data:
        if y == 1:
            fn += 1
        else:
            tn += 1
    acc = (tp + tn) / len(data)
    recall = tp / (tp + fn) if tp + fn else 0.0
    return acc, recall, (tp, fp, fn, tn)


def undersample(data, seed=7):
    """欠采样多数类到 1:9,重复实验要固定种子"""
    rng = random.Random(seed)
    pos = [d for d in data if d[1] == 1]
    neg = [d for d in data if d[1] == 0]
    return pos + rng.sample(neg, len(pos) * 9)


if __name__ == "__main__":
    acc, recall, cm = always_majority(DATA)
    print(f"原始分布: {dict(Counter(y for _, y in DATA))}")
    print(f"全预测多数类: 准确率 {acc:.1%} 但少数类召回 {recall:.0%} 混淆矩阵(TP,FP,FN,TN)={cm}")
    print(f"欠采样后分布: {dict(Counter(y for _, y in undersample(DATA)))}")
    print("要点:不平衡场景看召回与 PR 不看准确率;处理=重采样/类别权重/下调判定阈值;训练集可重采样,评估集必须保持原始分布")
