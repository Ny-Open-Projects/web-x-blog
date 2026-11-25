---
title: [WEB-179] HTTP 头注入（CRLF 注入）是什么原理？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-179：HTTP 头注入（CRLF 注入）是什么原理？
**答**：
- HTTP 头以 CRLF 分隔，若把用户输入拼进响应头且值里含 \r\n，攻击者可提前结束头部区并注入新头甚至新响应体。
- 危害：注入 Set-Cookie（种会话）、Location（任意跳转）等任意头；配合缓存投毒影响其他用户。
- 修复：任何写入响应头的值先拒绝 CR 与 LF；现代框架与新版 Node 的 setHeader 会直接抛 ERR_INVALID_CHAR，但自研网关与老代码仍需自查。
- 延伸：请求侧头同样要校验，防止为请求走私做铺垫。

```javascript
// Node 侧的正确处理：拒绝带换行的头值
const http = require('http');
http.createServer((req, res) => {
  const lang = new URL(req.url, 'http://x').searchParams.get('lang') || 'zh';
  // 漏洞写法（老版本可能被注入）：res.setHeader('Content-Language', lang)
  if (/[\r\n]/.test(lang)) {              // 修复：显式拒绝控制字符
    res.writeHead(400).end('bad lang');
    return;
  }
  res.setHeader('Content-Language', lang);
  res.end('ok');
});
// 攻击样例（旧环境可复现）：?lang=zh%0d%0aSet-Cookie:%20pwned=1
```
