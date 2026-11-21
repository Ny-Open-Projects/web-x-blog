"""连接超时与读超时的定位实验: 回环 socket 三场景(纯标准库)。"""
import socket
import threading
import time


def read_timeout_demo():
    """对端 accept 后装死: 连接建立成功但 recv 等不到数据 -> 读超时。"""
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))
    srv.listen(1)
    port = srv.getsockname()[1]
    conns = []

    def server():
        conn, _ = srv.accept()
        conns.append(conn)                       # 收下连接但永不响应
    worker = threading.Thread(target=server, daemon=True)
    worker.start()

    cli = socket.socket()
    cli.settimeout(0.5)
    cli.connect(("127.0.0.1", port))
    t0 = time.perf_counter()
    try:
        cli.recv(1024)
        outcome, kind = "意外收到数据", "ok"
    except socket.timeout:
        outcome, kind = "读超时: 连接已建立但对端不吐数据", "read-timeout"
    elapsed = time.perf_counter() - t0
    cli.close()
    if conns:
        conns[0].close()
    srv.close()
    worker.join(1)
    return kind, outcome, elapsed


def connect_refused_demo():
    """端口没有监听: 内核立即回 RST -> 快速失败而不是超时。"""
    probe = socket.socket()
    probe.bind(("127.0.0.1", 0))
    dead_port = probe.getsockname()[1]
    probe.close()
    cli = socket.socket()
    cli.settimeout(0.5)
    try:
        cli.connect(("127.0.0.1", dead_port))
        cli.close()
        return "意外连通"
    except ConnectionRefusedError:
        return "连接拒绝: 端口无监听, 立即失败而非超时"
    except socket.timeout:
        return "连接超时"


def connect_timeout_demo():
    """不可路由地址: SYN 无应答 -> 超时发生在 connect 阶段。"""
    cli = socket.socket()
    cli.settimeout(0.5)
    try:
        cli.connect(("10.255.255.1", 81))        # 演示用私网黑洞地址
        cli.close()
        return "意外连通"
    except socket.timeout:
        return "连接超时: SYN 无应答, 卡在 connect 阶段"
    except OSError as exc:
        return "网络不可达快速失败: {}".format(exc)


kind, outcome, elapsed = read_timeout_demo()
print("场景一 {:6s} 耗时 {:.2f}s -> {}".format(kind, elapsed, outcome))
assert kind == "read-timeout"
assert 0.4 <= elapsed <= 2.0, "读超时应在 settimeout 附近触发"

print("场景二 ->", connect_refused_demo())
print("场景三 ->", connect_timeout_demo())

print("定位口诀:")
print("  立即 ConnectionRefused -> 端口没监听, 进程挂了或没启动")
print("  卡在 connect 后超时   -> 网络丢包或防火墙 DROP, 查路由与安全组")
print("  连接成功后读超时      -> 上游挂起, 查慢查询 持锁 与死循环")
print("  网关报 502 或 504     -> 对照上游日志确认是拒绝服务还是等超时")
print("要点: 两类超时是两种病, connect 超时指向网络链路, read 超时指向应用挂起; "
      "连接拒绝不超时, 说明请求根本没到达对端应用")
