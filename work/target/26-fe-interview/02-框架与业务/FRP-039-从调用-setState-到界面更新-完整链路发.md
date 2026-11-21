---
title: [FRP-039] 从调用 setState 到界面更新，完整链路发生了什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-039：从调用 setState 到界面更新，完整链路发生了什么？

**答**：
- 1）`setState` 创建 update 对象，push 进对应 hook 的 updateQueue，并调用 `scheduleUpdateOnFiber`。
- 2）`markRootUpdated` 把本次 lane 并入 root.pendingLanes，`ensureRootIsScheduled` 根据最高 lane 选择调度器回调（同步/Scheduler 并发）。
- 3）render 阶段：从 root 向下 beginWork，遇到有 update 的 hook 就循环计算新 state，props 变化的子树重新 render，产出带 flags 的 workInProgress 树（可中断）。
- 4）commit 阶段：mutation 同步应用 DOM 变更 → layout 同步跑 useLayoutEffect → paint → passive 异步跑 useEffect。
- 面试可压缩为四步：**排队 update → 调度 lane → 可中断 render → 同步 commit**。

```javascript
// 简化实现，帮助理解完整链路
function setState(fiber, hook, action) {
  // 步骤 1：创建 update 并排队
  const update = { action, lane: requestUpdateLane() }; // 事件内 Sync，transition 内低优
  hook.queue.push(update);

  // 步骤 2：把 lane 合入 root，安排调度
  const root = markRootUpdated(fiber, update.lane);     // pendingLanes |= lane
  ensureRootIsScheduled(root);                          // 选最高 lane 决定同步或并发
}

function ensureRootIsScheduled(root) {
  const nextLanes = getHighestPriorityLanes(root.pendingLanes);
  if (includesSyncLane(nextLanes)) {
    // 同步 lane：微任务内同步 render，一气呵成
    queueMicrotask(() => performSyncWorkOnRoot(root));
  } else {
    // 并发 lane：交给 Scheduler，帧预算内切片（见 FRP-027）
    scheduleCallback(priorityFromLanes(nextLanes), () => performConcurrentWorkOnRoot(root));
  }
}

function performSyncWorkOnRoot(root) {
  // 步骤 3：render 阶段 —— 构建 workInProgress 树
  renderRootSync(root);   // beginWork/completeWork，可被打断（并发路径）
  // 步骤 4：commit 阶段 —— 同步应用
  commitRoot(root);
  root.pendingLanes = markRootFinished(root.pendingLanes, root.finishedLanes);
}
```
