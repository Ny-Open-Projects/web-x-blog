---
title: [JS-408] 笔试：手写空闲期任务队列（requestIdleCallback 调度）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-408：笔试：手写空闲期任务队列

**答**：实现 `IdleQueue`：① push(task, { priority })：任务按优先级排序在空闲期执行；② 每个空闲回调只执行到 deadline 剩余 <3ms 就让出；③ 高优先级任务可指定 timeout（超时后即使不空闲也必须执行）；④ 无 requestIdleCallback 环境（Safari）降级 setTimeout 0 + 16ms 预算；⑤ destroy() 清空。写出实现。

```javascript
class IdleQueue {
  #tasks = []; #scheduled = false; #ric = typeof requestIdleCallback === 'function';
  push(task, { priority = 0, timeout } = {}) {
    this.#tasks.push({ task, priority, timeout });
    // 有 timeout 的高优任务用 setTimeout 兜底
    if (timeout != null) setTimeout(() => this.#force(task), timeout);
    this.#schedule();
  }
  #schedule() {
    if (this.#scheduled || !this.#tasks.length) return;
    this.#scheduled = true;
    const drain = (deadline) => {
      this.#scheduled = false;
      this.#sort();
      while (this.#tasks.length) {
        const remain = deadline ? deadline.timeRemaining() : (performance.now() % 16 < 14 ? 14 : 1);
        if (remain < 3) break;                       // 预算不足让出
        const { task } = this.#tasks.shift();
        try { task(); } catch (e) { console.error(e); }
      }
      if (this.#tasks.length) this.#schedule();       // 剩余继续排
    };
    this.#ric ? requestIdleCallback(drain) : setTimeout(() => drain(null), 0);
  }
  #sort() { this.#tasks.sort((a, b) => b.priority - a.priority); }
  #force(task) {
    const i = this.#tasks.findIndex(t => t.task === task);
    if (i < 0) return;                                // 已执行
    this.#tasks.splice(i, 1);
    task();
  }
  destroy() { this.#tasks = []; }
}
// 用法: 非关键预计算
idleQ.push(() => precomputeIndex(), { priority: 5, timeout: 5000 });
```

**评分点**：
- deadline.timeRemaining 预算控制（<3ms 让出）与剩余任务重排
- 优先级排序在每次 drain 前重算（动态插入）
- timeout 强制执行兜底（防永远空闲不执行）
- Safari 降级 16ms 帧预算模拟
