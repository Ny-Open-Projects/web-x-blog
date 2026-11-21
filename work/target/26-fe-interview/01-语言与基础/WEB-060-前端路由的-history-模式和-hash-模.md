---
title: [WEB-060] 前端路由的 history 模式和 hash 模式有什么区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-060：前端路由的 history 模式和 hash 模式有什么区别？
**答**：
- hash 模式：URL 形如 `/#/detail`，改变 hash 不发请求，靠 `hashchange` 事件监听；实现简单、部署无需服务端配置，但 URL 带 # 不美观，锚点功能被占用。
- history 模式：`pushState/replaceState` 改变路径不刷新页面，`popstate` 监听前进后退（pushState 本身不触发 popstate）；URL 与后端路径一致，需要服务端把所有路径 fallback 到 index.html，否则刷新 404。
- SEO 与规范上 history 更优；现代框架路由默认 history。
- 两者的路由变化都不会重新请求页面，本质都是浏览器端的状态切换。

```javascript
// 最小 hash 路由实现
class HashRouter {
  constructor() {
    this.routes = {};
    window.addEventListener('hashchange', () => this.render());
  }
  register(path, view) {
    this.routes[path] = view;
  }
  push(path) {
    location.hash = path; // 改 hash，触发 hashchange，不发请求
  }
  render() {
    const path = location.hash.slice(1) || '/';
    document.getElementById('app').innerHTML = this.routes[path] || '404';
  }
}

const router = new HashRouter();
router.register('/', '<h2>首页</h2>');
router.register('/detail', '<h2>详情页</h2>');
router.render();
```

```javascript
// 最小 history 路由实现
class HistoryRouter {
  constructor() {
    // popstate 只在浏览器前进后退时触发，pushState/replaceState 不会触发它
    window.addEventListener('popstate', () => this.render());
  }
  push(path) {
    history.pushState({ path }, '', path); // 改路径不刷新页面、不发请求
    this.render(); // 编程式跳转需要手动渲染
  }
  render() {
    const path = location.pathname;
    document.getElementById('app').innerHTML =
      path === '/detail' ? '<h2>详情页</h2>' : '<h2>首页</h2>';
  }
}

const router = new HistoryRouter();
document.querySelector('a').addEventListener('click', (e) => {
  e.preventDefault(); // 拦截默认跳转，改用 pushState
  router.push(e.target.pathname);
});
```

```nginx
# history 模式的服务端配套：所有路径 fallback 到 index.html，否则刷新 404
server {
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

## 十二、HTTP 语义进阶
