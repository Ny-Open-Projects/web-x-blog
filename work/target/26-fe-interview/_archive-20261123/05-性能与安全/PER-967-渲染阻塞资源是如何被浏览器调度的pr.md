---
title: [PER-967] 渲染阻塞资源是如何被浏览器调度的？preload/priority 怎么影响
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-967：渲染阻塞资源是如何被浏览器调度的？preload/priority 怎么影响

**答**：
- 阻塞链：同步 CSS 阻塞渲染、同步 script 阻塞解析；浏览器 Preload Scanner 会提前发现 <link>/<script> 并按优先级发起请求。
- 优先级控制：fetchpriority="high/low" 直接指定（LCP 图片 high、非关键脚本 low）；preload 提升优先级但不执行；prefetch 降为空闲下载。
- 深水点：HTTP/2 下浏览器用可扩展优先级（priority hints）调度流；滥用 preload 会挤占带宽反而劣化 LCP。
- 方法：Performance 面板 Network 瀑布看 Priority 列，确认 LCP 资源是否 high 且无竞争。

```javascript
<head>
  <!-- LCP 图：提高优先级，不预载入内存 -->
  <link rel="preload" as="image" href="/hero.avif" fetchpriority="high">
  <!-- 非关键脚本：降低优先级，空闲执行 -->
  <script src="/analytics.js" defer fetchpriority="low"></script>
  <!-- 关键 CSS 保持阻塞但尽量小 -->
  <link rel="stylesheet" href="/critical.css">
  <!-- 早期提示：服务端 103 Early Hints 提前推送，此处配合 -->
</head>
<script>
// 验证：performance.getEntriesByType('resource') 的
// responseStart - requestStart 与 nextHopProtocol
const hero = performance.getEntriesByName('/hero.avif')[0];
console.log(hero?.deliveryType, hero?.nextHopProtocol);
</script>
```
