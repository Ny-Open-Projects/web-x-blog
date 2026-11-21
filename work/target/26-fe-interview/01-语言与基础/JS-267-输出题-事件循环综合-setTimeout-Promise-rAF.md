---
title: [JS-267] 输出题：事件循环综合（setTimeout/Promise/rAF）
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 事件循环]
type: 笔试题
---

## JS-267：输出题：事件循环综合

**题目**：写出下列代码的完整输出顺序，并解释每一层的调度原因。

**答**：
```javascript
console.log('A');
setTimeout(() => console.log('B'), 0);
Promise.resolve()
  .then(() => { console.log('C'); setTimeout(() => console.log('D'), 0); })
  .then(() => console.log('E'));
requestAnimationFrame(() => console.log('F'));
queueMicrotask(() => console.log('G'));
console.log('H');
```
```
输出：A H G C E F B D
解释：
1. 同步：A、H
2. 微任务清空（含嵌套）：G → C（注册 D 的 setTimeout）→ E（C 之后注册的 then 入队）
3. 渲染阶段：F（rAF 在渲染前执行，优先于宏任务）
4. 宏任务队列 FIFO：B（先注册）→ D
关键：then 链的第二段要等第一段执行完才入队；rAF 属于渲染步骤，在同一轮循环里先于 setTimeout。
```

**评分点**：
- 完整顺序正确（微任务嵌套与 then 链的入队时序是难点）
- rAF 处于渲染步骤、优先于宏任务的理解
- setTimeout 注册顺序决定宏任务先后
- 能画「同步→微任务→渲染→宏任务」的轮次图（加分）
