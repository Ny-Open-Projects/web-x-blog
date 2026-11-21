---
title: 渲染引擎：读 Schema 画 UI 的运行时核心
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 概念, 渲染引擎, Schema]
---

## 渲染引擎：读 Schema 画 UI 的运行时核心

渲染引擎职责一条链：**读 Schema → 按 type 查注册表 → 摊开 props 渲染组件 → 处理数据回写（onChange → 回写 Schema）与联动**。关键设计包括递归渲染（容器嵌套）、编辑态/渲染态同构、数据绑定、服务端渲染出 HTML。

**本项目实例**：课程版的渲染链路是 `getComponentById → generateComponent → getComponentByType → toJS → 展开 props`，画布和预览页复用同一链路；发布端 Next.js App Router 的 Server Component 直接 fetch 组件数据 SSR 直出，输入型组件再由 client 端 ComponentRender 补 onChange/onUpdate 回调收集答案。自研参考实现则走另一条路：后端 `render-page.ts` 把 PageSchema 渲染成自包含 HTML，`GET /api/pages/:id/render` 直接返回 text/html——即"渲染闭环在服务端"。

两种形态对比：React 组件级渲染（可交互、问卷提交）vs 服务端 HTML 渲染（零依赖、首屏快）。

出处「课程25 · 19-3、20-6；scan3」
