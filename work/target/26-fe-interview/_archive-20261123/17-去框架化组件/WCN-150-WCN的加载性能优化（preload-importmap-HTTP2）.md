---
title: [WCN-150] WCN 的加载性能优化：modulepreload、importmap、HTTP2 汇流与体积预算怎么落地？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-150：WCN 的加载性能优化：modulepreload、importmap、HTTP2 汇流与体积预算怎么落地？

**答**：
- modulepreload：对首屏组件在 head 里声明 `<link rel="modulepreload">`，并行预取 + 预解析；非首屏组件走视口触发 import。
- importmap：集中管理组件与共享依赖的 URL 映射，灰度切版本只改 map；配合 es-module-shims 兼容旧浏览器。
- HTTP2/3 汇流：组件小文件多，同域 HTTP2 下多路复用无队头问题；但注意 CDN 边缘缓存命中率——chunk 稳定 hash + 版本目录隔离。
- 体积预算：CI 里对每个组件产物设阈值（如 gzip ≤ 8KB，共享 runtime ≤ 25KB），超限阻断；用 source-map-explorer 定位。
- 加载时序验证：Lighthouse/WebPageTest 观察 define 完成时间分布；`performance.mark('wc-defined:'+tag)` 全链路追踪。

```html
<link rel="modulepreload" href="https://cdn.acme.com/wc/button/1.4.2/button.js" crossorigin>
<script type="importmap">
{ "imports": {
  "acme/button": "https://cdn.acme.com/wc/button/1.4.2/button.js",
  "@acme/signals-core": "https://cdn.acme.com/vendor/signals-core/1.0.0/index.js" } }
</script>
<!-- 组件内部 import '@acme/signals-core' → 全站共享单份 runtime -->
```
