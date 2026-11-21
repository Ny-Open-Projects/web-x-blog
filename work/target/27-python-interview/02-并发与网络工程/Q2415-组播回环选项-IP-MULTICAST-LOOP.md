---
title: [Q2415] 组播回环选项 IP_MULTICAST_LOOP
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2415 · 组播回环选项 IP_MULTICAST_LOOP

> 难度:★★★ | 标签:组播, IP_MULTICAST_LOOP, 回环

**问**:组播联调时本机订阅者收不到包,第一个该查什么?

**答**:查 IP_MULTICAST_LOOP:它决定发出的组播包是否喂回本机,回环关了,同机一个订阅者都收不到,而remote 侧完全正常——同机联调最容易踩的坑。

- 实测 LOOP=1:同机两个订阅者同时收到同一份数据;

- 实测 LOOP=0:两个订阅者全部收不到,包只往网外走;

- 选项长在发送 socket 上,getsockopt 可读,实测关掉后读回 0;

- 配套三件套一起记:IP_MULTICAST_IF 指定出口网卡、IP_MULTICAST_TTL 控制跨越路由器跳数、SO_REUSEPORT 让同机多进程各自收到副本。

```python
# file: code/02_并发与网络工程/q2415_multicast_loop.py
# -*- coding: utf-8 -*-
"""组播回环选项 IP_MULTICAST_LOOP: 这一开关决定本机收不收得到。

- LOOP=1 时, 发出去的组播包会喂回本机所有加入该组的 socket;
- LOOP=0 是给"发送者不在订阅者之列"的场景省一份回环拷贝;
- 同机联调最容易踩的坑: 把 LOOP 关了, 然后怀疑组播坏了。
"""
import socket
import struct
import time

GROUP = "239.255.0.250"
PORT = 24150
IFACE = "127.0.0.1"


def make_receiver(name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    except OSError:
        pass                                     # 平台没有就靠 SO_REUSEADDR
    s.bind(("", PORT))
    mreq = struct.pack("4s4s", socket.inet_aton(GROUP), socket.inet_aton(IFACE))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    s.settimeout(1.0)
    return s, name


def make_sender(loop_on):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(IFACE))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1 if loop_on else 0)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    return s


def drain(s):
    got = []
    while True:
        try:
            got.append(s.recv(64))
        except socket.timeout:
            return got


def main():
    rx1, _ = make_receiver("订阅者甲")
    rx2, _ = make_receiver("订阅者乙")
    time.sleep(0.05)                             # 等成员关系生效

    # 场景一: LOOP=1, 本机订阅者应收得到
    tx = make_sender(loop_on=True)
    time.sleep(0.05)
    tx.sendto(b"loop-on", (GROUP, PORT))
    got1, got2 = drain(rx1), drain(rx2)
    print("LOOP=1: 甲收到 %s, 乙收到 %s" % (got1, got2))
    assert b"loop-on" in got1 and b"loop-on" in got2, "回环开, 本机订阅者必须收到"

    # 场景二: LOOP=0, 同机的订阅者全部收不到
    tx.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 0)
    time.sleep(0.05)
    tx.sendto(b"loop-off", (GROUP, PORT))
    got1, got2 = drain(rx1), drain(rx2)
    print("LOOP=0: 甲收到 %s, 乙收到 %s" % (got1, got2))
    assert got1 == [] and got2 == [], "回环关, 本机一个订阅者都收不到"

    # 读回选项, 证明它确实长在 socket 上
    cur = tx.getsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP)
    print("发送 socket 当前的 LOOP 值:", cur)
    assert cur == 0
    tx.close(); rx1.close(); rx2.close()


if __name__ == "__main__":
    main()
```

**追问**:1) LOOP 开着会重复收吗?——每个加入组的不同 socket 各收一份,这正是同机多实例测试的期望行为。2) TTL 设 0 会怎样?——包不出本机但回环仍在,常见于纯本机组播,跨网段必须 TTL 至少 1。3) IP_MULTICAST_LOOP 的语义与适用场景?——LOOP=1 发出的包喂回本机所有加入组的 socket(同机多实例测试的期望行为);LOOP=0 给「发送者不是订阅者」的场景省一份回环拷贝——「选项长在发送 socket 上」,收发两端配错就出现「同机收不到、remote 正常」的经典联调坑。4) 组播选项四件套怎么记?——LOOP(回环)、IF(出口网卡)、TTL(跨路由跳数,0=纯本机,1=本网段)、SO_REUSEPORT(同机多进程各自收副本)——四件套都要 getsockopt 读回验证(Q1600 模板)。5) 生产陷阱?——LOOP 关了怀疑组播坏了(第一排查点);TTL=0 跨网段(包不出本机);SO_REUSEPORT 缺失(macOS 多路同收失败,Q2147);IF 指错网卡(包走错出口);组地址非管理域段(冲突)。

---
