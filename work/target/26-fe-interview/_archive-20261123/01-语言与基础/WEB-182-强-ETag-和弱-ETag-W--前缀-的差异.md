---
title: [WEB-182] 强 ETag 和弱 ETag（W/ 前缀）的差异是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-182：强 ETag 和弱 ETag（W/ 前缀）的差异是什么？
**答**：
- 强校验器：字节级唯一，资源任何字节变化都变——适合 Range 断点续传（同一资源的所有分段必须来自同一实体）。
- 弱校验器 W/"..."：语义等价即可（内容一致但压缩、元数据不同也没关系）——适合 HTML 这类"渲染结果一致就行"的资源。
- 条件请求：If-None-Match 可带多个值；命中返回 304 不带 body；If-Match 用于并发写保护（乐观锁），不符返回 412。
- 工程坑：集群节点间 ETag 不一致会让协商缓存命中率暴跌；代理层压缩后对弱 ETag 处理不当会出现 304 与实际内容不符。

```http
# 首次响应：弱 ETag，语义级一致即可
HTTP/1.1 200 OK
ETag: W/"33a64df5"

# 再次请求：条件头可带多个值
GET /index.html HTTP/1.1
If-None-Match: W/"33a64df5", "abc123"

# 内容语义未变则返回 304 Not Modified，无 body
# 并发写保护：If-Match 与当前 ETag 不符时返回 412 Precondition Failed
```
