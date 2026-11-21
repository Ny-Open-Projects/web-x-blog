---
title: [CSS-121] CSS 文件如何组织与做请求优化？Critical CSS 怎么提取？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-121：CSS 文件如何组织与做请求优化？Critical CSS 怎么提取？

**答**：
- 组织：按 @layer/ITCSS 分层分文件，构建期合并；路由级样式按需拆分，避免单包巨型 CSS。
- 请求优化：杜绝 @import 串行链；`<link rel="preload">` 关键样式，非首屏样式异步加载。
- Critical CSS：提取首屏必需样式内联进 `<head>`，剩余样式 `media="print"` + onload 切换或 `rel=preload` 异步注入，消除渲染阻塞。
- 工具链：critters（beasties）构建期自动内联，penthouse 抽取关键规则。
- 同时砍体积：purge 未用类、压缩、字体子集化。

```html
<!-- 关键样式内联，其余异步 -->
<style>/* critters 提取的首屏规则：布局骨架、header、hero */</style>
<link rel="preload" href="/main.css" as="style" onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="/main.css"></noscript>
```

```css
/* 反例：@import 串行阻塞（浏览器要下完 a.css 才知道还要下 b.css） */
/* a.css */
/* @import url("./b.css"); ← 移除，构建期合并或改用 link */

/* 正解：构建产物单文件，路由样式独立 chunk 由框架按需注入 */
```

## 二十一、新特性与兼容
