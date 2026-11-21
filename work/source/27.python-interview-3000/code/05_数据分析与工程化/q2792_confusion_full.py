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
