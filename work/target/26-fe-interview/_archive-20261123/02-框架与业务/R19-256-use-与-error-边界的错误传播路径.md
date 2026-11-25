---
title: [R19-256] use(Promise) reject 时的错误传播路径完整描述
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-256：use(Promise) reject 时的错误传播路径完整描述
**答**：
- promise reject → React 把 rejection 作为渲染错误抛出（从使用 use 的组件向上）→ 最近的 ErrorBoundary 捕获 → 边界渲染 fallback UI。
- 无边界：错误传播到根，页面崩溃（开发环境重抛 + 生产白屏/全局兜底）。
- retry：边界 UI 提供重试按钮 → 重新触发取数（新 promise）→ 子树重新渲染。
- 错误分类处理：业务错误（404 → 显示空态）与程序错误（500 → 边界兜底）应在数据层区分：404 可以 resolve 为空对象而非 reject。
- 组合：Suspense（等待）与 ErrorBoundary（失败）是一对搭档，每个异步域两个边界都要有。
