---
title: [V3-505] Vue 的 Server Component 探索与边界
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, SSR]
type: 面试题
---

## V3-505：Vue 的 Server Component 探索与边界

**答**：
- 现状：Vue 官方没有完整 RSC 等价物；Nuxt 生态探索「Server Components」（Nuxt Labs 实验）——服务端渲染 + 无客户端 JS 的组件形态
- 与 SSR 的差异：SSR 组件仍要 hydrate（客户端 JS 重建响应式）；Server Component 只输出 HTML，零客户端运行时——静态内容区的体积收益
- 边界约束：无响应式/无事件/无生命周期——只能做「展示」；交互必须包在客户端组件岛内
- 混合模型：Server Component 输出 + 客户端 islands（交互区）——与 Astro islands 同构思路，Vue 生态的落地形态是「框架无关 islands + Vue 客户端组件」
- 落地判断：内容型站点（文档/营销页）收益大；重交互应用收益趋零——按「交互密度」评估

```text
组件分类决策:
  纯展示(无交互) → Server Component (零 JS)
  轻交互(按钮/hover) → 客户端 island (小)
  重交互(表单/图表) → 常规 SSR 组件
```
