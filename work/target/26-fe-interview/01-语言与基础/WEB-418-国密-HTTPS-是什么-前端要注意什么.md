---
title: [WEB-418] 国密 HTTPS 是什么，前端要注意什么
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, HTTPS]
type: 面试题
---

## WEB-418：国密 HTTPS 是什么，前端要注意什么

**答**：
- 国密：国内商用密码标准（SM2/SM3/SM4），政府、金融、国企项目常被要求国密改造
- 浏览器支持分裂：主流 Chrome/Safari 不支持国密套件（GM TLS），需国产浏览器（360、奇安信等）或网关双证书兼容
- 常见架构：网关同时挂 RSA 证书和国密证书，按客户端能力协商，前端代码无感
- 前端注意点：JS 加密库若需配合国密（SM2/SM4 加密敏感字段），用 sm-crypto 这类库，不要混用 RSA 的思路
- 面试钩子：能说出「双证书兼容方案」和「SM4 是对称、SM2 是非对称」就够大多数岗位了

```javascript
// 前端配合国密做字段加密（sm-crypto）
const sm2 = require('sm-crypto').sm2;
const publicKey = '04ABCD...'; // 后端下发的 SM2 公钥
const cipher = sm2.doEncrypt(JSON.stringify({ idCard: '110...' }), publicKey, 1);
fetch('/api/submit', { method: 'POST', body: JSON.stringify({ data: cipher }) });
```
