"""Q2995 A/B 实验的分配与统计:稳定分桶+转化对比+显著性检验。

A/B 分配的铁律是稳定性:同一用户每次进来必须落在同一组,否则体验
抖动且统计被污染——用用户 id 的哈希取模做确定性分桶,而不是每次
随机。统计端用两比例 z 检验近似,给出提升幅度与显著性结论;样本
不足时明确说「证据不足」,不要宣布胜利。
"""

import hashlib
import math

BUCKETS = 100
TREATMENT_RATIO = 0.5


def assign(user_id):
    """确定性分桶:哈希取模,同一 user_id 永远同组。"""
    h = int(hashlib.md5(user_id.encode("utf-8")).hexdigest(), 16)
    bucket = h % BUCKETS
    return "treatment" if bucket < BUCKETS * TREATMENT_RATIO else "control"


class Experiment:
    def __init__(self):
        self.exposed = {"control": 0, "treatment": 0}
        self.converted = {"control": 0, "treatment": 0}

    def record(self, user_id, converted):
        group = assign(user_id)
        self.exposed[group] += 1
        if converted:
            self.converted[group] += 1
        return group

    def rates(self):
        return {g: self.converted[g] / self.exposed[g]
                for g in self.exposed if self.exposed[g]}

    def z_test(self):
        """两比例 pooled z 检验,返回 (z, p 近似, 显著)。"""
        n1, c1 = self.exposed["control"], self.converted["control"]
        n2, c2 = self.exposed["treatment"], self.converted["treatment"]
        if n1 == 0 or n2 == 0:
            return None, None, False
        p_pool = (c1 + c2) / (n1 + n2)
        se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
        if se == 0:
            return None, None, False
        z = (c2 / n2 - c1 / n1) / se
        p = 2.0 * (1.0 - 0.5 * (1.0 + math.erf(abs(z) / math.sqrt(2))))
        return round(z, 4), round(p, 6), p < 0.05


def main():
    # 稳定性:同一用户反复分配,结果不变
    g42 = assign("u_42")
    assert all(assign("u_42") == g42 for _ in range(100))
    groups = {assign("u_%d" % i) for i in range(200)}
    assert groups == {"control", "treatment"}       # 两组都有人

    exp = Experiment()
    # 构造确定性流量:treatment 每第 5 个曝光转化,control 每第 10 个
    counters = {"control": 0, "treatment": 0}
    for i in range(400):
        uid = "u_%d" % i
        g = assign(uid)
        counters[g] += 1
        conv = (counters[g] % 5 == 0) if g == "treatment" \
            else (counters[g] % 10 == 0)
        exp.record(uid, conv)
    rates = exp.rates()
    n_t, n_c = exp.exposed["treatment"], exp.exposed["control"]
    assert n_t + n_c == 400 and n_t > 100 and n_c > 100
    assert rates["treatment"] > 0.15 and rates["control"] < 0.15, rates
    assert rates["treatment"] > rates["control"], rates
    z, p, sig = exp.z_test()
    assert sig and z > 2.5, (z, p, sig)             # 提升显著

    # 样本不足:证据不足要说人话
    tiny = Experiment()
    tiny.record("a", False)
    tiny.record("b", True)
    z2, p2, sig2 = tiny.z_test()
    assert not sig2, (z2, p2)
    lift = rates["treatment"] - rates["control"]
    print("转化率: control=%.3f treatment=%.3f" % (rates["control"],
                                                    rates["treatment"]))
    print("z=%.2f p=%.4f 显著=%s 提升=%.1f%%" % (z, p, sig, lift * 100))
    print("小样本结论: z=%s p=%s 证据不足,继续观察" % (z2, p2))


if __name__ == "__main__":
    main()
