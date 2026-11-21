"""配平质量诊断: 标准化均值差 SMD, 阈值 0.1 以内才算配平"""
import math

# 三个相关协变量: pre_score 是匹配键, tenure 与 spend 随之被带平
TREATED = [(3.2, 21.0, 68.0), (3.5, 21.5, 72.0), (3.9, 23.5, 74.5), (4.1, 24.5, 76.5),
           (4.4, 25.5, 79.0), (4.8, 27.0, 83.0), (5.1, 28.5, 86.0), (5.6, 30.0, 90.5),
           (6.0, 31.5, 94.0), (6.4, 33.5, 97.5), (6.9, 35.5, 102.0), (7.3, 37.0, 106.0),
           (7.8, 39.0, 110.0), (8.2, 41.0, 114.0), (8.9, 44.0, 120.0), (9.4, 46.0, 124.5)]
CONTROL = [(1.0, 12.0, 48.5), (1.3, 13.0, 51.5), (1.6, 14.5, 54.0), (1.9, 15.5, 57.0),
           (2.2, 16.5, 59.5), (2.5, 18.0, 62.5), (2.8, 19.0, 65.0), (3.1, 20.5, 67.5),
           (3.4, 21.5, 70.5), (3.7, 23.0, 73.0), (4.0, 24.0, 76.0), (4.3, 25.0, 78.5),
           (4.6, 26.5, 81.0), (4.9, 27.5, 84.0), (5.2, 28.5, 87.0), (5.5, 30.0, 89.5),
           (5.8, 31.0, 92.5), (6.1, 32.5, 95.0), (6.5, 34.0, 98.5), (7.0, 36.0, 103.0),
           (7.6, 38.5, 108.0), (8.4, 42.0, 115.5), (9.3, 45.5, 124.0), (10.4, 50.0, 133.5)]


def pooled_sd(xs, ys):
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    vx = sum((x - mx) ** 2 for x in xs) / (len(xs) - 1)
    vy = sum((y - my) ** 2 for y in ys) / (len(ys) - 1)
    return math.sqrt((vx + vy) / 2)


def smd(t_vals, c_vals):
    mt, mc = sum(t_vals) / len(t_vals), sum(c_vals) / len(c_vals)
    sd = pooled_sd(t_vals, c_vals)
    return abs(mt - mc) / sd if sd else 0.0


def band_of(v, edges):
    for i in range(len(edges) - 1):
        if edges[i] <= v < edges[i + 1] or i == len(edges) - 2:
            return i
    return len(edges) - 2


def match_on_score(treated, control):
    """在 pre_score 上做同层卡尺匹配, 返回配对索引"""
    all_scores = [r[0] for r in treated] + [r[0] for r in control]
    s = sorted(all_scores)
    edges = [s[min(len(s) * i // 5, len(s) - 1)] for i in range(6)]
    sd = pooled_sd([r[0] for r in treated], [r[0] for r in control])
    caliper = 0.25 * sd
    pool = {}
    for j, c in enumerate(control):
        pool.setdefault(band_of(c[0], edges), []).append(j)
    pairs = []
    for i, t in sorted(enumerate(treated), key=lambda kv: kv[1][0]):
        cands = [j for j in pool.get(band_of(t[0], edges), [])
                 if abs(control[j][0] - t[0]) <= caliper]
        if not cands:
            continue
        best = min(cands, key=lambda j: abs(control[j][0] - t[0]))
        pool[band_of(t[0], edges)].remove(best)
        pairs.append((i, best))
    return pairs


if __name__ == "__main__":
    names = ["pre_score", "tenure_days", "spend"]
    pairs = match_on_score(TREATED, CONTROL)
    mt = [TREATED[i] for i, _ in pairs]
    mc = [CONTROL[j] for _, j in pairs]
    print(f"匹配对数 {len(pairs)}, 各协变量 SMD (阈值 0.1):")
    all_pass = True
    for k, name in enumerate(names):
        before = smd([r[k] for r in TREATED], [r[k] for r in CONTROL])
        after = smd([r[k] for r in mt], [r[k] for r in mc])
        verdict = "OK" if after < 0.1 else "未配平"
        print(f"  {name:<12} 匹配前 {before:.3f} -> 匹配后 {after:.3f}  [{verdict}]")
        all_pass = all_pass and after < 0.1
    assert all_pass, "匹配后各协变量 SMD 都应低于 0.1"
    assert smd([r[0] for r in TREATED], [r[0] for r in CONTROL]) > 0.25, "匹配前主协变量应明显失衡"
    print("要点: 匹配键配平会带动相关协变量一起配平, SMD 用合并标准差消除量纲, 0.1 是通行验收线")
