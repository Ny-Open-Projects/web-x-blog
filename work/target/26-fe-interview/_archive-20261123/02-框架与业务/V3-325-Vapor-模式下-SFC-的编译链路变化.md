---
title: [V3-325] Vapor 模式下 SFC 的编译链路有什么变化？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-325：Vapor 模式下 SFC 的编译链路有什么变化？
**答**：
- @vue/compiler-sfc 增加 vapor 目标：解析 SFC → 同一套 AST → transform 阶段按目标模式走 vapor transform → codegen 输出 helper 调用而非 createVnode。
- `<script setup>` 语义保留：defineProps/defineModel 等宏照常展开，setup 返回值改为 DOM block + 生命周期清理。
- 模板中无法静态确定的复杂表达式仍会降级为「Vapor 里可运行的 render 表达式」，编译器做可行性检查并告警。
- 工具链配套：vue-tsc 类型检查不受影响；HMR 以 block 为单位做局部替换。
- 调试：产物里保留 sourcemap 映射到模板，但断点落在 helper 调用上，读产物前先看模板对应关系。
