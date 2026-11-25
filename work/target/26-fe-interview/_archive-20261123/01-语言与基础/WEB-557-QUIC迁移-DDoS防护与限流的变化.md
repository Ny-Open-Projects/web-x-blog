---
title: [WEB-557] QUIC 迁移后 DDoS 防护与限流的变化
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-557：QUIC 迁移后 DDoS 防护与限流的变化

**答**：
- UDP 无连接特性让反射/洪泛面变化：QUIC Initial 有反放大限制（≤3x），但攻击者可伪造大量 Initial 消耗服务端 CPU（握手计算），防护重点从「带宽」转向「握手 CPU」
- 必开 Retry/地址验证：让未验证地址的包最多回 Retry 包，计算成本压到最低；进一步可对可疑 IP 段直接丢 Initial
- Session resumption token 也可能被滥用刷 0-RTT：token 签发要限频 + 绑定客户端指纹，0-RTT 处理有 CPU 成本
- 限流维度调整：TCP 时代按连接数限流，QUIC 连接建立极快且单连接多流，要按「Connection ID + 请求速率 + 流数」多维限流
- 与安全设备兼容：很多老 WAF/IDS 不解析 QUIC（加密后中间盒不可见），迁移后要确认安全设备是「旁路解密」还是「仅在 TLS 终止点之后检测」，避免防护盲区

```text
防护栈变化:
  边缘: 丢伪造 Initial (地址未验证只回 Retry)
  网关: 按 CID + IP 双维限速 / 0-RTT token 限频
  应用: 业务限流保持不变 (在 TLS 终止后, 语义可见)
盲区检查: 老入侵检测设备在 UDP 443 上是否形同虚设?
```
