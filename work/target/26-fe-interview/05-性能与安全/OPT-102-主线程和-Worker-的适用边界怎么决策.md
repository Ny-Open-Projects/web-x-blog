---
title: [OPT-102] 主线程和 Worker 的适用边界怎么决策？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-102：主线程和 Worker 的适用边界怎么决策？

**答**：
- 核心判断两维：**任务耗时**（预估 >16ms 值得离开主线程）与**是否碰 DOM/同步 API**（碰了就只能主线程）。
- 决策树：能删/能减（不需要算）> 能异步 IO（fetch/流式，不用 Worker）> 纯计算且贵（Worker）> 纯计算但便宜（直接算，别为 2ms 开 Worker）。
- Worker 的隐性成本要计入：启动 40-100ms（要复用/预热）、消息克隆成本、代码要单独打包。**短平快任务留在主线程反而更快**。
- 常见误判：把 5ms 的小计算扔进 Worker，启动+克隆成本 100ms，纯负优化；把 DOM 操作试图搬进 Worker，架构失败。

```javascript
// 一一对应：边界决策函数 + 各路径的典型实现
function routeTask(task) {
  const estimate = task.estimateMs;
  if (task.needsDOM || task.needsSyncAPI) {
    return { path: 'main-thread', note: '碰 DOM/同步 API，必须主线程，用切片防长任务' };
  }
  if (estimate <= 5) {
    return { path: 'main-thread-sync', note: '太短，Worker 启动+克隆成本反超收益，直接算' };
  }
  if (estimate <= 16) {
    return { path: 'main-thread-idle', note: 'requestIdleCallback 空闲期消化' };
  }
  if (estimate <= 200 && task.frequency === 'rare') {
    return { path: 'worker-single', note: '复用长驻 Worker，避免每次新建' };
  }
  return { path: 'worker-pool', note: '重型/高频计算，池化并行' };
}

// 各路径实现要点示例：
// main-thread-idle：空闲期跑小任务
requestIdleCallback(() => computeSmall(), { timeout: 500 });

// worker-single：模块级单例长驻预热，掩盖启动成本
const worker = new Worker('compute.worker.js', { type: 'module' }); // 打包器自动分 chunk
// Vite: new Worker(new URL('./compute.worker.js', import.meta.url), { type: 'module' })

// worker-pool：见 OPT-099
// const pool = new WorkerPool('compute.worker.js');

// 主线程兜底：即使必须主线程，也要切片（见 OPT-057）而不是一口气算
// await processInChunks(bigList, step, { budget: 40 });

// 决策口诀：
// 先问能不能不算（需求/数据减量），再问能不能不现在算（idle/懒加载），
// 最后才问要不要搬到 Worker——顺序反了就是过度设计
```

## 十七、媒体与视觉优化

## 追问（补充）

**追问**：

1. Worker 反而更慢的情况？ → 数据量小、计算量低于序列化开销时，结构化克隆和线程启动成本会吃掉全部收益。
2. 什么不能放 Worker？ → 依赖 DOM/BOM、需要同步返回结果给渲染、以及访问主线程闭包状态的逻辑，拆出去只会更复杂。
3. 怎么快速决策？ → 单次任务超过 50ms 且无 DOM 依赖就上 Worker，否则用时间切片加让出主线程，先测量再决定，别凭直觉拆分，先看耗时分布与序列化成本。
