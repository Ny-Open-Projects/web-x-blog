---
title: [FRP-312] 框架运行时剖析：SSR 与水合的框架差异
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, SSR]
type: 面试题
---

## FRP-312：框架运行时剖析：SSR 与水合的框架差异

**答**：
- 水合策略谱系：全量水合（React/Vue 传统）、部分水合（Astro islands）、选择性水合（React 流式优先级）、_resumable（Qwik——不水合，恢复执行）——运行时成本递减
- Qwik 的 resumable：序列化「应用状态 + 事件监听位置」到 HTML——客户端零重建（不重跑组件函数），按需加载 handler——激进但生态成本高
- React 19 的选择性水合：流式 chunk 到达 + 用户交互优先——「用户点击哪块先水合哪块」
- Vue 的 SSR 成本：水合要重建响应式关系（effect 链）——Vapor 模式的水合更轻（订阅点编译期已知）
- 决策维度：页面交互密度（静态内容多 → islands/resumable 收益大）与团队生态绑定

```text
水合成本对比:
  全量:    全部 JS + 全部组件重建 (最重)
  islands: 只水合交互岛
  选择式:  按交互优先级渐进
  resumable: 零重建, 按需加载 handler (最轻)
```
