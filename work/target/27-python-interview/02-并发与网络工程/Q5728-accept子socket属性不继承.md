---
title: "[Q5728] accept 出的子 socket：阻塞属性不继承与显式设置"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5728 · accept 出的子 socket：阻塞属性不继承与显式设置

难度：P6 ｜ 标签：socket、accept、settimeout、setblocking、非阻塞、不继承、selector

**问**：监听 socket 设了 `settimeout(1.0)`，那 accept 出来的连接 socket 有超时吗？监听 socket 是非阻塞的，accept 出来的连接也是非阻塞的吗？"select 就绪后 accept，然后 worker 里 recv 卡死"这类偶发事故的根因是什么？正确做法是什么？

**答**：
结论：**accept 出来的 socket 不继承监听 socket 的 timeout/阻塞属性**——监听 socket 的 settimeout/setblocking 只影响监听 socket 自己的 accept/读写行为，新连接 socket 默认回到**系统默认状态**（阻塞、无超时）。推导链条：①监听 socket `settimeout(1.0)` 后 accept 带 1 秒超时，但 accept 返回的 `conn.gettimeout()` 是 None——conn 上任何 `recv` 都可能**永久阻塞**；②监听 socket `setblocking(False)` 后 accept 立即抛 BlockingIOError（无 pending 连接时），但此时 accept 出来的 conn2 仍是阻塞的；③这就是"偶发 worker 卡死"的经典根因：selector 报可读 → accept → 把 conn 扔给 worker，worker 的第一个 `recv` 在客户端静默（发完请求等响应、或半开连接）时永久挂起，连接池占满、线程泄漏；④唯一例外是**全局默认**：`socket.setdefaulttimeout(t)` 设置的默认值会作用于 accept 出的新 socket——它是创建新 socket 时的出厂设置；⑤正确顺序：accept → 立即 `conn.settimeout(业务超时)` 或 `conn.setblocking(False)` 注册进 selector，二选一，绝不能裸用。

取舍：a) 线程池 per-connection 模型：accept 后立刻 `settimeout(30)`——给业务 IO 一个兜底超时，防止半开连接挂死 worker；b) selector/事件驱动模型：`setblocking(False)` 后注册 selector，读写全靠就绪事件 + 自维护的应用层 deadline（selector 层面没有 per-socket 超时，Q5721 的 EAGAIN 容错是前置知识）；c) 全局 `setdefaulttimeout` 是偷懒方案：影响进程内**所有**新 socket（包括 urllib、httpx 裸用底层的调用方），副作用面大，只适合小工具脚本；d) 监听 socket 自身要不要超时：阻塞式 accept 场景下 settimeout(1.0) 是为了让 accept 周期醒来做信号检查/优雅退出判断，与 conn 无关；e) 别忘了 conn 的写侧：send 大对象时同样受这个属性影响，设置超时覆盖读写两侧。

实战：事故形态是"网关服务每隔几天线程池打满、新连接 accept 不动，dump 线程栈发现几十个 worker 全挂在 conn.recv()——客户端建连后不发数据（健康检查探针只 connect 不写、或攻击者的 slowloris），监听 socket 设了非阻塞大家就以为 conn 也非阻塞"。修复：accept 后第一行 `conn.settimeout(READ_TIMEOUT)`，超时关闭连接。下面实测不继承语义。

