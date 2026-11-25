---
title: [XP-217] 跨端 UI 一致性：设计 token 与组件库映射
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-217：跨端 UI 一致性：设计 token 与组件库映射

**答**：
- 题目：跨端 UI 一致性——设计 token（颜色/间距/字号）定义一次，映射到各端（Web CSS 变量/RN StyleSheet/Flutter ThemeData）。
- 思路：token 源（JSON/DSL）→ 代码生成器（输出各端样式文件）→ 组件库消费 token；暗色主题 = token 换组。
- 评分点：token 源单一；代码生成；暗色映射。

```javascript
// tokens.json（设计 token 源）
const tokens = {
  color: { primary: '#1890ff', danger: '#f5222d', bg: { light: '#fff', dark: '#1a1a1a' } },
  spacing: { xs: 4, sm: 8, md: 16, lg: 24 },
  fontSize: { sm: 12, md: 14, lg: 18 },
};
// 代码生成器输出：
// Web：--color-primary: #1890ff（CSS 变量）
// RN：export const colors = { primary: '#1890ff' };（StyleSheet）
// Flutter：Color primary = Color(0xFF1890FF);（ThemeData）
// 组件库消费 token → 一致性自动保障（改 token 全端生效）
// 暗色：tokens.color.bg.dark 组替换 → 三端同步切换
```
