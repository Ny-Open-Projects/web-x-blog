---
title: [WEB-247] no-cache 与 no-store 与 must-revalidate 的区别
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-247：no-cache 与 no-store 与 must-revalidate 的区别

**答**：
- no-cache：可以缓存，但使用前必须协商验证（304 复用）——「缓存但每次确认」，HTML 常用。
- no-store：完全不缓存，请求响应都不落盘——敏感数据（账户信息）用，性能最差。
- must-revalidate：缓存过期后必须验证后才可用，不许浏览器在断网时用过期缓存兜底；与 max-age 配合。
- proxy-revalidate 只约束共享缓存（CDN/代理）；private/public 控制谁能缓存（private 只允许浏览器，public 允许 CDN——CDN 缓存带 Authorization 的响应必须显式 public）。
- max-age=0 与 no-cache 的细微差别：前者表述「现在已过期」，无 must-revalidate 时理论上可被启发式续命，no-cache 更明确。

```http
# 常用组合
Cache-Control: no-cache                       # HTML：每次协商
Cache-Control: max-age=31536000, immutable    # 带 hash 静态资源
Cache-Control: no-store                       # 敏感接口
Cache-Control: public, max-age=86400          # CDN 可缓存的公开 API
Cache-Control: private, no-cache              # 带用户数据的动态页，禁 CDN 缓存
```
