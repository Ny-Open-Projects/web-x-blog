---
title: [WEB-234] SSRF 与前端：为什么后端服务要限制出网请求？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-234：SSRF 与前端：为什么后端服务要限制出网请求？

**答**：
- SSRF（服务端请求伪造）：后端按用户输入发起请求（如「输入 URL 提取网页标题」「上传头像从 URL 拉取」），攻击者让它请求内网——`http://169.254.169.254/`（云元数据，可偷 AK/SK）、`http://127.0.0.1:6379`（Redis 未授权）。
- 前端相关的关联面：开放重定向可当 SSRF 跳板；SSO 回调地址不校验也会被利用；前端负责的 URL 校验不可信，校验必须在服务端做。
- 防御：出网域名白名单、禁止解析到内网 IP（DNS 解析后再校验 IP，防 DNS rebinding）、禁用 30x 跟随或每跳重校验、云上禁用元数据 v1（用 v2 带 token）。
- 前端视角的价值：能画出「不可信输入从页面到后端出网」的数据流，说明自己有端到端安全意识。

```javascript
// 后端 URL 校验示意（Node）
const dns = require('dns').promises;
async function safeFetchUrl(raw) {
  const u = new URL(raw);
  if (!['http:', 'https:'].includes(u.protocol)) throw new Error('bad protocol');
  const { address } = await dns.lookup(u.hostname);
  if (isPrivateIP(address)) throw new Error('内网地址拒绝'); // 10/172.16/192.168/169.254/127
  // 用解析后的 IP 发起并带 Host 头，防止 lookup 与请求之间 DNS 被改（rebinding）
  return fetch(u.hostname, { resolvedIP: address });
}
```
