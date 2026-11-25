---
title: [WEB-246] 启发式缓存是什么？为什么没设 Cache-Control 也会缓存？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-246：启发式缓存是什么？为什么没设 Cache-Control 也会缓存？

**答**：
- HTTP 规范：响应没有显式缓存指令时，浏览器可用启发式策略估算新鲜期，常见实现 `寿命 = (Date - Last-Modified) × 10%`。
- 后果：图片站一年没改过的图，浏览器会缓存 36 天——你以为没缓存，实际强缓存了，改完图用户还看旧图，是「线上资源不更新」的经典排查点。
- 解决：所有静态响应显式设 Cache-Control，不把新鲜度交给启发式（显式 > 启发式 > Date 头估算）。
- 验证方法：DevTools Network 看响应是否 `(from disk cache)`，或 curl 看有没有 Cache-Control 头。

```http
# 没有缓存指令的响应
HTTP/1.1 200 OK
Last-Modified: Tue, 18 Nov 2025 00:00:00 GMT   # 距今366天
# 浏览器启发式: 366天 * 10% ≈ 36天 强缓存

# 显式修复
Cache-Control: no-cache   # 强制走协商，杜绝启发式
```
