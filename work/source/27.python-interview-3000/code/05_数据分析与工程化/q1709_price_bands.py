"""价格带分箱:业务自定义分箱用 bisect 实现,分位分箱各箱容量均衡"""

import bisect
from collections import defaultdict

ORDERS = [23, 45, 49, 55, 68, 88, 99, 110, 128, 149, 158, 199,
          210, 258, 320, 480, 520, 680, 890, 1200]
BANDS = [0, 50, 100, 200, 500]  # 上界序列,最后一段开区间到无穷,左闭右开


def band_label(x):
    idx = bisect.bisect_right(BANDS, x) - 1
    lo = BANDS[idx]
    hi = BANDS[idx + 1] if idx + 1 < len(BANDS) else None
    return f"{lo}-{hi}" if hi else f"{lo}以上"


def aggregate(orders):
    stats = defaultdict(lambda: [0, 0])
    for x in orders:
        s = stats[band_label(x)]
        s[0] += 1
        s[1] += x
    return stats


def quantile_cuts(orders, k=4):
    """分位分箱:每箱单量接近,但边界不规整,适合看分布不适合做活动门槛"""
    xs = sorted(orders)
    n = len(xs)
    return [xs[min(int(n * i / k), n - 1)] for i in range(k)]


if __name__ == "__main__":
    stats = aggregate(ORDERS)
    total_amt = sum(ORDERS)
    labels = [f"{BANDS[i]}-{BANDS[i + 1]}" for i in range(len(BANDS) - 1)] + [f"{BANDS[-1]}以上"]
    print("业务价格带:")
    for label in labels:
        cnt, amt = stats.get(label, [0, 0])
        print(f"  {label:<10} 单数 {cnt:>2}  金额占比 {amt / total_amt:.1%}")
    print("分位分箱边界(四分位):", quantile_cuts(ORDERS))
    print("要点:业务带便于解读与对活动规则;分位带适合看形态;边界归属(左闭右开)必须写进口径文档,50 归哪带要定死")
