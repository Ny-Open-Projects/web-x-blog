---
title: [WEB-345] hash / chunkhash / contenthash 有什么区别？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-345：hash / chunkhash / contenthash 有什么区别？
**答**：
- hash：整个构建的哈希，任一文件改动全变——js/css 会一起失效，缓存利用率低。
- chunkhash：按入口/分块粒度，同一 chunk 内改动才变，适合 js。
- contenthash：按文件内容，css 抽离（MiniCssExtractPlugin）必用，css 没改就不变；现代 vite 直接按内容 hash，三者概念弱化但面试仍考。

```javascript
const names = {
  js: '[name].[chunkhash:8].js',      // chunk 级
  css: '[name].[contenthash:8].css',  // 内容级（css extract 必须）
  lib: '[name].[hash:8].js',          // 全局（不推荐主资源用）
};
// vendor 未动 → chunkhash 不变 → 用户 vendor 依然命中缓存
console.log('目标：改动最小化 → 失效文件最少');
```
