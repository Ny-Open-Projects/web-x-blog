---
title: [NODE-230] worker_threads 的异常与生命周期管理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-230：worker_threads 的异常与生命周期管理？
**答**:
- 错误路径四类：worker 崩溃（error/uncaughtException）、消息处理抛错（主线程 promise reject）、worker 主动 exit（非 0）、超时无响应（僵尸）。
- 处理策略：错误 message 透传到任务 promise；非 0 exit 自动重建池成员；超时 terminate + 标记任务失败（terminate 是暴力杀，可能丢消息——最后手段）。
- 优雅关闭：SIGTERM 时主线程发关闭信号 → worker 完成在途任务 → exit；超时强杀兜底。
- 观测：worker 生命周期事件（online/exit）进指标（池活跃数/队列长度）。

```javascript
class Pool {
  #spawn() {
    const w = new Worker('./worker.js');
    w.on('error', e => this.#failAll(w, e));           // 崩溃 → 该 worker 全部任务失败
    w.on('exit', (code) => { if (code !== 0) this.#respawn(); });
    return w;
  }
  #failAll(w, err) {
    for (const [id, task] of this.#busy)
      if (task.w === w) { task.rej(err); this.#busy.delete(id); }
    this.#respawn();
  }
  run(task, { timeout = 30000 } = {}) {
    return new Promise((res, rej) => {
      const timer = setTimeout(() => {                 // 僵尸：超时强杀
        this.#busy.get(task.id)?.w.terminate();
        rej(new TimeoutError());
      }, timeout);
      // ... message 处理 clear timer
    });
  }
  async shutdown({ timeout = 5000 } = {}) {            // 优雅关闭
    this.#closing = true;
    await Promise.race([this.#drain(), new Promise(r => setTimeout(r, timeout))]);
    for (const w of [...this.#idle, ...this.#busy.values().map(t => t.w)]) w.terminate();
  }
}
```
