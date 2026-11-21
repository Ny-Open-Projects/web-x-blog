---
title: [WEB-444] window.open 与 noopener 有什么安全关系
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-444：window.open 与 noopener 有什么安全关系

**答**：
- 默认情况下 `window.open(url)` 打开的新页面通过 `window.opener` 拿到原页面引用，能改原页面地址（tabnabbing 钓鱼）
- 经典攻击：用户停留在被打开的低质页面，攻击者趁机把原 tab 改成伪造的登录页
- 修复：`<a target="_blank" rel="noopener noreferrer">` 或 `window.open(url, '_blank', 'noopener,noreferrer')`；现代浏览器对 target=_blank 默认隐式 noopener，但显式写仍是规范
- opener 断掉后新页面拿不到 opener（为 null），需要通信时用 postMessage 并校验 origin
- 相关姊妹头：COOP（Cross-Origin-Opener-Policy）在 HTTP 层整体隔离 opener 关系

```javascript
const win = window.open(url, '_blank', 'noopener,noreferrer');
console.log(win); // null 或受限引用——这正是预期行为
// 反向提醒：自己页面也别依赖 window.opener 做关键逻辑
```
