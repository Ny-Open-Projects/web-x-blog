---
title: [R19-296] Next 的 Client Router Cache（客户端路由缓存）怎么失效？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-296：Next 的 Client Router Cache 怎么失效？
**答**：
- 缓存内容：已访问段（layout/page 的 RSC payload）的客户端缓存，back/forward 立即命中。
- 默认失效：staleTime 动态段 30s、静态段 5min（Next 14）；刷新（router.refresh/revalidate）后清空。
- 控制：experimental.staleTimes 自定义；revalidatePath/Tag 服务端失效随 action 下发。
- 常见问题：「返回上一页数据没更新」——动态段 staleTime 内命中旧缓存，业务需要强实时就在目标页禁缓存或 refresh。
- 设计意识：Router Cache 是「导航体验 vs 数据新鲜度」的调节阀，按路由粒度配置。
