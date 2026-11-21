"""异常值三方法实测:IQR、z-score、MAD 在同一份重尾数据上的表现对比"""

DATA = [12, 13, 12, 14, 13, 11, 12, 13, 14, 12,
        13, 12, 15, 13, 12, 13, 14, 12, 13, 12,
        11, 13, 12, 14, 13, 12, 13, 12, 90, 130]  # 末尾两个真异常


def iqr_flags(xs, k=1.5):
    s = sorted(xs)
    n = len(s)
    q1, q3 = s[n // 4], s[3 * n // 4]
    iqr = q3 - q1
    lo, hi = q1 - k * iqr, q3 + k * iqr
    return [x for x in xs if x < lo or x > hi], (q1, q3)


def zscore_flags(xs, z=3.0):
    n = len(xs)
    mean = sum(xs) / n
    std = (sum((x - mean) ** 2 for x in xs) / n) ** 0.5
    return [x for x in xs if abs((x - mean) / std) > z], (round(mean, 1), round(std, 1))


def mad_flags(xs, c=3.5):
    """修正 z = 0.6745*(x-中位数)/MAD,阈值 3.5 是经典取值"""
    med = sorted(xs)[len(xs) // 2]
    mad = sorted(abs(x - med) for x in xs)[len(xs) // 2]
    return [x for x in xs if 0.6745 * abs(x - med) / mad > c], (med, mad)


if __name__ == "__main__":
    for name, fn in [("IQR 1.5 倍", iqr_flags),
                     ("z-score 3σ", zscore_flags),
                     ("MAD 3.5", mad_flags)]:
        out, params = fn(DATA)
        print(f"{name:<12} 参数{params} -> 异常 {len(out)} 个: {sorted(set(out))}")
    print("要点:z-score 的均值与σ被异常值自己污染产生掩蔽,90 可能漏报;IQR 与 MAD 基于分位数,先 IQR 后 MAD 复核,再人工确认")
