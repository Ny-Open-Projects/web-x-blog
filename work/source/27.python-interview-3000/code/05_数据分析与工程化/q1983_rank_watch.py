"""排名波动监控:Top-N 榜单日间对比,进出榜与位移超限告警"""

YESTERDAY = ["商品A", "商品B", "商品C", "商品D", "商品E",
             "商品F", "商品G", "商品H", "商品I", "商品J"]
TODAY = ["商品B", "商品A", "商品K", "商品C", "商品L",
         "商品D", "商品F", "商品E", "商品G", "商品M"]
ALARM_TURN = 2    # 进出榜家数阈值
ALARM_SHIFT = 3   # 单品最大位移阈值


def rank_map(lst):
    return {name: i + 1 for i, name in enumerate(lst)}


def compare(prev, curr):
    r_prev, r_curr = rank_map(prev), rank_map(curr)
    dropped = sorted(set(r_prev) - set(r_curr))
    entered = sorted(set(r_curr) - set(r_prev))
    moves = {k: r_curr[k] - r_prev[k]
             for k in set(r_prev) & set(r_curr) if r_curr[k] != r_prev[k]}
    return dropped, entered, moves


if __name__ == "__main__":
    r_prev, r_curr = rank_map(YESTERDAY), rank_map(TODAY)
    dropped, entered, moves = compare(YESTERDAY, TODAY)
    print(f"掉榜: {dropped}  新进: {entered}")
    for k, m in sorted(moves.items(), key=lambda x: x[1]):
        print(f"  {k}: 第{r_prev[k]} -> 第{r_curr[k]} ({m:+d})")
    alarm = len(dropped) + len(entered) > ALARM_TURN or \
        any(abs(m) > ALARM_SHIFT for m in moves.values())
    print(f"告警判定: {'触发,榜单结构剧变,先查口径与爬虫流量' if alarm else '正常波动'}")
    print("要点:排名天然高波动,监控比的是榜单结构(进出榜/位移分布)而不是单点名次;阈值按历史位移分位数定")
