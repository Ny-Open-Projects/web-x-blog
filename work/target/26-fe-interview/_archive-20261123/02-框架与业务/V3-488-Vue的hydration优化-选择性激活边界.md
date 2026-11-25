---
title: [V3-488] Vue 的 hydration 优化：选择性激活边界
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## V3-488：Vue 的 hydration 优化：选择性激活边界

**答**：
- 全量 hydration 成本：下载全部 JS + 每个组件重建响应式 + 逐节点匹配——静态为主的页面大部分白花
- 选择性激活（Selective Hydration）：v-on-viewport/v-on-intersect 指令类方案（Nuxt 生态）——交互到才激活该组件（下载 + 挂载）；静态内容永不激活
- Vue 官方路线：Vapor 模式 + 部分激活——编译器标记交互点，激活引擎只恢复交互所需的响应式链
- 边界与风险：激活延迟期间的交互丢失（点击无响应窗口）——必须保留「激活前的占位交互」（loading 态/按钮禁用态）；共享状态激活顺序（store 全局先激活）
- 度量：TTI（交互可用时间）对比全量 hydration——核心页面目标「可交互时间减半」

```vue
<!-- 选择性激活示意 (Nuxt Labs 方向) -->
<div v-on-intersect>
  <HeavyInteractiveChart />   <!-- 可见才下载+激活 -->
</div>
```