```python
# accept 出的子 socket: 阻塞属性不继承, 必须显式设置
import socket

srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("127.0.0.1", 0))
srv.listen(8)
port = srv.getsockname()[1]

print("[1] 关键事实: accept 出来的 socket 不继承监听 socket 的 timeout")
srv.settimeout(1.0)
c1 = socket.create_connection(("127.0.0.1", port))
conn, _ = srv.accept()
print("    srv.gettimeout() =", srv.gettimeout(), "-> conn.gettimeout() =", conn.gettimeout(), "(None=阻塞)")

print("[2] 监听是非阻塞时, accept 出来的也未必是非阻塞")
srv.setblocking(False)
c2 = socket.create_connection(("127.0.0.1", port))
conn2, _ = srv.accept()
print("    srv.getblocking() =", srv.getblocking(), "-> conn2.getblocking() =", conn2.getblocking())
print("    conn2.gettimeout() =", conn2.gettimeout())
conn2.setblocking(False)
print("    显式 setblocking(False) 后:", conn2.getblocking())

print("[3] 若不显式设置: conn 无数据 -> recv 永久阻塞")
print("    这是'偶发 worker 卡死'的经典根因: select 就绪后 accept, 却忘了给 conn 设超时")

print("[4] 正确顺序: accept -> 立即 settimeout(业务超时) 或 setblocking(False) 交给 selector")
conn2.settimeout(2.0)
print("    conn2.gettimeout() =", conn2.gettimeout())

print("[5] socket.setdefaulttimeout(t) 的全局默认会作用于 accept 出的新 socket")
print("    getdefaulttimeout() =", socket.getdefaulttimeout())
c1.close(); c2.close(); conn.close(); conn2.close(); srv.close()
```

**追问一**：为什么语言层面会这样设计？监听 socket 的非阻塞不是"这个服务的属性"吗？—— 因为 accept 在 POSIX 语义里只是"从完成队列取出一条已建立的连接"，返回的**新文件描述符**是内核为连接单独创建的，其 O_NONBLOCK 标志独立于监听 fd（POSIX 明确不要求继承；Linux 内核在实践中也不继承 O_NONBLOCK，但很多新手被"BSD 某些版本继承"的传说误导）。Python 的 socket 模块对 timeout 的实现依赖 fd 的非阻塞标志 + 超时循环，监听 fd 上设置的是它自己的标志，自然传不到新 fd。把"阻塞属性"设计为 per-fd 而不是 per-socket-family，让同一监听 socket 上可以混合"超时 accept + 阻塞 conn / 非阻塞 conn"的策略，是更细粒度的控制权——代价就是把显式设置的义务交给应用。

**追问二**：`settimeout(0)`、`setblocking(False)`、`settimeout(None)` 三者什么关系？混用会怎样？—— `settimeout(0.0)` 与 `setblocking(False)` 等价（都进入非阻塞模式）；`settimeout(None)` 与 `setblocking(True)` 等价（回到阻塞）。注意 `settimeout(0)` 和 `settimeout(None)` **不是**一回事：前者是"立即失败"，后者是"永远等待"。混用陷阱：先 settimeout(5) 再 setblocking(False)，非阻塞覆盖超时模式；先 setblocking(False) 再 settimeout(5)，又切回超时模式——后调者生效。语义上 Python 把 socket 分为三种模式：blocking（None）、non-blocking（0）、timeout（>0），timeout 模式内部靠"非阻塞 fd + select 重试"实现，所以 timeout 模式下如果信号处理器抛异常，可能出现 `InterruptedError` 之外的半途状态（PEP 475 之后系统调用自动重试，超时会顺延），测得的状态永远以 `gettimeout()/getblocking()` 为准。

## 背诵要点
- accept 出的 conn **不继承**监听 socket 的 timeout/非阻塞属性，默认回到阻塞无超时。
- 偶发 worker 卡死经典根因：selector 就绪 → accept → 忘设 conn 超时 → 慢客户端/探针把 recv 挂死。
- 三种模式互斥：blocking(None) / non-blocking(0) / timeout(>0)，后调者生效；setdefaulttimeout 只影响新 socket。

## 复盘追问
- 线程池 worker 全挂在 conn.recv，线程栈之外还要查什么？（accept 代码是否漏 settimeout；客户端是否 connect 后不发数据；全局 setdefaulttimeout 是否被依赖）
- settimeout(0) 和 settimeout(None) 区别？（0=非阻塞立即抛 BlockingIOError；None=阻塞；timeout 模式内部是非阻塞 fd + select 循环）
