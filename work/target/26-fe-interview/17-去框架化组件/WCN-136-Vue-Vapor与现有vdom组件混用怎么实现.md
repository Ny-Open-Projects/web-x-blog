---
title: [WCN-136] Vue Vapor 与现有 vdom 组件如何混用？渐进迁移策略是什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-136：Vue Vapor 与现有 vdom 组件如何混用？

**答**：
- 混用机制：runtime 提供 bridge——vdom 组件树中可以渲染 vapor 块（作为特殊 vnode 类型，实际渲染交给 vapor helper），反向 vapor 组件里可通过 `<VaporToVdom>` 包装使用 vdom 组件。
- 渐进迁移路径：① 新页面/新组件用 vapor（编译目标 per-file 配置）；② 老页面保持 vdom；③ 热点组件（列表、高频更新）优先迁移——收益最大；④ 整页迁移时用路由级配置。
- 配置方式：`vapor` 编译选项（Vite 插件 per-SFC `vapor` 属性或目录 glob）；类型与组合式 API 完全兼容，迁移成本低。
- 风险点：生态依赖（第三方组件库）在 bridge 下的行为差异、SSR 双模式产物一致性、v-if/v-for 边缘语义差异（vapor 编译更严格）。
- 验证：迁移组件跑双模式 diff 测试（同一 props 输入，DOM 输出一致）。

```vue
<!-- App.vue：vdom 页面混用 vapor 组件 -->
<template>
  <VaporList :items="items" />   <!-- 编译目标 vapor -->
  <LegacyChart :data="data" />   <!-- 编译目标 vdom -->
</template>
<script setup>
// vite.config：vapor: ['src/components/Vapor*.vue']（按 glob 指定编译目标）
</script>
<!-- 迁移优先级：热点列表组件 → 表单组件 → 全页 -->
```
