---
title: [Q6005] 多 worker 下的会话粘性为什么靠不住
date: 2026-11-18
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6005 · SSE/WebSocket 多 worker 下的会话粘性为什么靠不住

> 难度:★★★ | 标签:uvicorn, SSE, WebSocket, 水平扩展

**问**：uvicorn 起多个 worker（或多副本 pod）跑 SSE/WebSocket，负载均衡配「会话粘性」能解决问题吗？长连接场景的正确架构是什么？

**答**：粘性只解决「找到连接」，解决不了另外两个更硬的问题：1) **广播天然跨进程**：每个 worker 的连接注册表只覆盖自己进程内的连接，用户 A 在 worker1、用户 B 在 worker2，房间广播靠进程内遍历必然漏人——粘性路由是对单个客户端而言的，房间的成员分布你控制不了；2) **粘性是延迟故障**：worker 重启、扩缩容、健康剔除都会甩掉粘住的长连接，如果客户端没有重连+状态恢复能力（SSE `Last-Event-ID`、WS 重连后重新订阅），粘性只是把「必现故障」变成「偶发故障」。正确架构是**无粘性 + 外部总线**：连接落在哪个 worker 都行，跨 worker 消息走 Redis pub/sub（或 MQ），每个 worker 订阅频道后转发给本进程成员——任何 worker 都能服务任何会话，水平扩展天然成立，某 worker 挂掉只影响它上面的连接（客户端重连即恢复）。粘性仍有两个合理小场景：进程内缓存亲和（省一次缓存回源）、以及 pub/sub 未就绪时的过渡方案；但要明确它不承载正确性。

```python
# 基线:uvicorn workers>1 / Redis 6-7。本 demo 用标准库模拟两 worker 的注册表与总线,直接运行。
import threading, time

class WorkerSim:
    """模拟一个 worker:进程内注册表只看得到自己的连接"""
    def __init__(self, wid, bus):
        self.wid, self.bus, self.conns = wid, bus, {}
        bus.register(self)                      # 正解:所有 worker 订阅同一总线

    def accept(self, uid):
        self.conns[uid] = f"ws-{uid}"
        print(f"worker{self.wid} accept {uid}(本进程连接:{list(self.conns)})")

    def local_broadcast(self, room, msg):
        hit = [u for u in self.conns]
        print(f"worker{self.wid} 本地广播 → {hit}(看不到其他 worker 的连接!)")
        return hit

    def on_bus_message(self, room, msg):
        self.local_broadcast(room, msg)

class Bus:
    """外部总线(Redis pub/sub 的本地模拟):跨 worker 广播的事实源"""
    def __init__(self):
        self.workers = []
    def register(self, w):
        self.workers.append(w)
    def publish(self, room, msg):
        for w in self.workers:                  # 等价于 Redis pub/sub 分发给订阅者
            w.on_bus_message(room, msg)

bus = Bus()
w1, w2 = WorkerSim(1, bus), WorkerSim(2, bus)
w1.accept("alice")   # alice 落在 worker1 —— 粘性路由保证她下次还在 w1
w2.accept("bob")     # bob 落在 worker2
print("--- 房间广播『你们都来了』 ---")
w1.local_broadcast("room", "hi")   # 粘性视角:只发给自己进程 → bob 漏收
bus.publish("room", "hi")          # 总线视角:每个 worker 都转发 → 无一漏收
```

**追问**：
1) Redis pub/sub 挂了或丢消息怎么办？——pub/sub 是 fire-and-forget，订阅断线期间的发布不补投。要求不丢的推送（订单状态变更）改用 Redis Streams/带 ack 的 MQ，按用户消费位回放；pub/sub 只适合「丢了可容忍/可重查」的通知。
2) SSE 断线重连的服务端要配合什么？——维护每连接的单调事件序号（或事件 ID），响应 `Last-Event-ID` 头从回放缓冲（或历史表）补发缺口；补不齐就下发「快照+新游标」。没有这套序号机制，重连窗口内的事件就是黑洞。
3) 多 worker 下进程内限流/在途计数还有效吗？——无效，退化为每 worker 各自一份；全局限流必须落到共享存储（Redis INCR），这也是为什么「本地内存限流在多 worker 下不可信」。
