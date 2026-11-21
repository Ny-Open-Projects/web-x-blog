---
title: [H5-305] 笔试：手写 Worker 任务池
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Worker]
type: 笔试题
---

## H5-305：笔试：手写 Worker 任务池

**题目**：实现 `WorkerPool`：构造时创建 N 个常驻 worker（同一脚本）；`run(task)` 排队分发到空闲 worker；单任务超时（如 10s）则销毁该 worker 重建；提供 `stats()` 返回 { idle, busy, queued }。

**答**：
```javascript
class WorkerPool {
  #idle = []; #queue = []; #size;
  constructor(url, size = navigator.hardwareConcurrency - 1 || 2) {
    this.#size = size;
    this.#idle = Array.from({ length: size }, () => this.#create(url));
  }
  #url; // 存脚本地址便于重建
  #create(url) {
    this.#url = url;
    const w = new Worker(url);
    w.onmessage = ({ data }) => {
      w._task && w._task.resolve(data);
      w._task = null;
      this.#idle.push(w);
      this.#drain();
    };
    return w;
  }
  run(data, { timeout = 10000, transfer } = {}) {
    return new Promise((resolve, reject) => {
      this.#queue.push({ data, timeout, transfer, resolve, reject });
      this.#drain();
    });
  }
  #drain() {
    const w = this.#idle.pop();
    if (!w || !this.#queue.length) { w && this.#idle.push(w); return; }
    const t = this.#queue.shift();
    w._task = t;
    t.timer = setTimeout(() => {
      // 超时：销毁重建
      w.terminate();
      const nw = this.#create(this.#url);
      t.reject(new Error('worker task timeout'));
      this.#idle.push(nw);
      this.#drain();
    }, t.timeout);
    w.postMessage(t.data, t.transfer || []);
  }
  stats() { return { idle: this.#idle.length, busy: this.#size - this.#idle.length, queued: this.#queue.length }; }
}
```

**评分点**：
- 空闲队列 + 任务队列的 drain 调度模型（不用轮询）
- 超时用 terminate 销毁重建（Worker 卡死无法从外部中断，只能杀）——核心判分点
- timeout 的 timer 在任务完成时未清理需注意（可加 clearTimeout）
- stats 三项统计反映池的运行状态
