---
title: [V3-375] Nuxt 的 payload 提取（payload extraction）是什么？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-375：Nuxt 的 payload 提取（payload extraction）是什么？
**答**：
- 构建期把预渲染页面的数据 payload 抽成独立 `_payload.json`，HTML 里只留引用；首次进入静态页时 payload 可由 CDN 分发，不占 HTML 体积。
- 收益：HTML 更小（TTFB 降）、payload 可单独缓存、CDN 命中率更高。
- 客户端导航：目标页 payload 提前获取即可渲染，无需等服务端重新执行 SSR。
- 配置：`experimental: { payloadExtraction: true }`，配合 prerender 的路由生效；动态路由需 generate 列表。
- 注意：payload 与页面强绑定，页面数据实时性要求高（秒级）的页面不要开，会导致 CDN 缓存脏读。
