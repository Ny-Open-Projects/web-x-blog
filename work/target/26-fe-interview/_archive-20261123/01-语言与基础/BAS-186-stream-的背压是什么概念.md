---
title: [BAS-186] stream 的背压是什么概念？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-186：stream 的背压是什么概念？
**答**：
- 读的速度远快于写时，数据会在内存里堆积；背压（backpressure）是下游告诉上游"慢一点"的机制。
- `ws.write()` 返回 false 表示写缓冲已满，应暂停读取；收到 drain 事件再恢复。
- pipe/web streams 的 pipeline 内建了背压处理，手写时必须自己 pause/resume。

```javascript
const fs = require('fs');
const rs = fs.createReadStream('big.bin');
const ws = fs.createWriteStream('out.bin');
rs.pipe(ws); // 写不过去时自动 pause 读，drain 后 resume，这就是背压

// 手写等价逻辑（理解用）
ws.on('drain', () => rs.resume());
rs.on('data', chunk => {
  if (!ws.write(chunk)) rs.pause(); // write 返回 false 说明缓冲已满
});
```
