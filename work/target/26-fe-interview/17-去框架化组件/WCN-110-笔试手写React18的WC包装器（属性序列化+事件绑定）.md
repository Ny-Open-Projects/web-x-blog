---
title: [WCN-110] 笔试：手写 React 18 的 WC 包装器（属性白名单序列化 + CustomEvent 绑定）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 跨框架复用]
type: 笔试题
---

## WCN-110：笔试：手写 React 18 的 WC 包装器

**题目**：在 React 18（无原生 WC prop 支持）下实现 `wrap(tag, { props, events })`：① 返回 React 组件：对象/数组 props 走 property 赋值，基础类型走 attribute；② events 列表（如 `['change']`）映射为 `onChange` prop，组件卸载时解绑；③ ref 转发到元素；④ useEffect 中 diff 属性变化只更新变更项；⑤ 类型签名示例。

**答**：

```tsx
import * as React from 'react';

export function wrap(tag, { props = [], events = [] } = {}) {
  const primitive = (v) => ['string', 'number', 'boolean'].includes(typeof v);
  return React.forwardRef(function WcWrapper(rawProps, ref) {
    const elRef = React.useRef(null);
    const prev = React.useRef({});

    React.useEffect(() => {
      const el = elRef.current;
      if (!el) return;
      const unbinders = events.map((name) => {
        const handler = rawProps[`on${name[0].toUpperCase()}${name.slice(1)}`];
        const wrapped = handler ? (e) => handler(e) : undefined;
        if (wrapped) el.addEventListener(name, wrapped);
        return () => el.removeEventListener(name, wrapped);
      });
      return () => unbinders.forEach((u) => u());
    }, events.map((n) => rawProps[`on${n[0].toUpperCase()}${n.slice(1)}`]));

    React.useEffect(() => {
      const el = elRef.current, p = prev.current;
      for (const key of props) {
        const nv = rawProps[key], ov = p[key];
        if (Object.is(nv, ov)) continue;             // diff：只更新变更项
        p[key] = nv;
        if (nv === undefined || nv === null) el.removeAttribute(key);
        else if (primitive(nv)) el.setAttribute(key, String(nv));
        else el[key] = nv;                            // 对象/函数走 property
      }
    });

    return React.createElement(tag, { ref: (el) => { elRef.current = el; ref?.(el); } });
  });
}

// 用法
export const XTagInput = wrap('x-tag-input', { props: ['tags', 'max'], events: ['tag-add'] });
// <XTagInput tags={['a']} onTagAdd={(e) => console.log(e.detail.value)} />
```

**评分点**：
- 基础类型 vs 复杂类型的 attribute/property 分流（React18 痛点核心）。
- 事件绑定/解绑在 useEffect 依赖数组上（handler 变化重绑），卸载清理。
- prev.current diff 避免全量重写属性。
- forwardRef 转发到真实元素（命令式 API 可用）。
