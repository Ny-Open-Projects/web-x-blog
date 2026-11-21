---
title: [RBL-050] 笔试：手写并行模块转换池（模拟 Rspack Rayon 调度）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-050：笔试：手写并行模块转换池（模拟 Rspack Rayon 调度）
**题目**：实现 transformAll(files, worker, concurrency)：1) concurrency 个并发槽位并行执行 worker(file)；2) 任一失败要整体 reject 且已完成的任务不浪费；3) 保持输出顺序与输入顺序一致（并行但结果有序）；4) 支持 concurrency 动态取消（借 AbortSignal）；5) 统计吞吐（tasks/s）。

```javascript
async function transformAll(files, worker, concurrency = 4, signal = new AbortSignal()) {
  const results = new Array(files.length);
  let next = 0, done = 0;
  const start = performance.now();

  const runner = async (i) => {
    while (next < files.length) {
      const idx = next++;              // 原子取任务（单线程 JS 下安全）
      if (signal.aborted) throw new Error('aborted');
      results[idx] = await worker(files[idx]);
      done++;
    }
  };

  const slots = Array.from({ length: Math.min(concurrency, files.length) },
    (_, i) => runner(i).catch(err => { signal.aborted = true; throw err; }));

  await Promise.all(slots);
  const sec = (performance.now() - start) / 1000;
  return { results, throughput: +(done / sec).toFixed(1) }; // 顺序与输入一致
}
module.exports = { transformAll };

// 用法：模拟 8 个文件 4 并发
// const { results, throughput } = await transformAll(files, f => compile(f), 4);
```
**评分点**：
- 任务指针 next++ 抢占式分发（线程池模型正确）。
- 结果按下标写回，输出顺序与输入一致（并行有序，易漏）。
- 失败传播 + 停止取新任务（fail-fast）。
- 并发槽位 = min(concurrency, 任务数)（不空转）。
- 能联系 Rspack：Rayon 同样是「N 线程抢任务队列」，JS 单线程下用 async 槽位模拟同等语义。
