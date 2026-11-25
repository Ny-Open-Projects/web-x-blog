---
title: [WCN-573] 跨框架「中间表示 IR」：如何设计一种 IR 让同一份模板编译到 Solid / Vapor / Svelte 不同后端？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-573：跨框架「中间表示 IR」：如何设计一种 IR 让同一份模板编译到 Solid / Vapor / Svelte 不同后端？

**答**：
- 结论：IR 采用「语义节点 + 更新意图」两层——语义层描述结构（element/text/if/for），更新意图描述响应式关系（bind/derive）。
- IR 节点平台无关，后端 codegen 各自映射到目标 API（Solid 的模板、Vapor 的 block、Svelte 的 signal）。
- 关键是把「响应式意图」抽象出来，而非绑定某框架的运行时。
- 追问：IR 如何表达各框架特有能力（如 Qwik 的 QRL）？（答：用扩展节点 + 后端能力协商，不支持则降级）

```javascript
const ir = {
  type: 'Fragment', children: [
    { type: 'Element', tag: 'button',
      props: [{ name: 'onClick', value: { type: 'Bind', expr: 'inc', kind: 'event' } }],
      children: [{ type: 'Text', value: { type: 'Derive', expr: 'count + 1' } }] },
  ],
};
function codegen(ir, backend) {
  switch (backend) {
    case 'solid': return solidGen(ir);     // 生成细粒度 DOM 更新
    case 'vapor': return vaporGen(ir);     // 生成 block + patch 指令
    case 'svelte': return svelteGen(ir);   // 生成 signal + effect
  }
}
```
