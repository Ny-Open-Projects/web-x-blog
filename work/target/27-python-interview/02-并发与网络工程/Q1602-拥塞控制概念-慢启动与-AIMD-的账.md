---
title: [Q1602] 拥塞控制概念:慢启动与 AIMD 的账
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1602 · 拥塞控制概念:慢启动与 AIMD 的账

> 难度:★★★☆ | 标签:TCP, 拥塞控制, cwnd

**问**:TCP 为什么刚开始传得慢?cwnd 和 ssthresh 到底谁管什么?

**答**:cwnd(拥塞窗口)决定在途数据上限,每过一个 RTT 调整一次。慢启动阶段 cwnd 小于 ssthresh,每个 RTT 翻倍——不是慢,是指数起步的探路;到达 ssthresh 换挡进拥塞避免,每个 RTT 加 1,这是 AIMD 的加法增;丢包时乘法减:ssthresh 降为 cwnd 的一半,Tahoe 把 cwnd 打回 1 重新慢启动,Reno 直接从 ssthresh 续跑(快恢复,省一个慢启动)。账目实验:20 个 RTT 里 cwnd 从 1 冲到 16,丢包瞬间砍半再爬坡——这就是 TCP 激进探路、保守收敛的全部智慧。

```python
# file: code/02_并发与网络工程/q1602_congestion.py
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
```

**追问**:1) BBR 为什么不一样?——BBR 不以丢包为信号,而是主动测带宽与 RTT 的乘积来定发送速率,绕开填满缓冲才知拥塞的传统假设。2) Tahoe 与 Reno 的分界为什么要记?——丢包后从「cwnd=1 慢启动」还是「ssthresh 快恢复」决定恢复时长差一个指数期;现代内核(如 CUBIC)又在此基础上改了增长函数,但 AIMD 的「加法增乘法减」骨架不变——面试要能把内核名挂到模型上。3) ssthresh 的角色边界?——它不是速率上限,是「指数转线性」的换挡点;初始 ssthresh 大时整个传输都是慢启动(指数冲);被丢包不断压低后稳态在拥塞避免——理解「换挡」才能解释「为什么传着传着变慢了」。4) 生产陷阱?——应用层大量短连接,每次都从慢启动开始(永远吃不到拥塞窗口,长连接复用的又一理由,Q1597);把吞吐差全归「带宽不够」不看 RTT 与 cwnd;调大 socket 缓冲想绕过 cwnd(缓冲膨胀 bufferbloat,延迟暴涨);BBR 与丢包式算法混部同链路互相挤压。

---
