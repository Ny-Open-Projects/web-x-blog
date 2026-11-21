---
title: [FRP-098] Jotai / Recoil 的原子化（atom）思想是什么？派生状态如何形成依赖图？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-098：Jotai / Recoil 的原子化（atom）思想是什么？派生状态如何形成依赖图？

**答**：
- 核心思想：**状态最小单元是 atom**（原子），组件订阅的是"一组 atom 值"而非整棵 store 树；派生状态（derived atom）由 `get()` 读取其他 atom 自动建立**依赖图**，依赖的 atom 变化才重算、才通知订阅者。
- 与 Redux/Zustand 的结构差异：全局单一 store 树 vs **多粒度独立节点**；后者天然规避 Context 式"一个变全量通知"，也避免了 selector 手写记忆化。
- 派生是惰性的：依赖图上的派生 atom 只在**被读取时**才重算（pull 模型，Recoil 用 selector get/set，Jotai 用 read/write），并且可以按需缓存。
- 订阅实现：`useAtom` 内部是 useSyncExternalStore——atom 有自己的 subscribers；写 atom 时沿依赖图**反向通知**（依赖了它的派生 atom 与组件）。

```javascript
// 简化实现，帮助理解 atom 依赖图与反向通知
function atom(read, write) {
  const a = { subscribers: new Set(), value: undefined, deps: new Set(), read, write };
  if (typeof read !== 'function') a.init = read; // 原始 atom：直接初值
  return a;
}
let activeGetter = null; // 收集派生 atom 的依赖

function readAtom(a) {
  if (!a.read) return a.value;                 // 原始 atom
  const get = (dep) => {
    activeGetter?.deps.add(dep);               // 建立 a -> dep 边
    return readAtom(dep);
  };
  const prev = activeGetter;
  activeGetter = a;
  a.value = a.read(get);                       // 执行派生函数
  activeGetter = prev;
  return a.value;
}

function writeAtom(a, value) {
  if (a.write) return a.write(value);          // 派生 atom 可写
  a.value = value;
  a.subscribers.forEach((s) => s());           // 通知直接订阅者
  // 反向通知：依赖图中所有依赖 a 的派生 atom
  [...a.subscribers].forEach((s) => s());
}

function useAtomValue(a) {
  readAtom(a);                                 // 读时建立依赖图
  a.subscribers.add(currentComponent);         // 订阅
  return a.value;
}
let currentComponent = null;

// 用法：count -> doubled -> label 三层依赖图
const countAtom = atom(0);
const doubledAtom = atom((get) => get(countAtom) * 2);
const labelAtom = atom((get) => `count is ${get(doubledAtom)}`);

currentComponent = 'LabelView';
console.log(useAtomValue(labelAtom)); // count is 0，依赖图：label -> doubled -> count
currentComponent = null;

let renders = 0;
labelAtom.subscribers.add(() => { renders++; console.log('LabelView re-render'); });
writeAtom(countAtom, 5);
readAtom(labelAtom); // count is 5：依赖链自动重算
console.log('通知次数:', renders); // 1：只有依赖链上的订阅者被通知
```
