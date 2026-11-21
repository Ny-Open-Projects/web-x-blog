---
title: [WEB-096] 启发式缓存是什么？没有 Cache-Control 时浏览器怎么决定缓存多久？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-096：启发式缓存是什么？没有 Cache-Control 时浏览器怎么决定缓存多久？
**答**：
- 响应只有 Last-Modified 没有 Cache-Control 时，HTTP 缓存仍可工作：浏览器按启发式算法猜一个保鲜期。
- 主流实现取"距上次修改时间的 10%"：`（Date - Last-Modified）× 0.1`；资源越久没改，猜的缓存期越长。
- 启发式期内命中不发请求；过期后走协商（If-Modified-Since/If-None-Match），304 续用并可能重新做启发式。
- 工程结论：显式 Cache-Control 永远优先于猜，静态资源务必显式声明，别让缓存时长不可控。

```http
HTTP/1.1 200 OK
Content-Type: text/css
Date: Wed, 07 Oct 2026 12:00:00 GMT
Last-Modified: Tue, 01 Sep 2026 12:00:00 GMT

# 无 Cache-Control，浏览器启用启发式缓存：
# (Date - Last-Modified) = 36 天，启发式保鲜期 = 36 天 * 10% ≈ 3.6 天
# 3.6 天内：直接用本地缓存，零网络请求
# 3.6 天后：带 If-Modified-Since: Tue, 01 Sep 2026 12:00:00 GMT 发起协商缓存
# DevTools Network 的 Size 列显示 (disk cache / memory cache) 即为命中
```
