---
title: [FRP-363] 跨框架的 CDN 与缓存协同
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## FRP-363：跨框架的 CDN 与缓存协同

**答**：
- 产物分层缓存：内核 chunk（稳定 → immutable 长缓存）、框架 runtime（版本化 → 长）、壳与应用（发版频繁 → 短/协商）——缓存层级与发布节奏对齐
- 跨应用共享 chunk 的缓存收益：module federation shared（React 单例）命中率高——「版本兼容范围」决定共享是否安全
- 缓存失效协同：子应用发版不影响主应用缓存——独立 hash 路径；「内核升级」→ 所有壳 chunk hash 变化（缓存全失效）——内核升级频率的约束
- 预加载协同：跨框架导航预取（CDN 层 prefetch hint）——`<link rel=preload>` 注入协议
- 深水点：CDN 缓存 key 的 query 参数规范化（子应用版本参数剥离）——命中率与版本控制的平衡

```text
缓存分层:
  core chunk:    immutable, max-age=1y (内核稳定)
  react runtime: versioned, max-age=1y
  app chunks:    hash, max-age=7d (发布频繁)
  html:          no-cache (协商)
内核升级 = 全部壳缓存失效 → 内核升级低频化 (聚合 minor)
```
