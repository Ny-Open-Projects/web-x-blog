"""拥塞控制概念: 慢启动与 AIMD 的账。

cwnd(拥塞窗口)决定在途数据量, 每过一个 RTT 调整一次:
- 慢启动: cwnd < ssthresh 时每个 RTT 翻倍(指数), 到 ssthresh 封顶;
- 拥塞避免: cwnd >= ssthresh 后每个 RTT 加 1(线性, AIMD 的加法增);
- 丢包(Tahoe): ssthresh 降为 cwnd/2, cwnd 回到 1 重新慢启动;
- ssthresh 不是速率上限, 是"指数转线性"的换挡点。
"""
def simulate(mode="tahoe", rtts=20, loss_at=12, ssthresh_init=8.0):
    cwnd, ssthresh = 1.0, ssthresh_init
    rows, delivered = [], 0
    for rtt in range(1, rtts + 1):
        phase = "slow-start" if cwnd < ssthresh else "congestion-avoid"
        rows.append((rtt, cwnd, phase))
        delivered += int(cwnd)
        if rtt == loss_at:                   # 第 12 个 RTT 发生丢包
            ssthresh = max(2.0, cwnd / 2)    # AIMD 的乘法减
            cwnd = ssthresh if mode == "reno" else 1.0
        elif cwnd < ssthresh:
            cwnd = min(cwnd * 2, ssthresh)   # 指数增长, 封顶换挡
        else:
            cwnd += 1.0                      # 线性增长
    return rows, delivered


def main():
    for mode in ("tahoe", "reno"):
        rows, delivered = simulate(mode=mode)
        print("== %s ==" % mode)
        for rtt, cwnd, phase in rows:
            mark = " <- 丢包" if rtt == 12 else ""
            print("  RTT %2d  cwnd=%5.1f  %s%s" % (rtt, cwnd, phase, mark))
        print("  累计发送报文:", delivered)
        if mode == "tahoe":
            tahoe_rows = rows

    reno_rows, _ = simulate(mode="reno")
    # 结构断言: 换挡点、乘法减与两条恢复路径
    assert tahoe_rows[3][1] == 8.0 and tahoe_rows[3][2] == "congestion-avoid", \
        "cwnd 到达 ssthresh=8 后应换挡为线性增长"
    assert tahoe_rows[11][1] == 16.0, "丢包发生在 cwnd=16 的 RTT"
    assert reno_rows[12][1] == 8.0, "Reno 丢包后直接从 ssthresh=8 续跑"
    assert tahoe_rows[12][1] == 1.0 and tahoe_rows[13][1] == 2.0, \
        "Tahoe 丢包后回到 1 重新慢启动"
    print("结论: 慢启动探路, AIMD 收敛; Tahoe 更保守, Reno 快恢复省一个慢启动")


if __name__ == "__main__":
    main()
