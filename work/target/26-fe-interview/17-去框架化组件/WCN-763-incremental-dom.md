---
title: [WCN-763] 编译响应式与增量 DOM（incremental DOM）结合有什么取舍？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-763：编译响应式与增量 DOM（incremental DOM）结合有什么取舍？

**答**：
- 结论：增量 DOM 不创建虚拟树，直接在真实 DOM 上 open/element/text/close 做 diff，内存占用低；编译响应式可把模板编译成这些指令序列，省去 VDOM 分配。
- 取舍：增量 DOM 省内存但指令式代码可读性差、跨平台（SSR/原生）抽象弱；VDOM 更灵活但每次渲染有分配成本。
- 追问钩子：增量 DOM 如何支持 keyed 列表复用？考察「按 key 匹配 + move 指令」的实现复杂度。

```javascript
// 增量 DOM 渲染指令（编译产物风格）
function render(data) {
  elementOpen('ul');
  for (const item of data) {
    elementOpen('li', item.id);       // key = item.id
    text(item.name);
    elementClose('li');
  }
  elementClose('ul');
}
// 运行时根据 current pointer 与 key 决定 patch/move
let pointer = 0;
const dom = [];
function elementOpen(tag, key) { console.log('open', tag, key); }
function elementClose(tag) { console.log('close', tag); }
function text(v) { console.log('text', v); }
render([{ id: 1, name: 'A' }]);
```
