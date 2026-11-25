---
title: [WEB-406] 浏览器兼容策略：feature detect、UA 嗅探、polyfill 怎么选？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-406：浏览器兼容策略：feature detect、UA 嗅探、polyfill 怎么选？
**答**：
- 首选 feature detect（IntersectionObserver in window）+ 按需 polyfill：精准、不受 UA 伪造影响。
- UA 嗅探只在"能力无法探测"时用（已知浏览器 bug 区分），且用 UA-CH 的 Sec-CH-UA 结构化头更稳。
- 工程化：browserslist 定目标 → core-js/babel 精确注入；CSS 用 @supports 分支；错误兜底监控按浏览器聚合。

```javascript
if ('IntersectionObserver' in window) initLazy();
else { loadPolyfill('intersection-observer').then(initLazy); }
// CSS: @supports (backdrop-filter: blur(4px)) { ... }
console.log('探测能力 > 探测身份（UA）');
```
