---
title: "[Q5754] 半关闭作为协议信号：SHUT_WR 的 FIN 语义与 close 丢未读数据的边界"
date: 2026-11-25
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5754 · 半关闭作为协议信号：SHUT_WR 的 FIN 语义与 close 丢未读数据的边界

难度：P6 ｜ 标签：TCP、半关闭、shutdown、SHUT_WR、FIN、RST、EOF 分帧、close、socketpair

**问**：一个"请求-响应"代理需要在发完请求后告诉上游"我没有更多数据了"，于是调用了 `sock.close()`，结果上游偶尔收不到完整请求，还报 `Connection reset by peer`；改成 `sock.shutdown(SHUT_WR)` 后恢复正常，但代码里又多了一处"什么时候真正 close"的困惑。`shutdown(SHUT_WR)` 和 `close()` 在内核里各做了什么？为什么 close 会丢数据？什么样的协议适合用"半关闭"表示消息结束？

**答**：

- **结论**：`shutdown(SHUT_WR)` 只关闭**发送方向**：内核把发送缓冲里的数据发完，然后发一个 FIN，对端读到 EOF（`recv` 返回 `b""`）；本端的 socket 仍然打开，**仍可继续 `recv`**，`fileno()` 不变。`close()` 是**关闭整个文件描述符**：引用计数减到 0 时，如果接收缓冲里还有未读数据，内核会直接丢弃并给对端发 RST（而不是等对端读完再 FIN）——对端可能先看到已收到的部分数据，随后 `recv` 报 `ECONNRESET`，在途数据全丢。所以"发完请求但还要读响应"的连接绝不能用 `close` 表达"我说完了"，必须用 `shutdown(SHUT_WR)`；真正释放 fd 要等响应读完后再 `close`。`shutdown` 发的是 FIN，属于**有序关闭**；`close` 带未读数据触发的是 RST，属于**异常中止**，两者在对端看来是完全不同的语义。

- **取舍**：a) 用半关闭做"消息边界"：适合"一问一答、请求长度事先未知、以 EOF 结尾"的协议（HTTP/1.0 的无 Content-Length 响应、SMTP 的 DATA 结束、部分 Redis 内联命令），优点是实现简单，缺点是连接不能复用（发完 FIN 后这一方向就永久关闭）；b) 长连接/多路复用协议（HTTP/1.1 keep-alive、HTTP/2）不能用半关闭分帧，必须用长度前缀或 chunked，否则一次"我说完了"会把整条连接废掉；c) `close` 前要先 `shutdown(SHUT_WR)` 再读完对端数据（"优雅关闭"），或者用 `SO_LINGER` 控制是否等待；直接 `close` 是最容易丢数据的方式；d) `shutdown(SHUT_RD)` 在各平台语义不一致（有的丢弃接收缓冲、有的只让后续 read 返回 EOF），跨平台代码不要依赖它。

- **实战**：事故形态是"代理转发大请求，偶发上游 400"——代理把请求 body 写完后立刻 `close()`，此时上游可能还没读完内核接收缓冲里的数据，close 触发 RST，上游解析到一半收到连接重置；小请求因为数据早已被读走而侥幸正常，所以是"偶发、且只在大 body 时出现"。修复：写完请求后 `shutdown(SHUT_WR)`，然后继续 `recv` 直到 EOF 或响应完整，最后 `close`；同时把"是否读完"做成显式状态（读满 Content-Length / 读到 chunked 终止块 / 读到 EOF），不要用"睡眠 100ms 再 close"这种碰运气写法。

