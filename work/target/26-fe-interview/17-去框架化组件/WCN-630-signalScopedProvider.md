---
title: [WCN-630] 笔试：实现 signal-scoped provider（上下文注入 + 元素断开时自动 dispose 订阅）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-630：笔试：实现 signal-scoped provider（上下文注入 + 元素断开时自动 dispose 订阅）

**答**：
- 需求：实现 withScope(root, store) 与 useSignalIn(el, key)：组件从最近 scope 取 signal 并建立 effect；el 从 DOM 断开时自动清理 effect，防止内存泄漏。
- 思路：scope 存 WeakMap；用 MutationObserver 或 disconnectedCallback 钩子触发清理；effect 返回 dispose 函数登记到 el 的清理表。
- 边界：同一 el 多次 use 要累积清理函数；scope 找不到要报错；清理要幂等。

```javascript
const scopes = new WeakMap();
const cleanups = new WeakMap();
export function withScope(root, store) { scopes.set(root, store); }
function findScope(node) {
  let r = node;
  while (r) { if (scopes.has(r)) return scopes.get(r); r = r.parentNode || r.host; }
  throw new Error('scope not found');
}
export function useSignalIn(el, key, render) {
  const sig = findScope(el)[key];
  const dispose = effect(() => render(sig.get()));
  if (!cleanups.has(el)) cleanups.set(el, []);
  cleanups.get(el).push(dispose);
  const obs = new MutationObserver(() => {
    if (!el.isConnected) {
      cleanups.get(el)?.forEach(fn => fn());
      cleanups.delete(el); obs.disconnect();
    }
  });
  obs.observe(el.parentNode || document.body, { childList: true, subtree: true });
}
```

**评分点**：
- scope 沿 DOM/host 链向上查找（支持 Shadow DOM 的 host 链）。
- effect 的 dispose 登记并在元素断开时自动执行（防泄漏）。
- cleanups 用 WeakMap，不阻止元素被 GC。
- 清理幂等（重复触发不报错、不重复执行）。
