---
title: [WEB-634] 笔试：手写 WASM Worker 任务池
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, WebAssembly]
type: 笔试题
---

## WEB-634：笔试：手写 WASM Worker 任务池

**答**：实现 `WasmPool`：① 启动 N 个 Worker，每个 Worker 加载同一 wasm 模块（独立实例）；② `run(task)`：取空闲 Worker 执行，无空闲入队等待；③ 每个 Worker 维护冷启动状态：首次实例化完成前的任务排队等待（ready promise）；④ 任务超时（默认 60s）后 reject 并把该 Worker 标记为 poisoned 重建（防 trap 后状态污染）；⑤ destroy() 终止全部并拒绝 pending。写出主线程侧核心实现。

```javascript
class WasmPool {
  constructor(size, wasmUrl, { taskTimeout = 60_000 } = {}) {
    this.workers = Array.from({ length: size }, () => this._spawn(wasmUrl));
    this.queue = []; this.timeout = taskTimeout;
  }
  _spawn(wasmUrl) {
    const w = new Worker('wasm-worker.js');
    const w2 = w;
    w2.readyState = new Promise((resolve) => {
      w.onmessage = ({ data }) => {
        if (data?.ready) resolve();
        else if (data?.resId) w2._handlers?.get(data.resId)?.(data);
      };
      w.postMessage({ init: wasmUrl });
    });
    w2._handlers = new Map();
    w2.busy = false;
    w2.poisoned = false;
    return w2;
  }
  async run(task) {
    const w = this.workers.find(w => !w.busy && !w.poisoned)
      || await new Promise((res) => this.queue.push(res));
    if (w.poisoned) return this.run(task); // 重建后的 worker 重试
    w.busy = true;
    await w.readyState;
    const resId = ++w.seq || (w.seq = 1);
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        w._handlers.delete(resId); w.busy = false;
        w.poisoned = true; w.terminate();      // 超时: 状态不可信, 重建
        this.workers[this.workers.indexOf(w)] = this._spawn();
        reject(new Error('task timeout'));
        const next = this.queue.shift(); if (next) next(this.workers.find(x => !x.busy && !x.poisoned));
      }, this.timeout);
      w._handlers.set(resId, ({ ok, result }) => {
        clearTimeout(timer); w.busy = false; w._handlers.delete(resId);
        ok ? resolve(result) : reject(new Error(result));
        const next = this.queue.shift(); if (next) next(w);
      });
      w.postMessage({ reqId: resId, ...task });
    });
  }
  destroy() { this.workers.forEach(w => w.terminate()); this.queue.forEach(r => r(null)); }
}
```

**评分点**：
- 空闲分配 + 排队等待的调度模型正确
- ready promise 处理冷启动排队
- 超时/失败后 poisoned 标记 + terminate + 重建（trap 后实例不可复用）
- destroy 清理 pending，队列消费者判空防 null 解引用
