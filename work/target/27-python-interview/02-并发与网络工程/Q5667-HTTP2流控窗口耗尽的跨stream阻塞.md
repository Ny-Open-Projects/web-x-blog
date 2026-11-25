---
title: "[Q5667] HTTP/2 流控窗口耗尽的跨 stream 阻塞"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5667 · HTTP/2 流控窗口耗尽的跨 stream 阻塞

难度：P7 ｜ 标签：HTTP/2、流控窗口、WINDOW_UPDATE、队头阻塞、吞吐上限

**问**：HTTP/2 多路复用在一条 TCP 连接上跑多个 stream，为什么"一个 stream 的窗口耗尽"会拖累别的 stream、而"连接级窗口耗尽"会让**所有** stream 一起停？`SETTINGS_INITIAL_WINDOW_SIZE` 与 `WINDOW_UPDATE` 各自管什么？为什么窗口大小会直接决定单连接吞吐上限（窗口 / RTT），不同 RTT 下怎么配？这和 Q5508 讲的"TCP 丢包导致所有 stream 卡住"是同一个瓶颈吗？

**答**：
结论：HTTP/2 有两级流控——**连接级窗口**（整条连接未确认的字节数）与**每 stream 窗口**（单个 stream 未确认的字节数），发送方必须同时满足两者才能发数据，任一为 0 就停。**stream 级**耗尽只卡那一条流（其它流还能用剩余连接窗口）；**连接级**耗尽则所有流一起停——因为所有流共享同一个连接窗口，这就是"多路复用下的队头阻塞"的另一种形态，与 TCP 丢包触发的阻塞**不同**：流控阻塞是"接收方处理慢/窗口没及时回补"的**主动限速**，丢包阻塞是"TCP 层重传、拥塞窗口收缩"的**被动限速**，两者可叠加。窗口上限直接决定吞吐：`max_throughput ≈ window / RTT`——65535 字节窗口、50ms RTT 的链路上，单流上限约 1.3MB/s；要跑满 10ms RTT 的 100Mbps，窗口得在 125KB 以上，所以 `SETTINGS_INITIAL_WINDOW_SIZE` 默认 64KB 常需调大，且接收端要及时 `WINDOW_UPDATE`。

取舍：调窗口不是越大越好——窗口越大，接收端需要缓冲的"在途数据"越多，慢消费者场景放大内存与丢包重传代价；正确做法是**按 BDP（带宽时延积）配窗口**，并让 `WINDOW_UPDATE` 的触发阈值基于"已消费"而非"已收到"（收到不等于应用读完，提前回窗口会把缓冲压力转嫁给接收端）。诊断要看两级窗口各自剩余量与 WINDOW_UPDATE 频率：连接窗口长期接近 0 说明接收端处理慢或更新不及时；单流窗口小但连接窗口充足则是流级窗口配置问题。

实战：事故形态是"HTTP/2 gRPC 大响应在特定网络下吞吐骤降、所有 stream 一起停"——排查先看连接级窗口。下面用纯 Python 模拟两级窗口：多个 stream 发送、连接窗口耗尽后全部停、某个 stream 收到 WINDOW_UPDATE 后恢复，并算出"窗口 / RTT"的吞吐上限。

```python
CONN_WIN = 65535
STREAM_WIN = 65535

class H2Flow:
    def __init__(self):
        self.conn = CONN_WIN
        self.streams = {}
    def send(self, sid, want):
        sw = self.streams.setdefault(sid, STREAM_WIN)
        n = min(want, sw, self.conn)
        self.streams[sid] = sw - n
        self.conn -= n
        return n
    def window_update(self, sid, n):
        self.streams[sid] = self.streams.get(sid, 0) + n
        self.conn += n

f = H2Flow()
for sid in (1, 3, 5):
    print(f"stream {sid} send 30000 ->", f.send(sid, 30000))
print("conn window left:", f.conn)
print("stream 1 send again ->", f.send(1, 30000), " <- 连接窗口耗尽，全停")

f.window_update(1, 65535)                 # 对 stream 1 的 WINDOW_UPDATE 也回补连接窗口
print("after WINDOW_UPDATE, stream 1 ->", f.send(1, 30000), " <- 连接窗口恢复，可继续")

# stream 级耗尽：把 stream 3 自己的窗口打空后，即便连接窗口还有也发不动
f.send(3, 40000)
print("stream 3 own window left:", f.streams[3])
print("stream 3 send again ->", f.send(3, 1000), " <- 流级窗口耗尽，单流停")

rtt = 0.05
print(f"throughput ceiling = window/RTT = {CONN_WIN}/{rtt} = {CONN_WIN/rtt/1024:.0f} KiB/s")
print("for 100Mbps @10ms need window >= ", int(100e6/8*0.01), "bytes")
```

**追问一**：stream 级窗口耗尽与连接级窗口耗尽，排查时怎么快速区分？——看"是否所有 stream 同时停"：只有一条流停、别的还能推进 → 该 stream 的窗口没回补（可能接收端应用没读这条流）；所有流一起停 → 连接窗口见底（接收端整体处理慢或 WINDOW_UPDATE 发得少）。`h2` 库可打印 `local_flow_control_window`/`remote_flow_control_window` 两个值做对照，或抓包看 WINDOW_UPDATE 帧的频率与增量。

**追问二**：为什么"收到数据就立刻 WINDOW_UPDATE"反而可能有害？——因为窗口表示"接收方愿意缓冲多少字节"，若应用还没读完就回补窗口，发送方会继续灌数据，数据堆积在接收端的 TCP/HTTP2 缓冲里，放大内存占用与端到端延迟（bufferbloat），一旦丢包还要重传更多在途数据。正确策略是基于"应用实际消费"回补，并配合消费速率设定回补增量——把背压信号真实地传回发送端。

## 背诵要点
- 两级流控：连接窗口 + 每 stream 窗口，发送需同时满足；连接窗口耗尽 → 所有 stream 停（跨流队头阻塞）。
- 流控阻塞是接收慢的主动限速，区别于 TCP 丢包/拥塞的被动限速，两者可叠加。
- 吞吐上限 ≈ 窗口 / RTT；按 BDP 配窗口，WINDOW_UPDATE 基于已消费量回补，避免 bufferbloat。

## 复盘追问
- HTTP/2 大响应在多 stream 下吞吐骤降且全部停住，如何用两级窗口排查并配窗口？（区分连接级/流级耗尽、BDP 计算、WINDOW_UPDATE 策略，讨论与丢包阻塞的叠加）
- 为什么"收到就回 WINDOW_UPDATE"会放大延迟？（窗口代表缓冲意愿，提前回补导致 bufferbloat，讨论基于消费量回补）
