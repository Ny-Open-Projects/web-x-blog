---
title: [NODE-011] 如何逐行处理一个 10GB 的日志文件而不爆内存？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-011：如何逐行处理一个 10GB 的日志文件而不爆内存？
**答**：
- 禁止 `fs.readFile`（10GB 全量进内存必 OOM）。方案按推荐度：
  1. `readline` 模块 + `createReadStream`（最简单，逐行 emit）。
  2. `stream.consumers` / 第三方 `byline` / `split2` 处理分隔。
  3. 手工按 chunk 切分 + `remainder` 缓存行尾残片（面试要求能手写）。
- 多字节字符截断用 `StringDecoder`；行逻辑有状态聚合（如 PV 统计）时注意每行的归并写法；超大数据集输出也用流写，避免结果集堆积。

```javascript
const fs = require('node:fs');
const readline = require('node:readline');
const { StringDecoder } = require('node:string_decoder');

// 方案一：readline（生产首选）
async function countErrorLines(path) {
  const rl = readline.createInterface({
    input: fs.createReadStream(path, { highWaterMark: 1024 * 1024 }), // 1MB 一块
    crlfDelay: Infinity,
  });
  let errorCount = 0, total = 0;
  for await (const line of rl) {   // for-await 逐行，内存恒定
    total++;
    if (line.includes('ERROR')) errorCount++;
  }
  return { total, errorCount };
}

// 方案二：手写分块 + 行边界 + 多字节安全（面试加分项）
function readLinesByChunk(path, onLine) {
  return new Promise((resolve, reject) => {
    const rs = fs.createReadStream(path, { encoding: 'binary' });
    const decoder = new StringDecoder('utf8');
    let remainder = '';
    rs.on('data', (chunk) => {
      const text = remainder + decoder.write(chunk);
      const lines = text.split('\n');
      remainder = lines.pop();          // 最后一段可能不是完整行，缓存到下一块
      lines.forEach(onLine);
    });
    rs.on('end', () => { if (remainder) onLine(remainder); resolve(); });
    rs.on('error', reject);
  });
}
```
