---
title: "[Q6188] gunicorn preload_app 与 fork 继承连接：协议错位事故"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6188 · gunicorn preload_app 与 fork 继承连接：协议错位事故

难度：P7 ｜ 标签：gunicorn、preload_app、fork、连接池、post_fork

**问**：为了省内存开了 `preload_app=True`，上线后 worker 偶发 `SSL error: decryption failed or bad record mac`、PG 报 `unexpected message type`、Redis 报协议错误，重启就好。preload 到底 preload 了什么？为什么 fork 之后连接会坏？`post_fork` 里该做什么？

**答**：
结论：preload 是在 **master 进程**里 import 应用并执行模块级初始化（包括建连接池、连 Redis、初始化 TLS），然后 fork 出 worker。fork 复制的是文件描述符表——所有已打开的 socket 被父子共享，指向**同一条 TCP 连接**。多个进程往同一个连接上写，字节流在协议层交错（实测两条流变成 P0 C0 P1 C1），长度前缀、TLS 记录序号全部错位。这不是"偶发网络问题"，是确定性的协议破坏。

取舍：preload 的收益是 COW 共享代码与只读数据（省内存）、启动更快（import 只做一次）；代价是必须显式处理"fork 后不可继承的资源"。正确做法：`post_fork` 里关掉所有继承的连接再重建——Django 的 `connections.close_all()`、SQLAlchemy 的 `engine.dispose(close=False)`、Redis 客户端的 `connection_pool.disconnect()`；或者干脆在 preload 阶段只做 import、不建连接（懒连接），把初始化推迟到 worker。

实战：事故形态是"低流量时正常，一上量就零星 SSL/协议错误，重启恢复"，因为空闲连接在 fork 时也处于打开状态。排查线索：错误只在多 worker 时出现、单 worker 无法复现、错误类型是"协议层"而非"业务层"。下面用 socketpair 模拟"preload 阶段建好的连接"，父子进程各写 6 帧，看对端收到什么。

```python
import os
import socket
import time

writer, reader = socket.socketpair()   # 模拟 preload 阶段就建好的 DB/TLS 连接

pid = os.fork()
who = "child" if pid == 0 else "parent"
tag = b"C" if pid == 0 else b"P"
for i in range(6):
    os.write(writer.fileno(), tag + str(i).encode())   # 父子共用同一个 fd
    time.sleep(0.002)                                  # 让两个进程交错写
if pid == 0:
    os._exit(0)
os.waitpid(pid, 0)

data = reader.recv(65536)
frames = [data[i:i + 2] for i in range(0, len(data), 2)]
print("[1] 客户端收到的帧序列:", frames)
clean = [b"P0", b"P1", b"P2", b"P3", b"P4", b"P5"]
print("[2] 父进程自己那 6 帧是否连续:", frames[:6] == clean)
print("[3] 帧总数:", len(frames), "| 内容齐全:",
      sorted(frames) == sorted(clean + [b"C%d" % i for i in range(6)]))
print("[4] 结论：两条流写进同一条连接，长度前缀/SSL 记录都会错位")

writer.close()
reader.close()
```

**追问一**：为什么不能靠"用完就关"避免？—— 连接池里的**空闲**连接在 fork 时同样是打开的 fd，只要被继承就共享同一条 TCP 连接。哪怕业务代码每次都"取-用-还"，池里那几条空闲连接已经同时属于父子进程了。唯一的办法是 fork 之后主动断开（关闭 fd 并让池丢弃引用），或者 preload 阶段根本不建池。

**追问二**：`uvicorn --workers` 有这个问题吗？—— 取决于启动方式：`uvicorn --workers` 在 Unix 上用 spawn（子进程重新 import），不继承 fd，问题小；`gunicorn -k uvicorn.workers.UvicornWorker` 默认 fork，仍然中招。判断标准不是"用哪个服务器"，而是"worker 是 fork 出来的还是 exec/spawn 出来的"。

## 背诵要点
- `preload_app` 在 master 里建连接后 fork：fd 被继承 → 多进程共享同一条 TCP/TLS 连接 → 协议错位。
- `post_fork` 必须关闭并重建：`connections.close_all()`、`engine.dispose(close=False)`、Redis pool disconnect。
- 判断风险看"fork 还是 spawn"，不是看服务器名字；空闲池连接也会被继承。

## 复盘追问
- 多 worker 下偶发 SSL/pg 协议错误，如何证明是 preload 继承连接？（fd 共享、单 worker 不可复现）
- post_fork 里要清理哪些资源？懒连接方案怎么落地？（连接池/Redis/TLS、preload 只 import）
