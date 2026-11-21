---
title: "G10. Netty：Reactor 模型/粘包拆包/零拷贝？（高并发深挖追问）"
date: 2026-11-18
categories: [Java面试, 追问地图]
tags: [Java面试, 补漏卡, 33]
type: 补漏卡
disableNunjucks: true
---

### G10. Netty：Reactor 模型/粘包拆包/零拷贝？（高并发深挖追问）

**【参考回答（可背）】** 三块：
1. **Reactor 模型演进**：单 Reactor 单线程（Redis 模式）→ 单 Reactor 多工作线程 → **主从 Reactor 多线程**（Netty 默认：boss 接收连接、worker 处理 IO，EventLoop 绑定线程——一个 Channel 生命周期锁定一个 EventLoop，无锁串行处理）；
2. **粘包拆包**：TCP 是字节流无消息边界——Netty 解码器四种解法：定长、分隔符、**长度域解码器 LengthFieldBasedFrameDecoder**（最常用）、自定义；本质都是"在应用层定义消息边界"；
3. **零拷贝**：堆外内存（DirectBuffer 避免堆内→堆外拷贝）+ CompositeByteBuf（逻辑聚合不拷贝）+ FileRegion（sendfile）；呼应第 7 章 Kafka zero-copy。
**【追问链】** Netty 空轮询 bug？→ JDK epoll 空轮询导致 100% CPU，Netty 检测后重建 Selector。为什么业务网关用 WebFlux 而不直接 Netty？→ Netty 是传输层框架，业务网关要的是"协议+路由+过滤器"生态（WebFlux/自研），直接 Netty 的团队要自己补齐整栈——选型讲清层次。
**【P10 加分项】** "我们对自研长连接网关的选型结论：Netty 做接入层、业务逻辑走独立服务（网关只做编解码与路由）——'Netty 只做 IO，业务不进 EventLoop'是长连接网关稳定的第一原则。"
