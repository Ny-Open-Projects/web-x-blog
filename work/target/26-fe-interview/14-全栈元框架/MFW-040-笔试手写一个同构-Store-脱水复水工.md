---
title: [MFW-040] 笔试：手写同构 Store 的脱水复水工具（createIsomorphicStore）
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-040：笔试：手写同构 Store 的脱水复水工具（createIsomorphicStore）
**答**：实现 `createIsomorphicStore(name, reducer)`：服务端每次调用 `dehydrate()` 把状态序列化为可嵌 HTML 的 JSON（防 XSS 转义 `<`）；客户端首次挂载从 `window.__STORE__` 复水（严格模式与重复复水防御），之后走普通内存 store。要求支持 Date 复原、循环引用检测报错。

```javascript
function createIsomorphicStore(name, reducer) {
  let state = typeof window === 'undefined' ? undefined : undefined;
  const listeners = new Set();

  function dispatch(action) {
    state = reducer(state, action);
    listeners.forEach((l) => l(state));
  }

  // 服务端：脱水为安全 JSON（防 </script> 逃逸 + XSS）
  function dehydrate() {
    const seen = new WeakSet();
    const safe = JSON.stringify(state, (k, v) => {
      if (typeof v === 'object' && v !== null) {
        if (seen.has(v)) throw new Error('循环引用不可序列化');
        seen.add(v);
        if (v instanceof Date) return { __type: 'Date', value: v.toISOString() };
      }
      return v;
    }).replace(/</g, '\\u003c'); // 关键：防 </script> 提前闭合
    return `<script>window.__STORE__=Object.assign(window.__STORE__||{},{${name}:${safe}})</script>`;
  }

  // 客户端：复水（幂等防御 + Date 复原）
  function rehydrate() {
    if (typeof window === 'undefined') return;
    if (state !== undefined) return;            // 已初始化：跳过（StrictMode/双调用安全）
    const raw = window.__STORE__?.[name];
    if (!raw) return;
    state = JSON.parse(JSON.stringify(raw), (k, v) => {
      if (v && v.__type === 'Date') return new Date(v.value);
      return v;
    });
    delete window.__STORE__[name];              // 消费后删除：防止二次复水脏读
    listeners.forEach((l) => l(state));
  }

  function subscribe(fn) { listeners.add(fn); return () => listeners.delete(fn); }
  function getState() { return state; }
  return { dispatch, dehydrate, rehydrate, subscribe, getState };
}

// **评分点**
// 1. XSS 防线：序列化后把 `<` 转义成 \\u003c，堵住 </script> 提前闭合与恶意脚本注入。
// 2. 复水幂等：state 已存在直接返回 + 消费后 delete，双调用/多 bundle 场景不脏读。
// 3. Date 保留（自定义 replacer/reviver），不是简单 JSON 往返丢信息。
// 4. 循环引用显式报错而非静默截断，面试官看重边界意识。
```
