---
title: [PER-1020] DNS 层的性能优化手段有哪些
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1020：DNS 层的性能优化手段有哪些

**答**：
- DNS 预解析：dns-prefetch 对后续可能用到的域提前解析；preconnect 包含 DNS+TCP+TLS 全链路。
- 分层缓存：浏览器缓存 → OS 缓存 → 本地 DNS → 权威 DNS；TTL 设置权衡缓存收益与故障切换速度。
- HTTPDNS：绕过运营商 LocalDNS 的劫持与调度不准问题，App 内收益大，Web 可通过服务端下发解析结果间接使用。
- 故障视角：DNS 是"最隐形也最致命"的一层——解析失败表现为白屏但常被误判为前端问题，需在监控中单独拆出。

```javascript
<link rel="dns-prefetch" href="//api.example.com">
<link rel="preconnect" href="https://cdn.example.com" crossorigin>
<script>
// DNS 阶段单独告警：domainLookupEnd-start 持续偏高时切换 HTTPDNS
const nav = performance.getEntriesByType('navigation')[0];
if (nav.domainLookupEnd - nav.domainLookupStart > 100)
  report({ type: 'dns-slow', ms: nav.domainLookupEnd - nav.domainLookupStart });
</script>
```
