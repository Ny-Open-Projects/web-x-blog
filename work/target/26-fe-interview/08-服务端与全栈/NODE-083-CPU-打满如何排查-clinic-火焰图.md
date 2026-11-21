---
title: [NODE-083] CPU 打满如何排查（clinic、火焰图）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-083：CPU 打满如何排查（clinic、火焰图）？
**答**：
- 症状识别：QPS 下降但内存正常、`event loop lag` > 100ms、接口耗时长但下游都快 → 主线程被同步计算阻塞。
- 排查工具：① `clinic doctor`（体检：CPU/事件循环/GC 综合诊断）→ `clinic flame`（火焰图：找到最宽的栈）；② `node --cpu-prof` 生成 cpuprofile（DevTools Performance 面板打开）；③ 线上无侵入：`kill -USR1` 后 Chrome inspect 或 `node --inspect` 连接。
- 常见元凶：大 JSON.stringify/parse、正则回溯灾难、同步 crypto、模板大循环、`JSON.parse` 大 body。
- 治理：拆分计算（分片 + setImmediate 让路）、移入 worker_threads、换高效算法/库（如 fast-json-stringify）、缓存计算结果。

```bash
# 1. clinic 体检 + 火焰图（压测同时运行）
npm i -g clinic autocannon
clinic doctor -- node dist/main.js &
autocannon -c 50 -d 20 http://localhost:3000/api/heavy
clinic flame -- node dist/main.js        # 输出火焰图 HTML：宽度 = CPU 占用

# 2. 生产低开销采样
node --cpu-prof --cpu-prof-dir=/tmp --cpu-prof-interval=1000 dist/main.js
```

```javascript
// 典型阻塞代码与修复对照
// ❌ 阻塞：10 万条记录一次 stringify，事件循环卡 800ms
app.get('/report/bad', async (ctx) => {
  const rows = await db.query('SELECT * FROM orders LIMIT 100000');
  ctx.body = JSON.stringify(rows);           // 同步计算，全服务停摆
});

// ✅ 修复一：分片让路（每片之间 yield 事件循环）
function chunkStringify(rows, size = 5000) {
  return new Promise((resolve) => {
    const parts = [];
    let i = 0;
    (function next() {
      const end = Math.min(i + size, rows.length);
      parts.push(rows.slice(i, end).map((r) => JSON.stringify(r)).join(','));
      i = end;
      if (i < rows.length) setImmediate(next);   // 让路：别的请求插得进来
      else resolve(`[${parts.join(',')}]`);
    })();
  });
}

// ✅ 修复二：CPU 密集移入 worker 线程（NODE-007）
const { Worker } = require('node:worker_threads');
function heavyComputeInWorker(input) {
  return new Promise((resolve, reject) => {
    const w = new Worker('./heavy-worker.js', { workerData: input });
    w.on('message', resolve).on('error', reject);
  });
}
```
