---
title: [H5-253] SW 的作用域 scope 是什么，与路径的关系
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-253：SW 的作用域 scope 是什么，与路径的关系

**答**：
- scope 默认等于 sw.js 文件所在路径：`/js/sw.js` 的 scope 是 `/js/`，只能拦截该路径下的页面请求
- 想控制整站就要把 sw.js 放在根路径（或用 `Service-Worker-Allowed` 响应头放开更大 scope）
- scope 决定两件事：能控制哪些页面、能拦截哪些请求；scope 外的资源 SW 无感
- 多应用共存：`/app1/sw.js`、`/app2/sw.js` 各管各的，互不干扰——微前端/多站点常用
- 排查钩子：SW「注册成功但不拦截请求」，第一反应查 scope 与页面路径是否匹配

```javascript
// 根路径注册，scope = '/'，全站可控
navigator.serviceWorker.register('/sw.js');
// 响应头放开：Service-Worker-Allowed: /
```
