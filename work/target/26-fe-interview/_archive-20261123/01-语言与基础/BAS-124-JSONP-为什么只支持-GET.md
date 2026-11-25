---
title: [BAS-124] JSONP 为什么只支持 GET？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-124：JSONP 为什么只支持 GET？
**答**：
- JSONP 本质是用 `<script src>` 绕过同源策略：script 标签加载不受 CORS 限制，但它只能发起 GET 请求。
- 服务端把数据包进回调返回 `callback({"data": 1})`，浏览器当作 JS 执行从而拿到数据。
- 现代方案是 CORS，JSONP 只在维护老系统时出现；回调名可被注入，存在 XSS 风险。

```html
<script>
  function handle(data) { console.log('拿到数据', data); }
</script>
<!-- 服务端返回 handle({"code": 0, "data": [1, 2, 3]}) 作为 JS 执行 -->
<script src="https://api.example.com/list?callback=handle"></script>
```
