---
title: [WEB-367] 为什么 SameSite=None 必须配 Secure？第三方 Cookie 的命运是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-367：为什么 SameSite=None 必须配 Secure？第三方 Cookie 的命运是什么？
**答**：
- SameSite=None 意味着跨站也发送 Cookie，若允许在 HTTP 上明文传，中间人可直接窃取——规范因此强制 None 必须 Secure，否则浏览器拒收。
- 第三方 Cookie（广告/嵌入式登录）正被 Chrome 逐步限制，依赖它的功能（跨站 SSO iframe、支付跳转回传）要转向 CHIPS（分区 Cookie）、Storage Access API 或第一方化。
- 前端动作：盘点跨站 iframe 登录/支付链路，提前适配。

```javascript
// Set-Cookie: sid=abc; SameSite=None; Secure; Partitioned;
const thirdParty = (strategy) => ({
  partitioned: 'CHIPS: 每个站点一份独立分区 Cookie',
  storageAccess: 'Storage Access API: 用户授权后读取',
  firstParty: '重定向回第一方域名写 Cookie',
}[strategy]);
console.log(thirdParty('partitioned'));
```
