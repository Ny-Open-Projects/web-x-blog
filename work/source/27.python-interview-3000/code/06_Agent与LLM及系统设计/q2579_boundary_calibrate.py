"""Q2579 语义边界阈值的标定:扫参选 F1 最高点。

阈值拍脑袋定不可靠;拿人工标注的边界当真值,扫一遍阈值,
逐点算精确率 召回率 F1,取 F1 最高且落在平台期的阈值上线。
"""
import math
import re

DIM = 64


def embed(text):
    v = [0.0] * DIM
    for w in re.findall(r"[a-z0-9]+", text.lower()):
        h = 0
        for ch in w:
            h = (h * 31 + ord(ch)) % DIM
        v[h] += 1.0
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def adjacent_sims(sentences):
    embs = [embed(s) for s in sentences]
    return [sum(x * y for x, y in zip(embs[i], embs[i + 1]))
            for i in range(len(embs) - 1)]


def f1(detected, truth):
    tp = len(set(detected) & set(truth))
    p = tp / len(detected) if detected else 0.0
    r = tp / len(truth) if truth else 0.0
    return 2 * p * r / (p + r) if p + r else 0.0


def calibrate(sims, truth, thresholds):
    curve = []
    for th in thresholds:
        det = [i + 1 for i, s in enumerate(sims) if s < th]
        curve.append((th, f1(det, truth), det))
    return curve


SENTS = ["cat eats fish", "cat likes fish", "fish feeds cat",
         "database stores rows", "database stores rows fast", "rows live in database",
         "cache misses hurt", "cache misses slow reads"]


def main():
    sims = adjacent_sims(SENTS)
    truth = [3, 6]  # 两组主题切换点
    thresholds = [round(0.05 + 0.05 * i, 2) for i in range(10)]
    curve = calibrate(sims, truth, thresholds)
    best = max(curve, key=lambda x: x[1])
    assert best[1] == 1.0, curve            # 存在完美阈值
    assert best[2] == truth, best            # 且检测恰等于真值
    print("相似度:", [round(s, 3) for s in sims])
    for th, f, det in curve:
        print("阈值", th, "F1", round(f, 3), "检测", det)
    print("选定阈值:", best[0])


if __name__ == "__main__":
    main()
