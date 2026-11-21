---
title: [WEB-309] 证书透明度（CT）是什么？和普通 HTTPS 有什么区别？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-309：证书透明度（CT）是什么？和普通 HTTPS 有什么区别？
**答**：
- CA 体系的问题：任何受信 CA 都能给任何域名签证书（DigiNotar 事件即此塌方）；CT 要求每张公开证书必须登记到公开可审计的日志。
- 机制：证书里嵌入 SCT（签名时间戳）证明已上日志；浏览器验证 SCT，无 SCT 的证书可能被拒。
- 价值：域名所有者可用 ct 工具监控"有没有人给我的域名签了未知证书"，劫持能被及时发现。

```javascript
// 证书扩展：Signed Certificate Timestamp
const cert = { subject: 'example.com', scts: [{ logId: 'argon2026', timestamp: 1731888000000, sig: '...' }] };
function audit(domain, ctLogs) {
  const bad = ctLogs.filter(e => e.subject === domain && !e.expectedIssuers.includes(e.issuer));
  return bad.length ? '发现异常签发，立即吊销排查' : '正常';
}
console.log('crt.sh / Google CT 搜索自己的域名');
```
