---
title: [PER-441] HTTP/3 (QUIC) 的弱网收益：0-RTT、连接迁移与队头消除对真实弱网用户的量化影响？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-441：HTTP/3 (QUIC) 的弱网收益：0-RTT、连接迁移与队头消除的量化影响？

**答**:
- 三个弱网收益机制：① 握手 0/1-RTT——TCP+TLS1.2 要 3 RTT，QUIC 首连 1-RTT、重连 0-RTT，弱网（RTT 300ms）省 600~900ms 建连；② 连接迁移——基于 Connection ID 而非四元组，WiFi↔蜂窝切换不断连（弱网切换高频场景的体验救星）；③ 无队头阻塞——QUIC 流级独立重传，一个丢包不再阻塞所有流（HTTP/2 TCP 层队头阻塞在高丢包率下吞吐腰斩）。
- 量化参考（业界公开数据）：高丢包（2%+）场景 HTTP/3 吞吐比 H2 高 30%~50%；0-RTT 让重复访问首字节提前 1~2 RTT。
- 前端侧配合：Alt-Svc 头让浏览器发现 H3（`alt=":443" h3=":443"`）；CDN/网关开启 H3；0-RTT 的安全边界（0-RTT 数据可被重放——只用于幂等 GET，写接口禁 0-RTT，服务端配置）。
- 验收：RUM 按协议版本切片（Navigation Timing 的 nextHopProtocol === 'h3'），对比弱网下 h2 vs h3 的 TTFB/加载时长分布——用自家数据说话。

```text
H3 弱网收益机制与量化：
0/1-RTT 握手：弱网（RTT 300ms）省 600~900ms 建连；重连 0-RTT
连接迁移：WiFi↔蜂窝切换不断连（Connection ID）—— 弱网切换体验
无队头阻塞：2% 丢包下吞吐比 H2 高 30~50%（流级独立重传）
前端配合：Alt-Svc: h3=":443"；服务端 0-RTT 仅限幂等 GET（重放风险）
验收：RUM nextHopProtocol 切片（h2 vs h3）弱网 TTFB 分布对比 —— 用自家数据
```
