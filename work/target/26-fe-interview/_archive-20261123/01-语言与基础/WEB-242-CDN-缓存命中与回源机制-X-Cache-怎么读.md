---
title: [WEB-242] CDN 缓存命中与回源机制？X-Cache 怎么读？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, CDN]
type: 面试题
---

## WEB-242：CDN 缓存命中与回源机制？X-Cache 怎么读？

**答**：
- 命中链路：请求到边缘节点 → 查节点缓存（HIT 直接返回）→ MISS 则向上级中间层节点要（二级缓存）→ 仍 MISS 才回源站。
- 回源风暴：缓存过期瞬间大量 MISS 同时回源（类似缓存击穿），CDN 用「合并回源」（同一资源只有一个请求真正回源，其余等结果）解决。
- 观测头：`X-Cache: HIT/MISS`、`X-Swift-Cache-Time`（剩余可缓存时间）、`X-Cache-Status`（Nginx）。
- 配置要点：静态资源源站给 `Cache-Control: max-age=31536000, immutable` + 文件名带 hash（非覆盖式发布）；HTML 不缓存或短缓存，保证发版即生效。

```bash
curl -sD - -o /dev/null https://cdn.example.com/app.9f3c1.js | grep -iE 'x-cache|cache-control|age'
# X-Cache: HIT
# Cache-Control: max-age=31536000, immutable
# Age: 12345   已被缓存了多久
```
