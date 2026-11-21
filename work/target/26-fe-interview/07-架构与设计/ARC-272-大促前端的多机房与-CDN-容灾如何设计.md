---
title: [ARC-272] 大促前端的多机房与 CDN 容灾如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-272：大促前端的多机房与 CDN 容灾如何设计？
**答**：
- 静态资源容灾：多 CDN 厂商互备（主+备，健康度自动切换）；HTML 是关键（不可长缓存）——边缘动态加速+源站多机房，HTML 加载失败走**本地兜底版本**（Service Worker 缓存的上次可用 HTML，标注"离线模式"）。
- 接口容灾：核心读接口同城双机房热备，前端做域名级自动切换（API 网关+多域名探测）；写接口不前端切换（一致性优先），失败给明确提示。
- 切换决策：前端探测（请求失败率+延迟）上报，网关/全局流量管理做切换；前端不做本地自动切域名（易放大故障），只上报+被动接受切换。
- 演练：T-7 前真实切一次备 CDN（灰度 1% 起），验证 DNS/TTL、证书、缓存预热全链路。

```typescript
// Service Worker HTML 兜底
self.addEventListener('fetch', (e) => {
  if (e.request.mode === 'navigate') {
    e.respondWith(fetch(e.request).catch(() => caches.match('/__fallback_home__', { ignoreSearch: true })));
  }
});
// 备 CDN 预热：warmupCdn('backup', topResources) 在 T-7 执行；探测上报：
reportProbe({ cdn: current, failRate: window5m.failRate, p95: window5m.p95 })  // GTM 据此切换
```
