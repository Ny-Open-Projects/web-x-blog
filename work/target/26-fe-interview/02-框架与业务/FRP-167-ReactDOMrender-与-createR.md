---
title: [FRP-167] ReactDOM.render 与 createRoot 在并发开关上有什么实质差异？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-167：ReactDOM.render 与 createRoot 在并发开关上有什么实质差异？

**答**：
- `ReactDOM.render`（legacy）：入口不创建并发 root，所有更新走**同步不可中断**路径——sync lane、整树一口气 render + commit，没有切片与插队。
- `createRoot`：入口创建 ConcurrentRoot，更新默认进**并发通道**（可中断、可插队、可被丢弃重试），只有离散事件与 flushSync 强制走同步路径。
- 卸载 API 对应变化：legacy 用 `ReactDOM.unmountComponentAtNode`，concurrent 用 `root.unmount()`——因为 root 对象持有调度状态。
- 中间态 `ReactDOM.createBlockingRoot`（React18 过渡期）已废弃——三入口设计最终收敛为"legacy 渐进淘汰 + concurrent 默认"。

```javascript
// 简化实现，帮助理解两种入口的调度分叉
function createLegacyRoot(container) {
  return {
    tag: 'legacy',
    render(children) {
      legacyRender(children, container);
    },
    unmount() { legacyUnmount(container); }
  };
}

function legacyRender(children, container) {
  // 同步路径：没有 Scheduler，没有切片
  performSyncWorkOnRoot();      // 整树 render -> commit 一气呵成
  // 期间任何 update 都排队到这次同步工作里（expirationTime 旧模型）
}

function createRoot(container) {
  const root = { tag: 'concurrent', pendingLanes: 0 };
  return {
    render(children) {
      root.children = children;
      scheduleUpdateOnRoot(root, DefaultLane);  // 默认进并发通道
    },
    unmount() {
      // 先排一个同步卸载任务，再清理调度状态
      scheduleCallback(NormalPriority, () => commitUnmount(root));
    }
  };
}

// 调度分叉的核心判断
function ensureRootIsScheduled(root) {
  if (root.tag === 'legacy') {
    // legacy：永远同步（SyncLane），不存在并发渲染
    scheduleMicrotask(() => performSyncWorkOnRoot(root));
    return;
  }
  const lanes = getNextLanes(root);
  if (includesSyncLane(lanes)) {
    scheduleMicrotask(() => performSyncWorkOnRoot(root));   // 离散事件：同步
  } else {
    scheduleCallback(priorityOf(lanes), () => performConcurrentWorkOnRoot(root)); // 切片
  }
}

// 升级影响（为什么必须换 createRoot）：
// ReactDOM.render 下即使代码里写了 startTransition，更新也不会并发——入口决定通道
```
