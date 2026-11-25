---
title: [988] XState 的 Actor 模型与并发状态管理
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, 状态机]
type: 面试题
---

## 988：XState 的 Actor 模型与并发状态管理

**答**：
- Actor 模型：每个 actor（机器实例）独立持有状态与消息队列——多实例并发（多个上传任务各自一台「上传机」实例）互不干扰；父 actor spawn 子 actor，通信靠事件（不共享内存）。
- 与全局 store 的对比：全局 store 是「单一共享状态」（并发任务互相覆盖），actor 是「实例化状态」（每个任务独立生命周期）——批量任务场景（N 个文件上传各自进度/失败重试）actor 模型天然契合。
- 实现：spawn(id => uploadMachine) 每任务一台机器，父机收集子机状态聚合出总进度（subscribe 子机状态聚合到全局 store 展示）。
- 追问钩子：为什么「批量任务」特别适合 actor？——批量任务的状态本质是「实例的集合」——用全局 store 管理需要手工维护「任务 id -> 状态」的 map 与生命周期清理；actor 把实例的生命周期交给机器框架管理（spawn/stop 自动化）。

```ts
const uploadFlow = createMachine({
  context: ({ spawn }) => ({ uploads: [] }),
  on: { ADD_FILE: { actions: assign(({ context, spawn, event }) => ({
    uploads: [...context.uploads,
      { id: event.id, ref: spawn(uploadMachine, { input: event.file }) }],
  })) } },
});
// 每个上传任务一台机器：进度/失败/重试实例化互不干扰
```
