---
title: [WEB-189] 深链与 App Link 的网络层配合是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-189：深链与 App Link 的网络层配合是什么？
**答**：
- URI scheme（myapp://）最简单但无归属校验，易被抢注；Android App Links 与 iOS Universal Links 走 HTTPS 域名下发的关联文件（.well-known/assetlinks.json 与 apple-app-site-association）做归属验证。
- 未安装时的体验靠 fallback URL：intent 链接的 browser_fallback_url，或 Universal Link 直接落到网页版——归因参数要随 URL 带下去。
- Deferred deep link：首次安装后仍能还原"点过的那个内容"，需要归因服务在启动时匹配点击指纹。
- 前端职责：落地页按是否装 App 分流、把 UTM/归因参数编码进两条路径、处理浏览器拦截 scheme 的弹窗逻辑。

```html
<!-- Android App Links：域名校验文件部署在 https://app.example.com/.well-known/assetlinks.json -->
<!-- 页面里的兜底跳转：未安装时落到带归因参数的网页版 -->
<a href="intent://promo/123#Intent;scheme=myapp;package=com.example.app;S.browser_fallback_url=https%3A%2F%2Fapp.example.com%2Fpromo%2F123%3Futm_source%3Dbanner;end">
  打开活动
</a>
<script>
  // iOS Universal Links 由系统直接拉起 App；未安装时 Safari 打开同一 HTTPS URL 的网页版
  // 两条路径都保留归因参数，安装后首次启动据此还原上下文，实现 deferred deep link
</script>
```

## 三十一、综合排查与收束
