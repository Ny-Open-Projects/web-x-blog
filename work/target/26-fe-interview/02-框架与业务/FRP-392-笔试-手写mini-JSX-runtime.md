---
title: [FRP-392] 笔试：手写 mini JSX runtime
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-392：笔试：手写 mini JSX runtime

**答**：实现 JSX 运行时（jsx-runtime 协议）：① `jsx(type, props, key)`：children 从 props 解出（children 不进 props，独立第三参语义）、扁平化、key 剥离；② Fragment 支持（Symbol 类型）；③ props 的布尔属性语义（true → 属性存在，false/null → 移除）；④ 与 mini vdom 的 mount 对接（FRP-378 的 h 等价物）；⑤ jsxs（静态 children 数组）与 jsx 的差异说明。写出实现。

```javascript
const Fragment = Symbol('Fragment');

function normalize(children) {
  return children.flat(Infinity).filter((c) => c != null && c !== false && c !== true)
    .map((c) => (typeof c === 'object' ? c : { type: 'text', props: { nodeValue: String(c) }, children: [] }));
}

function jsx(type, props, key) {
  const { children, ...rest } = props ?? {};
  return {
    type, key: key ?? null,
    props: Object.fromEntries(Object.entries(rest).filter(([k]) => k !== '__source' && k !== '__self')),
    children: children != null ? normalize(Array.isArray(children) ? children : [children]) : [],
  };
}
const jsxs = jsx;       // 静态 children 版本(编译器优化标记), 语义同 jsx

// Fragment: patch 层按 Symbol 类型「无壳挂载」(children 直接插入父容器)
// 布尔属性: <input disabled={false}> → 不设 attribute (jsx 层过滤)
// 与 mini vdom 对接: jsx 产物 = h() 的 vnode (type/props/children) — mount/patch 直接消费
export { jsx, jsxs, Fragment };
// 编译产物: jsx('div', { className: 'a' }, 'hello') → 同 h('div', {class:'a'}, 'hello')
```

**评分点**：
- children 从 props 解出与扁平化归一（jsx-runtime 协议核心）
- Fragment 的 Symbol 语义与无壳挂载说明
- 布尔/空值属性的过滤语义
- jsxs 与 jsx 的编译器标记差异
