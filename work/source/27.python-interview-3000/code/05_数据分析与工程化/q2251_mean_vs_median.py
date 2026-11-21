"""均值还是中位数: 同一实验两个口径给出相反结论"""

import statistics as st

GROUP_A = [80] * 19 + [4000]          # 对照组 20 单, 一笔企业大单
GROUP_B = [70] * 14 + [3000] * 6      # 实验组 20 单, 六笔中大型单


def summary(name, orders):
    top3 = sum(sorted(orders)[-3:]) / sum(orders)
    print(f"{name}: 均值 {st.mean(orders):.0f} 中位数 {st.median(orders):.0f} 头部3单占流水 {top3:.0%}")
    return st.mean(orders), st.median(orders)


if __name__ == "__main__":
    ma, med_a = summary("对照组", GROUP_A)
    mb, med_b = summary("实验组", GROUP_B)
    print(f"均值口径: 实验 vs 对照 {mb / ma - 1:+.1%} -> 实验胜")
    print(f"中位数口径: 实验 vs 对照 {med_b / med_a - 1:+.1%} -> 实验负")
    print("决策规则: 加总类指标看均值配头部集中度, 体验类指标看中位数; 头部占比过半先分层")
