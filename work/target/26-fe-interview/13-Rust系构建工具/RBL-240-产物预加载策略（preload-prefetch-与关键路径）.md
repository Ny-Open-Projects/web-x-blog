---
title: [RBL-240] 产物预加载策略（preload/prefetch 与关键路径）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-240：产物预加载策略（preload/prefetch 与关键路径）

**答**:
- 关键路径：入口 chunk 同步加载（preload 关键 chunk），非关键路由用 prefetch（空闲时低优先级）；动态 import 触发的 chunk 由浏览器在 import 时拉取
- 工具注入：html 插件根据 chunk 关系注入 `<link rel="preload">`（当前路由必需）与 `rel="prefetch"`（可能的下一跳）
- 判定数据来源：路由→chunk 映射（构建期可算）+ 用户行为统计（runtime 数据回流决定 prefetch 名单）
- 反模式：全量 preload（带宽挤占首屏关键请求）、prefetch 一切（浪费）；预算制：每页 prefetch 限额

```html
<!-- 构建期注入 -->
<link rel="preload" href="/chunk-vendor.abc.js" as="script">
<link rel="prefetch" href="/chunk-product.abc.js" as="script">
<!-- prefetch 名单由「路由→chunk 映射 + 行为统计」联合决定 -->
```
