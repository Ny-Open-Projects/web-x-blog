---
title: [PER-1213] 手写一个第三方 SDK 登记网关：未登记即拦截
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1213：手写一个第三方 SDK 登记网关：未登记即拦截

**答**：
- 需求：实现 VendorGate(registry)。registry 为 { domain: { fields, basis, region } }；inject(src) 加载脚本前校验其域名已登记且 region 允许（当前区域 CN 只允许 CN/全局）；未登记抛错并上报；wrapReport(vendor, payload) 按登记字段白名单过滤。
- 边界：src 非法 URL 抛错；basis=consent 且 consent 未授予则不加载（返回 null 而非抛错）；重复 inject 已加载域直接返回缓存。
- 评分点：域名登记校验；区域限制；同意门控；字段过滤

```javascript
class VendorGate {
  constructor(registry, consent) { this.registry = registry;
    this.consent = consent; this.loaded = new Set(); }
  inject(src, region = 'CN') {
    let host;
    try { host = new URL(src, location.href).host; }
    catch { throw new Error('bad url'); }
    const v = this.registry[host];
    if (!v) { report({ type: 'vendor-blocked', host }); throw new Error('未登记第三方'); }
    if (region === 'CN' && v.region === 'EU') throw new Error('区域不允许');
    if (v.basis === 'consent' && !this.consent.get().ads)
      return null;                                 // 未同意不加载
    if (this.loaded.has(host)) return { cached: true, host };
    const s = document.createElement('script');
    s.src = src;
    document.head.appendChild(s);
    this.loaded.add(host);
    return { host };
  }
  wrapReport(vendor, payload) {
    const v = this.registry[vendor];
    if (!v) return null;
    return Object.fromEntries(Object.entries(payload)
      .filter(([k]) => v.fields.includes(k)));
  }
}
```
