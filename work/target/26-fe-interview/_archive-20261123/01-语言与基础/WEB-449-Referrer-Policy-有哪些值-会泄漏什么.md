---
title: [WEB-449] Referrer-Policy 有哪些值，会泄漏什么
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-449：Referrer-Policy 有哪些值，会泄漏什么

**答**：
- Referrer 会把来源 URL（含路径与 query，可能带 token/订单号）发给目标站
- 常用值：`no-referrer`（不发）、`origin`（只发域名）、`strict-origin-when-cross-origin`（默认：同源全量、跨域只发 origin）、`same-origin`
- 泄漏场景：从详情页跳第三方支付，URL 里的订单参数被第三方收集；内网系统的完整 URL 泄到外网
- 工程建议：默认 `strict-origin-when-cross-origin`；跳转第三方敏感链接时对该链接单独加 `rel="noreferrer"` 或 meta 全站收紧
- 依赖 referrer 做防盗链的服务要注意：策略改严后自家资源被外站引用时 referer 可能缺失，判断逻辑要兼容空值

```html
<meta name="referrer" content="strict-origin-when-cross-origin">
<!-- 针对单个外链更收紧 -->
<a href="https://pay.partner.com" rel="noreferrer">去支付</a>
```
