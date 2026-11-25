---
title: [WCN-741] 笔试：手写 signal 驱动的极简 router（响应式 params）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-741：笔试：手写 signal 驱动的极简 router（响应式 params）

**答**：
- 需求：实现 `createRouter(routes)`，routes 形如 `[{ path:'/user/:id', name:'user' }]`。返回 `{ current, navigate, subscribe }`：current 为 computed 风格派生值 `{name, params}`；navigate(to) 更新内部 location signal 并通知订阅；subscribe(fn) 订阅变化。无需真实 history，内存态即可。
- 要点：把 path 模式编译成正则并提取命名参数；location 用 signal；current 由 computed 派生；边界：无匹配返回 {name:null,params:{}}，query 解析。

```javascript
function signal(v) {
  let val = v; const subs = new Set();
  return {
    get value() { return val; },
    set value(nv) { val = nv; subs.forEach((f) => f(val)); },
    subscribe(f) { subs.add(f); },
  };
}
function compile(path) {
  const keys = [];
  const re = new RegExp('^' + path.replace(/:([\w]+)/g, (_, k) => {
    keys.push(k); return '([^/]+)';
  }) + '/?$');
  return { re, keys };
}
function createRouter(routes) {
  const compiled = routes.map((r) => ({ ...r, ...compile(r.path) }));
  const location = signal('/');
  const current = {
    get value() {
      for (const r of compiled) {
        const m = location.value.split('?')[0].match(r.re);
        if (m) {
          const params = {}; r.keys.forEach((k, i) => params[k] = m[i + 1]);
          return { name: r.name, params };
        }
      }
      return { name: null, params: {} };
    },
  };
  return {
    current,
    navigate(to) { location.value = to; },
    subscribe(fn) { location.subscribe(fn); },
  };
}
const r = createRouter([{ path: '/user/:id', name: 'user' }]);
r.navigate('/user/42');
console.log(r.current.value);   // { name:'user', params:{ id:'42' } }
```

**评分点**：
- 路径模式正确编译为正则并提取命名参数（:id）。
- current 由 location signal 派生，导航后自动更新。
- query 与尾斜杠有处理，无匹配返回空结构。
- subscribe 通知机制完整，API 自洽可测。
