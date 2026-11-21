---
title: [WEB-520] 多域名证书 SAN 与域名规划
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTPS]
type: 面试题
---

## WEB-520：多域名证书 SAN 与域名规划

**答**：
- SAN（Subject Alternative Name）：一张证书绑定多个域名（如 example.com、api.example.com、cdn.example.net），现代证书的主体字段就是 SAN 列表
- 泛域名（*.example.com）只能覆盖一级子域，`a.b.example.com` 不在 *.example.com 内——层级深了要叠加 SAN
- 规划权衡：多域合一签发方便但「一损俱损」且吊销影响面大；独立证书隔离故障但运维成本高
- 工程实践：核心业务域名独立证书，静态资源聚合到一张泛域名证书；域名清单集中管理，避免「证书漏了新域名」事故
- ACME 场景：DNS-01 验证配合泛域名证书是主流方案

```bash
openssl x509 -in cert.pem -noout -text | grep -A1 "Subject Alternative Name"
# DNS:example.com, DNS:*.example.com, DNS:api.example.net
```
