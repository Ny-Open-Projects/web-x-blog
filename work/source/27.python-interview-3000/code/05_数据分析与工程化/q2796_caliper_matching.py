"""样本配平的分层卡尺匹配: 同层内贪心最近邻, 卡尺控制匹配质量"""
import math

TREATED = [3.2, 3.5, 3.9, 4.1, 4.4, 4.8, 5.1, 5.6,
           6.0, 6.4, 6.9, 7.3, 7.8, 8.2, 8.9, 9.4]
CONTROL = [1.0, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8, 3.1, 3.4, 3.7, 4.0, 4.3,
           4.6, 4.9, 5.2, 5.5, 5.8, 6.1, 6.5, 7.0, 7.6, 8.4, 9.3, 10.4]


def pooled_sd(a, b):
    ma, mb = sum(a) / len(a), sum(b) / len(b)
    va = sum((x - ma) ** 2 for x in a) / (len(a) - 1)
    vb = sum((x - mb) ** 2 for x in b) / (len(b) - 1)
    return math.sqrt((va + vb) / 2)


def strata_bands(all_vals, n_strata):
    """按合并样本的分位数分层, 返回每层的上下界"""
    s = sorted(all_vals)
    edges = [s[min(len(s) * i // n_strata, len(s) - 1)] for i in range(n_strata + 1)]
    return edges


def band_of(v, edges):
    for i in range(len(edges) - 1):
        if edges[i] <= v < edges[i + 1] or i == len(edges) - 2:
            return i
    return len(edges) - 2


def caliper_match(treated, control, edges, caliper):
    """同层贪心最近邻: 每个处理组找同层且距离不超过卡尺的对照"""
    caliper = min(caliper, 0.25 * pooled_sd(treated, control))
    pool = {}
    for c in control:
        pool.setdefault(band_of(c, edges), []).append(c)
    pairs, unmatched = [], []
    for t in sorted(treated):
        b = band_of(t, edges)
        cands = [c for c in pool.get(b, []) if abs(c - t) <= caliper]
        if not cands:
            unmatched.append(t)
            continue
        best = min(cands, key=lambda c: abs(c - t))
        pool[b].remove(best)
        pairs.append((t, best))
    return pairs, unmatched, caliper


if __name__ == "__main__":
    edges = strata_bands(TREATED + CONTROL, 5)
    before_gap = sum(TREATED) / len(TREATED) - sum(CONTROL) / len(CONTROL)
    pairs, unmatched, cal = caliper_match(TREATED, CONTROL, edges, caliper=0.7)
    mt = [t for t, _ in pairs]
    mc = [c for _, c in pairs]
    after_gap = sum(mt) / len(mt) - sum(mc) / len(mc)
    print(f"合并五分位分层, 卡尺 {cal:.2f}")
    print(f"匹配前: 处理组均值 {sum(TREATED) / len(TREATED):.2f}, 对照组均值 {sum(CONTROL) / len(CONTROL):.2f}, 差 {before_gap:.2f}")
    print(f"匹配 {len(pairs)} 对, 弃配 {len(unmatched)} 个处理组样本 {unmatched}")
    print(f"匹配后: 处理组均值 {sum(mt) / len(mt):.2f}, 对照组均值 {sum(mc) / len(mc):.2f}, 差 {after_gap:.2f}")
    assert len(pairs) >= 12, "多数处理组样本应匹配成功"
    assert after_gap < before_gap / 2, "配平后协变量均值差应至少减半"
    assert abs(after_gap) < 0.4, "配平后均值差应很小"
    print("要点: 分层解决'在同一段活动水平内找对手', 卡尺解决'不许硬凑远距离对手', 弃配好过硬配")
