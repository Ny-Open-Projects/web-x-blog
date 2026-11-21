---
title: [FRP-244] 微前端（qiankun）还是 Module Federation？论证框架？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-244：微前端还是 Module Federation？
**答**：
- qiankun iframe/wm 模式：强隔离（JS/CSS/路由）、异构技术栈、独立部署——代价：通信成本、内存开销、UX 割裂。
- Module Federation：同构建体系共享模块、运行时组合、体验一致——代价：依赖版本协调、全局污染风险、强绑定构建工具。
- 判据：技术栈异构/组织边界硬 → 微前端隔离；同 React 生态/需要共享状态与组件 → MF。
- 演进路径：MF 起步，边界失控时再物理隔离（iframe）。
- 面试表达：先问「隔离的是什么」（技术栈？发布节奏？团队权限？）——不同答案指向不同方案。
