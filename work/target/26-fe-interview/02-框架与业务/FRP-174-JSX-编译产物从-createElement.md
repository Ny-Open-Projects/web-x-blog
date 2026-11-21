---
title: [FRP-174] JSX 编译产物从 createElement 到 jsx-runtime 经历了什么演进？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-174：JSX 编译产物从 createElement 到 jsx-runtime 经历了什么演进？

**答**：
- 经典转换：JSX → `React.createElement(type, props, ...children)`——props 对象运行时构造、key/children 混在参数里、**React 必须在作用域内**（每个文件 import React）。
- 新 runtime（React 17+ automatic runtime）：`jsx(type, props, key)` ——key 从 props 中拆出单独传、children 直接进 props、**编译器自动注入 import**（`react/jsx-runtime`），源文件不再需要 import React。
- 收益：省掉每次的 `arguments` 展开、props 构造更直接、为"不写 import React"的现代化（RSC/服务端）铺路。
- Vue 也采用同名 jsx-runtime 约定（`vue/jsx-runtime`），工具链统一。

```javascript
// 简化实现，帮助理解两种产物
// —— 输入 JSX ——
// const el = <div className="box" key="k1">hello<span>{name}</span></div>;

// —— 经典产物（React 16 及以前） ——
const el = React.createElement(
  "div",
  { className: "box", key: "k1" },   // key 藏在 props 里，运行时要特殊处理
  "hello",
  React.createElement("span", null, name)
);
// 必须文件顶部 import React —— 即使源码没显式用到

// —— 新 runtime 产物（automatic JSX runtime） ——
import { jsx as _jsx } from "react/jsx-runtime";   // 编译器自动注入
const el = _jsx("div", {
  className: "box",
  children: ["hello", _jsx("span", { children: name })]
}, "k1");                                          // key 独立第三参：运行时无需再拆

// —— 编译器侧的转换差异 ——
function transformJSXClassic(node) {
  const props = { ...node.attributes };
  if (node.key) props.key = node.key;               // key 进 props
  return call('React.createElement', node.type, props, ...node.children);
}
function transformJSXRuntime(node) {
  const props = { ...node.attributes };
  props.children = node.children.length === 1 ? node.children[0] : node.children;
  const { key, rest } = splitKey(props);
  return call(node.children.length ? '_jsx' : '_jsxs', node.type, rest, key);
  // 还有两个细节：jsxDEV 注入 __source/__self（dev 定位）、
  // 静态子树可用 _jsx + 冻结 props 复用
}

// 运行时对 key 的处理简化：
function jsx(type, props, key) {
  return { $$typeof: ELEMENT, type, key: key ?? null, props, ref: props.ref ?? null };
}
```
