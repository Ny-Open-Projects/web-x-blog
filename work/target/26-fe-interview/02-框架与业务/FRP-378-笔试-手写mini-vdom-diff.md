---
title: [FRP-378] 笔试：手写 mini vdom（h + diff + patch）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-378：笔试：手写 mini vdom

**答**：实现 mini vdom：① `h(type, props, ...children)`（扁平化 children、props 与 children 冲突处理——children 不进 props）；② mount：创建 DOM/挂 props（class 与 style 特殊处理、事件 onX 绑定）；③ patch（diff）：文本/props/children 三段——children 用「无 key 快速路径 + 有 key 的 map 复用」；④ 事件更新的处理（旧 handler 解绑新绑）；⑤ 卸载清理（事件/子树递归）。写出核心实现。

```javascript
export function h(type, props = {}, ...children) {
  return { type, props, children: children.flat(Infinity).filter((c) => c != null && c !== false) };
}

function setProp(el, k, nv, ov) {
  if (k.startsWith('on')) {
    const ev = k.slice(2).toLowerCase();
    ov && el.removeEventListener(ev, ov);
    nv && el.addEventListener(ev, nv);              // 事件: 解旧绑新
  } else if (k === 'class') el.className = nv ?? '';
  else if (k === 'style') el.style.cssText = typeof nv === 'string' ? nv : Object.entries(nv ?? {}).map(([p, v]) => `${p}:${v}`).join(';');
  else if (nv != null) el.setAttribute(k, nv);
  else el.removeAttribute(k);
}

export function mount(vnode, container) {
  const el = (vnode.el = vnode.type === 'text'
    ? document.createTextNode(vnode.props.nodeValue)
    : document.createElement(vnode.type));
  for (const [k, v] of Object.entries(vnode.props)) setProp(el, k, v, null);
  vnode.children.forEach((c) => mount(typeof c === 'object' ? c : h('text', { nodeValue: c }), el));
  container.appendChild(el);
}

export function patch(n1, n2) {
  if (n1.type !== n2.type) { const parent = n1.el.parentElement; unmount(n1); mount(n2, parent); return; }
  const el = (n2.el = n1.el);
  for (const k of Object.keys(n2.props)) setProp(el, k, n2.props[k], n1.props[k]);
  for (const k of Object.keys(n1.props)) if (!(k in n2.props)) setProp(el, k, null, n1.props[k]);
  // children: key 对齐复用
  const oc = n1.children, nc = n2.children;
  const keyed = new Map(oc.map((c, i) => [c.props?.key ?? `#${i}`, { c, i }]));
  nc.forEach((c, i) => {
    const old = keyed.get(c.props?.key ?? `#${i}`);
    if (old && typeof c === 'object') { patch(old.c, c); keyed.delete(c.props?.key ?? `#${i}`); }
    else if (typeof c === 'object') mount(c, el);
    else el.childNodes[i] ? (el.childNodes[i].nodeValue = c) : el.appendChild(document.createTextNode(c));
  });
  for (const { c } of keyed.values()) unmount(c);   // 剩余卸载
}
function unmount(v) { v.el.parentElement?.removeChild(v.el); }
```

**评分点**：
- h 的 children 扁平化与 props/children 分离
- 事件属性的解旧绑新（引用变化才重绑更优——答出加分）
- props 的 class/style/onX 特殊处理
- children 的 key map 复用 + 剩余卸载
