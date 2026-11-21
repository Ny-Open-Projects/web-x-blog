---
title: [FRP-150] 根节点渲染失败后的重试与"panicked lane"恢复机制是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-150：根节点渲染失败后的重试与"panicked lane"恢复机制是什么？

**答**：
- 并发渲染是**可中断**的：如果 render 到一半出了错（或更新的数据不一致），React 会**丢弃半成品 workInProgress 树**，改用**同步 lane 整树重试**——因为同步路径保证一次 render 一定跑完、一定 commit，绝不会出现"永远渲染不完"。
- 这就是源码里的"render 阶段 panic -> 恢复"：`attemptSynchronousRetry`，错误同时上报给 error boundary（recoverable error）。
- 连续失败会升级：重试也失败 -> 走 error boundary；root 级失败 -> 卸载整树（白屏兜底）并打印致命错误。
- 对开发者的含义：并发渲染中的错误可能被重试"吞掉一次"，DevTools 里会看到 recoverable error 但 UI 正常——这是设计行为不是 bug。

```javascript
// 简化实现，帮助理解 panicked lane 的恢复
function renderRoot(lanes) {
  let rootExitStatus;
  try {
    do {
      workLoopConcurrent(lanes);            // 可中断循环
      break;
    } while (true);
    rootExitStatus = 'completed';
  } catch (error) {
    if (isConcurrentLane(lanes)) {
      // 并发 lane 失败：丢弃半成品，同步整树重试
      resetWorkInProgress();                // 丢弃 workInProgress 树
      reportRecoverableError(error);        // 上报可恢复错误（不立即卸载 UI）
      return renderRootSync(SyncLane);      // 同步路径：保证一定完成并 commit
    }
    // 同步 lane 也失败：升级为不可恢复
    rootExitStatus = 'fatal';
    throw error;
  }
  return rootExitStatus;
}

function renderRootSync(lanes) {
  // 同步循环：没有 shouldYield，一口气跑完
  while (workInProgress !== null) {
    performUnitOfWork(workInProgress);
  }
  commitRoot();                             // 一定会走到 commit
}

// —— 重试的调度入口（简化） ——
function ensureRootIsScheduled() {
  const nextLanes = getNextLanes(root);
  if (root.hasPendingRecoverableErrors && nextLanes !== SyncLane) {
    // 存在未消化的可恢复错误：下次渲染强制带同步兜底
    scheduleSyncRetryOnNextRender = true;
  }
  // ... 常规调度 ...
}

// 效果：用户几乎无感
// 1. 过渡渲染中出错 -> UI 保持旧内容（没有提交过任何东西）
// 2. 同步重试成功 -> 新内容正常上屏
// 3. 重试也出错 -> 最近 error boundary 介入
```
