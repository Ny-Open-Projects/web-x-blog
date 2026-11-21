---
title: [WEB-027] 什么是启发式缓存？没有 Cache-Control 时浏览器怎么办？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-027：什么是启发式缓存？没有 Cache-Control 时浏览器怎么办？
**答**：
- 响应里既没有 `Expires` 也没有 `Cache-Control` 时，浏览器按启发式公式估算新鲜度：`(Date - Last-Modified) * 10%`。
- 例：资源 10 天前修改，浏览器可能缓存约 1 天，期间不发请求；过期后进入协商缓存。
- 风险：启发式完全猜服务器意图，更新频繁的资源可能被缓存过久导致"改了不生效"。
- 结论：所有资源显式声明 `Cache-Control`，不要裸奔依赖启发式。

```bash
# 观察一个没有 Cache-Control 的响应
curl -sI https://example.com/ | grep -Ei 'date|last-modified|expires|cache-control'
# 假设输出 Date: Fri, 01 Nov 2026 03:00:00 GMT
#        Last-Modified: Tue, 20 Oct 2026 03:00:00 GMT
# 启发式新鲜度 = (12 天) * 0.1 ≈ 1.2 天，浏览器在这期间直接用本地缓存
```
