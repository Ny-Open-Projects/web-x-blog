---
title: "[Q5673] SCM_RIGHTS 跨进程传递文件描述符的所有权"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5673 · SCM_RIGHTS 跨进程传递文件描述符的所有权

难度：P7 ｜ 标签：Unix domain socket、SCM_RIGHTS、sendmsg、fd 传递、FD_CLOEXEC

**问**：多进程服务器想让 worker 直接处理 master 已 `accept` 的连接，而不是让 worker 自己抢 accept；常见做法是通过 Unix domain socket 把**文件描述符本身**发给 worker。`sendmsg` 的 ancillary data 里塞一个整数 fd，为什么对方收到的是"另一个 fd 号、但指向同一个打开文件描述"？发送方 `close` 后接收方还能读吗？为什么"传 fd"必须用 `SCM_RIGHTS` 而不能把 `int(fd)` 当普通字节发过去？这套机制和 Q5640（进程组/信号）、Q5672（makefile 缓冲）的边界在哪？

**答**：
结论：`SCM_RIGHTS` 是 Unix domain socket 的内核辅助消息：它传递的不是数字，而是**打开文件描述（open file description）的引用**。内核在接收进程里分配一个新 fd 号，指向同一个 file description（同一个文件偏移、同一组 flags）；因此发送方 `close` 自己的 fd 只是减引用，接收方仍能读写。文件偏移是共享的——接收方读了多少，发送方（若还持有）看到的位置也前进。`int(fd)` 只是本进程 fd 表的下标，发给别的进程毫无意义（对方表里可能指向完全不同的东西），所以必须走 `SCM_RIGHTS`，由内核做引用传递。

取舍：fd 传递适合 master/worker 架构（master accept 后分发、零拷贝地把连接交给 worker）、以及需要跨进程共享已打开文件/管道的场景。代价是：接收方必须显式 `os.close(recv_fd)`，否则 fd 泄漏；发送方 `close` 后若接收方也 `close`，file description 才真正释放；fd 默认是**非继承**的（PEP 446），但通过 `SCM_RIGHTS` 传过去的新 fd 在接收进程里同样默认 `FD_CLOEXEC`，如果 worker 要 `exec` 子进程并让子进程继承这个连接，需要显式 `os.set_inheritable(fd, True)`（并承担泄漏风险）。传输通道本身要是 `AF_UNIX`（`SOCK_STREAM`/`SOCK_SEQPACKET`/`SOCK_DGRAM` 均可，但消息边界/截断语义不同）。

实战：事故形态是"master 把连接 fd 发给 worker 后自己 close，worker 却读到 EOF/错乱"，根因往往是 worker 把收到的 ancillary data 解析错（只取 `data` 不取 `ancdata`），或者把 `int(fd)` 当普通 payload 发。下面用 socketpair + `sendmsg` 传一个管道读端：接收方拿到新 fd 号（与原 fd 不同），读到 `hello-through-fd`；发送端已 `close(w)`，说明 file description 由接收方的引用维持。

```python
import array
import os
import socket

a, b = socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM)
r, w = os.pipe()
os.write(w, b"hello-through-fd")
os.close(w)

fds = array.array("i", [r])
a.sendmsg([b"F"], [(socket.SOL_SOCKET, socket.SCM_RIGHTS, fds)])
os.close(r)                                   # 发送方立刻丢掉本地 fd

msg, ancdata, flags, addr = b.recvmsg(1, socket.CMSG_SPACE(fds.itemsize))
print("控制消息:", msg)

recv_fd = None
for level, ctype, data in ancdata:
    if level == socket.SOL_SOCKET and ctype == socket.SCM_RIGHTS:
        arr = array.array("i")
        arr.frombytes(data[:fds.itemsize])
        recv_fd = arr[0]
print("收到 fd:", recv_fd)
print("发送方 close 后仍读到:", os.read(recv_fd, 100))

os.close(recv_fd)
a.close()
b.close()
print("fd 传递的是 open file description 的引用，不是数字")
```

**追问一**：为什么 `recvmsg` 的缓冲区要按 `CMSG_SPACE` 算，而不是 fd 的字节数？——ancillary data 有对齐/头部开销：`CMSG_SPACE(n)` 包含控制消息头和对齐，`CMSG_LEN(n)` 是实际数据长度；缓冲区太小会触发 `MSG_CTRUNC`，fd 可能被截断/丢失（甚至内核关闭被截断的 fd）。正确写法是 `recvmsg(1, socket.CMSG_SPACE(array.array("i").itemsize))`，并检查返回的 `flags & socket.MSG_CTRUNC`；一次 `sendmsg` 可以传多个 fd，接收端要按 `itemsize` 循环解析。

**追问二**：fd 传过去后，文件偏移是共享还是独立？——共享同一个 open file description，所以偏移、`O_APPEND` 等 flags 都是同一份；接收方 `read` 会推进发送方看到的偏移（如果发送方还持有）。若想要独立偏移，接收方需要 `os.dup`？不——`dup` 仍共享 file description；要独立偏移必须重新 `open` 文件（得到新的 file description），或用 `pread/pwrite` 指定偏移。这个语义在"master 分发同一个日志文件给多个 worker"时尤其重要：共享偏移可能交错写，通常要 `O_APPEND` 或每 worker 独立打开。

## 背诵要点
- `SCM_RIGHTS` 传的是打开文件描述的引用；接收方得到新 fd 号，指向同一 file description（共享偏移/flags）。
- 必须用 `sendmsg/recvmsg` 的 ancillary data；`int(fd)` 当普通字节发毫无意义；发送方 close 后接收方仍可用。
- 接收缓冲区用 `CMSG_SPACE` 并检查 `MSG_CTRUNC`；收到的 fd 要显式 close，默认 `FD_CLOEXEC`，exec 继承需 set_inheritable。

## 复盘追问
- master accept 后把连接 fd 发给 worker，worker 读到 EOF/错乱，如何排查？（只读 data 忽略 ancdata、CMSG_SPACE/MSG_CTRUNC、fd 号不是全局的）
- 传过去的 fd 与发送方共享文件偏移，这对多 worker 写同一日志有什么影响？（共享 file description、交错写、O_APPEND/pwrite 取舍）
