---
title: [BAS-170] Vary 响应头有什么作用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-170：Vary 响应头有什么作用？
**答**：
- 告诉缓存（浏览器、CDN、代理）：响应内容会随 Vary 列出的请求头不同而不同，缓存时必须按这些头的组合分别存副本。
- 典型值 `Vary: Accept-Encoding`——gzip 版和原始版要分开缓存，否则会把压缩响应发给不支持的客户端。
- 坑：`Vary: User-Agent` 会让缓存键爆炸、命中率暴跌，能不用就不用。

```http
# 响应示例
Content-Encoding: gzip
Vary: Accept-Encoding
# 含义：缓存按请求头 Accept-Encoding 的取值分桶
# 同一 URL 下 gzip 版本与 identity 版本各存一份
# 面试追问：Vary: User-Agent 会导致缓存碎片化，命中率暴跌
```
