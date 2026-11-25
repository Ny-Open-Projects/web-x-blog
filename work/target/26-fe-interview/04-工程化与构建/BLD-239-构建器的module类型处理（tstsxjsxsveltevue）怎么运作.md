---
title: [BLD-239] 打包器的多类型模块（ts/tsx/vue/svelte）怎么处理？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-239：多类型模块怎么处理？
**答**：
- 转换链：每类文件一个转换链（.ts → swc/esbuild 类型擦除；.vue → vue-loader 三段拆分 template/script/style；.svelte → 编译器输出 DOM 代码）——链的顺序（pre→normal→post）与并发处理。
- 类型擦除的边界：ts 转换只擦类型不检查（isolatedModules 语义）——类型检查独立（tsc --noEmit 进 CI，SCN-ENG-246）；const enum/命名空间等「需要全程序信息」的特性受限。
- 框架编译的产物特征：vue/svelte 编译器生成「带运行时依赖的组件代码」——scope 样式/style 的提取与 JS 分离处理（SCN-BLD-206）。
- 追问钩子：为什么 ts 转换「只擦不查」是性能与正确性的权衡——全程序类型检查需要跨文件类型图（慢，秒级）；单文件擦除是毫秒级（HMR 要求）——代价是跨文件类型错误（改了接口忘改调用方）构建期发现不了，必须用独立的 tsc --noEmit 补上——两者分工而不是二选一。

```javascript
// vite 链
{ test: /\.ts$/, use: 'esbuild-loader' }             // 擦除（快）
// CI: tsc --noEmit                                   // 检查（全程序）
// vue 三段
vue-loader → { template: compileTemplate, script: ts, style: postcss }
```
