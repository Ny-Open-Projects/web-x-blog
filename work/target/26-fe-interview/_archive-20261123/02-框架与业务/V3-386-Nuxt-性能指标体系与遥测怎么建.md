---
title: [V3-386] Nuxt 应用的性能指标体系与遥测怎么建？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-386：Nuxt 应用的性能指标体系与遥测怎么建？
**答**：
- 服务端指标：SSR 渲染耗时（P50/P95）、缓存命中率（Nitro cache + CDN）、每路由 QPS 与错误率、payload 大小分布。
- 客户端指标：web-vitals（LCP/INP/CLS）、hydration 耗时、JS bundle 传输体积。
- 采集：Nitro hooks/中间件内打点上报（带 route 维度），客户端 web-vitals 库 + 采样。
- 观测联动：route 作为统一维度，能回答「哪个页面慢、慢在服务端还是客户端」。
- 预算治理：路由级性能预算（payload < 100KB、SSR P95 < 300ms），超预算 CI 阻断或告警。
