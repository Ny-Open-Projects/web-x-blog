---
title: [WEB-420] 证书自动续期 ACME 是怎么工作的
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTPS]
type: 面试题
---

## WEB-420：证书自动续期 ACME 是怎么工作的

**答**：
- ACME 协议：客户端（如 certbot）向 CA 自动证明域名所有权，签发/续期证书，Let's Encrypt 是代表
- 两种验证方式：HTTP-01（在 `/.well-known/acme-challenge/` 放一个文件，CA 来访问）和 DNS-01（加一条 TXT 记录，支持泛域名）
- 证书 90 天有效，自动续期靠 cron/systemd timer，运维不再手动换证书
- 前端相关：证书过期事故八成出在自动续期链路（.timer 停了、challenge 被 CDN 拦、DNS-01 权限丢失），值得在监控里加「证书剩余天数」告警

```bash
# HTTP-01 要求该路径可被公网直接访问——CDN/网关不要缓存或拦截它
curl -I https://example.com/.well-known/acme-challenge/test
certbot renew --dry-run   # 演练续期，验证整条链路
```
