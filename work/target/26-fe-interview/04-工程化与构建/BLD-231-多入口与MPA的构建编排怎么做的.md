---
title: [BLD-231] 多入口（MPA）的构建编排怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-231：MPA 构建编排怎么做？
**答**：
- 入口声明：多入口配置（页面列表驱动——glob 或显式枚举）；每个入口独立 chunk 树 + 独立 HTML。
- 共享层设计：公共 chunk（多入口共同依赖自动提取——minChunks 阈值）+ 布局级共享（同模板入口共享）——避免「每入口都打包一份公共库」。
- 编排差异：不同入口不同构建配置（PostCSS/PWA/SSG——每入口覆盖）。
- MPA 的缓存特性：入口间独立——改 A 页不影响 B 页缓存（hash 隔离，天然优于 SPA 全量）。
- 追问钩子：为什么 MPA 的「公共 chunk 提取」要用 minChunks 阈值而不是全部提取——只有 2 个入口用到的库提取成公共 chunk 会让这两个入口各多一次请求（收益 < 开销）；minChunks: 3（3 个以上入口共享才提取）是请求数与缓存收益的平衡点——共享提取的收益公式 = 缓存节省 − 额外请求数。

```javascript
// vite MPA
input: Object.fromEntries(glob.sync('./pages/*/index.html').map(
  f => [path.basename(dirname(f)), resolve(f)]))
// rollup 公共提取
output.manualChunks(id) {
  if (sharedBy(id) >= 3) return 'common';             // minChunks 阈值
}
```
