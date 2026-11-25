---
title: [RBL-238] Tree-shaking 失效的排查路径
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-238：Tree-shaking 失效的排查路径

**答**:
- 排查五步：①包是否有 ESM 构建（只发 CJS 必失效）→ ②sideEffects 配置是否正确（false/白名单）→ ③引入方式（`import { x } from 'pkg'` vs `import pkg`；babel 转译是否破坏语法）→ ④副作用代码（顶层 IIFE/ polyfill）→ ⑤bundler 特定（动态 require/装饰器/Proxy 逃逸）
- 工具链证据：Rspack stats 的 `usedExports`/`providedExports` 与 `optimization.usedExports`，看具体导出是否被标记 used
- 验证手段：产物内 grep 目标符号（未引用符号不该出现）；stats 里 unused 导出数统计趋势
- 高发场景清单：barrel 文件（index.ts 重导出全量）、类静态副作用、CSS-in-JS 注册、polyfill 库

```javascript
// stats 证据
// usedExports: true → webpack/rspack 标记每模块的 used exports
// barrel 失效例：index.ts export * from './a'; './b' —— sideEffects:false + 明确导出才可剪
```
