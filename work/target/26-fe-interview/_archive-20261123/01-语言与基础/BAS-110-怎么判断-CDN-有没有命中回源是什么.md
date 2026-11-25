---
title: [BAS-110] 怎么判断 CDN 有没有命中？回源是什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-110：怎么判断 CDN 有没有命中？回源是什么？
**答**：
- 看响应头 `X-Cache: HIT/MISS`（各厂商字段名略异，如 Ali-Swift-Cache）。
- MISS 表示边缘节点无缓存，回源站取数（回源），取回后按 Cache-Control 缓存到边缘，下次同节点 HIT。
- 排查：响应头看 X-Cache 和 Age（已缓存秒数），用 `curl -I` 连打几次观察 MISS → HIT 转变；长期 MISS 要查缓存配置与 URL 是否带随机参数。

```bash
curl -sI https://cdn.example.com/app.js | grep -iE 'x-cache|age|cache-control'
# x-cache: MISS        第一次请求，回源
# x-cache: HIT         再次请求命中边缘节点
# age: 120             已在边缘缓存 120 秒
```
