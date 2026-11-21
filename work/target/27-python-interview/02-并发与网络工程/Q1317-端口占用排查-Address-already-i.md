---
title: [Q1317] 端口占用排查:Address already in use 的检查链
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1317 · 端口占用排查:Address already in use 的检查链

> 难度:★★☆☆ | 标签:EADDRINUSE, SO_REUSEADDR, 排障

**问**:服务起不来,报 `Address already in use`,你的排查链是什么?

**答**:三步。第一步,用 bind 探测确认端口确实被占——注意 bind 报 EADDRINUSE 和 EADDRNOTAVAIL 是两回事:前者是端口冲突,后者是本机根本没有那个地址(常见于机器换了网卡还在连旧配置)。第二步,找出占用者:macOS 用 lsof,Linux 用 ss/lsof,拿到 PID 再 ps 看进程身份,确认是"我自己的旧实例没死"还是"别人的服务"。第三步,处理:自己的旧实例就 kill;真要"快速重启"则给监听 socket 加 SO_REUSEADDR,它允许绑定处于 TIME_WAIT 的残留端口,但注意它不能让两个进程同时监听同一端口(那是 SO_REUSEPORT 的语义,且要求两边都设置)。下面的演示把整条检查链跑一遍。

```python
# file: code/02_并发与网络工程/q1317_port_in_use_triage.py
import errno
import os
import socket
import subprocess


def probe_bind(port: int) -> str:
    s = socket.socket()
    try:
        s.bind(("127.0.0.1", port))
        return "FREE 端口可用"
    except OSError as exc:
        if exc.errno == errno.EADDRINUSE:
            return "EADDRINUSE 已被占用"
        if exc.errno == errno.EADDRNOTAVAIL:
            return "EADDRNOTAVAIL 本机没有该地址, 检查网卡与配置"
        return f"其他错误 {errno.errorcode.get(exc.errno, exc.errno)}"
    finally:
        s.close()


def find_listener(port: int):
    """lsof 找监听进程, 返回 (pid, 进程名), 失败返回 None。"""
    try:
        out = subprocess.run(
            ["lsof", "-nP", "-iTCP:%d" % port, "-sTCP:LISTEN"],
            capture_output=True, text=True, timeout=5).stdout
        for line in out.splitlines()[1:]:     # 跳过表头
            parts = line.split()
            if len(parts) >= 2:
                return int(parts[1]), parts[0]
    except (OSError, ValueError):
        return None
    return None


def main() -> None:
    srv = socket.socket()
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", 0))
    port = srv.getsockname()[1]
    srv.listen(1)

    print(f"步骤一 bind 探测: {probe_bind(port)}")

    found = find_listener(port)
    if found:
        pid, name = found
        who = "就是我自己(旧实例嫌疑)" if pid == os.getpid() else name
        print(f"步骤二 lsof 定位: PID={pid} 进程={name} -> {who}")
        assert pid == os.getpid()
    else:
        print("步骤二 lsof 定位: 本机无 lsof 或无结果, 跳过(替代: ss -ltnp / netstat)")

    srv.close()
    print(f"关闭后 bind 探测: {probe_bind(port)}")
    print("SO_REUSEADDR 只救 TIME_WAIT 残留, 不等于允许双进程同端口(SO_REUSEPORT 才是)")


if __name__ == "__main__":
    main()
```

**追问**:1) SO_REUSEADDR 和 SO_REUSEPORT 的区别一句话?——前者解决"TIME_WAIT 残留挡住重绑",后者解决"多进程安全共享同一监听端口",两者常被混为一谈但语义完全不同。2) EADDRINUSE 与 EADDRNOTAVAIL 怎么区分处置?——前者端口被占(找占用者);后者地址不存在(网卡/IP 配置变化,常见于容器网络重建、机器换网卡),两种错误的排查方向完全不同。3) 占用者的三种典型身份?——自己的旧实例没死(部署脚本没做进程管理);别人的服务撞端口(配置冲突);僵尸进程/socket 残留(父进程退出但子进程仍监听);lsof/ss 拿 PID 后先看进程名与启动时间再动手。4) 生产陷阱?——盲目加 SO_REUSEADDR 掩盖双实例同时运行(两个实例都「成功」绑定的假象要警惕 REUSEPORT 混淆);kill 占用者前没确认身份(误杀别人服务);TIME_WAIT 大量堆积时反复重启服务,问题周期性复现(Q619)。

---
