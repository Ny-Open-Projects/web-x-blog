---
title: [NODE-223] 流的多路复用与合并？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-223：流的多路复用与合并？
**答**：
- 合并：多源顺序合并（concat）vs 交错合并（merge）——stream-chain 自实现或 async generator 组合（Readable.from(mergeIterators(...))）。
- 多路分用：一个流按规则分发到多个下游（tee/duplex）——Transform 双 push 或 Web Streams 的 tee()。
- 背压注意：merge 多源时"慢源拖累快源"（交错输出）；下游慢时所有源都要能背压暂停。
- 实战：多实例日志合并采集（NODE-34x MQ 主题分流类似）、多源备份聚合。

```javascript
import { Readable } from 'node:stream';
// 顺序合并
async function* concat(...sources) { for (const s of sources) yield* s; }
// 交错合并（轮询制，保留各源背压）
async function* merge(...sources) {
  const iters = sources.map(s => s[Symbol.asyncIterator]());
  let alive = iters.length;
  const nexts = iters.map(it => it.next());
  while (alive) {
    const { idx, result } = await Promise.any(nexts.map(async (p, i) => ({ i, r: await p }))) || {};
    const i = idx;
    if (result.done) { alive--; nexts[i] = Promise.resolve({ done: true }); continue; }
    yield result.value;
    nexts[i] = iters[i].next();
  }
}
Readable.from(merge(streamA, streamB)).pipe(target);   // 交错消费 A/B
```
