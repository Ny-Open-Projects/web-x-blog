---
title: [Q1592] 半开连接检测:写超时、keepalive 与应用层探活
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1592 · 半开连接检测:写超时、keepalive 与应用层探活

> 难度:★★★★ | 标签:半开连接, keepalive, 探活

**问**:对端主机断电了,我这端的 TCP 连接会有什么表现?怎么发现?

**答**:什么表现都没有——这正是半开的欺骗性:对端没机会发 FIN 或 RST,你这端 send 照样成功(数据只是进了本地内核缓冲)。三条探测路径:写探测——持续写直到内核缓冲堆满,send 阻塞或超时,写不动是对端不收的直接证据;TCP keepalive——空闲后内核代发探测帧,连续无 ACK 判死,但默认 2 小时太迟,必须调空闲间隔;应用层心跳——自定义 PING 帧加超时,语义最可控,还能区分网络差与对端死。对照:对端正常关闭时 recv 返回空字节串,那是干净下线,不是半开。

```python
# file: code/02_并发与网络工程/q1592_halfopen_detect.py
"""半开连接检测: 写超时、keepalive 与应用层探活。

"半开"= 一端以为连接活着, 另一端其实已经消失(主机断电、网络静默丢弃)。
内核不帮你发现它, 三条探测路径:
- 写探测: 本地 send 只是进内核缓冲, 对端收不动时缓冲堆满, 写阻塞/超时;
- TCP keepalive: 空闲后内核代发探测包, 连续无 ACK 才判死(默认 2 小时, 必须调参);
- 应用层心跳: 自己定义 PING 帧 + 超时, 语义最可控。
"""
import socket
import threading
import time


def serve(srv, stop, mode):
    srv.listen(5)
    while not stop.is_set():
        try:
            conn, _ = srv.accept()
        except OSError:
            break
        if mode == "silent":
            # 收下连接后永不读、永不关: fd 挂着, 不发 FIN -> 模拟对端失联
            continue
        # fin 模式: 读一条就正常关闭, 客户端 recv 会拿到 b""
        try:
            conn.recv(4096)
        except OSError:
            pass
        conn.close()


def start_server(mode):
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if mode == "silent":
        # 小接收缓冲: 让"对端不读"更快把客户端堵死
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 8192)
    srv.bind(("127.0.0.1", 0))
    port = srv.getsockname()[1]
    stop = threading.Event()
    threading.Thread(target=serve, args=(srv, stop, mode), daemon=True).start()
    return srv, port, stop


def probe_write_stall(port):
    """写探测: 对端不收 -> 本地缓冲堆满 -> send 超时。"""
    s = socket.create_connection(("127.0.0.1", port), timeout=1.0)
    s.settimeout(0.3)
    total = 0
    stalled = False
    try:
        while total < 8 * 1024 * 1024:
            s.sendall(b"x" * 65536)
            total += 65536
    except (socket.timeout, OSError):
        stalled = True              # 写不动了 = 对端不再接收
    s.close()
    return total, stalled


def probe_fin(port):
    """FIN 探测: 对端正常关闭, recv 返回 b"" —— 这是干净的下线。"""
    s = socket.create_connection(("127.0.0.1", port), timeout=1.0)
    s.settimeout(1.0)
    s.sendall(b"hi")
    tail = s.recv(1024)
    s.close()
    return tail


def probe_keepalive_options():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    if hasattr(socket, "TCP_KEEPALIVE"):        # macOS
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPALIVE, 5)
    if hasattr(socket, "TCP_KEEPIDLE"):         # Linux
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 5)
    on = s.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)
    s.close()
    return on


def main():
    srv_s, port_s, stop_s = start_server("silent")
    srv_f, port_f, stop_f = start_server("fin")

    total, stalled = probe_write_stall(port_s)
    print("写探测: 已成功写入 %.0fKB 后写超时 -> 判定对端失联" % (total / 1024))
    assert stalled, "对端不读时写必然最终超时"
    assert total > 0, "超时前本地写入应当先成功(半开的欺骗性)"

    tail = probe_fin(port_f)
    print("FIN 探测: recv 返回 %r -> 对端正常关闭" % tail)
    assert tail == b"", "正常关闭应读到 EOF"

    on = probe_keepalive_options()
    print("keepalive 已开启:", bool(on), "(生产要调空闲探测间隔, 默认 2 小时太久)")
    assert on != 0, "SO_KEEPALIVE 应为开启状态"

    stop_s.set()
    stop_f.set()
    srv_s.close()
    srv_f.close()
    print("结论: 写超时是'对端不收'的证据, b'' 是'对端告别'的证据, 心跳兜住其余")


if __name__ == "__main__":
    main()
```

**追问**:1) keepalive 探测间隔设多少?——经验是空闲 30-120s 起探、间隔 5-10s、3 次失败判死;探测只在内核层,踢会话、转移等业务语义仍要应用层自己做。2) 半开探测的三条路径怎么分工?——写探测最直接但浪费带宽且慢(要堆满缓冲);keepalive 自动但平台参数繁琐且语义粗(只能判「链路死」);应用层心跳最可控(区分「网络差」与「对端死」、可带业务语义)——生产组合:心跳为主判据,keepalive 调参兜底,写超时做最后防线。3) 判死之后的动作清单?——close socket(释放 fd)、从注册表摘除、触发重连(带退避抖动)、未确认请求标记失败或转交重试——判死只是起点,恢复链路(Q623 状态机)才是完整答案。4) 生产陷阱?——把「send 成功」当「对端收到」(数据只在本地缓冲);keepalive 默认 2h 没调参,半开连接占资源数小时;判死误杀(高丢包网络下心跳超时阈值太紧);close 时残留未读数据变 RST,对端看到 reset 而不是 EOF(Q1608 的服务端注意点)。

---
