---
title: [WEB-561] QUIC 与代理/VPN/企业网关的兼容问题
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-561：QUIC 与代理/VPN/企业网关的兼容问题

**答**：
- HTTP 代理（正向代理）在 QUIC 下基本不可用：HTTP/3 的 CONNECT-UDP/MASQUE 是新机制，企业里大量老代理只支持 CONNECT over TCP
- 企业 SSL 解密网关（中间人证书）对 QUIC 要么拦截 UDP 迫使客户端回落 h2，要么需升级支持 QUIC 解密——迁移前必须摸清客户网络画像
- VPN 场景：全局 VPN 隧道内 QUIC 正常；但分流式 VPN/PAC 环境下 QUIC 直连可能绕过企业管控，触发安全策略封 UDP
- B 端产品的特殊性：你的 C 端灰度数据很漂亮，但 B 端客户（企业内网）可能一片失败——按「个人/企业」客群分别开 Alt-Svc
- 兜底闭环永远是「自动回落」：客户端 h3 失败自动回 h2 是底线保障，服务端做的只是别把失败地区往 h3 引

```text
客户画像分群:
  C端个人: h3 灰度正常路径
  B端企业: SSL解密网关/代理占比高 → 默认不下发 Alt-Svc, 白名单逐步放开
检测: 连接来源 ASN/企业出口 IP 段标记 → 策略路由
```
