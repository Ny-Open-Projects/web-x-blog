---
title: [BLD-281] 框架无关产物（Web Components/多框架输出）怎么构建？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-281：框架无关产物怎么构建？
**答**：
- 产物形态：Web Components（自定义元素——零框架依赖）/多框架封装层（React wrapper/Vue wrapper 各自薄层）/vanilla 核心框架适配器——核心逻辑与框架层分离构建。
- 构建要点：核心库零依赖（framework-agnostic——tree-shake 友好）；wrapper 层声明 peer（react/vue 各自 external）；样式作用域（shadow DOM 内 CSS 构建——SCN-BLD-206）。
- 多产物组织：一源多产物（core + react + vue 三个 entry）——共享核心 chunk（多产物引用同一 core 文件，缓存复用）。
- 追问钩子：为什么「核心零依赖 + wrapper 薄层」的分层构建优于「每框架一份完整实现」——每框架完整实现会把核心逻辑复制三份（体积×3 + 行为漂移风险——修 bug 要改三处）；分层后 core 单份（逻辑单源），wrapper 只是适配（几百行）——构建产物结构映射了架构上的依赖方向。

```javascript
// 一源多产物
entries: { core: 'src/core.ts', react: 'src/react.ts', vue: 'src/vue.ts' },
// core 零依赖（框架无关），react/vue wrapper peer external
externals: (id) => /^(react|vue)(\/|$)/.test(id)
```
