---
title: [NODE-708] 传输安全（TLS/mtls/内网加密）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-708：传输安全怎么做？
**答**：
- 外部 TLS：TLS 1.2+（1.3 优先——握手更快）、HSTS（强制 https——降级攻击防御）、证书轮换自动化（ACME——过期告警双保险，SCN-OPS-190 证书台账）。
- 内部 mTLS：服务间双向认证（零信任——内网也加密认证，防止内网横向移动）；证书分发（mesh/内部 CA）。
- TLS 配置审计：弱加密套件禁用、证书透明度、定期扫描（SSLLabs 等价扫描进 CI——配置漂移检测）。
- 敏感数据的应用层加密：TLS 之外对超敏感字段应用层加密（字段级——防日志/缓存泄露，SCN-FIN-509 联动）。
- 追问钩子：为什么内网也要 mTLS——「内网可信」假设在横向移动攻击下失效（攻破一台 → 内网明文全见）；mTLS 让每个调用都认证对端（证书即身份）——零信任模型的服务端落地，代价是证书管理复杂度（mesh 自动化是前提）。

```javascript
// mTLS 服务端
https.createServer({ cert, key, requestCert: true,
  ca: internalCA }, app);                              // 双向认证
// HSTS + TLS1.3
app.use(helmet.hsts({ maxAge: 31536000, includeSubDomains: true }));
```
