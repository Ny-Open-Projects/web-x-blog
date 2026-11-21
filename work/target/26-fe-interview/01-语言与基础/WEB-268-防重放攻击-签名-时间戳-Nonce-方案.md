---
title: [WEB-268] 防重放攻击：签名、时间戳、Nonce 方案
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-268：防重放攻击：签名、时间戳、Nonce 方案

**答**：
- 威胁：HTTPS 只保护传输过程，攻击者拿到（或客户端内部被劫持）完整请求可原样重放——重复下单、重复提现。
- 三件套：timestamp（窗口外直接拒绝，如 ±5min）、nonce（随机串，Redis 记录防重复，TTL=窗口大小）、signature（对参数+ts+nonce 用密钥/私钥签名，篡改任意一项签名失效）。
- 顺序：先验签 → 查时间窗 → 查 nonce 未用过（SETNX）。
- 注意：纯前端签名密钥会被扒出来，前端签名主要用于防参数篡改与业务侧重放，真正强防护要配合服务端风控（设备指纹、频控、幂等）。

```javascript
// 前端签名
async function signedFetch(url, body) {
  const ts = Date.now();
  const nonce = crypto.randomUUID();
  const sig = await sha256hex(`${url}|${JSON.stringify(body)}|${ts}|${nonce}|${secret}`);
  return fetch(url, { method: 'POST', body: JSON.stringify({ ...body, ts, nonce, sig }) });
}
// 服务端: 验签 → |now-ts|<300s → SETNX nonce 防重放
```
