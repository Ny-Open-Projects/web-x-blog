---
title: [FRP-106] 服务器组件（RSC）的序列化协议是怎样的？payload 流里都流过什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-106：服务器组件（RSC）的序列化协议是怎样的？payload 流里都流过什么？

**答**：
- RSC payload 是**流式 JSON**（React Flight 协议）：按行/分块输出，每块形如 `id:JSON`，id 是槽位引用；组件树被序列化为"对象图 + 占位引用"而非 HTML。
- 特殊引用类型：`$L1` / `$F1` 指向**懒加载的 Client 组件模块引用**（客户端拿到后按需拉 JS chunk）；`$Sreact.slot` 表示 **children 槽位**（服务器渲染结果作为 children 塞进客户端组件）；`$Kxx` 是 ScopeKey；`$@id` 是 **Promise 槽位**（Suspense 的后续流）。
- 流式行为：首屏先输出可完成的树 + Suspense fallback 占位（`$L` 引用），后台完成后**追加** `$RC=...`（React 完成标记脚本）把真实内容替换进去——与流式 SSR 的 out-of-order 机制是同一套协议层。
- 理解要点：RSC 传输的**不是 HTML 而是"结构化组件树"**，客户端 React 直接用它恢复树结构并 hydrate；Server Action 的调用也复用同一 Flight 协议（请求方向序列化）。

```javascript
// 简化实现，帮助理解 Flight 式序列化与流格式
// 服务器侧：组件树 -> 带引用的 JSON 块流
function serializeFlight(node, emit, seen = new Map()) {
  // 模拟：Client 组件引用、Promise 槽位、children 槽位
  if (typeof node === 'function' && node.isClientComponent) {
    const id = node.__id;                       // 模块引用只传 id
    emit(id, JSON.stringify({ $$F: 1, chunks: node.__chunks }));
    return `$L${id}`;
  }
  if (node instanceof Promise) {
    const id = Math.random().toString(36).slice(2, 5);
    emit(`@${id}`, '"pending"');                // Promise 槽位，后续流补齐
    node.then((v) => emit(`RC:${id}`, JSON.stringify(v))); // 完成后追加
    return `$@${id}`;
  }
  if (Array.isArray(node)) return node.map((n) => serializeFlight(n, emit, seen));
  if (node && typeof node === 'object') {
    return Object.fromEntries(Object.entries(node).map(([k, v]) => [k, serializeFlight(v, emit, seen)]));
  }
  return node;
}

// 客户端组件标记（构建产物注入）
const ClientButton = Object.assign(function Button() {}, {
  isClientComponent: true, __id: '1', __chunks: ['static/chunks/button.js'],
});

const blocks = [];
const emit = (id, json) => blocks.push(`${id}: ${json}`);
const tree = {
  type: 'ServerPage',
  children: [ClientButton, Promise.resolve({ type: 'ServerList', items: [1, 2] })],
};
const payload = serializeFlight(tree, emit);
console.log('--- payload 首块（树结构，引用占位）---');
console.log(JSON.stringify(payload, null, 1));
console.log('--- 后续流块 ---');
blocks.forEach((b) => console.log(b));
// 输出示例：children: [ "$L1", "$@x2" ] + "1: {$$F:1,chunks:[...]}" + "RC:x2: {...}"
// 客户端：解析引用 -> 按需加载 Client chunk -> $RC 到达后填充 Promise 槽位
```

## 十六、框架工程层
