---
title: [DP-154] 为什么说 React 并发调度是"优先级队列 + 状态机"？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-154：为什么说 React 并发调度是"优先级队列 + 状态机"？（高频）
**答**：
- 优先级队列：更新任务带 Lane 优先级（离散层），调度器每次取最高优先级任务；不同优先级可插队（用户输入 > 过渡更新），过期任务用 deadline 检查防止饿死。
- 状态机：Fiber 节点的 render 阶段在 `workLoop` 中可中断（shouldYield），中断/恢复/完成的状态转移由调度器管理——"可中断渲染"本质是状态机。
- 简化复刻：用 MessageChannel 模拟宏任务分片 + 小顶堆按优先级出队，面试可手写 30 行版（DP-096 tapable 对比：tapable 是同步发布订阅链，这里是异步调度）。

```javascript
// 极简并发调度器：优先级队列 + 时间切片 + 可中断状态机
class Scheduler {
  #queue = []; #running = false;
  #compare = (a, b) => a.priority - b.priority;               // 数字越小优先级越高
  schedule(task, priority = 3) {
    this.#queue.push({ task, priority, ts: Date.now() });
    this.#queue.sort(this.#compare);                          // 小顶堆的简化版：排序数组
    this.#flush();
  }
  #flush() {
    if (this.#running) return;
    this.#running = true;                                     // 状态机：running 态
    const channel = new MessageChannel();                     // 宏任务切片（浏览器版 requestIdleCallback）
    channel.port1.onmessage = () => this.#work(channel);
    channel.port2.postMessage(null);
  }
  #work(channel) {
    const deadline = performance.now() + 5;                   // 5ms 切片，时间到让出主线程
    while (this.#queue.length && performance.now() < deadline) {
      const { task } = this.#queue.shift();                   // 优先队列出队：最高优先级先执行
      task();                                                 // 注意：执行中可能 schedule 新高优任务插队
    }
    if (this.#queue.length) channel.port2.postMessage(null);  // 状态机：还没完 → 继续下一片
    else this.#running = false;                               // 状态机：队列空 → idle 态
  }
}
const scheduler = new Scheduler();
scheduler.schedule(() => renderList(10000), 5);               // 低优：大列表过渡更新
scheduler.schedule(() => updateInput(), 1);                   // 高优：用户输入插队先跑
```
