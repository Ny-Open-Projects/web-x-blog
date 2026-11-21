---
title: [Q1311] errno 分诊:连接失败的六种死法
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1311 · errno 分诊:连接失败的六种死法

> 难度:★★★☆ | 标签:errno, 排障, socket

**问**:connect 失败了,你怎么区分"服务没起"、"对端崩了"和"链路不通"?各自的 errno 和处置动作是什么?

**答**:异常类型本身就是分诊表。ConnectionRefusedError(ECONNREFUSED)=目标 IP 可达但端口没人监听,处置是查服务进程;ConnectionResetError(ECONNRESET)=连上了但被对端粗暴掐断,典型是进程崩溃或 SO_LINGER 零秒关闭,处置是看对端日志;socket.timeout=超时,可能链路丢包也可能负载过高;ConnectionAbortedError、BrokenPipeError 是写入方向的另一组死法;EHOSTUNREACH/ENETUNREACH 则是路由层问题。排障脚本的第一要务是把 OSError 翻译成"哪一层、谁该动"的结论,而不是只打一句"连接失败"。下面的演示在回环上真实制造拒绝、重置、读超时三种现场并逐一分诊。两个时序细节:RST 可能快于 connect 返回,create_connection 自身就会抛 ECONNRESET,捕获要覆盖 connect 与 recv 两处;loopback 上"监听但不 accept"的端口握手照样完成,connect 阶段造不出超时现场,超时演示要落在读阶段。

```python
# file: code/02_并发与网络工程/q1311_errno_triage.py
import errno
import socket
import struct
import threading
import time


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def connect(host: str, port: int, timeout: float = 0.5):
    """返回 (诊断结论, socket 或 None)。"""
    try:
        s = socket.create_connection((host, port), timeout=timeout)
        return "OK 已连通", s
    except ConnectionRefusedError:
        return "ECONNREFUSED 端口没人监听, 去查服务进程", None
    except ConnectionResetError:
        return "ECONNRESET 对端重置连接, 查对端崩溃日志", None
    except socket.timeout:
        return "TIMEOUT 链路或负载问题, 先 ping 再看监控", None
    except OSError as exc:
        code = errno.errorcode.get(exc.errno, "UNKNOWN")
        return f"{code} 路由/防火墙层问题: {exc}", None


def main() -> None:
    # 现场一: 端口没人监听
    dead_port = free_port()
    verdict, _ = connect("127.0.0.1", dead_port)
    print(f"拒绝现场   -> {verdict}")

    # 现场二: 接受后立刻 SO_LINGER 零秒关闭, 制造 RST
    reset_port = free_port()
    ready = threading.Event()
    def rst_server():
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", reset_port))
        srv.listen(1)
        ready.set()
        conn, _ = srv.accept()
        time.sleep(0.05)  # 等客户端 create_connection 返回, RST 落在 recv 阶段
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                        struct.pack("ii", 1, 0))   # 关闭即发 RST
        conn.close()
        srv.close()
    threading.Thread(target=rst_server, daemon=True).start()
    ready.wait(1)
    cli = None
    try:
        cli = socket.create_connection(("127.0.0.1", reset_port), timeout=0.5)
    except ConnectionResetError:
        # 时序残留: RST 快于 connect 返回时, create_connection 自身就会抛
        print("重置现场   -> connect 即抛 ECONNRESET, 对端 RST 而非优雅关闭")
    if cli is not None:
        try:
            data = cli.recv(64)
            print(f"重置现场   -> recv 返回 {data!r} (RST 未及, 按优雅关闭观察)")
        except ConnectionResetError:
            print("重置现场   -> recv 抛 ECONNRESET, 对端 RST 而非优雅关闭")
        cli.close()

    # 现场三: 接受后不回话, 客户端读阶段超时
    # (loopback 上 listening-but-not-accepting 的端口握手照样完成,
    #  connect 阶段造不出超时, 超时分诊演示落在读阶段)
    silent_port = free_port()
    ready2 = threading.Event()
    def silent_server():
        srv = socket.socket()
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", silent_port))
        srv.listen(1)
        ready2.set()
        conn, _ = srv.accept()
        time.sleep(1.0)                 # 故意不回复
        conn.close()
        srv.close()
    threading.Thread(target=silent_server, daemon=True).start()
    ready2.wait(1)
    cli = socket.create_connection(("127.0.0.1", silent_port), timeout=0.5)
    cli.settimeout(0.3)
    t0 = time.monotonic()
    try:
        cli.recv(64)
        print("超时现场   -> (对端提前回话, 现场未复现)")
    except socket.timeout:
        dt = (time.monotonic() - t0) * 1000
        print(f"超时现场   -> socket.timeout 读超时 ({dt:.0f}ms), 链路或负载问题, 先 ping 再看监控")
    cli.close()

    # 正常对照
    good_port = free_port()
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", good_port))
    srv.listen(1)
    threading.Thread(target=lambda: srv.accept()[0].close(), daemon=True).start()
    verdict, cli = connect("127.0.0.1", good_port)
    print(f"正常现场   -> {verdict}")
    cli.close()
    srv.close()


if __name__ == "__main__":
    main()
```

**追问**:1) ECONNRESET 和 EOF(recv 返回空串)怎么区分?——前者是 RST:对端异常终止,未读数据直接丢弃;后者是 FIN:对端走完关闭流程,数据已送达;前者该告警重试,后者是正常语义。2) RST 快于 connect 返回是什么场景?——对端收到 SYN 直接回 RST 时,ConnectionRefusedError 在 connect 调用内就抛出;而「连上后被 reset」发生在后续读写;两者病因不同(端口没人监听 vs 进程崩溃/中间设备掐断),分诊表要把时序也算进去。3) 六种死法分别归谁处置?——ECONNREFUSED 归服务部署(端口没监听);ECONNRESET 归对端稳定性(日志);timeout 归网络/容量(丢包或过载,Q665);EHOSTUNREACH/ENETUNREACH 归路由与防火墙;BrokenPipeError 归「对端已死还写」的代码缺陷(先处理 EOF 再写);EADDRNOTAVAIL 归本机配置(Q1319)。4) 生产陷阱?——统一 except OSError 一把抓,分诊信息全丢;把 reset 一律当网络抖动重试(对端可能已把业务做成一半,重试要幂等 Q706);超时上限缺失,排障脚本自身挂死。

---
