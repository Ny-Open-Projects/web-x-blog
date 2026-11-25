---
title: [WEB-549] QUIC Retry Token 与反放大机制要配合怎么用
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-549：QUIC Retry Token 与反放大机制要配合怎么用

**答**：
- 反放大是 QUIC 强制规则：服务器在验证客户端地址前，发送字节数不能超过收到的 3 倍，防 IP 伪造放大攻击（TCP SYN flood 的 QUIC 版）
- 代价：真实客户端也要多一次握手往返——服务端先回 Retry 包（带 token），客户端带 token 重发 Initial，服务端验证后才放开
- 实战取舍：高 DDoS 风险业务（C 端公网服务）开 Retry；内网/低风险业务可关，省 1 RTT
- Token 内容要含地址验证信息（IP 前缀 + 时间戳 + 服务端密钥签名），并在服务端校验时效，避免 token 被搬运重放
- 监控 Retry 命中率：token 失效率高（客户端换网络、时钟漂移、多实例密钥不一致）会白白多一次 RTT，多实例部署必须共享 Retry 密钥

```text
无 Retry: C:Initial → S:握手继续          (1 RTT 起)
有 Retry: C:Initial → S:Retry(token)
          C:Initial+token → S:验证后继续   (2 RTT 起, 但防放大)
多实例注意: token 签名密钥必须集群共享, 否则负载均衡到另一台就验证失败
```
