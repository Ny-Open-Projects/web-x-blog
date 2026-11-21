---
title: [WEB-104] CSP 的 nonce 模式和 hash 模式怎么选？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-104：CSP 的 nonce 模式和 hash 模式怎么选？
**答**：
- nonce：每次响应生成随机值写进 CSP 头与 `<script nonce="...">`，只有带当前 nonce 的内联脚本执行——适合 HTML 由服务端动态渲染的场景。
- hash：把内联脚本内容的 SHA-256 写死在 CSP 里，内容一变就失效——适合静态页、内容基本不变的脚本。
- 两者都要配套 `strict-dynamic`：被信任脚本动态插入的外链脚本自动继承信任，逐步淘汰域名白名单。
- 公共 CDN 场景注意：攻击者可利用同域已有脚本做 XSS 跳板（script gadget），白名单模式安全性弱于 nonce。

```http
# 动态渲染站点用 nonce：模板引擎每次输出都注入新随机值
Content-Security-Policy: script-src 'nonce-N0NCeUx2T2Q4' 'strict-dynamic'; object-src 'none'
```

```html
<!-- 服务器把同一 nonce 写进脚本标签，注入脚本因无 nonce 被拦截 -->
<script nonce="N0NCeUx2T2Q4">
  console.log('可信内联脚本，正常执行');
</script>
<script>
  console.log('攻击者注入的脚本，被 CSP 拦下'); // Refused to execute inline script
</script>

<!-- 静态站点用 hash：CSP 头写 script-src 'sha256-哈希值' -->
<script>console.log('内容不变的内联脚本');</script>
<!-- 生成方式：
     echo -n "console.log('内容不变的内联脚本');" | openssl dgst -sha256 -binary | base64 -->
```
