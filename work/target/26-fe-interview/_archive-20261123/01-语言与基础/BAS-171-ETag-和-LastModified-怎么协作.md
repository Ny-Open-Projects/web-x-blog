---
title: [BAS-171] ETag 和 Last-Modified 怎么协作？缓存决策链是什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-171：ETag 和 Last-Modified 怎么协作？缓存决策链是什么？
**答**：
- Last-Modified 是时间戳验证器（秒级精度、内容不变改时间也会失效）；ETag 是内容指纹（强验证器，优先级更高）。
- 协商缓存请求同时带上 If-None-Match 与 If-Modified-Since，服务器优先比对 ETag，都没变才回 304。
- 完整链路：强缓存（Cache-Control 未过期）→ 命中即用；否则走协商缓存 → 304 用本地或 200 拉新。

```http
# 首次响应同时下发两个验证器
ETag: "abc123"
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT

# 过期后的协商缓存请求
If-None-Match: "abc123"            # 优先比对，内容指纹最准
If-Modified-Since: Wed, 21 Oct 2025 07:28:00 GMT
# 都未变化 → 304 Not Modified（无响应体）
```

```mermaid
flowchart TD
    A[请求资源] --> B{强缓存未过期}
    B -- 是 --> C[直接读本地副本不发请求]
    B -- 否 --> D{有 ETag 或 Last-Modified}
    D -- 有 --> E[发协商缓存请求带 If 系列头]
    E --> F{服务端比对验证器}
    F -- 未变化 --> G[返回 304 用本地副本]
    F -- 已变化 --> H[返回 200 新资源与新验证器]
    D -- 没有 --> H
```
