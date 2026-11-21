---
title: [WEB-199] 第三方 Cookie 退场后，前端的网络层要怎么演进？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-199：第三方 Cookie 退场后，前端的网络层要怎么演进？
**答**：
- 总方向：从"依赖跨站标识"转向"第一方持有 + 服务端聚合"——登录态用第一方 Cookie/Token，统计走服务端埋点（server-side tagging）。
- 新工具箱：CHIPS 分区 Cookie（嵌 iframe 场景）、Storage Access API（用户授权后短暂访问第一方 Cookie）、Topics API 与 Protected Audience（广告）。
- 站点关系重构：同主体多域名按"第一方集合"思路收敛；跨站登录用 FedCM 让浏览器托管联合登录，摆脱 iframe 内第三方 Cookie。
- 工程动作：盘点所有依赖第三方 Cookie 的能力（广告归因、跨站登录、A/B 工具），逐个迁移并做兼容探测。

```javascript
// 嵌入 iframe 的业务申请访问其第一方 Cookie（Storage Access API）
async function ensureFirstPartyAccess() {
  if (await document.hasStorageAccess()) return true;
  try {
    await document.requestStorageAccess();   // 需要用户手势触发，浏览器会弹授权提示
    return true;
  } catch {
    // 未授权：降级为不依赖跨站 Cookie 的模式（分区 Cookie 或 URL 传参）
    return false;
  }
}
// FedCM（联合登录 API）：浏览器托管的第三方登录，无需第三方 Cookie
try {
  const cred = await IdentityCredential.get({
    providers: [{ configURL: 'https://idp.example.com/fedcm.json' }],
  });
  await loginWith(cred.token);
} catch (e) { /* 不支持或用户拒绝时，降级走传统 OAuth 流程 */ }
```
