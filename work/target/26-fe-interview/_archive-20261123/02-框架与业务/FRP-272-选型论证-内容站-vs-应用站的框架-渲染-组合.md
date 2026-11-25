---
title: [FRP-272] 选型论证：内容站 vs 应用站的框架/渲染组合？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-272：内容站与应用站的技术组合论证？
**答**：
- 内容站（博客/文档/营销）：Astro islands（最大静态占比）或 Next SSG + 少量 client 岛；SEO 与首屏是 KPI，框架运行时最小化。
- 应用站（后台/IM/编辑器）：Next/Nuxt 全功能（RSC/composables）+ 重客户端状态；交互性能与开发效率是 KPI。
- 混合产品（电商）：内容壳（SSG/ISR）+ 交互域（client 岛）——Next routeRules/Nuxt routeRules 按路由配置。
- 论证结构：先定 KPI（LCP/SEO vs 交互吞吐），再选渲染模式，最后选框架生态。
