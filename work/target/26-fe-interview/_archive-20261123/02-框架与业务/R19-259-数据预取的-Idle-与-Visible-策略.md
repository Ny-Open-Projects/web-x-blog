---
title: [R19-259] 数据预取的 idle/visible/hover 三种触发策略怎么搭配？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-259：数据预取的 idle/visible/hover 三种触发策略怎么搭配？
**答**：
- hover：意图最强，鼠标进入链接区域立即预取——转化率最高的路径。
- visible：IntersectionObserver 进入视口预取（列表卡片批量）——适合信息流。
- idle：requestIdleCallback 空闲时预取「大概率会去」的页面（首页→详情 Tab）——零交互成本。
- 搭配原则：主转化路径 hover + idle 兜底；长列表 visible；低概率页面不预取（exclude）。
- 约束：预取带 TTL 与去重（Map<prefetchKey>），失败可重试；服务端容量考虑——预取放大请求量，配合 CDN 缓存。
