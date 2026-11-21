"""用纯标准库演示 temperature 缩放与 top_p 截断对采样分布的影响。"""
import random

LOGITS = {"北京": 4.0, "上海": 3.0, "广州": 1.5, "乌鲁木齐": 0.1}


def softmax_temp(logits: dict, temp: float) -> dict:
    scaled = {k: v / temp for k, v in logits.items()}
    m = max(scaled.values())
    exp = {k: 2.718281828 ** (v - m) for k, v in scaled.items()}
    total = sum(exp.values())
    return {k: v / total for k, v in exp.items()}


def sample_top_p(probs: dict, top_p: float) -> str:
    items = sorted(probs.items(), key=lambda x: -x[1])
    kept, acc = [], 0.0
    for k, p in items:
        kept.append((k, p))
        acc += p
        if acc >= top_p:
            break
    total = sum(p for _, p in kept)
    r, cur = random.random() * total, 0.0
    for k, p in kept:
        cur += p
        if r <= cur:
            return k
    return kept[-1][0]


if __name__ == "__main__":
    random.seed(42)
    for t in (0.2, 1.0, 2.0):
        probs = softmax_temp(LOGITS, t)
        picks = [sample_top_p(probs, 1.0) for _ in range(5)]
        print(f"temp={t} 北京概率={probs['北京']:.3f} 采样={picks}")
    low = softmax_temp(LOGITS, 1.0)
    print("top_p=0.6 采样:", [sample_top_p(low, 0.6) for _ in range(5)])
