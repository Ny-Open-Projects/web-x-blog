---
title: [R19-416] 笔试：手写简易 Fiber 渲染器（可中断 workLoop）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, Fiber]
type: 笔试题
---

## R19-416：笔试：手写简易 Fiber 渲染器

**答**：实现极简 Fiber 渲染器：① createElement(tag, props, ...children) 生成 vnode；② render(el, container)：构建 fiber 树（child/sibling/return 链表）；③ workLoop 用 requestIdleCallback/time 分片——每个 fiber 一个工作单元，deadline 耗尽让出；④ performUnitOfWork：函数组件调用得到 children，DOM 元素创建节点；⑤ commitRoot 在渲染完成后一次性提交。写出核心实现（60 行内）。

```javascript
function createElement(type, props, ...children) {
  return { type, props: { ...props, children: children.map(c =>
    typeof c === 'object' ? c : { type: 'TEXT', props: { nodeValue: c } }) } };
}

let nextFiber = null, wipRoot = null, currentRoot = null, deadline = 0;

function render(el, container) {
  wipRoot = { type: 'ROOT', props: { children: [el] }, dom: container, alternate: currentRoot };
  nextFiber = wipRoot;
  requestIdleCallback(workLoop);
}

function workLoop(deadlineArg) {
  deadline = deadlineArg;
  while (nextFiber && deadline.timeRemaining() > 1) performUnitOfWork(nextFiber);
  if (!nextFiber && wipRoot) { commitRoot(); return; }
  requestIdleCallback(workLoop);                    // 让出后继续
}

function performUnitOfWork(fiber) {
  if (typeof fiber.type === 'function') {
    const children = [fiber.type(fiber.props)];     // 函数组件: 调用取 children
    reconcile(fiber, children);
  } else if (!fiber.dom) {
    fiber.dom = fiber.type === 'TEXT'
      ? document.createTextNode(fiber.props.nodeValue)
      : document.createElement(fiber.type);
  }
  const kids = fiber.props.children;
  let prevSibling;
  kids.forEach((child, i) => {
    const f = { type: child.type, props: child.props, parent: fiber, alternate: null };
    if (i === 0) fiber.child = f; else prevSibling.sibling = f;
    prevSibling = f;
  });
  nextFiber = fiber.child ?? fiber.sibling ?? findSibling(fiber);  // 深度优先游标
}
function findSibling(fiber) {
  while (fiber.return && !fiber.return.sibling) fiber = fiber.return;
  return fiber.return?.sibling;
}
function commitRoot() { commit(wipRoot.child); currentRoot = wipRoot; wipRoot = null; }
function commit(fiber) {
  if (!fiber) return;
  fiber.parent.dom?.appendChild(fiber.dom);
  commit(fiber.child); commit(fiber.sibling);
}
```

**评分点**：
- 链表化 fiber 树（child/sibling/return）与深度优先游标恢复
- 时间片让出（timeRemaining > 1）与游标续跑
- 函数组件与 DOM 组件的双分支
- commit 在渲染完成后一次性执行（原子提交）
