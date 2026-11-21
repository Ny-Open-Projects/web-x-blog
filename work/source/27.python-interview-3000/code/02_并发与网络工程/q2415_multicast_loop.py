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
