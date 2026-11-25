---
title: [ARC-312] 组件库的按需加载与 Tree-shaking 如何真正生效？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-312：组件库的按需加载与 Tree-shaking 如何真正生效？
**答**：
- Tree-shaking 生效三条件：ESM 产物（sideEffects: false 标注）、无顶层副作用代码、import 具名引入。组件库的职责是把这三件事做扎实，而不是依赖 babel-plugin-import 转换（那是 ES5 时代的兜底）。
- 产物组织：`sideEffects: ["*.css", "**/style/*"]`——样式文件有副作用要保留，JS 可摇；入口 re-export 的 Barrel 文件（ARC-012）配合 sideEffects 标注可被正确摇树。
- 样式按需：CSS 拆分到组件目录（button/style/index.css），用户按组件引入；或 CSS-in-JS/CSS Variables 全局层（免拆分）。unplugin 自动 import 样式作为 DX 兜底。
- 验证：CI 里跑"体积审计"——demo 项目引 10% 组件，产物体积必须 ≤ 全量的 15%，防回归。

```json
// package.json
{
  "main": "lib/index.js", "module": "es/index.js",
  "sideEffects": ["*.css", "**/style/**"],
  "exports": { ".": { "import": "./es/index.js" }, "./button": { "import": "./es/button/index.js" } }
}
```
```typescript
// 摇树验证（CI）：demo 里只 import { Button } from 'ui'
// 产物分析：rollup-plugin-visualizer 对比 → button 引入后 bundle ≤ 15% of full
```
