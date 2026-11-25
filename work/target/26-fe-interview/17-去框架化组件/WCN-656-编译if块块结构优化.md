---
title: [WCN-656] 编译器如何处理 v-if / v-for 的「块（Block）」结构以稳定更新顺序？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-656：编译器如何处理 v-if / v-for 的「块（Block）」结构以稳定更新顺序？

**答**：
- 结论：把 v-if/v-for 的边界作为 Block，动态节点数组按稳定顺序收集；同一 Block 内节点顺序固定，diff 只遍历动态节点数组。
- 机制：遇到结构性指令开新 Block；动态子节点 push 到 currentBlock；更新时按数组顺序 patch；v-for 用 keyed diff 处理移动。
- 追问钩子：Block 嵌套如何管理？用栈（openBlock/closeBlock）——考察对编译器「栈式上下文」的掌握。

```javascript
const blockStack = [];
let currentBlock = null;
function openBlock() { blockStack.push(currentBlock = []); }
function closeBlock() { currentBlock = blockStack.pop(); return currentBlock; }
function createVNode(tag, dynamic) {
  if (dynamic && currentBlock) currentBlock.push(tag);
  return { tag };
}
// 编译 <div><span v-if="ok">{{a}}</span><b>{{b}}</b></div>
openBlock();
createVNode('span', true);
createVNode('b', true);
const dynamics = closeBlock(); // ['span','b'] 稳定顺序
// 更新时只 patch dynamics 数组，静态结构不动
console.log(dynamics);
```
