---
title: [WEB-553] QUIC 丢包恢复：PTO 与快速重传的实战理解
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-553：QUIC 丢包恢复：PTO 与快速重传的实战理解

**答**：
- QUIC 每个包都带包号且单调递增、ACK 不含 RTT 采样的歧义（TCP 有重传歧义问题），RTT 估计更准，RTO/PTO 触发更及时
- PTO（Probe Timeout）：ACK 迟迟不来时主动发探测包（携带新数据或重传），不依赖「某个包超时」这一 TCP 弱信号，弱网下恢复更快
- 快速重传靠「ACK 中标记的丢包范围 + 3 个更高包号确认」判定，QUIC ACK Frame 能一次确认多个区间，信息密度高于 TCP SACK
- 实战含义：h3 在 2~3% 丢包下吞吐衰减明显小于 h2，这是弱网收益的主要来源；迁移效果评估要做「注入丢包」的对照压测
- 前端侧能感知的证据：弱网地区 h3 请求的 P75/P95 长尾显著短于 h2，但均值可能接近——评估要看长尾而不是均值

```text
丢包判定: ACK 区间出现空洞 + 后续 3 个包被确认 → 立即重传
探测: PTO = smoothRTT + 4*RTTvar + max_ack_delay → 发 probe
对照压测: tc/netem 注 2% loss, h3 吞吐保持 ~85%, h2 跌到 ~40%
```
