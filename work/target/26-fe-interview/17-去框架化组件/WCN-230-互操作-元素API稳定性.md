---
title: [WCN-230] 自定义元素公开 API（property/事件/part）的稳定性治理？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-230：自定义元素公开 API（property/事件/part）的稳定性治理？
**答**：
- API 清单显式化并版本化（元素 README 的 API 表 + 类型文件是契约）。
- 弃用流程：标记 @deprecated + 控制台警告 → 两个 minor 后移除（major 发布）。
- 不稳定实验 API 用下划线前缀或独立实验标签（goods-card-experimental）。
- CI 校验：API diff（类型文件对比）进发布流水线，breaking 需人工确认。

```javascript
/** @deprecated 使用 count 替代。将在 v6 移除 */
set num(v) { console.warn('[goods-card] num 已弃用，改用 count'); this.count = v; }
// CI: api-diff → breaking 变更阻断自动发版
r
```
