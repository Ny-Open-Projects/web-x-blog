---
title: [BLD-236] 资源内联与外部化（inline vs external）怎么权衡？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-236：内联与外部化怎么权衡？
**答**：
- 内联收益：省请求（RTT）、原子性（资源与代码同生命周期）；代价：不可缓存（随 chunk 变化）、体积膨胀（base64 +33%）、阻塞解析。
- 决策矩阵：高频复用小资源 → 内联（缓存无关且省请求）；一次性小资源 → 内联；大资源/高频变更 → 外部化（独立缓存）；关键渲染路径资源 → 内联或 preload（避免瀑布）。
- 特殊层：CSS 内联进 HTML（关键 CSS——首屏样式内联消 FOUC）vs 独立文件（全量样式可缓存）——首屏/全量的双通道。
- 追问钩子：为什么「关键 CSS 内联 + 全量 CSS 外链」是双通道而非二选一——内联首屏样式消除渲染阻塞（FOUC 消失），全量样式异步加载供后续路由；全内联则每路由样式都阻塞首屏，全外链则首屏有瀑布——双通道让「首屏速度」与「后续缓存」各取所得。

```javascript
// 关键 CSS 双通道
<style>${criticalCss}</style>                        // 首屏内联（构建提取）
<link rel="preload" href="full.css" as="style" onload="this.rel='stylesheet'">   // 全量异步
// 内联决策
assetsInlineLimit: (file, content) =>
  content.length < 4096 && isReused(file)            // 高频复用小图才内联
```
