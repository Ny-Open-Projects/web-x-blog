---
title: [WEB-248] Vary 头在缓存中起什么作用？常见坑
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-248：Vary 头在缓存中起什么作用？常见坑

**答**：
- 作用：告诉缓存（浏览器/CDN/代理）按指定请求头的不同取值分别缓存同一 URL 的多个版本。`Vary: Accept-Encoding` 让 gzip 与 br 版本共存；`Vary: User-Agent`（反模式）按 UA 分缓存。
- 场景：图片服务按 `Accept` 头返回 webp/avif/jpeg，必须 Vary: Accept 才不会给不支持 webp 的浏览器回 webp。
- 坑一：Vary: User-Agent 使缓存命中率趋近于 0（UA 数百种），永远 MISS 回源。
- 坑二：动态内容忽略 Vary 导致「A 用户的会话内容被缓存给 B 用户」——带 Cookie 的响应绝不缓存或用 private。
- 坑三：CDN 忽略/剥离 Vary 造成内容错乱，需在 CDN 控制台确认 Vary 行为。

```http
# 图片服务按浏览器能力返回不同格式
HTTP/1.1 200
Content-Type: image/avif
Vary: Accept
# Chrome 发 Accept: image/avif → 缓存 avif 版本
# Safari 不带 avif → 缓存 jpeg 版本，互不污染
```
