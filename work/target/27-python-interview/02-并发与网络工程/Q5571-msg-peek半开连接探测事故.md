---
title: [Q5571] MSG_PEEK 探测半开连接的事故复盘
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5571 · MSG_PEEK 探测半开连接的事故复盘

> 难度:★★★★ | 标签:事故复盘, socket, MSG_PEEK, 半开连接

**问**：长连接网关要清理"客户端已断但服务端不知道"的半开连接，有同学在应用层用 `recv(MSG_PEEK)` 探测，结果出现"连接被误关"和"探测线程把 loop 卡死"两种事故。MSG_PEEK 的正确用法是什么？为什么它和异步框架组合容易出事？与 TCP keepalive、应用层心跳的分工是什么（保活矩阵见既有 Q5512）？

**答**：结论：`recv(sock, MSG_PEEK)` 是"偷看不移除"——读出缓冲区数据但不消费，用来判断连接状态：返回空串（EOF）= 对端正常关闭；`BlockingIOError/EWOULDBLOCK` = 无数据但连接可能还活着；超时/`ECONNRESET` = 网络侧故障。事故一（误关）：探测代码把 "PEEK 返回 EWOULDBLOCK" 当成"死连接"去关——**无数据是常态**（客户端就是没发消息），只有结合"超过 N 秒无任何字节且 PEEK 超时"才算死；另一个误关源是在**阻塞 socket** 上 PEEK：默认阻塞语义下会一直等，探测线程配了短超时（SO_RCVTIMEO）但该 socket 同时被业务线程读，超时打断了正在到达的合法数据。事故二（卡 loop）：直接在 asyncio 里 `loop.run_in_executor` 外裸调阻塞 PEEK，或对**非阻塞 socket 用阻塞式 PEEK**——正确姿势是把探测 fd 也挂进 selector（`selectors.DefaultSelector` 单独线程），或 asyncio 里用 `loop.add_reader` + 带超时的等待。取舍：MSG_PEEK 探测是"诊断手段"不是"保活手段"，规模化清理靠 TCP keepalive（内核代劳、空闲探测）+ 应用层心跳（穿透中间设备 NAT 表、检测应用假死）双保险，PEEK 只在"怀疑死连接但心跳没回复"时做最终确认。

```python
# file: code/02_并发与网络工程/q5571_msg_peek.py
import socket, selectors, time, threading

# 1) 搭一对 TCP socket 模拟"服务端探测客户端"
srv = socket.socket(); srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("127.0.0.1", 0)); srv.listen(1)
cli = socket.socket(); cli.connect(srv.getsockname())
conn, _ = srv.accept()
conn.setblocking(False)                 # 服务侧非阻塞: 探测必须非阻塞
cli.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

# 2) PEEK 偷看: 不消费, 再 recv 还能读到
cli.send(b"PING")
time.sleep(0.05)
peeked = conn.recv(4, socket.MSG_PEEK)
again = conn.recv(4)
print("peek 读到:", peeked, "| peek 不消费, 再 recv 同样数据:", again == peeked)

# 3) 正确的探测循环: selectors + 超时, 不卡线程
sel = selectors.DefaultSelector()
sel.register(conn, selectors.EVENT_READ)
def probe(sock, idle_timeout=0.3):
    if sel.select(idle_timeout):
        try:
            data = sock.recv(1, socket.MSG_PEEK | getattr(socket, "MSG_DONTWAIT", 0))
            if data == b"":
                return "eof"            # 对端正常关闭
            return "alive-with-data"
        except (BlockingIOError, ConnectionResetError) as e:
            return type(e).__name__     # EWOULDBLOCK=活着没数据 / RST=对端故障
    return "alive-idle"                 # 超时无数据 != 死连接(事故一的根因)

print("探测结果:", probe(conn))
cli.close(); time.sleep(0.05)
print("客户端关闭后探测:", probe(conn))     # eof
conn.close(); srv.close()

# 4) 分工矩阵(输出结论, 不另开真实 keepalive 以免平台差异)
print("keepalive=内核空闲探测(非阻塞零成本) | 应用层心跳=穿透NAT+应用假死 | MSG_PEEK=最终确认诊断")
```

**追问**：1) `MSG_PEEK|MSG_DONTWAIT` 与设 SO_RCVTIMEO 的区别？——DONTWAIT 是**单次调用**非阻塞，不污染 socket 全局状态，适合探测；SO_RCVTIMEO 是 socket 级配置，会影响同 socket 上所有读操作，业务线程与探测线程共用一个 fd 时会互相干扰（事故一的第二形态）；更稳的架构是探测与读数据走同一事件循环，不做旁路线程。2) PEEK 探测与 `loop.add_reader` 如何组合？——注册 reader 后由事件循环通知"可读"，再 PEEK 一次判断是数据还是 EOF，全程无阻塞调用；注意 reader 回调里若做重活会拖慢 loop（Q5524 手法监控 slow callback）。3) 半开连接为什么 keepalive 探得到而应用层探测常探不到？——keepalive 是内核对 TCP 层的探测（对端 OS 回 ACK/RST）；而"应用假死"（进程活着但不处理）TCP 层一切正常，只有应用层心跳超时能发现——所以矩阵里两者缺一不可，PEEK 探测处理不了假死（数据根本不来）。

## 背诵要点
- MSG_PEEK=偷看不消费：空串=EOF、EWOULDBLOCK=活着没数据、超时≠死连接；"无数据就关"是典型误判事故。
- 探测必须非阻塞（MSG_DONTWAIT 或挂 selector/add_reader），阻塞式 PEEK 会卡死线程或打断合法数据。
- 分工：TCP keepalive 管内核级死链、应用层心跳管假死与 NAT、MSG_PEEK 只做最终诊断，三者不是替代关系。

## 复盘追问
- 你们的"无数据即断开"策略上线前后误杀率变化如何？（提示：把探测结果分布（eof/idle/data）打成指标，先观察一周再收紧阈值）
- 探测线程与业务读线程共用 fd 吗？SO_RCVTIMEO 是否影响了业务路径的超时语义？（提示：单 fd 单职责，或全部并入事件循环，见 Q5512 保活矩阵统一收口）
