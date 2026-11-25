---
title: [R19-127] React 生态知识体系怎么收束？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-127：React 生态知识体系怎么收束？
**答**：
- 按层陈述：core（组件模型/并发/RSC）-> 路由（React Router 7 / Next App Router）-> 服务端状态（TanStack Query/RTK Query）-> 客户端状态（Zustand/Jotai/RTK）-> 表单（RHF + Zod）-> 工具 hooks（ahooks）-> 样式 -> 测试（Vitest/RTL/MSW/Playwright）-> 元框架（Next/Remix）。
- 面试中"先定层、再给候选、最后讲选型依据"比罗列 API 更能体现体系化。
- 每层记住一个默认答案 + 一个备选：默认 TanStack Query，备选 RTK Query（已深度用 Redux 时）。

```jsx
// React 生态全景图：面试收束时按层陈述
// core      ：React 19 —— 组件模型、并发、Suspense、Server Components
// 路由      ：React Router 7 / Next.js App Router —— URL 状态、数据加载、代码分割
// 服务端状态：TanStack Query / RTK Query / SWR —— 缓存、失效、乐观更新
// 客户端状态：Zustand / Jotai / Redux Toolkit —— 跨组件共享与可追溯
// 表单      ：React Hook Form + Zod —— 非受控性能 + schema 校验
// 工具 hooks：ahooks —— 工程常用的行为封装
// 样式      ：Tailwind / CSS Modules / vanilla-extract
// 测试      ：Vitest + RTL + MSW + Playwright
// 元框架    ：Next.js / Remix —— SSR、RSC、路由、缓存约定
// 面试时用"分层叙述"比罗列 API 更能体现体系化：先定层，再给候选，最后讲选型依据
```
