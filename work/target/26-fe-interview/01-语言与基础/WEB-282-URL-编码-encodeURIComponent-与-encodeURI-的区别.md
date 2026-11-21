---
title: [WEB-282] URL 编码：encodeURIComponent 与 encodeURI 的区别
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP]
type: 面试题
---

## WEB-282：URL 编码：encodeURIComponent 与 encodeURI 的区别

**答**：
- encodeURI 编码整个 URL，保留 URL 结构字符（:/?#[]@ 等）；encodeURIComponent 编码 URL 组件，连 :/?&= 一起转义。所以查询参数值必须用 encodeURIComponent，否则 `&`/`=` 会破坏参数结构。
- 常见坑：`+` 在 query 里按服务端惯例解析为空格，encodeURIComponent 不转义 `+`，含 + 的值要额外 `.replace(/\+/g, '%2B')` 或用 URLSearchParams（它自动处理）。
- 中文与 emoji：两者都会转成 UTF-8 百分号编码；解码用对应的 decode 系列，错配会产生「ä¸­æ–‡」乱码。
- 现代 API：`new URL()` 构造 + `URLSearchParams` 自动编码，避免手拼。

```javascript
const q = 'a=1&b=中文+词';
encodeURI(`https://x.com/s?kw=${q}`);           // 错：& 未转义，参数被拆
`https://x.com/s?kw=${encodeURIComponent(q)}`;  // 对：a%3D1%26b%3D...
const u = new URL('https://x.com/s');
u.searchParams.set('kw', q);                     // 最稳，自动编码
u.toString();
```
