---
title: [JS-191] 设计一个前端路由？history API、动态参数、守卫怎么实现？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-191：设计一个前端路由？history API、动态参数、守卫怎么实现？

**答**：
- history 模式：pushState 改 URL 不触发事件，靠 popstate 监听前进后退；拦截 `<a>` 点击改走 pushState（链接劫持），服务端需 fallback 到 index.html。
- 路由表预编译：`/user/:id` 在注册时编译成正则 + 参数名数组，匹配时 extract params；无匹配走 404。
- 守卫管线：beforeEach 支持异步，按序 await；返回 false 中止、返回字符串重定向，重定向复用 push 保证守卫再次生效。
- 订阅者模式：resolve 完成后通知渲染层（组件切换/回调），路由器与 UI 解耦。
- 与 hash 模式取舍：history 需服务端配合但 URL 干净；hash 自带 fallback 但 SEO 弱。

```javascript
// 1. 路径编译：/user/:id -> 正则 + 参数名
function compilePath(path) {
  const keys = [];
  const pattern = path
    .replace(/\/:([^/]+)/g, (_, k) => { keys.push(k); return '/([^/]+)'; })
    .replace(/\//g, '\\/');
  return { regex: new RegExp(`^${pattern}$`), keys };
}

// 2. Router：路由表 + history 集成 + 守卫管线
class Router {
  constructor(routes) {
    this.routes = routes.map((r) => ({ ...r, ...compilePath(r.path) }));
    this.guards = [];
    this.listeners = new Set();
    window.addEventListener('popstate', () => this.resolve(location.pathname)); // 前进后退
  }
  beforeEach(guard) { this.guards.push(guard); }
  subscribe(fn) { this.listeners.add(fn); return () => this.listeners.delete(fn); }

  push(to) {
    history.pushState({}, '', to);
    this.resolve(to);                               // pushState 不触发 popstate，需手动 resolve
  }
  async resolve(path) {
    let matched = null, params = {};
    for (const r of this.routes) {
      const m = r.regex.exec(path);
      if (m) {
        matched = r;
        params = Object.fromEntries(r.keys.map((k, i) => [k, decodeURIComponent(m[i + 1])]));
        break;
      }
    }
    const ctx = { path, params, route: matched };
    for (const guard of this.guards) {              // 守卫串行执行
      const result = await guard(ctx);
      if (result === false) return;                 // 中止
      if (typeof result === 'string' && result !== path) return this.push(result); // 重定向
    }
    this._notify({ ...ctx, component: matched?.component ?? 'NotFound' });
  }
  _notify(ctx) { this.listeners.forEach((fn) => fn(ctx)); }
}

// 3. 使用：动态参数 + 登录守卫 + 重定向
const isLogin = () => !!localStorage.getItem('token');
const router = new Router([
  { path: '/', component: 'HomePage' },
  { path: '/user/:id', component: 'UserPage' },
  { path: '/admin', component: 'AdminPage' },
]);
router.beforeEach((ctx) => {
  if (ctx.component === 'AdminPage' && !isLogin()) return '/login'; // 未登录重定向
  return true;
});
router.subscribe((ctx) => console.log('渲染', ctx.component, ctx.params));
router.push('/user/42');   // 渲染 UserPage { id: '42' }
router.push('/admin');     // 守卫重定向，渲染 LoginPage
```
