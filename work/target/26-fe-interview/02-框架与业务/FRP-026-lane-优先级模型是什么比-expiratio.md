---
title: [FRP-026] lane 优先级模型是什么？比 expirationTime 好在哪？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-026：lane 优先级模型是什么？比 expirationTime 好在哪？

**答**：
- lane 用一个 31 位整数的**每个二进制位**表示一种优先级，如 SyncLane=0b0001、InputContinuousLane=0b0010、DefaultLane=0b0100、TransitionLane、IdleLane……
- 优势一：**批量表达**。`lanes` 字段可以同时持有多个优先级（按位或），一次更新中"紧急 + 过渡"两类任务能共存于同一棵树上分别处理。
- 优势二：**批量比较**。`lanes & SyncLane` 一条位运算判断是否含某优先级，比 expirationTime 的数值比较灵活得多。
- 计算过程：`update.lane` 通过 `requestUpdateLane` 按调用上下文决定（事件处理器、startTransition、useEffect 各不相同），更新时取 `nextLanes = getHighestPriorityLanes(fiber.lanes)` 处理最高位优先。

```javascript
// 简化实现，帮助理解 lane 位运算模型
const TotalLanes = 31;
const SyncLane = 1 << 0;            // 0b0000001 同步：离散事件点击输入
const InputContinuousLane = 1 << 1; // 0b0000010 连续：scroll hover
const DefaultLane = 1 << 2;         // 0b0000100 默认
const TransitionLane1 = 1 << 3;     // 0b0001000 过渡：startTransition
const IdleLane = 1 << 30;           // 最低优先级：离屏渲染

// 批量收集：一次更新可能携带多个 lane（NoLanes 即 0，表示无待处理优先级）
let rootLanes = 0;
rootLanes |= DefaultLane;        // 0b100
rootLanes |= TransitionLane1;    // 0b1100 —— 两个优先级共存

// 判断包含：一条位运算
function includesAnyLanes(lanes, subset) {
  return (lanes & subset) !== 0;
}
console.log(includesAnyLanes(rootLanes, TransitionLane1)); // true

// 取最高优先级：找最低位的 1（数值越小优先级越高）
function getHighestPriorityLane(lanes) {
  return lanes & -lanes; // 0b1100 & -0b1100 = 0b100 => DefaultLane
}
console.log(getHighestPriorityLane(rootLanes) === DefaultLane); // true

// 合并与清除
function markRootFinished(rootLanes, finishedLanes) {
  return rootLanes & ~finishedLanes; // 清掉已完成的 lane，剩余的下次继续
}
```
