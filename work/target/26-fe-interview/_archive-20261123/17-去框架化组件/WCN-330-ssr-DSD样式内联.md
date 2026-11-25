---
title: [WCN-330] DSD 的样式内联体积问题与治理？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-330：DSD 的样式内联体积问题与治理？
**答**：
- 每元素 DSD 内联 <style> ——多元素页面样式重复传输。
- 治理 1：critical 样式内联 + 非关键样式经 constructable stylesheet 全局一次（水合后 adopt）。
- 治理 2：样式压缩（去空格/合并规则）构建期完成。
- 治理 3：元素样式共享层（同元素多次出现只一份模板——浏览器 template 复用无解，内容仍重复——按使用频次评估）。
- 度量：样式占 HTML 体积比。

```javascript
// 关键样式内联 + 水合后 adopt 全局表
renderDSD = (p) => `<template shadowrootmode="open">
<style>${criticalCSS}</style>${body}</template>`;
// 客户端注册时：shadowRoot.adoptedStyleSheets.push(globalSheet) 替换补全
r
```
