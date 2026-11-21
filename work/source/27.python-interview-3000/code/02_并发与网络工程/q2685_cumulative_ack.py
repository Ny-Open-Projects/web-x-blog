# -*- coding: utf-8 -*-
"""累积 ACK 与延迟 ACK: 回程带宽的经济学。

- 逐帧 ACK: 一个数据帧换一个回包, 回程被确认流量挤爆;
- 延迟累积 ACK: 攒 N 帧才回一个包, "到 seq N 为止全收到"一句话顶 N 句;
- 代价: 确认变慢, 依赖超时重传的协议会被拖长恢复时间。
"""


def simulate(frames, ack_every, drain_ticks):
    """每拍一帧到达; 攒满 ack_every 生成一个累积 ACK; 回程每 drain_ticks 拍放行一个。"""
    pending = 0
    ret_q = 0
    acks = 0
    max_backlog = 0
    for t in range(frames):
        pending += 1
        if pending >= ack_every:
            ret_q += 1                       # 生成一个累积 ACK
            acks += 1
            pending = 0
        if t % drain_ticks == drain_ticks - 1 and ret_q:
            ret_q -= 1                       # 回程槽放行一个
        max_backlog = max(max_backlog, ret_q)
    return acks, max_backlog, ret_q


if __name__ == "__main__":
    FRAMES, DRAIN = 200, 3                   # 回程带宽: 3 拍才放行一个包
    print("前向 %d 帧, 回程每 %d 拍放行一个包" % (FRAMES, DRAIN))
    print("%-12s %-10s %-14s %-10s" % ("策略", "ACK 数", "回程积压峰值", "未清 ACK"))
    for name, every in (("逐帧 ACK", 1), ("延迟累积 4", 4), ("延迟累积 8", 8)):
        acks, peak, left = simulate(FRAMES, every, DRAIN)
        print("%-12s %-10d %-14d %-10d" % (name, acks, peak, left))
    print("要点: 累积确认把回程压力砍掉一个数量级")
    print("要点: 确认粒度变粗后, 丢包恢复靠重传超时, 延迟上限要设短")
