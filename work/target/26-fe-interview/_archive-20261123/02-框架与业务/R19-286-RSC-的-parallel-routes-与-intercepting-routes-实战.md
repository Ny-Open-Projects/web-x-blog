---
title: [R19-286] Next 的 Parallel Routes 与 Intercepting Routes 是什么？什么场景用？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-286：Parallel Routes 与 Intercepting Routes 的场景？
**答**：
- Parallel Routes（@slot 并行段）：同一布局渲染多个独立段（@modal、@chart），各段独立加载/错误边界——仪表盘多面板。
- Intercepting Routes（(.) 拦截）：站内导航时把 /photo/1 渲染成 modal（拦截），直接输入 URL 则是整页——Instagram 式体验。
- 组合：@modal 并行段 + intercepting route = 站内点开弹层、刷新/直达走完整页，SEO 与 UX 兼得。
- 实现要点：并行段独立 loading/error，互相不阻塞；拦截层级（(.)同层 (..)上级 (…)多级）按路由深度选。
- 坑：拦截路由的软导航判定依赖 Link 导航，编程式 push 也会走拦截——需要整页时用 router.push + 刷新策略。
