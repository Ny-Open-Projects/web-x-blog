---
title: [H5-249] Manifest 的关键字段有哪些
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-249：Manifest 的关键字段有哪些

**答**：
- 身份字段：name（全名）/ short_name（桌面图标下最多约 12 字符）/ id（唯一标识，决定安装去重）
- 入口字段：start_url（启动落地页，建议带 `?source=pwa` 做来源统计）/ scope（应用边界，scope 外链接开浏览器）
- 展示字段：display（standalone 去浏览器外壳；fullscreen 游戏用）/ orientation（方向锁定）/ theme_color 与 background_color（启动闪屏）
- 图标：192/512 两档必备；`purpose: "maskable"` 声明可裁剪图标（安卓自适应形状）
- 安装条件细节：display 非 browser、图标尺寸合规、start_url 与页面同源——漏一个就不能安装

```html
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#3367d6">
<link rel="apple-touch-icon" href="/icon-192.png"> <!-- iOS 需要单独声明 -->
```
