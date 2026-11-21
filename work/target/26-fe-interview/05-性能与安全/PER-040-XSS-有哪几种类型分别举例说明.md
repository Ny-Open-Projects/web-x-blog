---
title: [PER-040] XSS 有哪几种类型？分别举例说明。
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-040：XSS 有哪几种类型？分别举例说明。

**答**：
- **存储型**：恶意脚本被存入数据库（如评论），所有访问者都会执行，危害最大。
- **反射型**：恶意脚本藏在 URL 参数中，服务器把它"反射"进响应页面，需诱导用户点击特制链接。
- **DOM 型**：纯前端问题，前端把不可信数据（location.hash、URL 参数）直接写入 `innerHTML`，不经过服务器。
- 共同本质：**不可信数据被当作 HTML/JS 执行**。防御核心是"数据与代码分离"，永远不信任用户输入。

```javascript
// DOM 型 XSS：把 location.hash 直接写入 innerHTML
// 攻击者构造链接 https://site.com/page#<img src=x onerror=alert(document.cookie)>
const hash = decodeURIComponent(location.hash.slice(1));
document.getElementById('content').innerHTML = hash; // 漏洞点：不可信数据被当 HTML 执行

// 安全写法：纯文本场景用 textContent，浏览器不会解析任何标签
document.getElementById('content').textContent = hash;
```
