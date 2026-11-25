---
title: [V3-337] Vue 编译器与 Vite 插件（vue plugin）的协作顺序是怎样的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-337：Vue 编译器与 Vite 插件的协作顺序是怎样的？
**答**：
- @vitejs/plugin-vue 在 transform 阶段拦截 .vue 请求：先 script（含 setup 宏展开）、再 template、再 style，产出三段虚拟模块。
- script 代码经过 esbuild/TS 转译；template 调 compiler-sfc 的 compileTemplate 生成 render 函数；样式走 CSS 管道并注入 scope id。
- 顺序要点：宏展开发生在 vue 插件内部，先于 TypeScript 类型检查（vue-tsc 独立跑）；自定义编译选项通过插件 compilerOptions 注入。
- 与其他插件的协作：unplugin-auto-import 等要在 vue 插件处理后的虚拟模块上工作；自定义 directiveTransform 也从这里注入。
- 排查手段：`vite-plugin-inspect` 看每个模块经过的插件顺序与产物，定位「宏没展开/样式没加 scope」类问题。
