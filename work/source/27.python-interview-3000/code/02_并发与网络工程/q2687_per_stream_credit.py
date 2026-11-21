# -*- coding: utf-8 -*-
"""多路复用的每流信用: 一条流卡死不拖垮别人。

- 单一共享信用池: 慢流的接收方迟迟不还信用, 全连接跟着停摆;
- 每流独立信用: 信用按流记账归还, 一条流卡死只冻住它自己;
- 这就是 HTTP/2 流控与队头阻塞治理的核心机制。
"""
from collections import deque

TICKS = 40


class Stream:
    def __init__(self, name, grant_every):
        self.name = name
        self.credits = 2                 # 每流初始信用
        self.grant_every = grant_every   # 接收方每 N 拍归还 1 信用
        self.clock = 0
        self.backlog = 100
        self.delivered = 0


def run(scheme, streams):
    pool = {"credits": 4}                # 共享信用池(仅 shared 方案用)
    for _ in range(TICKS):
        for s in streams:                # 接收方处理并归还信用
            s.clock += 1
            if s.clock % s.grant_every == 0:
                if scheme == "per":
                    s.credits += 1
                else:
                    pool["credits"] += 1
        for s in streams:                # 发送方轮询, 有票就发
            while s.backlog > 0:
                if scheme == "per":
                    if s.credits <= 0:
                        break
                    s.credits -= 1
                else:
                    if pool["credits"] <= 0:
                        break
                    pool["credits"] -= 1
                s.backlog -= 1
                s.delivered += 1
    return [s.delivered for s in streams]


if __name__ == "__main__":
    slow = Stream("A-慢流", 8)            # 接收方很慢: 8 拍才还 1 信用
    fast_b = Stream("B-快流", 1)
    fast_c = Stream("C-快流", 1)

    shared = run("shared", [slow, fast_b, fast_c])
    per = run("per", [slow, fast_b, fast_c])

    print("共享信用池 40 拍交付: %s" % dict(zip(("A", "B", "C"), shared)))
    print("每流独立信用 40 拍交付: %s" % dict(zip(("A", "B", "C"), per)))
    print("要点: 共享池下慢流 A 吃光全部信用, B 与 C 直接饿死")
    print("要点: 每流信用把故障隔离在流内, 这就是多路复用的公平底线")
