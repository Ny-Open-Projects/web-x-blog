---
title: [WEB-374] 前端加密的意义和边界在哪？能替代 HTTPS 吗？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-374：前端加密的意义和边界在哪？能替代 HTTPS 吗？
**答**：
- 前端加密（RSA 混合/AES）防的是"日志泄漏、代理明文缓存密码"这类边缘场景，密钥随 JS 下发即对攻击者公开，不能防中间人。
- 不可替代 HTTPS：TLS 的密钥协商与证书验证才是传输安全根基；前端加密是纵深防御的一层。
- 合理用途：表单密码先哈希再传（防服务端日志带原密码）、本地敏感数据加密存储、与风控配合的签名防重放。

```javascript
// 混合加密示意（但密钥来自 JS = 公开）
const aesKey = genKey();
const encrypted = AES.encrypt(password, aesKey);
const wrapped = RSA.encrypt(aesKey, serverPubKey); // 公钥公开分发
console.log('攻击者也能拿到 JS 里的逻辑 → 只能防日志/缓存明文');
// 真正的防线: HTTPS + 服务端加盐哈希
```
