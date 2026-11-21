---
title: [V3-380] SSR 与 CDN 缓存策略怎么配合？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-380：SSR 与 CDN 缓存策略怎么配合？
**答**：
- 分级缓存：CDN 缓存匿名页 HTML（Cache-Control: public, s-maxage=60, stale-while-revalidate=300），回源打 SSR 集群；个性化页绕过 CDN 或边缘拆分。
- 用户态拆分：HTML 只含公共骨架，用户数据（购物车、头像）客户端/边缘单独拉取，让页面可缓存——这是 SSR + 缓存的核心矛盾解法。
- 回源保护：CDN 回源加请求合并（single-flight）+ Nitro swr 双层兜底，防止缓存失效瞬间打爆源站。
- 失效机制：内容更新时主动 purge（按 URL/tag），或用短 s-maxage + swr 自然过期。
- 观测：CDN 命中率、回源 QPS、源站 P95 三个指标联动看。
