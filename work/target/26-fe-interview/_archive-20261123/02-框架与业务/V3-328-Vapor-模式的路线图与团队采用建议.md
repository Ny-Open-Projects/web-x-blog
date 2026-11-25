---
title: [V3-328] Vapor 模式的路线图与团队采用建议是什么？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-328：Vapor 模式的路线图与团队采用建议是什么？
**答**：
- 现状：RFC 已通过、实验性落地于 vuejs/core vapor 分支与 @vue/macro 生态，内建组件与特性仍在补齐（KeepAlive/Suspense/Transition 等）。
- 定位：不是 Vue 4 的强制方向，而是 opt-in 的编译目标；VDOM 与 Vapor 长期共存、支持 interop。
- 采用建议：小项目可尝鲜新页面；中大型项目等内建组件矩阵齐、工具链稳定（devtools 完整支持）后再按页面灰度。
- 评估清单：内建组件覆盖、SSR/水合支持、自定义指令兼容、核心三方库（UI 库、图表）适配、团队调试心智。
- 面试话术：先答「无 VDOM、编译期生成细粒度 DOM 更新、运行时极小」，再答「opt-in、与 VDOM 共存、渐进迁移」，体现工程判断。
