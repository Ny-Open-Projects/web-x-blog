---
title: [NODE-128] SSRF 如何防御（出网白名单与 DNS 校验）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-128：SSRF 如何防御（出网白名单与 DNS 校验）？
**答**：
- 高发场景：webhook 回调、URL 预览、在线文件拉取——凡"服务端替用户发请求"的地方都可能被指到内网。
- 三层防御：协议白名单（禁 file/gopher/dict）、域名白名单、**解析后校验 IP**——只查域名不够，DNS rebinding 可以让域名解析到 127.0.0.1。
- 必封内网段：10/8、172.16/12、192.168/16、127/8、169.254/16（云元数据 169.254.169.254 偷凭证的头号目标）。
- 附加：禁跟随重定向（302 跳内网绕过校验）、限制响应大小与超时、出网走统一代理便于审计。

```javascript
const dns = require('dns').promises;
const net = require('net');
const ALLOW_HOSTS = new Set(['api.github.com', 'notify.internal.com']);

function isPrivate(ip) {
  if (net.isIPv4(ip)) {
    const [a, b] = ip.split('.').map(Number);
    return a === 10 || (a === 172 && b >= 16 && b <= 31) || (a === 192 && b === 168)
      || a === 127 || (a === 169 && b === 254) || a === 0;
  }
  return ip === '::1' || ip.startsWith('fc') || ip.startsWith('fd') || ip.startsWith('fe80');
}

async function safeFetch(raw) {
  const u = new URL(raw);
  if (u.protocol !== 'https:' && u.protocol !== 'http:') throw new Error('bad protocol');
  if (!ALLOW_HOSTS.has(u.hostname)) throw new Error('host not allowed'); // 出网白名单
  const { address } = await dns.lookup(u.hostname);
  if (isPrivate(address)) throw new Error('intranet blocked'); // 解析后校验，防 rebinding
  const res = await fetch(u, {
    redirect: 'error',                    // 禁重定向，防 302 跳内网
    signal: AbortSignal.timeout(5000),
  });
  return res; // 响应体建议流式限长读取，防超大响应打爆内存
}
```
