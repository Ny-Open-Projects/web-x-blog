---
title: [V3-216] Vapor 模式的编译产物长什么样？与 VDOM 产物对比差在哪？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-216：Vapor 模式的编译产物长什么样？与 VDOM 产物对比差在哪？
**答**：
- VDOM 产物：setup 返回渲染函数，运行时反复执行生成 vnode 树，再 diff + patch 更新真实 DOM。
- Vapor 产物：编译期直接生成**一次性 DOM 创建代码** + 更新时只执行靶向 DOM 操作的回调，全程不构建 vnode。
- 更新路径：`template` 编译为 `createNodes` 直接 `appendChild`；动态点编译为 `_setText(n3, () => text.value)` 这类 effect 包装的定向更新。
- 体积：无 vnode/diff 运行时，同组件产物体积更小、内存（无 vnode 树驻留）更省。
- 追问钩子：v-if/v-for 在 Vapor 里怎么处理？——编译为 `if`/`for` 原生控制流 + `createIf/createFor` 的块（Block）结构，动态块只含动态节点。

```javascript
// 源模板：<button @click="n++">{{ n }}</button>
// VDOM 产物（简化）
function render(_ctx) {
  return (openBlock(), createBlock("button", { onClick: _ctx.n++ }, toDisplayString(_ctx.n), 9 /* TEXT, PROPS */));
}
// Vapor 产物（简化示意）
import { template, setText, delegateEvents } from 'vue/vapor';
const t0 = template('<button></button>');
function setup() {
  const n = ref(0);
  const n0 = t0(); // 克隆模板节点，无 vnode
  setText(n0, () => n.value);          // 靶向更新：只写 textContent
  delegateEvents(n0, 'click', () => n.value++);
  return n0;
}
```
