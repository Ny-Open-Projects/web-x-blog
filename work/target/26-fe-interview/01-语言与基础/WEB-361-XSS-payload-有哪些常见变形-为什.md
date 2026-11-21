---
title: [WEB-361] XSS payload 有哪些常见变形？为什么"关键词过滤"防不住？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-361：XSS payload 有哪些常见变形？为什么"关键词过滤"防不住？
**答**：
- 变形手段：大小写混写（ScRiPt）、编码（HTML 实体/unicode/eval(atob())）、拆分拼接（<scr+ipt>）、事件属性（onerror=）、svg/math 等非常规标签。
- 黑名单过滤注定滞后：绕法无限，正确思路是输出编码（按上下文 HTML/URL/JS 转义）+ CSP + Trusted Types。
- 示例：filter(script 标签) 拦得住，但 <img src=x onerror=...>、<iframe srcdoc=...> 都不带 script 关键字。

```javascript
const payloads = [
  '<ScRiPt>alert(1)</sCrIpT>',
  '<img src=x onerror=alert(1)>',          // 无 script 关键词
  '<svg onload=alert(1)>',
  '<a href="javascript:alert(1)">x</a>',
  '<iframe srcdoc="&lt;script&gt;alert(1)&lt;/script&gt;">',
];
const badFilter = s => /<script/i.test(s);  // 形同虚设
console.log(payloads.filter(p => !badFilter(p)).length, '个绕过黑名单');
// 正解: DOMPurify.sanitize + 输出编码
```
