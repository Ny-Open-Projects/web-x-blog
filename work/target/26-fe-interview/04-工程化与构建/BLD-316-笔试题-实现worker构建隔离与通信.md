---
title: [BLD-316] 笔试题——实现 worker 构建隔离与通信（批处理池）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-316：手写 worker 池

**需求与边界**：
- 需求：转换任务的 worker 池（SCN-BLD-212）——① 批处理调度（每 worker 处理一批模块——粒度太小 IPC 吞收益）；② 负载均衡（慢任务不阻塞空闲 worker——动态分配）；③ 结果回传与缓存写入（worker 结果直接进持久缓存）；④ 崩溃恢复（worker 崩溃任务重新分配）。
- 边界：① 批大小自适应（按平均模块耗时调整——通信开销占比）；② worker 崩溃检测（退出事件 + 未完成任务回收）；③ 主线程不阻塞（调度在主线程微任务完成）。

**答**：
```javascript
class TransformPool {
  constructor({ workers = os.cpus().length, batchSize = 50 } = {}) {
    this.pool = Array.from({ length: workers }, () => this.spawn());
    this.queue = []; this.pending = new Map();         // 任务 → worker
  }
  spawn() {
    const w = new Worker('./transform.worker.js');
    w.on('message', ({ results }) => this.onResults(w, results));   // 结果回传
    w.on('exit', () => this.respawnAndReassign(w));    // 崩溃：重生 + 任务回收
    return w;
  }
  async transform(modules) {
    // 批处理调度：按预估耗时分批（自适应——通信开销占比目标 < 10%）
    const batches = this.splitByCost(modules, { ipcOverheadTarget: 0.1 });
    return Promise.all(batches.map(batch => this.assign(batch)));
  }
  assign(batch) {
    const idle = this.pool.find(w => !this.pending.has(w));   // 动态负载均衡
    const w = idle ?? this.pool[this.roundRobin()];
    this.pending.set(w, batch);
    w.postMessage({ batch });
    return new Promise(res => this.resolveMap.set(batch, res));
  }
  onResults(w, results) {                              // 结果直接写持久缓存（SCN-BLD-211）
    results.forEach(r => persistCache(r.id, r.output));
    this.resolveMap.get(this.pending.get(w))?.(results);
    this.pending.delete(w);
  }
}
```

**评分点**:
- 批处理调度（自适应批大小——IPC 开销占比目标）。
- 动态负载均衡（空闲 worker 优先——慢任务不阻塞）。
- 崩溃恢复（exit 事件 + 任务回收重分配）。
- 结果直写持久缓存（转换与缓存协同——SCN-BLD-211）。
