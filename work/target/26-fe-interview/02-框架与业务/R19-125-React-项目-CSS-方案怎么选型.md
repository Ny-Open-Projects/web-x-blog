---
title: [R19-125] React 项目 CSS 方案怎么选型？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-125：React 项目 CSS 方案怎么选型？
**答**：
- Tailwind：原子类零命名成本、约束强，适合中后台与新起的设计系统；代价是 JSX 里类名冗长、团队需统一约定。
- CSS Modules：编译期作用域隔离，学习成本最低，适合老项目渐进迁移。
- vanilla-extract：TypeScript 写样式、构建期产出零运行时 CSS，RSC 友好，是 CSS-in-JS 的替代升级。
- styled-components 等运行时 CSS-in-JS：动态主题能力强，但运行时开销 + RSC 兼容成本，新项目慎选。

```jsx
// CSS 方案选型：按"隔离强度 + 团队规模 + 渲染模式"决策

// 1. Tailwind：原子类，零命名成本，设计约束强
<button className="rounded-md bg-blue-500 px-4 py-2 text-white hover:bg-blue-600">
  提交
</button>

// 2. CSS Modules：编译期作用域隔离，适合渐进迁移
import styles from './Card.module.css';
<div className={styles.card}>{children}</div>

// 3. vanilla-extract：TypeScript 写样式、构建期生成、零运行时，RSC 友好
// theme.css.ts
// import { createTheme } from '@vanilla-extract/css';
// export const [lightTheme, darkTheme] = createTheme(
//   { vars: { colorPrimary: '#1677ff' } },
//   { vars: { colorPrimary: '#0958d9' } },
// );

// 4. styled-components 等运行时 CSS-in-JS：RSC 下有额外客户端成本，新项目慎选
```
