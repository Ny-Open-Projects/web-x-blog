---
title: [H5-006] HTML5 相对 HTML4 新增了什么、废弃了什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-006：HTML5 相对 HTML4 新增了什么、废弃了什么？
**答**：
- 新增语义标签（header/main/article 等）、表单类型与校验、多媒体标签 video/audio、绘图 canvas/svg。
- 新增 API：拖放、地理定位、Web Storage、Web Workers、History pushState、FileReader 等（多数随 HTML5 概念提出，由 JS API 实现）。
- 废弃纯表现类标签：`font`、`center`、`big`、`strike`；废弃 `frame/frameset`；样式类标签由 CSS 取代。
- `b/i/s/u` 未废弃但语义弱化，表达强调优先用 strong/em。

```html
<!-- 已废弃的写法（仅用于识别老代码） -->
<!-- <font color="red">文字</font>        样式交给 CSS -->
<!-- <center>内容</center>               text-align: center -->
<!-- <frameset><frame src="a.html"></frameset>  用 iframe 或 SPA 路由替代 -->

<!-- HTML5 推荐写法 -->
<p style="color: red;">样式进 CSS</p>
<video controls src="/media/demo.mp4"></video>
<input type="email" required />
```
