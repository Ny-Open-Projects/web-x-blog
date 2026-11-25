---
title: [BLD-206] CSS 的构建处理（提取/作用域/变量）怎么运作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-206：CSS 构建处理怎么运作？
**答**：
- 管线：CSS 入口（import/style 标签）→ 转换（postcss：autoprefixer/嵌套/变量兼容）→ 提取（mini-css-extract/vite 独立 chunk）→ 压缩（cssnano）→ 与 JS 的加载顺序协调（FOUC 防御：样式 chunk 与路由 chunk 关联预载）。
- 作用域方案构建差异：CSS Modules（类名 hash）、CSS-in-JS（运行时 or 编译期提取——Linaria/vanilla-extract 构建期零运行时）、Tailwind（按内容扫描生成，JIT）。
- CSS 代码分割：异步 chunk 的样式拆分（路由样式只随路由加载）+ 关键 CSS 内联（SSR 场景提取首屏样式）。
- 缓存友好：内容 hash 文件名；Tailwind 全量重建问题（内容变更导致 hash 变化——影响缓存命中）。
- 追问钩子：为什么 CSS-in-JS 的「构建期提取」（vanilla-extract）优于「运行时注入」——运行时注入 = 样式随 JS 执行才出现（FOUC + 阻塞渲染路径）+ 序列化开销；构建期提取产出静态 CSS 文件（可缓存可 preload），是性能与 SSR 兼容的正解。

```javascript
// vite: 异步路由样式自动拆分 + 预载
// rollup: cssCodeSplit: true → route-abc123.css 与 route chunk 同步加载
// vanilla-extract: styles.css.ts → 构建期产出 .css（零运行时）
import { style } from '@vanilla-extract/css';
export const card = style({ display: 'flex' });      // 编译期生成类名+CSS
```
