---
title: [WCN-095] 笔试：手写 Signals 版路由状态（URL ↔ signal 双向同步）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-095：笔试：手写 Signals 版路由状态

**题目**：实现 `createRouteSignal()`：① `route` signal 反映当前 hash 路由（含 query 参数对象）；② `navigate(path, { replace })` 更新 URL 并同步 signal；③ 浏览器前进后退自动同步 signal；④ query 参数变更触发 signal 更新但保留 scroll 位置；⑤ 组件销毁移除监听；⑥ query 序列化/反序列化对称。

**答**：

```javascript
import { createSignal } from './mini.js';

function parseHash() {
  const raw = location.hash.slice(1) || '/';
  const [path, qs] = raw.split('?');
  const query = Object.fromEntries(new URLSearchParams(qs ?? ''));
  return { path, query };
}
const same = (a, b) => a.path === b.path && JSON.stringify(a.query) === JSON.stringify(b.query);

export function createRouteSignal() {
  const [route, setRoute] = createSignal(parseHash());
  const onHash = () => { const n = parseHash(); if (!same(untrack(route), n)) setRoute(n); };
  window.addEventListener('hashchange', onHash);

  function navigate(path, { replace = false, query = {} } = {}) {
    const qs = new URLSearchParams(query).toString();
    const target = `#${path}${qs ? '?' + qs : ''}`;
    if (replace) location.replace(target);          // 不留历史
    else location.hash = target.slice(1);           // 入栈
    onHash();                                       // hash 赋值相同字符串不触发事件，手动同步
  }

  return { route, navigate,
    destroy() { window.removeEventListener('hashchange', onHash); } };
}
// 绑定：effect(() => { const { path, query } = route(); router.render(path, query); });
// effect(() => { if (route().query.tab === 'pay') highlightPay(); }); // query 级细粒度
```

**评分点**：
- 双向同步的两个入口（事件 + navigate 手动）都覆盖；同值赋值不触发 hashchange 的坑处理。
- replace 语义用 location.replace；query 对象对称序列化。
- same 浅比较避免冗余 setRoute（短路下游 effect）。
- destroy 移除监听。
