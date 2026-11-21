---
title: [WEB-360] Trusted Types 是什么？它防住什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-360：Trusted Types 是什么？它防住什么？
**答**：
- Trusted Types（CSP: require-trusted-types-for script）禁止把字符串直接赋给 innerHTML 等注入点，必须传 TrustedHTML 对象。
- 强制应用走统一净化函数（DOMPurify → createHTML），让"漏一处 innerHTML 就是 XSS"变成"类型不过编译不过"。
- 现状：Chrome 已支持，Safari/Firefox 未落地；生产用法是先 report-only 统计注入点再逐步改造。

```javascript
// CSP: require-trusted-types-for 'script'; trusted-types dompurify
const policy = trustedTypes.createPolicy('dompurify', {
  createHTML: (s) => DOMPurify.sanitize(s),
});
el.innerHTML = policy.createHTML(userInput); // 必须过净化
// el.innerHTML = userInput;  ← 直接 TypeError
console.log('把 XSS 从"运行时漏洞"变成"类型错误"');
```
