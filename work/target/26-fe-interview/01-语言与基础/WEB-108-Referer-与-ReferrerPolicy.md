---
title: [WEB-108] Referer 与 Referrer-Policy 如何控制来源信息的暴露？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-108：Referer 与 Referrer-Policy 如何控制来源信息的暴露？
**答**：
- 默认策略 `strict-origin-when-cross-origin`：同源带完整 URL，跨源只带 origin，降级 HTTP 不发送。
- 更严的 `strict-origin`、`no-referrer`（全不发）、`same-origin`（跨源不发）按隐私需求选择；`unsafe-url` 反向全裸，禁用。
- 配置层级：CSP 头 `referrer` / Referrer-Policy 头 / `<meta name="referrer">` / 每个标签的 referrerpolicy 属性，就近覆盖。
- 工程影响：图片防盗链依赖 Referer；改为 same-origin 后 CDN 防盗链统计会失真，需要同步调整。

```html
<meta name="referrer" content="strict-origin-when-cross-origin">

<!-- 单元素覆盖：打点请求只带 origin，外链完全不带 -->
<a href="https://partner.com" referrerpolicy="no-referrer">合作方</a>
<img src="https://track.example.com/pixel" referrerpolicy="strict-origin">
```

```http
# 服务端统一策略，优先级高于页面 meta
Referrer-Policy: strict-origin-when-cross-origin
```
