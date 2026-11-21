---
title: [WEB-290] Alt-Svc 和 HTTPS/SVCB 记录是怎么帮浏览器"发现"HTTP/3 的？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTP3]
type: 面试题
---

## WEB-290：Alt-Svc 和 HTTPS/SVCB 记录是怎么帮浏览器"发现"HTTP/3 的？
**答**：
- Alt-Svc 是"事后发现"：第一次仍走 TCP+TLS，响应头告知可用 h3，浏览器缓存后下次连接试 UDP，失败自动回退。
- HTTPS（SVCB）DNS 记录是"事前发现"：DNS 查询阶段就拿到 h3 支持、端口与 ECH 配置，省掉一次试探往返。
- 两者都只是"提示"：h3 握手失败必须能无缝回退 HTTP/2，所以服务端双栈要长期共存。

```javascript
// 响应头: Alt-Svc: h3=":443"; ma=86400
const dnsHttpsRecord = { priority: 1, alpn: ['h3'], port: 443, ech: '...' };
function connect(host) {
  const rec = dnsHttpsRecord;            // 事前：DNS 里已知 h3
  if (rec && rec.alpn.includes('h3')) return tryQUIC(host, rec.port)
    .catch(() => tryTCP(host));          // 失败回退
  return tryTCP(host).then(res => rememberAltSvc(res.headers));
}
console.log('Alt-Svc 事后提示，SVCB 事前直连');
```
