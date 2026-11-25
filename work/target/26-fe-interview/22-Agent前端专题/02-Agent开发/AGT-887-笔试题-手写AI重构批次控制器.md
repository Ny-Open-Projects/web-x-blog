---
title: [AGT-887] 手写 refactorBatch：分批调度、验证失败回滚、进度台账、失败清单？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-887：手写 refactorBatch：分批调度、验证失败回滚、进度台账、失败清单

**需求与边界**：
- 实现 RefactorController：enqueue(modules)/run(batchSize)/status()。
- 边界要求：① 每批跑三重验证（test/type/visual），任一失败整批回滚并记失败清单；② 失败模块自动进重试队列（最多 2 次，之后转人工）；③ status 返回（done/failed/pending/progress）计数；④ 中断恢复（已验证模块跳过）；⑤ 回滚用 git 精确还原该批文件。

**答**：
```javascript
class RefactorController {
  constructor(modules, { batchSize = 50 } = {}) {
    this.queue = modules; this.batchSize = batchSize;
    this.done = []; this.failed = []; this.retries = new Map();
  }
  async run() {
    while (this.queue.length) {
      const batch = this.queue.slice(0, this.batchSize);
      const snapshot = await git.snapshot(batch);  // 精确快照
      await transform(batch);
      const checks = await verify(batch, ['test', 'type', 'visual']);
      if (checks.ok) { this.done.push(...batch); }
      else {
        await git.restore(snapshot);               // 整批回滚
        for (const m of batch) {
          const n = (this.retries.get(m) ?? 0) + 1;
          this.retries.set(m, n);
          n <= 2 ? this.queue.push(m) : this.failed.push(m); // 转人工
        }
      }
      this.queue = this.queue.slice(batchSize);
    }
    return this.status();
  }
  status() {
    return { done: this.done.length, failed: this.failed.length,
      pending: this.queue.length,
      failedList: this.failed };                   // 台账
  }
}
```

**评分点**:
- 整批原子性（快照→验证→失败整批回滚）；失败模块重试上限后转人工。
- git 精确还原该批文件（不影响其他进行中改动）。
- status 台账（done/failed/pending）可恢复续跑。

