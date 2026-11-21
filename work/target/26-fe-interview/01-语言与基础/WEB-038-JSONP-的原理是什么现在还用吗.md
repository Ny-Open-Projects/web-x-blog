---
title: [WEB-038] JSONP 的原理是什么？现在还用吗？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-038：JSONP 的原理是什么？现在还用吗？
**答**：
- 利用 `<script src>` 加载不受同源策略限制：前端定义全局回调函数，请求带上 `?callback=fnName`，服务器返回 `fnName(数据)` 形式的 JS，脚本加载即执行回调。
- 只能发 GET，没有错误处理（加载失败只有全局 onerror），还要承担执行第三方 JS 的 XSS 风险。
- 只兼容老浏览器时代有意义，现代开发一律用 CORS；面试答原理 + 明确说已淘汰即可。
- 服务端对 callback 参数要做白名单校验，否则是反射型 XSS 注入点。

```html
<!-- 客户端：定义全局回调，动态插入 script -->
<div id="weather"></div>
<script>
  // 1. 预先定义全局回调函数
  window.handleWeather = function (data) {
    document.getElementById('weather').textContent = `${data.city} ${data.temp}度`;
  };

  // 2. 动态创建 script，callback 名随请求传给服务端
  const cb = 'handleWeather';
  const s = document.createElement('script');
  s.src = `https://api.other-origin.com/weather?city=beijing&callback=${cb}`;
  document.body.appendChild(s); // 加载完成即执行 handleWeather(data)
</script>
<!-- 服务端返回内容实际是：handleWeather({"city":"北京","temp":18}) -->
```
