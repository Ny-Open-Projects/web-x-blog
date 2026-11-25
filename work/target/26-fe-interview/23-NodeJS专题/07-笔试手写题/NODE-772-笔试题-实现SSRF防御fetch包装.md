---
title: [NODE-772] 笔试题——实现 SSRF 防御 fetch 包装（白名单 + DNS 校验）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-772：手写 SSRF 防御

**需求与边界**：
- 需求：SSRF 防御（SCN-NODE-719）——① 域名白名单（预检）；② DNS 解析后校验 IP（防 rebinding——解析与请求 IP 一致）；③ 内网 IP 段拒绝（10/172/169.254/127——metadata 防御）；④ 禁重定向（redirect: 'error'——重定向绕过）。
- 边界：① DNS rebinding 的 TOCTOU（解析与连接的 IP 不一致——自定义 lookup 保障一致）；② IPv6 内网段（::1/fc00——双栈覆盖）；③ URL 解析的异常处理（畸形 URL 拒绝）。

**答**：
```javascript
import dns from 'dns';
function isPrivate(ip) {                               // 内网 IP 段（IPv4+IPv6）
  return /^(10\.|172\.(1[6-9]|2\d|3[01])\.|192\.168\.|127\.|169\.254\.|0\.)/.test(ip)
    || /^(::1|f[cd][0-9a-f]{2}:|fe80:)/i.test(ip);
}
async function safeFetch(userUrl, { allowedHosts } = {}) {
  const url = new URL(userUrl);                        // 畸形 URL 抛错（防御）
  if (url.protocol !== 'https:') throw new Error('HTTPS_ONLY');
  if (!allowedHosts.includes(url.hostname)) throw new Error('HOST_BLOCKED');   // 白名单预检
  // 自定义 lookup：解析后立即校验（防 rebinding 的 TOCTOU——SCN-NODE-719）
  const agent = new https.Agent({
    lookup: (hostname, opts, cb) => dns.lookup(hostname, { all: true }, (err, addrs) => {
      if (err) return cb(err);
      if (addrs.some(a => isPrivate(a.address))) return cb(new Error('PRIVATE_IP'));   // 内网拒绝
      cb(null, addrs);
    }) });
  return fetch(userUrl, { agent, redirect: 'error' }); // 禁重定向（重定向绕过白名单）
}
```

**评分点**:
- 白名单预检 + HTTPS 强制（SCN-NODE-719）。
- 自定义 lookup 解析后校验（DNS rebinding TOCTOU 防御——核心难点）。
- 内网段全覆盖（IPv4 + IPv6 + metadata 169.254）。
- 禁重定向（重定向绕过白名单——redirect: 'error'）。
