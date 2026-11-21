---
title: [V3-381] Nuxt 的实验性视图 API 与组件级隔离有哪些值得关注的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-381：Nuxt 的实验性视图 API 与组件级隔离有哪些值得关注的？
**答**：
- View Transitions 集成：experimental.viewTransition 开启后路由切换走浏览器原生视图过渡（Chrome/Edge），fallback 到无动画，注意降级体验设计。
- 组件级 SPA 隔离：experimental.componentIslands 实现局部组件独立水合/跳过水合（server: false / static 属性），大页面里把「重交互岛」与「静态内容」拆开。
- Payload 精简：experimental.payloadExtraction、renderJsonPayloads 减少 script 注入体积。
- 未来方向：partial hydration、islands 架构——静态站点享受 SPA 交互的部分能力。
- 使用原则：experimental 特性先在灰度构建验证，不直接全量开。
