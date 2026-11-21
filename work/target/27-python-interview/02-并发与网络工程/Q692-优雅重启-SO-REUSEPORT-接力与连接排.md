---
title: [Q692] 优雅重启:SO_REUSEPORT 接力与连接排水
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q692 · 优雅重启:SO_REUSEPORT 接力与连接排水

> 难度:★★★★ | 标签:SO_REUSEPORT, 优雅重启, 零停机

**问**:发新版怎么做到"不拒绝任何请求"?SO_REUSEPORT 方案的全流程是什么?

**答**:SO_REUSEPORT 允许多个 socket 绑定同一端口,内核对新连接做负载分配,这是零停机重启的钥匙:新版本先启动并绑定同端口(与旧版共存),然后旧版关闭自己的监听 socket(新连接全进新版),旧版排水——等存量连接处理完(或超时强制断),最后退出。对比传统方案:kill+重启有连接损失窗口;fork/exec 继承 socket(Q692 的另一变体)单机可用但难滚动多版本。注意点:新旧版本必须协议兼容(客户端无感知);排水超时要与 LB/K8s 摘流配合;macOS/Linux 均支持 REUSEPORT 但行为细节略有差异。

```python
# file: code/02_并发与网络工程/q692_graceful_restart.py
import socket
import threading
import time

SO_REUSEPORT = getattr(socket, "SO_REUSEPORT", 15)
keeping = [True, True]  # v1, v2 存活标志


def make_listener(port: int) -> socket.socket:
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, SO_REUSEPORT, 1)  # 关键: 允许共存绑定
    s.bind(("127.0.0.1", port))
    s.listen(8)
    return s


def serve_version(tag: str, listener: socket.socket, active: list,
                  keep_flag_idx: int) -> None:
    listener.settimeout(0.2)
    while keeping[keep_flag_idx]:
        try:
            conn, _ = listener.accept()
        except socket.timeout:
            continue
        active.append(conn)
        print(f"[v{tag}] 接受连接 (活跃 {len(active)})")
        threading.Thread(target=handle, args=(tag, conn, active), daemon=True).start()


def handle(tag: str, conn: socket.socket, active: list) -> None:
    conn.settimeout(3)
    try:
        data = conn.recv(64)
        time.sleep(0.3)  # 模拟处理
        conn.sendall(f"answered-by-v{tag}:{data.decode()}".encode())
    except OSError:
        pass
    finally:
        if conn in active:
            active.remove(conn)
        conn.close()


if __name__ == "__main__":
    # 1. v1 上线
    active_v1: list = []
    l1 = make_listener(0)
    port = l1.getsockname()[1]
    t1 = threading.Thread(target=serve_version, args=("1", l1, active_v1, 0), daemon=True)
    t1.start()
    time.sleep(0.1)

    # 2. 客户端 A 连到 v1
    a = socket.create_connection(("127.0.0.1", port))
    print("[client-a] 连接建立 (落在 v1)")

    # 3. v2 上线: 与 v1 共存绑定
    active_v2: list = []
    l2 = make_listener(port)
    t2 = threading.Thread(target=serve_version, args=("2", l2, active_v2, 1), daemon=True)
    t2.start()
    time.sleep(0.1)
    print("[deploy] v2 已共存绑定同端口")

    # 4. v1 停止接受: 关闭监听, 新连接只会到 v2
    keeping[0] = False
    l1.close()
    t1.join(timeout=1)
    print("[deploy] v1 停止接受新连接, 进入排水")

    # 5. 新客户端 B → 必然落在 v2
    b = socket.create_connection(("127.0.0.1", port))
    b.sendall(b"new-request")
    print("[client-b]", b.recv(64).decode(), "← 新流量已切到 v2")

    # 6. 客户端 A 的请求由 v1 排水完成
    a.sendall(b"old-request")
    print("[client-a]", a.recv(64).decode(), "← 存量连接由 v1 优雅处理完")
    a.close()
    b.close()
    keeping[1] = False
    l2.close()
    print("零停机重启完成: 全程无连接被拒绝")
```

**追问**:1) 排水多久算合理?——覆盖 p99 请求时长 + 心跳周期余量;K8s 里等于 terminationGracePeriodSeconds 减去 preStop 摘流等待,典型 30-60s,超时后强杀是兜底不是常态。2) 排水期间存量连接怎么处理?——停接新连接后存量请求服务到完成;推送类长连接发「服务下线通知」让客户端带抖动重连到新版(Q623);排水超时强断是兜底不是常态——目标是「不丢请求」不是「无限等」。3) 与 K8s 滚动更新怎么配合?——SIGTERM/preStop 里先等 readiness 摘流生效(约探针间隔时长)再排水;terminationGracePeriodSeconds 覆盖全程;漏了摘流等待就是「实例退出了但 LB 还在发流量」。4) 生产陷阱?——REUSEPORT 共存期新旧版本协议不兼容,客户端收到混合行为;关闭监听的时序不对,REUSEPORT 内核分流下旧版仍收新连接;排水只管 HTTP 请求,WS/SSE 长连接被强断。

---
