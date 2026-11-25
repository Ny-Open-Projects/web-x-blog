---
title: [FRP-149] lane 模型下多个更新的优先级是如何合并与收敛的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-149：lane 模型下多个更新的优先级是如何合并与收敛的？

**答**：
- 每个更新携带 lane（位图），入队时按位**或**进 `root.pendingLanes`；调度器每次取 pendingLanes 中**最高优先级**（数值最小的位）对应的 lane 批量渲染。
- 同一优先级的多个 setState（同一次事件里）合并进同一个 lane，**一次 render** 全部处理完——这就是"批量"的来源。
- 低优渲染进行中来了高优更新：当前 render 被丢弃，先渲染高优 lane；低优 lane 仍在 pendingLanes 里，之后**补渲染**——保证每个更新最终被处理。
- 渲染完成后 commit 该 lane 的更新并从 pendingLanes 清除该位；`nextLanes` 计算还会参考"已过期"（expiration 已到）的 lane 强制提升，避免饥饿。

```javascript
// 简化实现，帮助理解 lane 合并与补渲染
const TotalLanes = 31;
// lane 位：数值越小优先级越高（1 = Sync/离散输入，16 = Transition）
const SyncLane = 1, InputLane = 2, TransitionLane = 16;

const root = {
  pendingLanes: 0,                          // 所有未完成更新的 lane 并集
  callbackNode: null,
};

function scheduleUpdateOnLane(lane) {
  root.pendingLanes |= lane;               // 合并：多个更新按位或
  ensureRootIsScheduled();
}

function getNextLanes() {
  // 取最高优先级：最低有效位
  const lanes = root.pendingLanes;
  if (lanes === 0) return 0;
  return lanes & -lanes;                    // 位运算技巧：取出最低位的 1
}

function ensureRootIsScheduled() {
  const nextLanes = getNextLanes();
  const isSync = nextLanes === SyncLane || nextLanes === InputLane;
  // 同步 lane 走微任务/同步 flush，并发 lane 走 Scheduler 宏任务切片
  scheduleRender(nextLanes, isSync ? 'microtask' : 'scheduler-callback');
}

function performWorkOnRoot(nextLanes) {
  // render 可中断；期间来了更高优 -> 抛弃当前渲染
  const result = renderRootConcurrent(nextLanes);
  if (result === 'interrupted-by-higher-priority') {
    ensureRootIsScheduled();                // 立刻按新优先级重排
    return;                                 // 当前 lane 的更新仍在 pendingLanes，不会丢
  }
  commitRoot();
  root.pendingLanes &= ~nextLanes;          // 清掉已完成的 lane
  if (root.pendingLanes !== 0) ensureRootIsScheduled(); // 剩余 lane 补渲染
}

// 演示收敛过程
scheduleUpdateOnLane(TransitionLane); // 低优：过渡更新开始渲染
scheduleUpdateOnLane(TransitionLane); // 同 lane 合并，仍一次 render
// 此时用户点击 -> scheduleUpdateOnLane(SyncLane)
// pendingLanes = 10001 | 00001 = 10001... SyncLane 优先 -> 打断过渡 render
// commit 同步更新后：pendingLanes &= ~SyncLane -> 剩 TransitionLane -> 继续补渲染
```
