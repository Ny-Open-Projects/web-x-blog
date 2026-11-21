---
title: [FRP-023] Fiber 架构是什么？为什么用链表结构？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-023：Fiber 架构是什么？为什么用链表结构？

**答**：
- React 15 的 Stack Reconciler 递归更新整棵树，**不可中断**——大组件树更新会长时间占住主线程。
- Fiber 把每个组件/元素变成一个 Fiber 节点，用**链表**代替递归树：`child`（第一个子节点）、`sibling`（下一个兄弟）、`return`（父节点）三个指针，遍历可以用**循环 + 指针回退**完成，随时暂停、保存现场、下次继续。
- 每个节点还带 `alternate`（双缓冲指向另一棵树的对应节点）、`lanes`（优先级）、`effectTag/flags`（增删改标记）、`stateNode`（真实 DOM/实例）。
- 链表结构的本质动机：把"递归"改造成"可暂停的迭代"，这是 Concurrent 渲染的数据结构基础。

```javascript
// 简化实现，帮助理解 Fiber 链表遍历（深度优先 + 指针回退）
function fiberToTree(fiber, depth = 0) {
  console.log(' '.repeat(depth * 2) + typeOf(fiber));
  // 先深入 child，没有 child 再找 sibling，都没有就回到 return 的 sibling
  if (fiber.child) fiberToTree(fiber.child, depth + 1);
  if (fiber.sibling) fiberToTree(fiber.sibling, depth);
}
function typeOf(f) { return typeof f.type === 'function' ? f.type.name : f.type; }

// Fiber 节点核心字段（示意）
function createFiber(type, props, key) {
  return {
    type, props, key,
    child: null,      // 第一个子 Fiber
    sibling: null,    // 下一个兄弟 Fiber
    return: null,     // 父 Fiber
    alternate: null,  // 双缓冲：指向另一棵树上对应的 Fiber
    flags: 0,         // Placement 2 / Update 4 / Deletion 8，commit 阶段执行
    lanes: 0,         // 本节点的更新优先级
    stateNode: null,  // Host 组件对应真实 DOM；类组件对应实例
    memoizedState: null, // Hooks 链表头（见 FRP-028）
  };
}

// 用循环模拟 beginWork 的移动过程（react-reconciler 的 workLoop 核心）
function walk(rootFiber) {
  let fiber = rootFiber;
  while (fiber) {
    console.log('beginWork:', typeOf(fiber)); // 处理当前节点
    if (fiber.child) { fiber = fiber.child; continue; }   // 深入
    while (fiber) {
      console.log('completeWork:', typeOf(fiber));        // 回溯
      if (fiber.sibling) { fiber = fiber.sibling; break; } // 换兄弟
      fiber = fiber.return;                               // 回到父级继续回溯
    }
  }
}
```
