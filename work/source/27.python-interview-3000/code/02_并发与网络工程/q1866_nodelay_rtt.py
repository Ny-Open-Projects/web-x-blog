# -*- coding: utf-8 -*-
"""TCP_NODELAY 延迟实测方法论: 回环上的真相与设置读写验证。

- 回环 ping-pong RTT 实测: 127.0.0.1 往返约 0.1ms, ACK 立即返回;
- 回环上 nodelay on/off 中位数无差异: Nagle 需要真实网络 RTT 才有"攒包"窗口;
- TCP_NODELAY 必须用 getsockopt 读回验证, 写了没生效是常见事故;
- 教学点: 在错误环境做延迟实验, 会得出错误结论。
"""
import socket
import threading
import time


def wait_port(port, timeout=3.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return
        except OSError:
            time.sleep(0.05)
    raise RuntimeError("端口未就绪")


def start_echo_server():
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    srv.listen(5)

    def serve():
        srv.settimeout(0.2)
        while True:
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            conn.settimeout(3.0)

            def pump(c):
                try:
                    while True:
                        data = c.recv(4096)
                        if not data:
                            break
                        c.sendall(data)
                except OSError:
                    pass
                c.close()

            threading.Thread(target=pump, args=(conn,), daemon=True).start()

    threading.Thread(target=serve, daemon=True).start()
    port = srv.getsockname()[1]
    wait_port(port)
    return port


def pingpong_rtt(port, nodelay, rounds=200, wwr=False):
    c = socket.socket()
    c.connect(("127.0.0.1", port))
    c.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY,
                 1 if nodelay else 0)
    readback = c.getsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY)
    # Darwin 读回的是位掩码(开启时为 4), Linux 读回 1/0, 非零即生效
    assert (readback != 0) == nodelay, "TCP_NODELAY 设置必须读回验证"
    c.settimeout(3.0)
    rtts = []
    for _ in range(rounds):
        t0 = time.perf_counter()
        if wwr:
            c.sendall(b"a")
            c.sendall(b"b")               # 背靠背两次小写, Nagle 的经典靶子
            got = b""
            while len(got) < 2:           # 两次回包可能被服务端一次读完合并发出
                got += c.recv(2 - len(got))
            assert got == b"ab"
        else:
            c.sendall(b"p")
            assert c.recv(1) == b"p"
        rtts.append(time.perf_counter() - t0)
    c.close()
    rtts.sort()
    return rtts[len(rtts) // 2], rtts[int(len(rtts) * 0.99)]


def main():
    port = start_echo_server()
    print("本机回环 ping-pong 实测, 每组 200 轮:")
    medias = {}
    for nodelay in (False, True):
        med, p99 = pingpong_rtt(port, nodelay, 200, wwr=False)
        medias[nodelay] = med
        print("  nodelay=%-5s 中位 RTT %.3fms  p99 %.3fms" % (nodelay, med * 1000, p99 * 1000))
    assert medias[True] < 0.002, "回环 nodelay 开启时 RTT 应在毫秒内"
    assert medias[False] < 0.002, "回环上关闭 nodelay 也不该慢"

    print("背靠背两写一读(触发 Nagle 攒包的模式):")
    for nodelay in (False, True):
        med, p99 = pingpong_rtt(port, nodelay, 100, wwr=True)
        print("  nodelay=%-5s 中位 RTT %.3fms  p99 %.3fms" % (nodelay, med * 1000, p99 * 1000))

    print("结论: 回环 ACK 即时, Nagle 无在途小段可攒, on/off 无差异;")
    print("      真实网络上第二写才会被扣 40ms+, 这就是交互式服务必开 NODELAY 的原因")


if __name__ == "__main__":
    main()
