---
title: [WCN-770] 编译平台如何做多目标输出（Web/SSR/小程序）并统一抽象？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-770：编译平台如何做多目标输出（Web/SSR/小程序）并统一抽象？

**答**：
- 结论：引入中间表示 IR（platform-agnostic 的节点/指令树），前端把模板编译到 IR，多个后端各自把 IR 生成目标代码（Web 渲染函数、SSR 字符串拼接、小程序模板/WXML）。
- IR 层统一表达结构、绑定、指令；后端只关心「如何输出」；通过能力声明处理平台差异（小程序无 DOM，事件/生命周期需映射）。
- 追问钩子：某些 Web 特性在小程序无法表达怎么办？考察「降级策略 + 编译告警 + 平台能力检测」。

```javascript
// IR（与平台无关）
const ir = { type: 'Element', tag: 'view',
  children: [{ type: 'Interpolation', expr: 'title' }] };
// 后端1：Web
function webBackend(node) {
  if (node.type === 'Element') return `h('div', null, ${node.children.map(webBackend).join(',')})`;
  if (node.type === 'Interpolation') return `ctx.${node.expr}`;
}
// 后端2：小程序（WXML）
function mpBackend(node) {
  if (node.type === 'Element') return `<view>${node.children.map(mpBackend).join('')}</view>`;
  if (node.type === 'Interpolation') return `{{${node.expr}}}`;
}
console.log(webBackend(ir));
console.log(mpBackend(ir));
```
