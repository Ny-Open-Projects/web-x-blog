---
title: [WEB-301] 证书吊销有哪几种方式？OCSP Stapling 解决了什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-301：证书吊销有哪几种方式？OCSP Stapling 解决了什么？
**答**：
- CRL：客户端下载完整吊销列表，又大又滞后；OCSP：客户端实时查证书状态，但多一次外网请求且泄露浏览行为给 CA。
- OCSP Stapling：由服务器定期取 OCSP 响应并"钉"在握手里下发，客户端免外查、隐私保住，CA 侧压力也小。
- 现实：很多浏览器对 OCSP 失败选择"软失败"（继续信任），吊销检查实际是弱保证，所以有 Must-Staple 扩展和短周期证书（如 7 天）的方案。

```javascript
// 握手时服务器附带 stapled OCSP 响应
const stapled = { certSN: '04ab...', status: 'good', producedAt: '2026-11-18', nextUpdate: '2026-11-20' };
function checkOCSP(resp) {
  if (Date.now() > new Date(resp.nextUpdate)) return '过期需重新 stapling';
  return resp.status === 'good' ? '放行' : '吊销';
}
console.log(checkOCSP(stapled));
```
