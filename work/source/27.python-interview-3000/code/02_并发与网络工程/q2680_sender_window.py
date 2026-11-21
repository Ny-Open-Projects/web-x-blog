# -*- coding: utf-8 -*-
"""发送端滑动窗口: 在途上限与 ACK 推进 base。

- 停等: 每帧必等 ACK, 20% 丢包下效率被 RTT 拖死;
- 滑动窗口: 一次允许 window 帧在途, 丢帧只占住窗口等超时重传;
- 实测同一有损链路上三种窗口的总拍数, 吞吐随窗口放大但不是无限。
"""
import random


def sender_window(total, window, loss, seed):
    """拍语义: 结算 ACK -> 超时重传 -> 推进 base -> 发新帧 -> 倒计时。

    帧发出后 2 拍 ACK 到达; 丢帧永远等不到 ACK, 4 拍后判超时重传。
    """
    rng = random.Random(seed)
    t = 0
    base = 0                 # 最小未确认序号
    acked = set()
    inflight = {}            # seq -> 剩余拍数, 丢失帧走负数
    nxt = 0
    rtx = 0
    while base < total:
        t += 1
        for s in [s for s, v in inflight.items() if v == 0]:
            del inflight[s]
            acked.add(s)
        for s in [s for s, v in inflight.items() if v <= -4]:
            inflight[s] = 2                  # 超时重传
            rtx += 1
        while base in acked:
            acked.discard(base)
            base += 1
        while nxt < total and len(inflight) < window:
            if rng.random() < loss:
                inflight[nxt] = -1           # 丢失: 不会有 ACK
            else:
                inflight[nxt] = 2
            nxt += 1
        for s in inflight:
            inflight[s] -= 1
    return t, rtx


if __name__ == "__main__":
    TOTAL, LOSS, SEED = 200, 0.2, 7
    print("链路: %d 帧, 丢包率 %.0f%%" % (TOTAL, LOSS * 100))
    print("%-8s %-10s %-8s %-12s" % ("window", "ticks", "重传", "吞吐 帧/拍"))
    for w in (1, 4, 8, 16):
        t, rtx = sender_window(TOTAL, w, LOSS, SEED)
        print("%-8d %-10d %-8d %.2f" % (w, t, rtx, TOTAL / t))
    print("要点: 窗口越大吞吐越高, 但丢帧会占住窗口坑位, 收益有天花板")
    print("要点: base 只被连续 ACK 推进, 这就是累计确认的语义")
