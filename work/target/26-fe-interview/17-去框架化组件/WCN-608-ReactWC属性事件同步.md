---
title: [WCN-608] 笔试：手写 React → Web Component 双向同步适配器（属性 + 事件 + 布尔特判）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-608：笔试：手写 React → Web Component 双向同步适配器（属性 + 事件 + 布尔特判）

**答**：
- 需求：实现 useWC(tag, props, handlers)，对象/数组写 property、基础类型写 attribute、布尔 false 要移除属性、事件用 addEventListener 并正确清理。
- 思路：用 useRef 拿 DOM；useEffect 里 diff 新旧 props；事件名从 handlers 映射；返回 ref 挂到元素。
- 边界：null/undefined 移除属性；函数不写进 DOM；卸载时移除所有监听器避免泄漏。

```javascript
import { useRef, useEffect } from 'react';
export function useWC(tag, props, handlers = {}) {
  const ref = useRef(null);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    for (const [k, v] of Object.entries(props)) {
      if (typeof v === 'object' && v !== null) el[k] = v;
      else if (v === false || v == null) el.removeAttribute(k);
      else el.setAttribute(k, String(v));
    }
    const offs = Object.entries(handlers).map(([evt, fn]) => {
      const name = evt.startsWith('on') ? evt.slice(2).toLowerCase() : evt;
      const h = e => fn(e.detail ?? e);
      el.addEventListener(name, h);
      return () => el.removeEventListener(name, h);
    });
    return () => offs.forEach(off => off());
  }, [props, handlers]);
  return ref;
}
// 用法：const ref = useWC('ds-input', { value, disabled }, { onDsChange: setV });
```

**评分点**：
- 对象/数组写 property、基础类型写 attribute（区分处理）。
- 布尔 false 与 null/undefined 正确移除属性。
- 事件名 onDsChange→ds-change 映射正确，且清理监听器。
- useEffect 依赖与返回清理函数完整（无泄漏）。
