---
title: [DP-087] React 源码里能识别出哪些设计模式？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-087：React 源码里能识别出哪些设计模式？（高频）
**答**：
- **优先级队列（策略 + 命令）**：Scheduler 用小顶堆按 `expirationTime/优先级` 排序任务，高优先级任务插队——调度策略集中封装。
- **职责链**：beginWork/completeWork 的 return 链 + 合成事件从 target 向 root 冒泡收集监听。
- **备忘录**：fiber.alternate 双缓冲树（上一次渲染的快照），commit 前可随时丢弃重算。
- **享元**：lane 二进制位复用优先级常量；**模板方法**：类组件生命周期骨架、ErrorBoundary 的固定流程；**迭代器**：effectList 链表遍历 commit。

```javascript
// React Scheduler 简化：小顶堆优先级队列（策略 + 命令）
class TaskQueue {
  #heap = [];
  #getId = 0;
  schedule(task, priority) {       // task 是命令对象：描述"做什么"不含"何时做"
    this.#push({ id: this.#getId++, sortIndex: priority, task });
  }
  #push(node) {                    // 标准二叉堆插入
    this.#heap.push(node);
    let i = this.#heap.length - 1;
    while (i > 0) {
      const parent = (i - 1) >> 1;
      if (this.#compare(this.#heap[parent], this.#heap[i]) <= 0) break;
      [this.#heap[parent], this.#heap[i]] = [this.#heap[i], this.#heap[parent]];
      i = parent;
    }
  }
  #compare(a, b) { return a.sortIndex - b.sortIndex || a.id - b.id; } // 优先级相同时先来先执行
  #pop() {
    const top = this.#heap[0];
    const last = this.#heap.pop();
    if (this.#heap.length) {
      this.#heap[0] = last;
      let i = 0;
      while (true) {
        const l = 2 * i + 1, r = l + 1;
        let min = i;
        if (l < this.#heap.length && this.#compare(this.#heap[l], this.#heap[min]) < 0) min = l;
        if (r < this.#heap.length && this.#compare(this.#heap[r], this.#heap[min]) < 0) min = r;
        if (min === i) break;
        [this.#heap[min], this.#heap[i]] = [this.#heap[i], this.#heap[min]];
        i = min;
      }
    }
    return top;
  }
  workLoop(deadline) {           // 时间切片：每帧空闲时间内的循环
    while (this.#heap.length && deadline.timeRemaining() > 1) {
      const { task } = this.#pop();     // 每次取最高优先级任务
      task();                            // 高优先插队的实现基础
    }
    if (this.#heap.length) requestIdleCallback((dl) => this.workLoop(dl));
  }
}
const scheduler = new TaskQueue();
scheduler.schedule(() => console.log('低优：数据上报'), 10);
scheduler.schedule(() => console.log('高优：用户输入'), 1);   // 数值小 = 优先级高
scheduler.workLoop({ timeRemaining: () => 50 });
// 高优：用户输入 -> 低优：数据上报

// 备忘录：双缓冲 fiber 树
// current.alternate === workInProgress —— 两棵树互为快照，commit 前可整体丢弃
```
