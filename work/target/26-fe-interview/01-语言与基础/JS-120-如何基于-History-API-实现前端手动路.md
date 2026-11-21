---
title: [JS-120] 如何基于 History API 实现前端手动路由？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-120：如何基于 History API 实现前端手动路由？

**答**：
- 三件套：pushState / replaceState 修改地址不刷新页面，popstate 监听浏览器前进后退。
- 关键坑：pushState/replaceState 不会触发 popstate，必须手动调用渲染函数。
- 链接拦截：捕获 a 标签点击，preventDefault 后改走 pushState，实现 SPA 体验。
- state 可以携带自定义数据；刷新页面时由服务端兜底（history 模式必须配 nginx fallback）。

```javascript
class MiniRouter {
  constructor() { this.routes = new Map(); this.current = null; }

  register(path, handler) { this.routes.set(path, handler); return this; }

  push(path) {
    history.pushState({ path }, '', path); // 不触发 popstate！
    this._render(path);
  }

  replace(path) {
    history.replaceState({ path }, '', path);
    this._render(path);
  }

  back() { history.back(); } // 前进/后退会触发 popstate

  _render(path) {
    this.current = path;
    const handler = this.routes.get(path);
    handler ? handler(path) : console.log('404:', path);
  }
}

const router = new MiniRouter()
  .register('/',      () => console.log('渲染首页'))
  .register('/user',  () => console.log('渲染用户页'))
  .register('/about', () => console.log('渲染关于页'));

// 浏览器前进/后退 → popstate
window.addEventListener('popstate', (e) => {
  console.log('popstate, state =', e.state);
  router._render(location.pathname);
});

// 拦截链接点击 → 走 pushState
document.addEventListener('click', (e) => {
  const a = e.target.closest('a[data-link]');
  if (!a) return;
  e.preventDefault(); // 阻止真实跳转
  router.push(a.getAttribute('href'));
});

router.push('/user'); // 渲染用户页，地址栏变为 /user，无刷新
```

## 十八、错误处理与调试
