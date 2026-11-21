---
title: [Q2792] 混淆矩阵全套指标:从 TP FP FN TN 到 MCC
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2792 · 混淆矩阵全套指标:从 TP FP FN TN 到 MCC

> 难度:★★☆☆ | 标签:评估指标, 混淆矩阵

**问**:面试官:模型准确率 99.7%,这个模型能上线吗?

**答**:先看混淆矩阵再说。稀疏正例场景 TP40 FP10 FN20 TN9930:准确率 99.7% 光鲜,但召回只有 66.7%——三分之一的正例漏掉;精确率 80%,F1 0.727,MCC 0.729 才反映综合判别力。把同样的错分结构放到平衡样本 TP40 FP10 FN20 TN70 上,准确率立刻掉到 78.6%——准确率被类别分布支配,正例越稀疏越像"全猜负例"刷出来的假象。全套指标各自回答一个问题:精确率管误报、召回管漏报、特异度与 FPR 管负例侧、F1 是精确率与召回的调和平均(天然偏向较小一方)、MCC 同时压四个格子且随机猜测期望为 0。不平衡数据先看召回与 MCC,准确率只做参考。

```python
# file: code/05_数据分析与工程化/q2792_confusion_full.py
"""混淆矩阵全套指标: 从 TP FP FN TN 到 MCC"""


def safe_div(a, b):
    return a / b if b else 0.0


def confusion_metrics(tp, fp, fn, tn):
    acc = safe_div(tp + tn, tp + fp + fn + tn)
    precision = safe_div(tp, tp + fp)
    recall = safe_div(tp, tp + fn)
    specificity = safe_div(tn, tn + fp)
    fpr = 1 - specificity
    f1 = safe_div(2 * precision * recall, precision + recall)
    mcc_den = ((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)) ** 0.5
    mcc = safe_div(tp * tn - fp * fn, mcc_den)
    return {"acc": acc, "precision": precision, "recall": recall,
            "specificity": specificity, "fpr": fpr, "f1": f1, "mcc": mcc}


if __name__ == "__main__":
    # 场景一: 正负极度不平衡, 10000 个样本只有 5% 正例
    m1 = confusion_metrics(tp=40, fp=10, fn=20, tn=9930)
    print("场景一 稀疏正例 TP40 FP10 FN20 TN9930:")
    for k, v in m1.items():
        print(f"  {k:<11} {v:.4f}")
    assert m1["acc"] > 0.99, "准确率应被负例稀释到接近 1"
    assert m1["recall"] < 0.7, "召回应暴露漏报问题"
    # 场景二: 同一模型放到平衡样本上, 指标完全换了一副面孔
    m2 = confusion_metrics(tp=40, fp=10, fn=20, tn=70)
    print("场景二 平衡样本 TP40 FP10 FN20 TN70:")
    print(f"  acc={m2['acc']:.4f} precision={m2['precision']:.4f} recall={m2['recall']:.4f} "
          f"f1={m2['f1']:.4f} mcc={m2['mcc']:.4f}")
    assert m2["acc"] < 0.9, "同样的错分率在平衡样本上准确率应明显降低"
    # F1 是 precision 与 recall 的调和平均, 夹在两者之间且偏向较小者
    assert m1["precision"] <= m1["f1"] <= m1["recall"] or \
        m1["recall"] <= m1["f1"] <= m1["precision"], "F1 应夹在 P 与 R 之间"
    assert m1["f1"] < max(m1["precision"], m1["recall"]), "调和平均应偏向较小的一方"
    assert m1["mcc"] > 0, "模型优于随机猜测时 MCC 应为正"
    print("要点: 不平衡数据先看 recall 与 MCC, 准确率 99% 可能只是'全猜负例'的假象")
```

**追问**:
- 追问 1:MCC 比 F1 好在哪?—— MCC 考虑全部四个格子,类别翻转只变号不失真,极端不平衡下比 F1 稳定得多。
- 追问 2:特异度和 FPR 什么关系?—— FPR = 1 - 特异度,风控反欺诈等负例敏感场景盯 FPR 更直观。
