---
title: [WCN-310] 元素库的包结构（per-element 入口/tree-shaking 友好）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-310：元素库的包结构（per-element 入口/tree-shaking 友好）？
**答**：
- 每元素独立入口（ds/goods-card）——消费方只打包用到的元素。
- sideEffects: false 声明 + 避免顶层副作用（注册放显式 define 函数或入口自动注册可选）。
- 自动注册入口（全量）与手动入口（按需）双入口。
- 审计：CI 检查「引一个元素带出全库」的打包事故。

```javascript
{
  "exports": { "./goods-card": "./dist/goods-card.js", "./all": "./dist/all.js" },
  "sideEffects": ["*.define.js"]
}
r
```
