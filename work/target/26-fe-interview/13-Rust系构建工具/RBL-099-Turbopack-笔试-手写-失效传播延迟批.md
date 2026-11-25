---
title: [RBL-099] 笔试：手写失效传播节流器（高频变更合并重算）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-099：笔试：手写失效传播节流器（高频变更合并重算）
**答**：实现 DebouncedRevalidator(recompute)：1) invalidate(ids) 标记失效集合；2) 50ms 窗口内的高频 invalidate 合并成一次 recompute（参数为合并后的 id 集合）；3) recompute 进行中到达的新失效：标记为 pending，当前完成后立即再跑一轮（不丢失效）；4) 支持并发去重（同一时刻最多一个 recompute）；5) 返回统计 { runs, dropped }。

```javascript
function createRevalidator(recompute) {
  let dirty = new Set();       // 待重算失效集合
  let timer = null;
  let running = false;
  const stats = { runs: 0, dropped: 0 }; // dropped: 被合并掉的独立重算次数

  async function flush() {
    if (running) return;                    // 并发去重
    const batch = [...dirty];
    dirty = new Set();
    if (!batch.length) return;
    running = true;
    stats.runs++;
    try { await recompute(batch); }
    finally {
      running = false;
      if (dirty.size) {                     // 窗口期外新失效：立刻补一轮
        stats.dropped += 1;                 // 这些失效被合并进了下一轮
        flush();
      }
    }
  }

  return {
    invalidate(ids) {
      ids.forEach(id => dirty.add(id));
      if (timer) clearTimeout(timer);
      timer = setTimeout(flush, 50);        // 50ms 微批窗口
    },
    stats,
  };
}
module.exports = { createRevalidator };

// 高频场景：1s 内 100 次文件变更 → 期望 runs ≈ 1~2 而不是 100
```
**评分点**：
- 窗口合并（50ms 防抖）减少重算次数。
- running 期间新失效进下一轮（不丢失，finally 里补跑）。
- 并发互斥（同一时刻一个 recompute）。
- 统计指标（runs/dropped）体现工程意识。
- 能联系 dev server：文件 watch 高频抖动（编辑器保存风暴）正是此场景。
