---
title: "[Q5724] CLOSE_WAIT 堆积：应用不收尾的定位与防线"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5724 · CLOSE_WAIT 堆积：应用侧不关闭的定位与防线

难度：P6 ｜ 标签：CLOSE_WAIT、TCP 状态机、EOF 处理、fd 泄漏、recv 返回 b''、TIME_WAIT 对比

**问**：CLOSE_WAIT 状态意味着什么？为什么它是"应用层不收尾"的指纹而不是网络问题？它和 TIME_WAIT 堆积的根因有什么本质区别？recv 返回 b'' 之后正确的动作序列是什么？怎么定位与告警？

**答**：
结论：CLOSE_WAIT 是**被动关闭方**在收到对端 FIN、且自身尚未调用 close 时的状态——内核已经完成了"对端不再发数据"的登记，剩下的收尾动作**只取决于应用代码**。所以 CLOSE_WAIT 持续上涨只有一个解释：应用收到了 EOF（recv 返回 b''）却没 close，fd 被占着直到进程重启。这与 TIME_WAIT 堆积是两种完全不同的病：TIME_WAIT 出现在**主动关闭方**，是内核的协议级延迟（2MSL），有系统参数可调（Q5582/Q5568 的端口耗尽治理）；CLOSE_WAIT 出现在**被动方**，是**应用 bug**，调内核参数毫无作用。正确动作序列：`recv` 返回 `b''` → 立即 `close()`（连接进入 LAST_ACK → CLOSED）；异常路径用 `finally: conn.close()` 兜底；长期连接加"EOF 即踢出连接表"逻辑。定位三板斧：①`ss -tanp | grep CLOSE-WAIT | wc -l` 观察趋势（不是瞬时值）；②`ss -p` 找到持有 fd 的进程，看该进程的连接处理代码路径；③对应用内连接注册表做对账（Q2693 的线程对账思路），找出"注册了但没回收"的路径。告警：CLOSE_WAIT 数持续 5 分钟单调上涨即触发，因为应用不修它不会自愈。

取舍：a) 读侧 EOF 处理：`if not data: break/close` 是 recv 循环的固定纪律，任何"EOF 后继续 recv"的代码都是 bug 温床（Q2148 的 recv 返回值矩阵）；b) 框架层：asyncio 的 `connection_lost`/Streams 的 `at_eof`（Q5696）已把 EOF 事件化，自研 reactor 才需要手工纪律；c) 超时兜底：给连接设硬超时（空闲踢除 Q624），EOF 之外的僵死连接一并治理；d) 进程级：fd 数量监控（Q5645/Q5553）与 CLOSE_WAIT 计数分开告警——前者抓泄漏总量，后者抓"对端已走应用未走"这一特定泄漏；e) 优雅停机时：先停收新连接，再逐个 close 残留 CLOSE_WAIT（它们对端早已离开，close 无副作用）。

实战：事故形态是"长连接网关的推送代码只在'有消息要发'时遍历连接，客户端断开后的 conn 留在注册表里，recv 从未被调用、EOF 永远不触发，CLOSE_WAIT 涨到 8 万触发 fd 上限告警（Q5553），新连接全部拒绝；修复为注册表挂 recv 探针 + EOF 即注销 + finally 收尾，并给 CLOSE_WAIT 加单调上涨告警"。下面复现 CLOSE_WAIT 的产生点与收尾纪律。

```python
# CLOSE_WAIT 堆积: 应用侧不关闭的定位与防线
import socket
import time

srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("127.0.0.1", 0))
srv.listen(8)
port = srv.getsockname()[1]

cli = socket.create_connection(("127.0.0.1", port))
conn, _ = srv.accept()
print("[1] 建连完成: client fd 与 accepted fd 都活着")

cli.close()                              # 客户端主动关闭 -> 发 FIN
print("[2] 客户端已 close, 服务端 conn 收到 EOF:")
first = conn.recv(1024)
print("    recv =", first, "(b'' 即对端半关闭, 内核进入 CLOSE_WAIT)")

print("[3] 此刻本端若不 close, TCP 状态停在 CLOSE_WAIT -- fd 一直占着")
print("    conn.fileno() =", conn.fileno(), "(仍有效, 但对端已走; 只能被动等待应用收尾)")
conn.close()                             # 应用必须自己 close, 状态才走 LAST_ACK->CLOSED
print("[4] conn.close() 后才真正终结; CLOSE_WAIT 堆积 = 应用层'收到 EOF 不收尾'的指纹")

print("[5] 防线: EOF 即关闭 + finally 兜底 + fd 数量监控")
def safe_echo(conn: socket.socket) -> None:
    try:
        while True:
            data = conn.recv(4096)
            if not data:                 # EOF: 立即关闭
                break
            conn.sendall(data)
    finally:
        conn.close()                     # 异常路径也不漏
print("    规则: recv 返回 b'' 就 close; 异常路径 finally close; CLOSE_WAIT 持续上涨即告警")
srv.close()
```

**追问一**：CLOSE_WAIT 和半关闭（shutdown 写端）是什么关系？—— 两者是同一状态机的不同分支：对端 `shutdown(SHUT_WR)`（Q664 的半关闭语义）也向本端发 FIN，本端同样进入 CLOSE_WAIT，但此时本端**仍可继续发送数据**（半关闭是有意设计）；而 close 触发的 FIN 通常意味着对端不再需要响应。应用层要区分这两种 FIN 的意图：协议里应有"结束请求但保留响应流"的显式信号（如 HTTP 的 Connection 头、消息协议的 finish 帧），否则一律按"对端已走"处理——用 shutdown 做半关闭通信的协议必须自带区分机制，否则 EOF 分支无法安全地收尾。

**追问二**：为什么 CLOSE_WAIT 堆积"调内核参数没用"？—— CLOSE_WAIT 的持有者是**进程**：fd 一直开着，内核无权（也不该）替应用关闭——协议上本端还可能要发数据，内核单方面断开违反 TCP 语义。可调的都是主动关闭侧的状态（TIME_WAIT 超时、端口范围），被动侧的 CLOSE_WAIT 只能靠应用 close 推进状态机。这也决定了监控语义的差异：TIME_WAIT 堆积是**容量问题**（调参数/加端口/连接复用），CLOSE_WAIT 堆积是**代码问题**（修 EOF 处理），把后者当容量问题调参数是复盘里最典型的误判。

## 背诵要点
- CLOSE_WAIT = 被动方收到 FIN 后未 close；堆积=应用 bug（EOF 未收尾），调内核参数无效。
- 与 TIME_WAIT（主动方、内核 2MSL 延迟）根因本质不同：一个是代码问题、一个是容量问题。
- 纪律：recv 返回 b'' 即 close、异常路径 finally close、连接注册表挂 EOF 探针；单调上涨即告警。

## 复盘追问
- 网关 CLOSE_WAIT 涨到 fd 上限新连接全拒，定位路径？（ss -p 找进程 → 连接注册表对账 → 补 EOF 探针与 finally）
- 为什么 CLOSE_WAIT 不能像 TIME_WAIT 一样调超时？（fd 归应用持有，内核无权代关；只能靠应用 close 推进状态机）
