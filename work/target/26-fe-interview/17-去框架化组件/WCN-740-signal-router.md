---
title: [WCN-740] 用 Signals 实现一个极简路由（signal 驱动的 router）怎么做？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-740：用 Signals 实现一个极简路由（signal 驱动的 router）怎么做？

**答**：
- 结论：把 location（pathname/search/hash）封装成 signal，路由匹配用 computed 派生当前路由记录与 params；popstate/hashchange 时写回 signal，导航时 pushState 后同步 signal。
- 优势：视图只需订阅当前路由 signal，参数变化自动触发细粒度更新，无需重新挂载整页；用 computed 缓存匹配结果。
- 追问钩子：路由守卫/重定向放哪里？考察「写 signal 前的拦截」与「导航事务」设计。

```javascript
function createRouter(routes) {
  const location = signal({ path: location.pathname, query: location.search });
  const match = computed(() => {
    const { path } = location.value;
    for (const r of routes) {
      const m = path.match(r.re);
      if (m) return { route: r, params: m.groups || {} };
    }
    return { route: null, params: {} };
  });
  function navigate(to) {
    history.pushState({}, '', to);
    location.value = { path: new URL(to, origin).pathname, query: new URL(to, origin).search };
  }
  window.addEventListener('popstate', () => {
    location.value = { path: location.pathname, query: location.search };
  });
  return { match, navigate };
}
console.log(typeof createRouter);
```
