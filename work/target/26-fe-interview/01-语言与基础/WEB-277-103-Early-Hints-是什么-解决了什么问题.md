---
title: [WEB-277] 103 Early Hints 是什么？解决了什么问题？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP]
type: 面试题
---

## WEB-277：103 Early Hints 是什么？解决了什么问题？

**答**：
- 问题：服务器「真正算出」响应前（动态页要查库、SSR），浏览器只能干等；等 200 回来才知道要加载哪些 CSS/JS/字体。
- 103 Early Hints：服务器在最终响应前先发一个 103 状态码，提前告诉浏览器「待会要用这些资源」，浏览器立刻并行预加载/预连接，把「等响应」的时间变成「提前加载」的时间。
- 对比 Server Push：Push 是服务器猜着推资源（推了不用浪费带宽，Chrome 已移除支持）；Early Hints 只是提示，浏览器自己决定按需加载，无浪费。
- 实践：Cloudflare 已支持；源站由框架/网关在渲染前输出常用资源的 hints。

```http
HTTP/1.1 103 Early Hints
Link: </style.css>; rel=preload; as=style
Link: </app.js>; rel=preload; as=script

HTTP/1.1 200 OK
Content-Type: text/html
...
```
