---
title: [FRP-025] React 的 render 阶段与 commit 阶段各自做什么？为什么这样划分？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-025：React 的 render 阶段与 commit 阶段各自做什么？为什么这样划分？

**答**：
- **render 阶段**（Reconciler）：从 root 开始 beginWork/completeWork 遍历，执行 render 函数、计算 diff、在 Fiber 上打 flags 标记——**纯计算、无副作用、可中断**。
- **commit 阶段**（Renderer）：把 flags 同步执行到 DOM（beforeMutation/mutation/layout 三个子阶段），依次触发 getSnapshotBeforeUpdate、DOM 操作、useLayoutEffect，最后异步调度 useEffect——**同步不可中断**，避免用户看到中间状态。
- 划分原因：可中断只能发生在"不碰真实 DOM"的阶段；一旦开始改 DOM 就必须一口气完成，否则视觉不一致。
- 生命周期的归属也由此决定：UNSAFE_componentWillReceiveProps 等在可中断的 render 阶段可能被多次执行，因此被标记 UNSAFE（见 useEffect 时机题）。

```mermaid
flowchart TD
  S[setState 或 useSyncExternalStore 触发更新] --> SCHED[Scheduler 选优先级入队]
  SCHED --> R[render 阶段 可中断]
  R --> B1[beginWork 处理单个 Fiber]
  B1 --> Y{shouldYield 让出}
  Y -->|帧时间耗尽| P[保存现场 恢复后继续]
  P --> R
  Y -->|未超时| B2[completeWork 打 flags 标记]
  B2 --> D{还有节点}
  D -->|是| B1
  D -->|否| C[commit 阶段 同步不可中断]
  C --> C1[beforeMutation getSnapshotBeforeUpdate]
  C1 --> C2[mutation 执行 DOM 增删改]
  C2 --> C3[layout 同步执行 useLayoutEffect]
  C3 --> C4[异步调度 useEffect paint 之后执行]
```

```javascript
// 简化实现，帮助理解两阶段划分
function renderRootSync(rootFiber) {
  // ===== render 阶段：纯计算，可中断，不碰 DOM =====
  let fiber = rootFiber;
  while (fiber) {
    beginWork(fiber);    // 执行函数组件 render 或类组件 render，diff 出子 Fiber
    // 真实源码在这里检查 shouldYield()，可暂停恢复（见 FRP-027）
    if (fiber.child) { fiber = fiber.child; continue; }
    while (fiber) {
      completeWork(fiber); // 生成/更新 DOM 描述，向父级冒泡 flags
      if (fiber.sibling) { fiber = fiber.sibling; break; }
      fiber = fiber.return;
    }
  }
  commitRoot(rootFiber);   // render 完成，进入同步 commit
}

function commitRoot(rootFiber) {
  // ===== commit 阶段：同步一口气完成，不可中断 =====
  // 1. beforeMutation：getSnapshotBeforeUpdate（拿到更新前 DOM 快照）
  // 2. mutation：按 flags 执行真实 DOM 操作
  const deletions = [], insertions = [], updates = [];
  collectFlags(rootFiber, { deletions, insertions, updates });
  deletions.forEach((d) => d.stateNode.remove());
  insertions.forEach((i) => i.parent.insertBefore(i.node.stateNode, i.before));
  updates.forEach((u) => Object.assign(u.node.stateNode, u.props));

  // 3. layout：同步执行 useLayoutEffect / componentDidMount
  flushLayoutEffects(rootFiber);

  // 4. passive：useEffect 调度到 paint 之后（宏任务/微任务）
  schedulePassiveEffects(rootFiber);
}
```
