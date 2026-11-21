---
title: [BAS-011] CSS 有哪几种引入方式？link 和 @import 的区别是什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-011：CSS 有哪几种引入方式？link 和 @import 的区别是什么？
**答**：
- 三种方式：外链 `<link>`、内联 `<style>`、行内 `style=""` 属性（行内优先级最高，仅次于 !important）。
- link 是 HTML 标签，CSS 并行下载，还可以被 JS 动态增删实现主题切换。
- @import 是 CSS 语法，必须等当前 CSS 下载解析完才发起下一个请求，串行阻塞、可能引起 FOUC，工程上一律用 link。

```html
<link rel="stylesheet" href="/main.css" />
<!-- link：HTML 标签，并行下载，JS 可增删切换主题 -->

<style>
  /* 内联 style 标签：适合放首屏关键 CSS */
  .hero { min-height: 100vh; }
</style>

<!-- 不推荐在 main.css 里写 @import url('./theme.css')：
     theme.css 要等 main.css 下载解析后才发起请求，串行阻塞 -->
```
