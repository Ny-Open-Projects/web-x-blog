---
title: [RBL-291] Rspack 缓存内部：条目结构与失效钩子
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-291：Rspack 缓存内部：条目结构与失效钩子

**答**:
- 缓存条目：模块级（转换结果 + 依赖指纹）与产物级（chunk 渲染结果）双层；条目键 = 模块路径 + 变换链参数 hash + 内容 hash
- 失效传播：源文件变 → 该模块条目失效 → 引用链上的模块（受 live binding 影响）按依赖图重算——Rust 侧内存图直接传播，持久层按指纹懒失效
- 插件感知：invalidate 钩子让插件在缓存失效时清理自己的关联缓存（如自定义 loader 的外部数据）——漏清理是「缓存命中但结果错」的插件 bug
- 观测：experiments.cache 输出命中率与 miss 原因（rust 侧埋点），接入构建遥测看趋势

```javascript
// 插件缓存联动
compiler.hooks.invalidated?.tap?.('MyCache', (file) => myExtCache.delete(file))
// miss 原因分类：content-change / options-change / missing
```
