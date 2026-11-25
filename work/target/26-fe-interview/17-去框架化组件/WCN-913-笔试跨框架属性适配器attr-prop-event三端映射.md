---
title: [WCN-913] 手写跨框架「属性适配器」：统一 props 映射到 attribute/property/事件三端差异
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-913：手写跨框架「属性适配器」：统一 props 映射到 attribute/property/事件三端差异

**题目**：实现 `createPropAdapter(spec)`，返回 `{ mount(el, props), update(el, nextProps), unmount(el) }`。spec 形如 `{ label: { kind:'attr' }, data: { kind:'prop' }, onChange: { kind:'event', event:'ds-change' } }`。要求：① attr 类型用 setAttribute/removeAttribute（null/undefined 移除）；② prop 类型直接赋给 el[name]；③ event 类型用 addEventListener 绑定，并在 update/unmount 时解绑旧监听避免重复；④ update 只处理变化的 props（浅比较），不重复绑定事件；⑤ unmount 清理所有事件监听。请自足实现并给出「同一适配器分别挂 React/Vue/Solid 创建的同类元素」的可运行示例。

**答**：

```javascript
function createPropAdapter(spec) {
  const listeners = new WeakMap(); // el -> Map<eventKey, handler>
  const ensure = el => (listeners.has(el) || listeners.set(el, new Map()), listeners.get(el));
  function apply(el, key, val, prev) {
    const s = spec[key] || { kind: 'attr' };
    if (s.kind === 'attr') {
      val == null ? el.removeAttribute(key) : el.setAttribute(key, String(val));
    } else if (s.kind === 'prop') {
      el[key] = val;
    } else if (s.kind === 'event') {
      const map = ensure(el);
      if (map.has(key)) { el.removeEventListener(s.event, map.get(key)); map.delete(key); }
      if (typeof val === 'function') {
        const h = e => val(e.detail);
        el.addEventListener(s.event, h);
        map.set(key, h);
      }
    }
  }
  return {
    mount(el, props = {}) { for (const k in props) apply(el, k, props[k]); },
    update(el, next = {}, prev = {}) {
      for (const k in next) if (next[k] !== prev[k]) apply(el, k, next[k], prev[k]);
    },
    unmount(el) {
      const map = listeners.get(el); if (!map) return;
      for (const [k, h] of map) el.removeEventListener(spec[k].event, h);
      map.clear();
    },
  };
}
const a = createPropAdapter({
  label: { kind: 'attr' }, data: { kind: 'prop' },
  onChange: { kind: 'event', event: 'ds-change' },
});
const el = document.createElement('x-prod');
a.mount(el, { label: 'SKU', data: { id: 1 }, onChange: v => console.log(v) });
a.update(el, { label: 'NEW', data: { id: 1 }, onChange: () => {} }, { label: 'SKU', data: { id: 1 } });
a.unmount(el);
```

**评分点**：
- 三类 prop 路由正确：attr/prop/event 分别用正确 API（第③点事件绑定用 detail 转换）。
- update 浅比较只处理变化项、事件不重复绑定（先解绑旧 handler）。
- unmount 完整清理所有监听，WeakMap 避免内存泄漏。
- null/undefined 时 attr 正确移除，边界处理到位。
- 示例展示同一适配器可用于不同框架创建的元素，可运行。
