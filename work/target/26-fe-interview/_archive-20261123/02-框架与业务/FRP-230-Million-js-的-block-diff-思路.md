---
title: [FRP-230] Million.js 的 block diff 思路是什么？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-230：Million.js 的 block diff 思路？
**答**：
- 思路：编译期把组件标记为 block，提取「动态路径」（哪个属性哪个位置会变），运行时只比较/更新动态路径——类似 Vue block tree 但作为库叠加在 React 上。
- 实现：babel 插件转换 JSX → block 定义；渲染时直接按路径 diff，跳过 React reconcile 的大树遍历。
- 收益：列表密集场景（表格）显著提速，官方基准常有数倍提升。
- 局限：兼容性风险（与 React 生态、并发特性、SSR 的交互）、心智负担（block 边界需理解）、React Compiler 官方化后价值被侵蚀。
- 面试表达：把它当「编译期优化在 React 生态的民间尝试」，说明其与官方 Compiler 的关系。
