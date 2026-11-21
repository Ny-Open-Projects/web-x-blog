---
title: [ALG-133] 设计一个前端路由：支持 `/user/:id` 动态段与 `/assets/*` 通配，hash 与 history 双模式，刷新后能恢复？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-133：设计一个前端路由：支持 `/user/:id` 动态段与 `/assets/*` 通配，hash 与 history 双模式，刷新后能恢复？
**答**：路由本质是"模式 → 正则"的编译与匹配：`:id` 编译为 `([^/]+)`（单段），`*` 编译为 `(.*)`（跨段），命中后把捕获组按序传给 handler。history 模式靠 `pushState` + `popstate` 监听；刷新恢复需要服务端把任意路径 fallback 到 index.html。匹配按注册顺序 O(路由数)，可用正则前缀树优化但一般不需要。

```javascript
class Router {
  constructor() { this.routes = []; }
  add(pattern, handler) {
    const re = new RegExp('^' + pattern
      .replace(/:[^/]+/g, '([^/]+)')   // /user/:id => /user/([^/]+)
      .replace(/\*/g, '(.*)') + '$');  // /assets/* => /assets/(.*)
    this.routes.push({ re, handler });
  }
  resolve(path) {
    for (const { re, handler } of this.routes) { // 按注册顺序匹配
      const m = path.match(re);
      if (m) return handler(...m.slice(1));      // 捕获组按序传参
    }
  }
  push(path) {
    history.pushState(null, '', path);           // 不触发页面刷新
    this.resolve(path);
  }
}
window.addEventListener('popstate', () => router.resolve(location.pathname)); // 前进后退
// 服务端需将任意路径 fallback 到 index.html，刷新才能恢复
```
