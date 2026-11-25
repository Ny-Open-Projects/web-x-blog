---
title: [V3-370] Nuxt layers（分层）是什么？怎么用？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-370：Nuxt layers（分层）是什么？怎么用？
**答**：
- layer = 一个可复用的「迷你 Nuxt 项目」（pages/components/plugins/modules/nuxt.config 全套），通过 extends 叠加到主应用。
- 用途一：多站点共享底座（组件库、设计系统、公共页面、统一中间件），base layer + 各站点薄层。
- 用途二：功能开关——layer 按环境 extends，实现「旗舰版/精简版」构建差异。
- 合并规则：主应用优先，layer 按声明顺序覆盖；pages/components 自动注册与去重。
- 落地建议：底座 layer 发私有 npm 包，版本化升级；layer 内不再互相依赖，保持单向叠加。
```javascript
// nuxt.config.ts
export default defineNuxtConfig({ extends: ['@acme/base', './layers/cn-site'] })
```
