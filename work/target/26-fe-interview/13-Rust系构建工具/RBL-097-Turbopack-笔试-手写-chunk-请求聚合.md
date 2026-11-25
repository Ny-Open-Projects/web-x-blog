---
title: [RBL-097] 笔试：手写模块请求聚合器（N 个请求合并为 chunk）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-097：笔试：手写模块请求聚合器（N 个请求合并为 chunk）
**答**：实现 chunkAggregator(compile)：1) 浏览器批量请求模块列表（如 import 分析后的依赖数组）；2) 将已在编译队列中的请求合并为一个 chunk 产物（一次编译调用，产物含所有模块）；3) 5ms 内到达的请求合并（微批处理窗口）；4) 重复模块去重；5) 返回 { chunkName, modules } 给每个请求方同一份结果。

```javascript
function createChunkAggregator(compile) {
  let pending = new Set();   // 待合并请求
  let timer = null;
  const waiters = [];        // 每个请求的 resolve 回调

  return function request(modules) {
    return new Promise((resolve) => {
      for (const m of modules) pending.add(m); // 去重合并进窗口
      waiters.push(resolve);
      if (timer) clearTimeout(timer);
      timer = setTimeout(async () => {
        const batch = [...pending];
        pending = new Set();
        const name = `chunk-${batch.length}-${Date.now()}`;
        const result = await compile(batch);   // 一次编译整批
        // 同一结果返回给所有等待者
        while (waiters.length) waiters.shift()({ chunkName: name, modules: batch, ...result });
      }, 5); // 微批窗口：5ms 内到达的请求合并
    });
  };
}
module.exports = { createChunkAggregator };

// 效果：同 tick 的 20 个模块请求 → 1 次 compile 调用 → 所有请求拿到同一 chunk
```
**评分点**：
- 微批窗口（setTimeout 延迟收集）合并请求。
- 请求方各自 resolve 但共享同一编译结果（waiters 数组）。
- pending Set 去重。
- 防抖逻辑正确（每来新请求重置窗口或保留窗口，讲清取舍）。
- 能联系 HMR：浏览器一次热更新会请求多个模块，聚合后一次编译往返，减少网络与编译次数。
