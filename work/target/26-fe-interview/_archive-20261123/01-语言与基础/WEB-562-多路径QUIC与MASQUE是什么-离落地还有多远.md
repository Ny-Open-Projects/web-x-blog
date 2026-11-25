---
title: [WEB-562] 多路径 QUIC 与 MASQUE 是什么，离落地有多远
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-562：多路径 QUIC 与 MASQUE 是什么，离落地有多远

**答**：
- 多路径 QUIC（MPQUIC，draft）：一条 QUIC 连接同时用多条路径（Wi-Fi + 蜂窝）传数据，目标是无缝切换与聚合带宽，还在草案阶段，浏览器未开放
- MASQUE：基于 QUIC 的代理标准（CONNECT-UDP/CONNECT-IP），解决「HTTP/3 时代怎么做代理/VPN」，是正向代理的正统替代
- 现实可用的近似形态：App 内嵌 cronet 类客户端可自己做多路径调度（双通道各自建连、应用层聚合），这是「伪多路径」，很多大厂弱网优化实际这么干
- 前端视角：MPQUIC/MASQUE 落地主要影响 App/网关架构，纯浏览器端短期接触不到；面试能讲清「是什么、解决什么、谁会用」即可
- 关注点：连接迁移只是「换路径续传」，多路径是「同时用多条」，不要混为一谈——后者才有带宽聚合

```text
连接迁移: Wi-Fi断 → 蜂窝接管 (先后使用, 单路径)
多路径:   Wi-Fi+蜂窝同时传不同流 (并发, 聚合带宽+无缝切换)
MASQUE:   CONNECT-UDP(代理UDP流量) / CONNECT-IP(三层VPN替代)
```
