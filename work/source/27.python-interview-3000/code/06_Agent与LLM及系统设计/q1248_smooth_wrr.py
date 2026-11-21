"""平滑加权轮询:Nginx 算法,验证权重比例与输出平滑性。"""
from collections import Counter


class SmoothWRR:
    def __init__(self, weights):
        self.weights = dict(weights)              # node -> weight
        self.current = {n: 0 for n in weights}

    def pick(self):
        for n in self.current:
            self.current[n] += self.weights[n]
        best = max(self.current, key=lambda n: self.current[n])
        self.current[best] -= sum(self.weights.values())
        return best

    def schedule(self, rounds):
        return [self.pick() for _ in range(rounds)]


def smoothness(seq):
    """连续相同节点最长游程:越小越平滑。"""
    run, best = 1, 1
    for a, b in zip(seq, seq[1:]):
        run = run + 1 if a == b else 1
        best = max(best, run)
    return best


if __name__ == "__main__":
    sw = SmoothWRR({"A": 3, "B": 1, "C": 1})
    seq = sw.schedule(20)
    dist = Counter(seq)
    print("20 轮分布:", dict(dist))
    assert dist["A"] == 12 and dist["B"] == 4 and dist["C"] == 4, "严格按 3:1:1"

    naive = ["A", "A", "A", "B", "C"] * 4         # 朴素按权重展开
    print("朴素展开游程:", smoothness(naive), "平滑算法游程:", smoothness(seq))
    assert smoothness(seq) <= 2, f"平滑调度游程应 <=2, 实际 {smoothness(seq)}"
    assert smoothness(seq) < smoothness(naive), "平滑算法显著优于朴素展开"

    sw2 = SmoothWRR({"X": 0, "Y": 3})
    seq2 = sw2.schedule(6)
    assert set(seq2) == {"Y"}, "权重 0 节点不参与调度"
    print("权重 0 支持摘除节点;current_weight 周期性回归实现均匀穿插")
