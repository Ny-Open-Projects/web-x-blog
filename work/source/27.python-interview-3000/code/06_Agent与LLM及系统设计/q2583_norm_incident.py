"""Q2583 归一化缺失的事故复现:模长压倒角度,检索排序错位。

同方向短文档被模长大的弱相关文档压过去,是线上最常见的
"为什么排第一的文档不对" 事故;归一化后按余弦排序立刻修复,
复现实验可当回归用例。
"""
import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def normalize(v):
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def rank(query, docs, metric):
    if metric == "dot":
        scored = [(d["id"], dot(query, d["vec"])) for d in docs]
    else:
        q = normalize(query)
        scored = [(d["id"], round(dot(q, normalize(d["vec"])), 4)) for d in docs]
    return [i for i, _ in sorted(scored, key=lambda x: -x[1])], dict(scored)


def main():
    query = [1.0, 1.0]
    docs = [
        {"id": "真相关-短文", "vec": [0.9, 0.9]},   # 角度完全一致,模长小
        {"id": "弱相关-长文", "vec": [2.0, 0.0]},   # 夹角 45 度,模长大
    ]
    bad, raw = rank(query, docs, "dot")
    good, ang = rank(query, docs, "cos")
    assert bad[0] == "弱相关-长文", bad        # 事故:点积让长文排前
    assert good[0] == "真相关-短文", good      # 修复:余弦回到正确顺序
    assert raw["弱相关-长文"] == 2.0 and raw["真相关-短文"] == 1.8
    assert ang["真相关-短文"] == 1.0 and ang["弱相关-长文"] == 0.7071
    print("未归一 dot 得分:", raw, "排序:", bad, "← 事故排序")
    print("归一后 cos 得分:", ang, "排序:", good, "← 正确排序")


if __name__ == "__main__":
    main()
