---
title: [Q5527] mkfifo 命名管道：无亲缘进程间的流管道
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5527 · mkfifo 命名管道：无亲缘进程间的流管道

> 难度:★★★★ | 标签:mkfifo, FIFO, IPC

**问**：匿名管道（`pipe()`）只能父传子，怎么让两个**毫无亲缘**的进程走同一条流管道？FIFO 的 open 阻塞语义（读端等写端、写端等读端）是什么？和 socketpair、Unix 域 socket 怎么选型？无读者时非阻塞写打开为什么抛 ENXIO？

**答**：`os.mkfifo(path)` 在文件系统里创建一个**命名管道**（FIFO，`ls` 显示为 `p` 类型设备）：任何进程都能凭路径打开它，走和匿名管道完全一样的内核字节流。语义要点：1) **open 双向阻塞**——`open(path, "r")` 阻塞到有写者打开，`open(path, "w")` 阻塞到有读者打开；这是握手的一部分，不是 bug；2) **非阻塞打开的边界**——`O_RDWR` 打开永不再阻塞（自己读自己写，进程内自洽），而 `O_WRONLY|O_NONBLOCK` 在**无读者**时立即抛 `ENXIO`（"没有这个设备"），`O_RDONLY|O_NONBLOCK` 总能成功；3) **数据不落盘**——只进内核缓冲，读端不消费且缓冲满时写端阻塞（与匿名管道同，64KB 量级，Q2144/Q5525）；4) **生命周期两段分离**——unlink 前路径一直在，但读者/写者全部关闭后，未读数据直接丢弃（没有"存起来等下次"）。选型：同主机、需要**路径可见**（跨用户/跨容器可配）且只要单向流 → FIFO；亲缘进程 → 匿名管道/socketpair（Q2146）更简单（无路径、无权限面）；需要双向、多路复用、或 async（asyncio 的 open_connection 支持 Unix 域 socket 而不是 FIFO）→ Unix 域 socket（Q2139）。经典用法：日志采集器让任意进程 `echo > /var/run/app.fifo` 投递、shell 管道跨界、以及"命令行工具的进度流"。

```python
# file: code/02_并发与网络工程/q5527_fifo_demo.py
import os, tempfile, threading, time

d = tempfile.mkdtemp()
fifo = os.path.join(d, "bus.fifo")
os.mkfifo(fifo, 0o600)               # 文件系统出现一个 p 类型设备,仅属主可读写

def reader():
    with open(fifo, "r") as f:       # 阻塞直到有写者打开
        for line in f:
            print("读到:", line.strip())

t = threading.Thread(target=reader)
t.start()

with open(fifo, "w") as f:           # 阻塞直到有读者打开(此刻 reader 已挂起等待)
    for i in range(3):
        f.write(f"msg-{i}\n")
        f.flush()
        time.sleep(0.01)
# 写端 with 退出关闭 -> 读端读到 EOF,循环自然结束
t.join(2)

try:
    os.open(fifo, os.O_WRONLY | os.O_NONBLOCK)   # 无读者时非阻塞写打开
except OSError as e:
    print("无读者非阻塞写:", e)                   # ENXIO: 设备上无读写端配对

os.unlink(fifo)
print("FIFO: 路径是插座,流在内核;unlink 只拆插座,不影响已打开的连接")
```

**追问**：1) 为什么 `O_RDWR` 自打开不算"作弊"？——POSIX 允许（Linux/macOS 均支持），进程自己就是读写两端，永不必阻塞握手；但失去了"对端存在性"语义，服务端场景还是分开_RDONLY/__WRONLY 配对清晰。2) FIFO 能否被 `select/epoll` 监听？——能，FIFO 两端都是 fd，语义同管道；但"监听新连接"做不到（FIFO 没有连接概念，多写者共享一条流、数据交错按写序混合），要"每个客户端一条线"必须换 Unix 域 socket。3) `cat a.fifo | grep x` 这类 shell 用法为什么天然可用？（提示：FIFO 就是管道，shell 的重定向把它接进管线；注意写端不关则读者永远等 EOF——工具链里用 timeout/显式关闭收尾）

## 背诵要点
1. mkfifo = 文件系统里的命名管道：跨亲缘进程凭路径打开，open 时读端等写端、写端等读者。
2. `O_WRONLY|O_NONBLOCK` 无读者抛 ENXIO，`O_RDWR` 永不阻塞；数据只进内核缓冲不落盘，两端全关即丢弃。
3. 选型：路径可见的单向流用 FIFO；多连接/双向/异步用 Unix 域 socket；亲缘进程用匿名管道。

## 复盘追问
1. 采集器进程崩溃重启后，写进程阻塞在 `echo > fifo` 上——怎么办？（提示：写端阻塞说明"路径存在但无读者"；采集器要用 O_RDWR 自持一根常开的 fd 保证"永远有读者"，或写端带 O_NONBLOCK+ENXIO 降级队列）
2. 多个写进程同时向一个 FIFO 写日志，行会交错吗？（提示：会按 write 调用交错；单条 write ≤ PIPE_BUF 对管道原子（Q380），但两次 write 之间可插——要么单行单 write，要么换队列/Unix 域 socket 按帧协议收）
