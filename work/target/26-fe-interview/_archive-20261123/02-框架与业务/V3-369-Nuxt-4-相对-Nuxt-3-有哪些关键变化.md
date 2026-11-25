---
title: [V3-369] Nuxt 4 相对 Nuxt 3 有哪些关键变化？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-369：Nuxt 4 相对 Nuxt 3 有哪些关键变化？
**答**：
- 目录结构变化：默认 srcDir 指向 `app/`（app.vue、pages、components 移入），服务器目录仍在顶层 server/——关注迁移脚手架自动处理。
- 数据层增强：useAsyncData/useFetch 的共享缓存与 keyed 去重更严格，多调用同 key 默认共享实例。
- 类型系统：生成的 tsconfig 更精确（项目引用拆分 app/server），TS 体验提升。
- Nitro 与 Vue 版本升级带来的运行时优化（Payload 更小、实验性视图 API）。
- 迁移要点：compatibilityVersion: 4 开启渐进兼容，按官方 codemods 跑迁移清单。
