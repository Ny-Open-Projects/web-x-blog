---
title: [WEB-428] 部署 HTTP/3 前要做哪些评估
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTP3]
type: 面试题
---

## WEB-428：部署 HTTP/3 前要做哪些评估

**答**：
- 传输评估：公司网络/目标用户运营商对 UDP 443 是否友好（有企业防火墙整段拦 UDP），要有 H2 回退
- 证书与协议：TLS 1.3 必备、证书要覆盖所有域名、QUIC 要求更完整的证书链
- CDN/负载均衡：确认接入层支持（或已支持）QUIC，Alt-Svc 头如何下发，多机房 CID 路由是否一致
- 观测体系：H3 下抓包能力下降，先补 RUM 指标（nextHopProtocol、TTFB 分布）再灰度
- 灰度策略：先用 Alt-Svc 引导少量流量（Chrome 可 chrome://flags 控制），对比 TTFB/错误率再放量

```bash
# 验证站点是否真的支持 H3
curl --http3 -I https://example.com 2>&1 | head -3
# 检查 Alt-Svc 通告
curl -sI https://example.com | grep -i alt-svc
```
