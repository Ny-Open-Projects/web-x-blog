"""流失线定界:用回访间隔分布分位数定静默期阈值,超过即判流失"""

GAPS = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 7,
        7, 8, 10, 12, 14, 18, 21, 30, 45]
USERS_LAST_ACTIVE = {"u1": 3, "u2": 9, "u3": 16, "u4": 25,
                     "u5": 40, "u6": 5, "u7": 12}


def quantile(xs, q):
    s = sorted(xs)
    pos = (len(s) - 1) * q
    lo, hi = int(pos), min(int(pos) + 1, len(s) - 1)
    frac = pos - lo
    return s[lo] * (1 - frac) + s[hi] * frac


if __name__ == "__main__":
    print("回访间隔分布:中位", quantile(GAPS, 0.5), "天, p90", round(quantile(GAPS, 0.9)), "天")
    for level in (0.90, 0.95):
        line = round(quantile(GAPS, level))
        churned = [u for u, d in USERS_LAST_ACTIVE.items() if d > line]
        print(f"p{int(level * 100)} 间隔 = {line} 天 -> 流失线 {line} 天,"
              f"当前判流失 {len(churned)} 人 {churned}")
    print("要点:流失线不拍脑袋定 30 天,用回访间隔分位数定再向上取整;口径一旦上线不要改,要改就走并行期桥接;运营'召回已流失'的召回窗口要在流失线之内")
