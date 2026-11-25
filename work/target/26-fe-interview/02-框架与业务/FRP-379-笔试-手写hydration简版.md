---
title: [FRP-379] 笔试：手写 hydration 简版
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, SSR]
type: 笔试题
---

## FRP-379：笔试：手写 hydration

**答**：在 mini vdom 上实现 hydration：① hydrate(vnode, dom)：不重建 DOM——「认领」现有节点（vnode.el = dom），校验 type 匹配；② props 只绑定事件（服务端 HTML 已有静态属性——class/style 不重复设置，事件必须补绑）；③ children 按序对齐（DOM childNodes 与 vnode children 一一对应，文本节点合并防御——浏览器可能合并空白文本）；④ mismatch 处理：type 不符 → 该子树客户端重建（丢弃服务端 DOM）；⑤ 与 mount 的统一（render 入口按「容器有无子节点」分派）。写出实现。

```javascript
export function hydrate(vnode, dom) {
  // type 校验
  if (vnode.type === 'text') { vnode.el = dom; return; }
  if (!dom || dom.tagName?.toLowerCase() !== vnode.type) {
    // mismatch: 重建该子树
    const rebuilt = document.createElement(vnode.type);
    dom?.replaceWith(rebuilt);
    mount(vnode, rebuilt.parentElement);
    return;
  }
  const el = (vnode.el = dom);
  // props: 只补事件(静态属性已在 HTML)
  for (const [k, v] of Object.entries(vnode.props)) {
    if (k.startsWith('on')) setProp(el, k, v, null);   // 事件必须补绑
    // class/style/attr: 跳过(SSR 已渲染) — 若需要校验可对比 dom.getAttribute
  }
  // children 按序对齐
  const domChildren = [...dom.childNodes].filter((n) => !(n.nodeType === 3 && !n.nodeValue.trim())); // 过滤空白
  vnode.children.forEach((c, i) => {
    const child = typeof c === 'object' ? c : h('text', { nodeValue: c });
    hydrate(child, domChildren[i]);
  });
}
// render 统一入口
export function renderApp(vnode, container) {
  container.childNodes.length ? hydrate(vnode, container.firstElementChild) : mount(vnode, container);
}
```

**评分点**：
- 「认领节点」语义（vnode.el 指向现有 DOM，不重建）
- 事件必须补绑 vs 静态属性跳过的区分
- 文本节点合并/空白过滤的浏览器行为防御
- mismatch 重建与 mount/hydrate 统一入口
