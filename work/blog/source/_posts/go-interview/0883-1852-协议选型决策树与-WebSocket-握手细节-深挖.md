---
disableNunjucks: true
title: "1852 协议选型决策树与 WebSocket 握手细节 深挖"
date: 2026-10-10 09:17:31
categories: [Go面试题集]
tags: [Go面试题集]
---

> 覆盖源 18-52 全文：按「通信模式 × 性能诉求 × 边界内外」三维做协议选型、WebSocket 升级握手的逐字段拆解、HTTP/2 如何改写「RPC 必快」的旧结论、RPC 框架的序列化账本。主卡已给三大协议的分工与分帧实测，本附录做选型决策与握手细节四层深挖。

## 思路与架构

```text
通信需求 -> 协议选型决策树
├─ 一问一答、客户端主动? -> HTTP/REST
│   ├─ 对外开放、多端、免 SDK -> 首选 (通用性最强)
│   └─ 性能敏感内网? -> 可换 RPC
├─ 服务端要主动推 / 双向实时? -> WebSocket
│   ├─ 聊天/游戏/行情/协同编辑
│   └─ 退化方案: SSE(单向推送) / 轮询(简单但低效)
└─ 内部微服务间高频调用? -> RPC (gRPC/thrift)
    ├─ 强类型接口 + 代码生成 + 长连接复用
    └─ 流式需求 -> gRPC streaming (基于 HTTP/2)
```

## 方案取舍
- **WebSocket 握手的逐字段拆解**：客户端发普通 HTTP GET + `Upgrade: websocket` + `Connection: Upgrade` + `Sec-WebSocket-Key`（随机 base64）；服务器回 **101 Switching Protocols** + `Sec-WebSocket-Accept`（对 Key 拼 GUID 后 SHA-1 base64，客户端校验防误升级）。升级完成后同一 TCP 连接改用**帧协议**（操作码 + 载荷，带掩码），与 HTTP 文本语义彻底告别。**借道 HTTP 的妙处**：复用 80/443 端口与既有基础设施（代理、证书），部署零成本 [源码]。
- **为什么「服务器主动推送」轮询撑不住**：HTTP/1.1 半双工下只能轮询——间隔短则大量无效请求（大多数轮空），间隔长则实时性差，且每次请求都带完整头部开销。WebSocket 把「问有没有」变成「来了就推」，消息延迟从轮询间隔级降到毫秒级，流量从 O(轮询次数×头大小) 降到 O(消息量)。中间态方案 SSE（Server-Sent Events）适合纯单向推送，比 WebSocket 轻但不能反向发 [经验]。
- **HTTP/2 改写了什么**：旧结论「RPC 比 HTTP 快」建立在 HTTP/1.1 的三个弱点上——文本协议解析贵、每请求一线程/连接、队头阻塞。HTTP/2 用**二进制分帧 + 单连接多路复用 + 头部压缩（HPACK）**逐一化解，性能上反超一批 RPC 实现。所以现代选型的重心从「快不快」转向「**接口治理**」：RPC 框架的强类型 IDL（proto/thrift 文件）、代码生成、服务发现、负载均衡、超时重试的**工程配套**才是选型决定因素 [经验]。
- **RPC 性能账本的另一半在序列化**：HTTP/1.1+JSON 的成本大头常在**文本序列化/反序列化**而非传输；gRPC + protobuf 用二进制变长编码 + 字段编号，体积小数倍、编解码快数倍。但 JSON 的人类可读性与调试便利是真实价值——**内部高频链路用 protobuf，边缘调试接口留 JSON**，是常见折中 [经验]。
- **「对外 HTTP 对内 RPC」的架构依据**：对外 HTTP 的价值是**生态通用**（任何语言/浏览器/curl 都能调）与安全边界清晰；对内 RPC 的价值是**契约强约束**（proto 变更编译期暴露）与连接复用。BS/CS 融合后这条分界线依然成立——它分的是「信任域内外」，不是「新旧技术」 [经验]。

## 答题技巧
- 先立「TCP 给流、协议给边界」的总纲，再按场景分派三个协议——结构感比名词罗列值钱 [经验]。
- 被问「WebSocket 和 socket 什么关系」→ 答没关系（纯命名巧合），顺带展示握手 101 与帧格式细节 [经验]。
- 被问「RPC 一定比 HTTP 快吗」→ 拿 HTTP/2 反例压住绝对化结论，再把话题引到「序列化 + 接口治理」，从背结论升级为讲权衡 [经验]。
- 手写分帧代码主动上：length-prefix 三行核心（写长度头 → ReadFull 头 → ReadFull 体），实测三帧还原，证明懂「流 vs 消息」 [实测]。
- 主动边界到 `1849-http-vs-tcp-keepalive`（HTTP 长连接与 TCP keepalive 两层含义）、`1853-http-render-close`、`713-http-graceful-shutdown`（连接生命周期工程侧），构成网络协议专题 [边界]。

## 细节与核心 API

```go
// 协议选型决策树（面试口述）：
//  需可靠有序流式？ -> TCP（HTTP/gRPC/DB）
//  需极低延迟/可丢？ -> UDP（DNS/音视频/游戏，自管重传）
//  请求-响应为主？   -> HTTP/1.1 或 HTTP/2
//  服务端主动推送？   -> WebSocket / SSE / gRPC stream
//  跨语言/强契约？   -> gRPC（HTTP/2 + protobuf）
// WebSocket 握手：HTTP Upgrade 升级，之后脱离 HTTP 帧，走 WS 帧
//  Go 示例（gorilla/websocket）：
upgrader := websocket.Upgrader{}
conn, _ := upgrader.Upgrade(w, r, nil) // 响应 101 Switching Protocols
for { _, msg, _ := conn.ReadMessage(); conn.WriteMessage(1, msg) } // 双向帧
// 关键：Upgrade 请求须带 Sec-WebSocket-Key/Version；握手失败回 400；之后是 WS 数据帧
```
