---
title: [R19-297] RSC 应用怎么做离线兼容（PWA 场景）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-297：RSC 应用的离线兼容策略？
**答**：
- RSC payload 依赖服务端：离线时导航必然失败——离线能力只在「已访问页面缓存」与「纯客户端交互」层面。
- 策略：Service Worker 缓存静态资源 + 已访问路由的 payload（stale-while-revalidate）；离线导航命中缓存展示旧内容 + 「离线」提示。
- 写操作：action 离线不可用——离线队列（IndexedDB）暂存，恢复在线后重放（幂等 requestId）。
- 边界：缓存 payload 的 key 含用户态要谨慎（同设备多账号串号风险）。
- 取舍：核心流程依赖服务端数据的应用，离线只做「浏览缓存内容」而非全功能。
