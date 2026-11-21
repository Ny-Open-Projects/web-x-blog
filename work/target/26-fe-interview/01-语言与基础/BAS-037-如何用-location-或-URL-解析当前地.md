---
title: [BAS-037] 如何用 location 或 URL 解析当前地址？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-037：如何用 location 或 URL 解析当前地址？
**答**：
- location.href 是完整地址（可赋值跳转），host 含端口、hostname 不含。
- search 是 `?` 后的 query 字符串，hash 是 `#` 后的部分。
- 现代解析推荐 URL + URLSearchParams，不用手写正则拆 query。

```javascript
const u = new URL('https://a.com:8080/list?kw=vue&page=2#top');
u.hostname;                // 'a.com'
u.port;                    // '8080'
u.searchParams.get('kw');  // 'vue'
u.searchParams.get('page');// '2'
u.hash;                    // '#top'
```
