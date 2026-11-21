---
title: [FRP-243] SSR 还是 CSR？决策因素清单怎么列？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-243：SSR 还是 CSR 的决策因素？
**答**：
- 选 SSR：SEO 是需求（内容可收录）、首屏性能敏感（营销页/内容页）、弱网用户占比高。
- 选 CSR：登录后工具型应用（无 SEO 需求）、强交互实时性、服务端成本受限。
- 混合策略才是常态：按路由选渲染（Next routeRules/Nuxt routeRules）——营销页 SSG、列表页 ISR/SWR、后台 CSR。
- 隐藏成本：SSR 的服务器容量、内存泄漏排查、hydration mismatch、双端兼容依赖。
- 决策公式：SEO 权重 + 首屏转化价值 vs 服务端成本 + 团队运维能力。
