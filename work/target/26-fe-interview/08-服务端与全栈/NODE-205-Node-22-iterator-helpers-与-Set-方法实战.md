---
title: [NODE-205] Node 22 iterator helpers 与 Set 方法实战？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-205：Node 22 iterator helpers 与 Set 方法实战？
**答**：
- iterator helpers（V8 12.4）：迭代器的 map/filter/take/flatMap/group——惰性求值，处理大集合不落地中间数组（对比 Array.filter 链的多次遍历+全量物化）。
- Set 数学：union/intersection/difference/symmetricDifference/isSubsetOf——权限码/标签运算的官方姿势（NODE 系列里手写过，现在原生）。
- 大文件/大流场景：iterator helpers 与 Node streams 的 async iterator 组合（readline → filter → take N）。
- 性能注意：helpers 惰性但要避免在同一迭代器上消费两次（消耗后为空）。

```javascript
// 大日志文件的惰性处理
import { createReadStream } from 'node:fs';
import readline from 'node:readline';
const rl = readline.createInterface({ input: createReadStream('app.log') });
const errors = rl[Symbol.asyncIterator]()      // 异步迭代器
  .filter(line => line.includes('ERROR'))
  .take(50)                                    // 惰性：找到 50 条即停，不读完文件
  .toArray();
// Set 数学：权限合并
const adminPerms = new Set(['read', 'write', 'delete']);
const editorPerms = new Set(['read', 'write']);
const shared = adminPerms.intersection(editorPerms);      // Set { 'read', 'write' }
const missing = adminPerms.difference(editorPerms);       // Set { 'delete' }
```
