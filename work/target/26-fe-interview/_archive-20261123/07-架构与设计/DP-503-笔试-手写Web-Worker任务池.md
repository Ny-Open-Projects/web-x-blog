---
title: [DP-503] 笔试：手写 Worker 任务池
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-503：笔试：手写 Worker 池

**题目**：实现 Worker 任务池 `WorkerPool`：① N 个 Worker（hardwareConcurrency-1 上限）——首任务懒创建；② 任务分发：空闲 Worker 执行，无空闲入队；③ reqId 关联（并发任务的消息匹配）；④ 毒任务防护：任务超时 → terminate 该 Worker 重建（trap 后实例不可信）；⑤ destroy：全部 terminate + pending reject。写出主线程实现。

```javascript
class WorkerPool {
  #workers = []; #queue = []; #max;
  constructor(url, max = Math.max(2, (navigator.hardwareConcurrency || 4) - 1)) {
    this.url = url; this.#max = max;
  }
  #spawn() {
    const w = new Worker(this.url);
    w.busy = false; w.seq = 0; w.handlers = new Map();
    w.onmessage = ({ data: { id, ok, result } }) => {
      const p = w.handlers.get(id);
      if (!p) return;
      w.handlers.delete(id); w.busy = false;
      clearTimeout(p.timer);
      ok ? p.resolve(result) : p.reject(new Error(result));
      this.#free(w);
    };
    return w;
  }
  run(payload, { timeout = 30_000 } = {}) {
    const w = this.#workers.find((x) => !x.busy && !x.poisoned) ?? (this.#workers.length < this.#max ? this.#spawn() : null);
    if (!w) return new Promise((res, rej) => this.#queue.push({ payload, timeout, res, rej })).then(() => this.run(payload));
    w.busy = true;
    const id = ++w.seq;
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {                  // 毒任务: 重建 Worker
        w.handlers.delete(id); w.poisoned = true;
        w.terminate();
        this.#workers[this.#workers.indexOf(w)] = this.#spawn();
        reject(new Error('worker task timeout'));
        this.#free(this.#workers.at(-1));
      }, timeout);
      w.handlers.set(id, { resolve, reject, timer });
      w.postMessage({ id, payload });
    });
  }
  #free(w) { const next = this.#queue.shift(); next ? this.run(next.payload, next) : null; }
  destroy() { this.#workers.forEach((w) => w.terminate()); }
}
```

**评分点**：
- 懒创建 + 并发上限（hardwareConcurrency-1）
- reqId 关联的并发消息匹配
- 超时 terminate 重建（trap 后状态不可信——毒任务防护）
- destroy 的 pending reject 清理
