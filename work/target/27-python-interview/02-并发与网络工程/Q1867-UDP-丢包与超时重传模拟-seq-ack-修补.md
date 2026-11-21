---
title: [Q1867] UDP 丢包与超时重传模拟:seq/ack 修补不可靠链路
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1867 · UDP 丢包与超时重传模拟:seq/ack 修补不可靠链路

> 难度:★★★ | 标签:UDP, 重传, 可靠性

**问**:UDP 不保证到达,要求可靠就得应用层自己补,最小实现长什么样?

**答**:最小可靠层三件套:序号(标识每个包)、确认(接收方回 ACK)、超时重传(发出后等 ACK,超时就重发)。

- 演示把服务端做成有损链路:对 2 号和 4 号包 '吃掉' 第一次到达的那份、不回 ACK,客户端等 0.12s 超时后重传,第二次到达拿到 ACK;

- 结果六个包全部确认,重传恰好发生在被丢的两个序号上,未丢的包一次到位——重传风暴没有发生;

- 更进一步就是滑动窗口、累积确认与快速重传,把 '停等' 升级为 '流水线',这正是 TCP 的进化路线。

自己写可靠 UDP 时要防 'ACK 丢失导致重复投递':接收方按序号去重,这就是至少一次语义的成本。

```python
# file: code/02_并发与网络工程/q1867_udp_retransmit.py
# -*- coding: utf-8 -*-
"""UDP 丢包与超时重传模拟: seq/ack 协议把不可靠链路修补成可靠投递。

- 服务端模拟有损链路: 对指定序号"吃掉"第一次到达的包, 不发 ACK;
- 客户端每包独立重传: 发出后等 ACK, 超时就重发, 直到确认或尝试耗尽;
- 实验证明: 重传机制让全部数据最终到达, 代价是重复传输与延迟抖动。
"""
import socket
import threading
import time

DROP_SEQS = {2, 4}                            # 这两个序号第一次到达会被丢弃
PACKETS = 6
ACK_TIMEOUT = 0.12


def start_lossy_server():
    srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    srv.bind(("127.0.0.1", 0))
    port = srv.getsockname()[1]
    seen_drop = set()

    def loop():
        srv.settimeout(0.2)
        while True:
            try:
                data, addr = srv.recvfrom(2048)
            except socket.timeout:
                continue
            seq = int(data.decode().split(":")[0])
            if seq in DROP_SEQS and seq not in seen_drop:
                seen_drop.add(seq)
                print("  链路吞掉包 seq=%d, 不回 ACK" % seq)
                continue
            srv.sendto(("ack:%d" % seq).encode(), addr)

    threading.Thread(target=loop, daemon=True).start()
    time.sleep(0.1)                            # UDP 无连接, 稍等收发循环就位
    return srv, port


def main():
    srv, port = start_lossy_server()
    cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cli.bind(("127.0.0.1", 0))
    cli.settimeout(ACK_TIMEOUT)

    acked = set()
    retransmits = {seq: 0 for seq in range(PACKETS)}
    for seq in range(PACKETS):
        payload = ("%d:payload-%d" % (seq, seq)).encode()
        for attempt in range(6):
            cli.sendto(payload, ("127.0.0.1", port))
            try:
                reply, _ = cli.recvfrom(2048)
                if reply == ("ack:%d" % seq).encode():
                    acked.add(seq)
                    break
            except socket.timeout:
                retransmits[seq] += 1
                print("  seq=%d 等 ACK 超时, 第 %d 次重传" % (seq, retransmits[seq]))
    cli.close()
    srv.close()

    print("确认到达的序号:", sorted(acked))
    print("重传统计:", {k: v for k, v in retransmits.items() if v})
    assert acked == set(range(PACKETS)), "重传机制保证全部数据最终到达"
    assert all(retransmits[s] >= 1 for s in DROP_SEQS), "被丢的包必然经历重传"
    assert sum(retransmits.values()) == len(DROP_SEQS), "未丢的包一次到位"
    print("结论: 可靠性是协议层的产物, UDP + seq/ack + 超时重传 = 简易 TCP")


if __name__ == "__main__":
    main()
```

**追问**:1) 重传间隔怎么定?——固定短间隔会放大网络抖动,应该指数退避加抖动,并区分 '首包超时' 与 '重传超时';有 RTT 样本时用 SRTT 加四倍偏差,这正是 TCP RTO 的思路。2) 停等 ARQ 与 TCP 的差距在哪几个维度?——停等每 RTT 一包(吞吐=包/RTT);TCP 滑动窗口流水线、累积确认、快速重传(3 个重复 ACK)、拥塞控制;UDP 可靠层的进化路线就是按 TCP 的清单补课(Q700/Q1602)——「知道差距在哪」比「能写停等」更重要。3) 重传间隔的 SRTT 公式怎么落地?——采样 RTT→SRTT=α·旧+ (1-α)·新→RTO=SRTT+4·RTTVAR;无样本时用保守初值+指数退避;Karn 算法:重传包的 RTT 不采样(分不清是原包还是重传包的 ACK)——这三个细节是 UDP 可靠层的专业分界。4) 生产陷阱?——固定短间隔重传(抖动放大);重传无上限(风暴);重传包 ACK 不区分(采样污染);序号空间用尽不回绕处理;ACK 丢失的重复交付没去重(Q1329 的去重)。


---
