---
title: [WEB-308] 双向认证 mTLS 是什么？什么场景下前端会遇到？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-308：双向认证 mTLS 是什么？什么场景下前端会遇到？
**答**：
- 常规 HTTPS 只验证服务器；mTLS 客户端也出示证书，服务器验证后建立双向身份。
- 前端会遇到的场景：企业内网系统、银行/支付后台、开放平台回调（微信支付 API v3 要求商户证书）、小程序/混合 App 内嵌的私有协议页。
- 浏览器侧用系统证书库选证书（证书选择弹窗）；前端开发更多是"配置问题"——把 p12 装进系统并让网关信任。

```javascript
// mTLS 握手多两步
// S: CertificateRequest + 证书
// C: Certificate(客户端证书) + CertificateVerify(私钥签名)
const gatewayCheck = (clientCert) => {
  const trusted = ['CN=merchant-01', 'CN=employee-ca'];
  return trusted.includes(clientCert.subject) ? 200 : 403;
};
console.log('微信支付 v3：请求带商户私钥签名 + 平台证书验签');
```
