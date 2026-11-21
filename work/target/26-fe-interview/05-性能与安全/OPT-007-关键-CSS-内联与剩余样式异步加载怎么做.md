---
title: [OPT-007] 关键 CSS 内联与剩余样式异步加载怎么做？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-007：关键 CSS 内联与剩余样式异步加载怎么做？

**答**：
- 渲染阻塞资源中 CSS 最容易被忽视：`<link rel="stylesheet">` 会阻塞首次渲染。
- 落地：提取首屏必需的关键 CSS（约 14KB 内）内联到 `<style>`，剩余样式异步加载。
- 异步加载的经典技巧是 `media="print"` 交换法或 `preload + onload`，两者都在不阻塞渲染的前提下提前下载。
- 工具链：critters（Vite 插件）、penthouse、Critical 可自动提取；注意内联样式无法被单独缓存，权衡后只内联真正关键的少量规则。

```html
<!-- 一一对应：关键 CSS 内联 + 剩余样式两种异步加载技巧 -->
<style>
  /* 首屏关键 CSS 内联：布局骨架、首屏文案样式 */
  header, .hero { display: block; }
  .hero { height: 300px; background: #f5f5f5; }
</style>

<!-- 技巧一：media=print 交换法。print 不阻塞渲染，加载完切回 all 生效 -->
<link rel="stylesheet" href="/styles/full.css" media="print" onload="this.media='all'" />

<!-- 技巧二：preload 提前下载，onload 时改为正式样式表 -->
<link rel="preload" href="/styles/full.css" as="style" onload="this.rel='stylesheet'" />

<!-- 兜底：JS 被禁用时仍能同步加载完整样式 -->
<noscript><link rel="stylesheet" href="/styles/full.css" /></noscript>
```
