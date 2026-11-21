---
title: [MFW-005] 笔试：手写一个极简 RSC 运行时（序列化组件树为 Payload 并渲染）
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-005：笔试：手写一个极简 RSC 运行时（序列化组件树为 Payload 并渲染）
**题目**：实现 `renderRSC(element, slots)`：服务端把组件树「求值」成 JSON Payload——Server Component 递归展开为普通节点，Client Component 记为 `{ type: 'client', id, props }` 引用；再实现客户端侧 `hydrateRSC(payload, registry)`：根据 registry 里注册的客户端模块重建可渲染树。要求：支持嵌套、props 校验（函数不允许下发）、children 引用。

```javascript
// ===== 服务端：把组件树求值为 RSC Payload =====
function renderRSC(el, ctx = { clientIds: new Map(), payload: [] }) {
  if (typeof el === 'string' || typeof el === 'number') return el;
  if (el == null || typeof el !== 'object') return null;
  const { type, props } = el;
  if (typeof type === 'function') {
    if (type.$$client) {
      // Client Component：不执行，记引用
      if (!ctx.clientIds.has(type)) ctx.clientIds.set(type, ctx.clientIds.size + 1);
      const id = ctx.clientIds.get(type);
      ctx.payload.push(`M${id}:${type.name}`);
      return { $client: id, props: serializeProps(props) };
    }
    // Server Component：继续在服务端执行展开
    return renderRSC(type(props), ctx);
  }
  // 普通 host 元素：递归 children
  const children = Array.isArray(props.children)
    ? props.children.map((c) => renderRSC(c, ctx))
    : renderRSC(props.children, ctx);
  return { type, props: { ...props, children } };
}

function serializeProps(props) {
  for (const v of Object.values(props)) {
    if (typeof v === 'function') {
      throw new Error('函数 props 不能传给 Client Component（Server Action 除外）');
    }
  }
  return JSON.parse(JSON.stringify(props)); // 保证可序列化
}

// ===== 客户端：根据 registry 重建树 =====
function hydrateRSC(node, registry) {
  if (typeof node === 'string' || typeof node === 'number') return node;
  if (!node) return null;
  if (node.$client) {
    const Comp = registry[node.$client]; // 引用 -> 客户端真实组件
    if (!Comp) throw new Error(`missing client module ${node.$client}`);
    const { children, ...rest } = node.props;
    return { ...Comp(rest), ...(children ? { children: hydrateRSC(children, registry) } : {}) };
  }
  return {
    type: node.type,
    props: {
      ...node.props,
      children: Array.isArray(node.props.children)
        ? node.props.children.map((c) => hydrateRSC(c, registry))
        : hydrateRSC(node.props.children, registry),
    },
  };
}

// **评分点**
// 1. Server Component 递归执行、Client Component 只记引用不执行——这是 RSC 的核心分叉。
// 2. 拦截函数 props 并报错，体现 Flight 协议可序列化约束（Server Action 除外可加分）。
// 3. 客户端通过 registry 按模块 id 动态还原，等同 __next_f 的模块引用机制。
// 4. children 树的深浅拷贝/数组分支处理无遗漏，不丢节点。
```