```python
# shutdown(SHUT_WR) 只关发送方向: 对端读到 EOF, 本端仍可收; close 之后不能再用
import socket

a, b = socket.socketpair()

a.sendall(b"hello")
a.shutdown(socket.SHUT_WR)          # 发 FIN, 但 socket 仍打开
print("→ shutdown 后 fileno 仍有效:", a.fileno())
assert a.fileno() != -1

assert b.recv(100) == b"hello"
assert b.recv(100) == b""           # 对端看到 EOF, 这是半关闭的信号
print("→ 对端读到 EOF, 但连接未断")

b.sendall(b"reply")                  # 反方向仍然畅通
reply = a.recv(100)
print("→ 半关闭后本端仍能收:", reply)
assert reply == b"reply"

a.close()
err = None
try:
    a.recv(1)
except OSError as e:
    err = e
print("→ close 后再 recv:", err.errno, err.strerror)
assert err is not None and err.errno == 9      # EBADF: fd 已释放

# 对端继续写: 收到 EPIPE/BrokenPipe, 说明连接已被彻底拆除
write_err = None
try:
    b.sendall(b"x")
except OSError as e:
    write_err = e
print("→ 对端写已关闭的连接:", type(write_err).__name__, write_err.errno)
assert isinstance(write_err, BrokenPipeError) and write_err.errno == 32

b.close()

# 应用层分帧: 读到 EOF 才知道"请求结束", 这是半关闭的典型用法
def read_until_eof(sock):
    chunks = []
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            return b"".join(chunks)
        chunks.append(chunk)

c, d = socket.socketpair()
c.sendall(b"part1-")
c.sendall(b"part2")
c.shutdown(socket.SHUT_WR)
payload = read_until_eof(d)
print("→ EOF 分帧收到:", payload)
assert payload == b"part1-part2"
c.close(); d.close()
```

**追问一**：为什么 close 带未读数据会发 RST，而不是像 shutdown 一样发 FIN？—— TCP 的关闭是"两个方向各自关闭"：`shutdown(SHUT_WR)` 只关发送方向，内核可以安全地排空发送缓冲再发 FIN，接收方向继续工作；`close` 则是"这个 fd 不要了"，内核必须决定接收缓冲里的数据怎么办——如果还有未读数据，语义上"应用已经不关心这些数据了"，继续等对端发完再 FIN 会浪费资源，而且应用再也读不到，所以内核选择丢弃并 RST，让对端立刻知道"别发了，数据没人要"。这也解释了为什么"先 shutdown 再读完再 close"是优雅关闭的标准姿势：先把"我不发了"和"我还在读"分开，确保接收缓冲排空后再释放 fd。

**追问二**：半关闭之后还能不能重新打开发送方向？如果协议需要"多轮对话"怎么办？—— 不能。FIN 一旦发出，这个方向的字节流就终止了，TCP 没有"重新打开"的机制；要再发数据只能新建连接（或协议层复用另一条连接）。所以半关闭只适合"一次性请求 + 一次性响应"的模型：客户端发完请求 `SHUT_WR`，服务端读完请求后把响应写完再 `close`；如果业务需要多轮（先发一批、等确认、再发一批），就必须用长度前缀/消息帧来划分边界，而不是用 EOF。另一个细节是"谁先关"：主动关闭方会进入 `TIME_WAIT`（占用四元组一段时间），高并发短连接场景要评估端口耗尽，长连接则要处理空闲超时与心跳。

## 背诵要点

- `shutdown(SHUT_WR)` 只关发送方向：排空发送缓冲 + 发 FIN，对端 `recv` 得 `b""`；socket 仍可读，fd 仍有效。
- `close()` 释放 fd；接收缓冲有未读数据时内核丢弃并发 RST，对端可能 `ECONNRESET`、在途数据丢失——这就是"close 丢数据"。
- 半关闭适合"以 EOF 分帧"的一次性请求/响应；长连接、多轮对话必须用长度前缀或 chunked，不能靠 FIN 划分消息。

## 复盘追问

- 为什么"写完请求立刻 close"会偶发丢数据，而小请求看起来正常？（close 带未读数据触发 RST；小请求的数据通常已被对端读走，大 body 还在内核缓冲里）
- 半关闭后还能再发数据吗？多轮协议该怎么分帧？（不能，FIN 终止该方向；用长度前缀/chunked/消息帧，不要用 EOF）
