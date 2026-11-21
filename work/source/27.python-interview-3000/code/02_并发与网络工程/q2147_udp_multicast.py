# -*- coding: utf-8 -*-
"""UDP 组播与广播: 一对多发送。

- 组播: 加入组 239.255.0.1 的所有 socket 都收到同一份数据, 一发多收;
- macOS 回环要点: 收发两端都把接口设成 127.0.0.1, LOOP=1 让本机也收到;
- 广播在 macOS 回环上不可达, 是实测出来的平台差异。
"""
import socket
import struct
import threading
import time

GROUP = "239.255.0.1"
IFACE = "127.0.0.1"


def receiver(tag, port, out):
    rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rx.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        rx.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    except (AttributeError, OSError):
        pass                            # BSD/macOS 需它才能多路同收
    rx.bind(("", port))
    mreq = socket.inet_aton(GROUP) + socket.inet_aton(IFACE)
    rx.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    rx.settimeout(2.0)
    try:
        data, addr = rx.recvfrom(2048)
        out[tag] = (data, addr)
    except socket.timeout:
        out[tag] = None
    finally:
        rx.close()


def main():
    port = 23991
    out = {}
    ts = [threading.Thread(target=receiver, args=(tag, port, out))
          for tag in ("r1", "r2")]
    for t in ts:
        t.start()
    time.sleep(0.2)                    # 两个接收者都入组

    tx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tx.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF,
                  socket.inet_aton(IFACE))
    tx.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
    tx.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    tx.sendto(b"mcast-hello", (GROUP, port))
    for t in ts:
        t.join(3)
    tx.close()

    for tag in ("r1", "r2"):
        got = out.get(tag)
        print("%s 收到: %s" % (tag, got[0].decode() if got else "超时"))
    both = all(out.get(tag) for tag in ("r1", "r2"))
    print("一对多成立:", both, "-> 同一份数据, 组内全员可达")

    # 广播对照: macOS 回环实测不可达
    rx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rx.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    rx.bind(("", 23992))
    rx.settimeout(1.0)
    bc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    try:
        bc.sendto(b"bcast-probe", ("127.255.255.255", 23992))
        send_ok = True
    except OSError:
        send_ok = False
    got = None
    try:
        got, _ = rx.recvfrom(2048)
    except socket.timeout:
        pass
    print("广播 127.255.255.255: 发送 %s, 回环接收 %s" %
          ("成功" if send_ok else "失败",
           got.decode() if got else "超时"))
    bc.close()
    rx.close()
    print("结论: 应用层一对多用组播, 广播留给 ARP/发现类协议")


if __name__ == "__main__":
    main()
