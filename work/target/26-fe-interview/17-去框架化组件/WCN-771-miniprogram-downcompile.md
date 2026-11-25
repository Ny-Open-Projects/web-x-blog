---
title: [WCN-771] 编译响应式框架如何做跨端（小程序）的模板降级编译？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-771：编译响应式框架如何做跨端（小程序）的模板降级编译？

**答**：
- 结论：小程序没有 DOM 与动态 JS 执行，编译器把模板转成 WXML/WXSS，把响应式数据绑定转成 `setData` 调用；动态表达式受限，需在编译期转成数据路径或计算属性。
- 事件、指令、组件模型都要按小程序语法重写（如 `bindtap`、条件 `wx:if`）；复杂的渲染函数无法直接移植，需降级为静态模板 + 数据驱动。
- 追问钩子：模板里用了 `new Date()` 这类任意 JS 表达式怎么处理？考察「编译期提升到计算字段 or 拒绝并告警」

```javascript
// Web 模板 -> 小程序降级
const tmpl = '<view wx:if="{{visible}}">{{message}}</view>';
function genMiniProgram(node) {
  if (node.type === 'If') return `<view wx:if="{{${node.cond}}}">${node.children.map(genMiniProgram).join('')}</view>`;
  if (node.type === 'Interp') return `{{${node.expr}}}`;
  return node.children?.map(genMiniProgram).join('') || '';
}
const ast = { type: 'If', cond: 'visible', children: [{ type: 'Interp', expr: 'message' }] };
console.log(genMiniProgram(ast));
console.log('数据更新走 setData:', 'this.setData({ message: ... })');
```
