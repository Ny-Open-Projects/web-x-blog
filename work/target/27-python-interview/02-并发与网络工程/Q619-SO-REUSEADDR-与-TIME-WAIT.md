---
title: [Q619] SO_REUSEADDR 与 TIME_WAIT
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q619 · SO_REUSEADDR 与 TIME_WAIT

> 难度:★★★☆ | 标签:SO_REUSEADDR, TIME_WAIT, 重启

**问**:服务重启时报 Address already in use,过几分钟又好了,为什么?

**答**:主动关闭的一方会进入 TIME_WAIT(默认 2MSL,约 1-4 分钟),期间五元组占着端口;重启后 bind 同一端口没有 SO_REUSEADDR 就会被拒。SO_REUSEADDR 允许绑定处于 TIME_WAIT 的地址(不等于允许多个活跃 socket 同时监听,那是 SO_REUSEPORT)。更工程的做法:让对端/客户端先关(把 TIME_WAIT 留在客户端),或用 SO_LINGER 控制,或服务端用 SO_REUSEADDR + 重试绑定。TIME_WAIT 本身是保护旧报文不污染新连接的机制,不要试图"消灭"它。

```python
# file: code/02_并发与网络工程/q619_reuseaddr.py
import socket
import time


def main() -> None:
    # 1. 建立连接, 服务端主动关闭 → 服务端侧进入 TIME_WAIT
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))  # 内核分配空闲端口, 避免与系统其他服务撞车
    port = srv.getsockname()[1]
    srv.listen(1)

    c = socket.socket()
    c.connect(("127.0.0.1", port))
    conn, _ = srv.accept()
    conn.close()          # 服务端先关: TIME_WAIT 留在服务端
    c.close()
    time.sleep(0.1)
    srv.close()           # 关键: 先彻底关闭监听 socket, 现场只留 TIME_WAIT;
                          # 监听 socket 还活着就去重绑, 任何平台都会 EADDRINUSE

    # 2. 不带 SO_REUSEADDR 重新绑定 → 撞 TIME_WAIT, 大概率 EADDRINUSE
    s1 = socket.socket()
    try:
        s1.bind(("127.0.0.1", port))
        print("无 REUSEADDR: 绑定成功 (本平台/此刻 TIME_WAIT 未阻塞)")
        s1.close()
    except OSError as e:
        print(f"无 REUSEADDR: 绑定失败 {e} → 这就是重启报错的原因")

    # 3. 带 SO_REUSEADDR → 立即成功
    s2 = socket.socket()
    s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s2.bind(("127.0.0.1", port))
    print("带 REUSEADDR: 绑定成功, 服务可以立即重启")
    s2.close()


if __name__ == "__main__":
    main()
```

**追问**:1) SO_REUSEADDR 和 SO_REUSEPORT 的区别?——前者允许抢占 TIME_WAIT 地址;后者(4.1 内核/macOS)允许多个 socket 同时监听同一端口并做内核级负载均衡,常用于优雅重启和多进程 accept。2) TIME_WAIT 为什么必须存在、能安全缩短吗?——它保证旧连接的迟到报文在网络中自然消亡,不污染复用同五元组的新连接;出站方向 tcp_tw_reuse(依赖时间戳)是合法手段,tcp_tw_recycle 在 NAT 下丢 SYN、已在 Linux 4.12 移除,是历史上著名的坑。3) 大量 TIME_WAIT 出现在哪一侧说明什么?——主动关闭方持有:服务端海量 TIME_WAIT 说明服务端在先关(短连接+没启用 keep-alive),正解是连接复用而不是调内核参数;客户端侧则是端口耗尽问题。4) 生产陷阱?——压测机 ip_local_port_range 范围内端口被 TIME_WAIT 占满,connect 报 EADDRNOTAVAIL;混淆 REUSEADDR(抢 TIME_WAIT 地址)与 REUSEPORT(多 socket 同监听)语义。

---
