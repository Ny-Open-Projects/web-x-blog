---
title: [WEB-178] URL 里的百分号编码、IDN、Punycode 是怎么回事？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-178：URL 里的百分号编码、IDN、Punycode 是怎么回事？
**答**：
- URL 只允许有限字符集，其余按 UTF-8 字节做百分号编码；encodeURI 保留 URL 结构字符，encodeURIComponent 编码得更彻底（查询参数值用它）。
- IDN（国际化域名）：中文/日文域名在 DNS 层不存在，转成 Punycode（xn-- 开头）才是真实协议值。
- 安全关联：同形异义字符（西里尔 a 与拉丁 a）可伪装钓鱼域名，浏览器靠 IDN 策略与显示 Punycode 缓解。
- 陷阱集：+ 在表单编码里是空格但 encodeURIComponent 不转它（变 %2B）；location.search 拿到的是已编码原文，读参数用 URLSearchParams。

```javascript
const raw = 'https://例え.jp/搜索 a?q=中文&plus=1+2';
const u = new URL(raw);
console.log(u.href);
// https://xn--r8jz45g.jp/%E6%90%9C%E7%B4%A2%20a?q=%E4%B8%AD%E6%96%87&plus=1+2
// 域名被转成 Punycode，路径与查询按 UTF-8 字节做百分号编码
console.log(encodeURIComponent('a+b'));   // a%2Bb，+ 必须编码否则被解析成空格
console.log(encodeURIComponent('中文'));  // %E4%B8%AD%E6%96%87
new URLSearchParams('?plus=1+2').get('plus');   // '1 2'，表单语义里 + 是空格
new URLSearchParams('?plus=1%2B2').get('plus'); // '1+2'
```
