---
title: [WCN-669] 同一套模板要编译到 React/Vue/Web Components 多个目标，如何设计中间表示（IR）？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-669：同一套模板要编译到 React/Vue/Web Components 多个目标，如何设计中间表示（IR）？

**答**：
- 结论：采用两层 IR——高层 HIR（保留语义：组件/指令/slot）→ 低层 LIR（平台无关的节点操作）→ 各目标后端生成具体代码。
- 好处：前端只解析一次，后端按平台能力映射（如 slot→React children / Vue <slot> / WC <slot>）。
- 追问钩子：平台能力不一致怎么办？IR 标记「必需能力」，后端声明「支持矩阵」，编译期校验并给出降级策略——考察工程化严谨性。

```javascript
// 统一 HIR
const hir = {
  type: 'component', name: 'Card',
  children: [{ type: 'slot', name: 'default', fallback: '加载中' }],
};
// 各后端生成
const backends = {
  react: (n) => `<Card>{children?.default ?? '加载中'}</Card>`,
  vue:   (n) => `<Card><slot>加载中</slot></Card>`,
  wc:    (n) => `<ds-card><slot>加载中</slot></ds-card>`,
};
console.log(backends.react(hir));
console.log(backends.wc(hir));
// HIR 隔离了语法差异，新增目标只需加一个后端
```
