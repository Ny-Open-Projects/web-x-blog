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
