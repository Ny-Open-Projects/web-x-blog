import statistics

def mad_flags(xs, k=3.5):
    med = statistics.median(xs)
    mad = statistics.median([abs(x - med) for x in xs])
    if mad == 0:
        return med, mad, [i for i, x in enumerate(xs) if x != med]
    scores = [0.6745 * abs(x - med) / mad for x in xs]
    return med, mad, [i for i, sc in enumerate(scores) if sc > k]

data = [10, 11, 12, 12, 13, 12, 11, 500]
med, mad, flags = mad_flags(data)
print("中位数:", med, "MAD:", mad)
print("异常下标:", flags, "对应值:", [data[i] for i in flags])
print("z-score 对照:均值", round(statistics.mean(data), 1), "被 500 严重拉高")
