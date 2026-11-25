---
title: [NODE-212] pipeline 与手工 pipe 的差异？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-212：pipeline 与手工 pipe 的差异？
**答**：
- 错误传播：pipe 不会把上游错误传给下游，也不会自动销毁流——错误后流悬挂（fd 泄漏）。pipeline 把任何一环的错误传到最终回调并 destroy 全链。
- 清理保证：pipeline 结束（成功/失败）都保证所有流关闭；pipe 需要手工逐个 destroy。
- async 化：stream/promises 的 pipeline 直接 await；gunzip 中间态、多级转换清晰可组合。
- 使用规范：凡 >1 段的流链一律 pipeline；abort signal 透传（node 18+ 支持 signal 参数）实现取消。

```javascript
import { pipeline } from 'node:stream/promises';
import { createReadStream, createWriteStream } from 'node:fs';
import { createGzip } from 'node:zlib';

// 手工 pipe 的坑：
// createReadStream(src).pipe(createGzip()).pipe(createWriteStream(dst));
// createReadStream 报错 → 后续流不关闭 → fd 泄漏；错误也不会到最终回调

// 正确：
try {
  await pipeline(
    createReadStream(src),
    createGzip(),
    createWriteStream(dst),
    { signal: req.abortSignal },            // 取消支持：客户端断开即中断管道
  );
} catch (e) {
  console.error('pipeline failed:', e);    // 任何一环的错误都到达这里
}
// pipeline 语义 = 每段 pipe + 全链 destroy + 错误聚合
```
