---
title: [V3-359] 在 setup 中直接 await（异步 setup）有什么限制与风险？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-359：在 setup 中直接 await（异步 setup）有什么限制与风险？
**答**：
- 语法：`<script setup>` 顶层 await 使组件成为异步组件，编译器自动包 defineAsyncComponent 并隐式依赖 Suspense 处理。
- 限制一：没有 Suspance 包裹会直接警告/挂起，模板必须由 Suspense 边界管理。
- 限制二：await 之后的代码不再处于同步 setup 上下文——`getCurrentInstance()`、onMounted 等生命周期注册可能失效（官方明确警告），必须在 await 前注册。
- 风险三：错误处理链变化：setup 内 await 抛错走 Suspense 错误通道，需要 ErrorBoundary 而非 try/catch 兜住渲染。
- 实践建议：数据获取尽量放 onMounted/composable 内用 ref 承载，异步 setup 仅在「强依赖 + 全页加载语义」时使用。
```javascript
// <script setup>
onMounted(() => {})          // 必须在 await 之前
const data = await fetchUser() // 之后组件进入 pending
```
