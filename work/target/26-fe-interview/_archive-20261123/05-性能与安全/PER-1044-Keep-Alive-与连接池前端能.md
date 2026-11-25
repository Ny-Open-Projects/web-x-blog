---
title: [PER-1044] Keep-Alive 与连接池：前端能做什么
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1044：Keep-Alive 与连接池：前端能做什么

**答**：
- 浏览器自动管理连接池（每域名 6/多路复用），前端可做的：避免频繁跨域请求（收敛域名）、保持长连接活跃（心跳）、Service Worker 代理合并请求。
- Server 端配合：keepalive_timeout 要大于客户端心跳间隔，否则频繁重建；TCP keepalive 与 HTTP keep-alive 是两回事。
- keepalive fetch：页面卸载时的请求用 fetch(url, { keepalive: true }) 替代 sendBeacon 以携带自定义头。
- 验证：Network 面板看 Connection ID 是否复用；频繁重建说明超时或域名切换。

```javascript
// 页面卸载上报：keepalive fetch 优于 beacon（可带 headers）
function unloadReport(data) {
  fetch('/rum', { method: 'POST', keepalive: true,          // < 64KB 限制
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
    credentials: 'include' }).catch(() => {});
}
addEventListener('pagehide', () => unloadReport(finalMetrics()));
// 对比 navigator.sendBeacon：不带自定义头、无法设置 credentials 精确值
```
