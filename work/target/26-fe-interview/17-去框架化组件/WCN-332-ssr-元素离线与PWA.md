---
title: [WCN-332] DSD 元素在离线/PWA 场景的行为（缓存 HTML 的元素）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-332：DSD 元素在离线/PWA 场景的行为（缓存 HTML 的元素）？
**答**：
- 缓存整页 HTML（含 DSD）→ 离线打开完整呈现（元素模板已在 HTML）。
- 水合：离线时实现 chunk 来自 SW 缓存（precache 或运行时缓存策略）。
- 版本一致性：HTML 与 chunk 缓存版本必须配套（cache key 带 build id）。
- 降级：chunk 缓存缺失 → 元素保持静态 DSD 内容（可读不可交互）+ 提示。

```javascript
// SW：build id 一致性
const BUILD = 'v2026.11.20-1';
caches.open(`ds-${BUILD}`).then(c => c.addAll(elementChunks));
// 离线：DSD 内容可读，chunk 缺失 → 静态降级提示
r
```
