---
title: [WEB-319] JWT 的三段分别是什么？为什么说它是"自证明"的？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 鉴权]
type: 面试题
---

## WEB-319：JWT 的三段分别是什么？为什么说它是"自证明"的？
**答**：
- Header（算法与类型）.Payload（claims）.Signature（对前两段的 HMAC 或 RSA 签名），前两段只是 base64url 编码不是加密，任何人都可读。
- 自证明：服务端只需验签即可信任 payload（userId/过期时间），不用查库；这是无状态扩容的关键。
- 陷阱：改了 payload 不重签会验签失败；但 alg:none 历史漏洞说明要白名单校验算法，且敏感数据绝不放 payload。

```javascript
function decodeJWT(token) {
  const [h, p, s] = token.split('.');
  const header = JSON.parse(atobURL(h)), payload = JSON.parse(atobURL(p));
  // 验签：只允许预期算法
  if (!['HS256', 'RS256'].includes(header.alg)) throw new Error('alg 不在白名单');
  return payload; // { sub, exp, role } —— 明文可读，勿放敏感信息
}
function atobURL(s) { return JSON.parse(Buffer.from(s, 'base64url').toString()); }
console.log(decodeJWT('eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIn0.abc'.replace('.abc', '.YWJj')));
```
