---
title: [BAS-003] href 和 src 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-003：href 和 src 有什么区别？
**答**：
- href 表示"关联引用"：资源与文档并行加载，不会替换当前元素内容，用于 a、link。
- src 表示"嵌入来源"：资源下载后嵌入替换当前元素内容，如 img、script、iframe。
- 经典差异：`<link href>` 不阻塞 HTML 解析（只阻塞渲染）；`<script src>` 同步脚本会暂停解析等它下载执行完。

```html
<link href="style.css" rel="stylesheet" />
<!-- href：并行下载，不阻塞解析继续向下 -->
<script src="app.js"></script>
<!-- src：同步脚本会暂停 HTML 解析，直到下载并执行完成 -->
<img src="logo.png" alt="logo" />
<!-- src：图片内容被下载后嵌入元素中展示 -->
```
