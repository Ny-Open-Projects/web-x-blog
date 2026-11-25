---
title: [H5-328] WebView 内核版本碎片化：兼容策略怎么定
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, Hybrid]
type: 面试题
---

## H5-328：WebView 内核版本碎片化：兼容策略怎么定

**答**：
- Android WebView 跟随系统/内核版本碎片化严重：老机型 Chromium 50~70 缺 CSS 特性、WebAssembly/ES2017+、Flexible API；iOS WKWebView 跟随系统版本相对收敛
- 基线策略：明确「支持矩阵」——功能分三档（全量支持/降级可用/不支持提示升级），用特性检测（不是 UA）分档执行
- 构建层兜底：Babel/core-js 按目标内核（如 Chromium 57）转译，CSS 用 postcss autoprefixer 加前缀；体积敏感时按内核版本下发不同 bundle（服务端 UA 分流）
- 能力探测优先于版本判断：`'fetch' in window`、CSS.supports()、WebAssembly.validate；版本号只做统计归因
- 监控归因：报错上报带 webviewVersion 字段，聚合出「崩溃/报错 top 内核版本」指导降级决策

```javascript
const CAPS = {
  wasm: (() => { try { return WebAssembly.validate(new Uint8Array([0,97,115,109,1,0,0,0])); } catch { return false; } })(),
  fetch: 'fetch' in window,
  IntersectionObserver: 'IntersectionObserver' in window,
  webp: new Image().src === 'data:image/webp;base64,UklGRhoAAABXRUJQVlA4TA0AAAAvAAAAEAcQERGIiP4HAA==',
};
window.__CAPS__ = CAPS;
// 降级执行: 不支持 IO 用 scroll 监听懒加载
const lazy = CAPS.IntersectionObserver ? ioLazy : scrollLazy;
```
