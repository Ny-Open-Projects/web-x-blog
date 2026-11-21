---
title: [FRP-092] React 的事件优先级与内部 lane 调度优先级是如何映射的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-092：React 的事件优先级与内部 lane 调度优先级是如何映射的？

**答**：
- 三层优先级概念：**事件优先级**（DiscreteEvent=离散点击/keydown、ContinuousEvent=连续 mousemove/input、DefaultEvent、IdleEvent）→ **lane 优先级**（SyncLane、InputContinuousLane、DefaultLane、TransitionLane、IdleLane，按位掩码）→ **Scheduler 优先级**（ImmediatePriority → IdlePriority，决定调度回调的到期时间）。
- 映射发生点：React 事件系统给原生事件绑定时用 `getEventPriority(domEventName)` 得到事件优先级，处理器里 setState 继承该优先级 → 转换为对应 lane → `lanesToEventPriority` 再转 Scheduler 优先级（SyncLane → ImmediateSchedulerPriority=99）。
- 结果：点击按钮的更新以 SyncLane 走**同步渲染**；input 持续输入用 InputContinuousLane（有 250ms 前后缓冲，防抖动）；TransitionLane 可被上述所有高优先级打断重放。
- 手写演示要点：一个 `dispatchSetState(fiber, lane, action)` 里 lane 从事件类型推导，`ensureRootIsScheduled` 按 lane 排序选最高者调度。

```javascript
// 简化实现，帮助理解三层优先级映射
const EventPriority = { Discrete: 'discrete', Continuous: 'continuous', Default: 'default', Idle: 'idle' };
const Lane = { Sync: 1, InputContinuous: 2, Default: 4, Transition: 8, Idle: 16 };
const SchedulerPriority = { Immediate: 99, UserBlocking: 98, Normal: 97, Idle: 95 };
const timeoutFor = { 99: -1, 98: 250, 97: 5000, 95: 1073741823 }; // 调度到期时间

// 第一层映射：DOM 事件名 -> 事件优先级
function getEventPriority(domEventName) {
  if (['click', 'keydown', 'focus', 'change'].includes(domEventName)) return EventPriority.Discrete;
  if (['mousemove', 'input', 'scroll', 'touchmove'].includes(domEventName)) return EventPriority.Continuous;
  return EventPriority.Default;
}
// 第二层：事件优先级 -> lane
function eventToLane(priority) {
  return { discrete: Lane.Sync, continuous: Lane.InputContinuous, default: Lane.Default, idle: Lane.Idle }[priority];
}
// 第三层：lane -> Scheduler 优先级（决定 setTimeout 到期时间）
function laneToScheduler(lane) {
  return lane === Lane.Sync ? SchedulerPriority.Immediate
       : lane === Lane.InputContinuous ? SchedulerPriority.UserBlocking
       : lane === Lane.Transition ? SchedulerPriority.Normal : SchedulerPriority.Idle;
}

function dispatchEvent(e, handler) {
  const eventPriority = getEventPriority(e.type);
  const lane = eventToLane(eventPriority);
  const schedulerPriority = laneToScheduler(lane);
  console.log(`${e.type}: ${eventPriority} -> lane ${lane} -> scheduler ${schedulerPriority} (timeout ${timeoutFor[schedulerPriority]}ms)`);
  handler(lane); // 更新继承 lane，调度器据此决定渲染时机
}

dispatchEvent({ type: 'click' }, () => console.log('  -> 同步渲染更新'));
dispatchEvent({ type: 'input' }, () => console.log('  -> 250ms 缓冲的连续更新'));
dispatchEvent({ type: 'load' }, () => console.log('  -> 默认优先级更新'));
// click: discrete -> lane 1 -> scheduler 99 立即执行
// input: continuous -> lane 2 -> scheduler 98 有 250ms 缓冲
```
