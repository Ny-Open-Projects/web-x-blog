---
title: [WCN-917] 手写跨框架事件桥：WC 的 CustomEvent 转 React/Vue 各自事件约定
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-917：手写跨框架事件桥：WC 的 CustomEvent 转 React/Vue 各自事件约定

**题目**：实现 `createEventBridge(el, eventName, adapters)`，其中 adapters 形如 `{ react: handler, vue: handler }`，要求：① 监听 el 上的 eventName（CustomEvent），一次派发分发给所有 adapter；② 每个 adapter 收到按框架约定的参数——react 版收到 detail（单参数），vue 版收到 detail（Vue @event 约定）；③ 提供 `on(framework, handler)` / `off(framework)` 动态增删；④ 提供 `destroy()` 移除底层监听；⑤ detail 为 null 时统一回退为空对象，保证 handler 不解构报错。请自足实现并给出「同一 WC 同时驱动 React 与 Vue 处理器」的可运行示例。

**答**：

```javascript
function createEventBridge(el, eventName) {
  const handlers = new Map(); // framework -> handler
  const native = e => {
    const detail = e.detail == null ? {} : e.detail;
    for (const [fw, h] of handlers) {
      if (fw === 'react') h(detail);          // React: 单参数 detail
      else if (fw === 'vue') h(detail);       // Vue: @event 收到 detail
      else h(detail);
    }
  };
  el.addEventListener(eventName, native);
  return {
    on(fw, h) { handlers.set(fw, h); return this; },
    off(fw) { handlers.delete(fw); return this; },
    destroy() { el.removeEventListener(eventName, native); handlers.clear(); },
  };
}
const el = document.createElement('ds-cart');
const bridge = createEventBridge(el, 'ds-change');
bridge.on('react', d => console.log('react:', d.total))
      .on('vue', d => console.log('vue:', d.total));
el.dispatchEvent(new CustomEvent('ds-change', { detail: { total: 199 } }));
// react: 199 / vue: 199
el.dispatchEvent(new CustomEvent('ds-change', {})); // detail=null 回退 {}
bridge.off('vue');
bridge.destroy();
```

**评分点**：
- 一次原生事件分发给所有 adapter（Map 遍历），且各框架参数约定正确。
- on/off/destroy 动态增删与清理，destroy 后不再响应。
- detail 为 null/undefined 时回退空对象，handler 不解构报错（健壮性）。
- 底层监听只注册一次，destroy 正确 removeEventListener 无泄漏。
- 示例覆盖 react/vue 双 handler 与销毁，可运行。
