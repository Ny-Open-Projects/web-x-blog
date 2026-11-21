# -*- coding: utf-8 -*-
"""TCP 服务端完整骨架: 绑定 -> 监听 -> 接受 -> 处理 -> 关闭。

- SO_REUSEADDR: 重启不必等 TIME_WAIT 散场;
- bind 端口 0: 内核分配空闲端口, 演示永不端口冲突;
- 每连接一个 daemon 线程, 单连接崩溃在 handler 内被隔离;
- 停机: accept 循环用短超时轮询停止位, 干净退出。
"""
import socket
import threading
import time


def wait_port(port, timeout=5.0):
    """端口就绪等待: 循环 connect 直到成功或超时。"""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True             # 这条探测连接也会被服务端 accept
        except OSError:
            time.sleep(0.05)
    return False


def handle(conn):
    """单连接处理: 行协议回显, 任何异常都隔离在本连接内。"""
    try:
        conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        buf = b""
        while True:
            data = conn.recv(1024)
            if not data:                # EOF: 对端半关闭, 收尾
                break
            buf += data
            while b"\n" in buf:
                line, buf = buf.split(b"\n", 1)
                conn.sendall(b"echo:" + line.upper() + b"\n")
    except OSError:
        pass                            # 单连接的网络错误不拖垮服务
    finally:
        conn.close()


def main():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))          # 端口 0: 内核分配
    srv.listen(64)                      # backlog: 全连接队列长度
    port = srv.getsockname()[1]
    srv.settimeout(0.1)                 # accept 短超时, 为停机让路
    print("listening on 127.0.0.1:%d" % port)

    stop = threading.Event()
    served = [0]

    def accept_loop():
        while not stop.is_set():
            try:
                conn, addr = srv.accept()
            except socket.timeout:
                continue                # 超时醒来检查停止位
            served[0] += 1
            threading.Thread(target=handle, args=(conn,), daemon=True).start()

    acc = threading.Thread(target=accept_loop, daemon=True)
    acc.start()
    wait_port(port)                     # 服务端就绪前客户端不出手

    for i in range(3):                  # 3 个客户端依次对话
        with socket.create_connection(("127.0.0.1", port), timeout=2) as c:
            c.settimeout(2)
            c.sendall(("hello-%d\n" % i).encode())
            resp = b""
            while not resp.endswith(b"\n"):
                chunk = c.recv(256)
                if not chunk:
                    break
                resp += chunk
            print("client %d got %r" % (i, resp.decode().strip()))

    stop.set()                          # 停机: 先停收, 再关监听
    acc.join(timeout=2)
    srv.close()
    print("served %d connections (含 1 条端口就绪探测)" % served[0])
    print("要点: 复用地址防 TIME_WAIT, 短超时 accept 让停机可控")


if __name__ == "__main__":
    main()
