---
title: [WEB-373] localStorage 存敏感数据的风险清单有哪些？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-373：localStorage 存敏感数据的风险清单有哪些？
**答**：
- XSS 可读：任何脚本都能 localStorage.getItem，token/身份证/手机号一偷一个准；且没有过期机制要自己管。
- 同源即共享：同域下任何路径/任何第三方脚本（广告、SDK）都可见；HTML 注入即全局泄漏。
- 替代方案：HttpOnly Cookie 存凭证、内存态存临时数据、确实要存的做加密（防君子不防 XSS 但防本地扫描）、敏感项走 sessionStorage 缩短寿命。

```javascript
const risk = {
  token: 'XSS 直接偷 → 改 HttpOnly Cookie',
  idCard: '个人信息 → 不落 localStorage',
  draft: '草稿类可用，注意清理',
  session: '临时态 → sessionStorage',
};
console.log('localStorage = 无过期+脚本可读，敏感数据慎用');
```
