---
title: [V3-382] Nuxt 项目怎么测试？nuxt/test-utils 提供哪些能力？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-382：Nuxt 项目怎么测试？nuxt/test-utils 提供哪些能力？
**答**：
- 三层：单测（vitest + @vue/test-utils 测组件/composable）、集成（@nuxt/test-utils 的 mountSuspended / $fetch 测 Nuxt 上下文内组件与 server route）、E2E（Playwright 验证 SSR 输出与水合后交互）。
- mountSuspended：把组件挂载在真实 Nuxt app 里，auto-import、插件、devtools 上下文都生效——比裸 test-utils 更真实。
- server route 测试：`$fetch('/api/xx')` 直测 Nitro 处理器，配合 setup 环境变量/mock 存储。
- 快照策略：SSR HTML 快照只用于关键页（首页/商品页），防 hydration 结构回归。
- CI 建议：类型检查（vue-tsc）→ 单测 → 集成 → E2E 关键路径，SSR 冒烟跑在预发构建。
