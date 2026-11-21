---
title: [BAS-004] defer 和 async 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-004：defer 和 async 有什么区别？
**答**：
- 共同点：都让外部 script 异步下载，不阻塞 HTML 解析。
- async：下载完立即执行，多个脚本执行顺序不保证，适合统计、埋点等独立脚本。
- defer：下载完后按出现顺序、在 DOMContentLoaded 之前执行，适合依赖 DOM 的主逻辑。
- 动态创建的 script 默认行为等同 async，需要顺序时设 `script.async = false`。

```html
<script async src="analytics.js"></script>
<!-- async：下载完立即执行，与其他脚本的相对顺序不保证 -->
<script defer src="vendor.js"></script>
<script defer src="app.js"></script>
<!-- defer：严格按出现顺序执行，且都早于 DOMContentLoaded 事件 -->
```
