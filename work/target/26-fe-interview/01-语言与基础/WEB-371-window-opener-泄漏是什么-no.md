---
title: [WEB-371] window.opener 泄漏是什么？noopener 与 noreferrer 的区别？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-371：window.opener 泄漏是什么？noopener 与 noreferrer 的区别？
**答**：
- target=_blank 打开的页面可通过 window.opener 控制原页面（opener.location = phishing），标签页反劫持。
- 解法：<a rel=noopener noreferrer target=_blank>，JS 窗口用 window.open(url, _blank, noopener)。
- 区别：noopener 断开 opener 引用但保留 Referer；noreferrer 连 Referer 一起去掉（隐含 noopener）。现代浏览器对 target=_blank 默认隐式 noopener，但显式写仍是最佳实践。

```javascript
// 反面: window.open(url) → 新页面 window.opener === 旧窗口
window.open(url, '_blank', 'noopener,noreferrer');
// <a href="..." target="_blank" rel="noopener noreferrer">
const links = document.querySelectorAll('a[target=_blank]');
links.forEach(a => a.relList.add('noopener', 'noreferrer'));
console.log('反向也成立：自己页面不要乱用 window.opener');
```
