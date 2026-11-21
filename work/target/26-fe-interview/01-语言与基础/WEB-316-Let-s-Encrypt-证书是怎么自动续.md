---
title: [WEB-316] Let's Encrypt 证书是怎么自动续期的？ACME 的原理是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-316：Let's Encrypt 证书是怎么自动续期的？ACME 的原理是什么？
**答**：
- ACME 协议：客户端向 CA 证明"我控制这个域名"，验证方式有 HTTP-01（放指定文件到 /.well-known）、DNS-01（加指定 TXT 记录，支持通配符）、TLS-ALPN-01。
- 证明通过后 CA 签发 90 天证书；certbot/acme.sh/caddy 用定时任务在到期前自动续，失败要告警。
- 坑：多机部署时 HTTP-01 会随机命中任一台，需统一；通配符必须 DNS-01，需要 DNS API 权限。

```javascript
# DNS-01 续期（acme.sh 示例）
# acme.sh --issue -d '*.example.com' --dns dns_ali
# 验证: _acme-challenge.example.com TXT = "xxxx"
const acme = { challenge: 'dns-01', wildcard: true, validityDays: 90 };
const renew = days => days < 30 && '触发续期';
console.log('90 天有效期倒逼自动化，renew(20) =', renew(20));
```
