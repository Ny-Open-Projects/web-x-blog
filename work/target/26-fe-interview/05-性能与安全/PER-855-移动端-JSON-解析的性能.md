---
title: [PER-855] 移动端 JSON 解析的性能：大 JSON 解析阻塞、流式解析与懒解析
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-855：移动端 JSON 解析的性能：大 JSON 解析阻塞、流式解析与懒解析

**答**：
- JSON.parse 是同步阻塞的：1MB JSON 在移动端解析可能 100~300ms（长任务），10MB 直接卡死——大响应必须拆。
- 三板斧：① 分块传输 + 逐块解析（NDJSON/JSON Lines 或手动切分，每块 < 100KB，块间让出主线程）；② Worker 解析（主线程零阻塞，结果 transferable 回传）；③ 懒解析（只解析当前视图用到的字段，或服务端裁剪字段——最优解是不传输无用数据）。
- 根因优先：先审计响应体积，很多"解析慢"其实是"传输了不该传的数据"（全量列表/冗余嵌套），字段裁剪比解析优化收益大。
- 序列化同理：上报时 JSON.stringify 大对象也是长任务，大日志序列化放 Worker 或分批。

```javascript
// NDJSON 分块流式解析
async function parseNdjson(streamUrl, onBatch, { batchLines = 50 } = {}) {
  const reader = (await fetch(streamUrl)).body.getReader();
  const decoder = new TextDecoder();
  let buf = '', lines = [];
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true });
    const parts = buf.split('\n');          // 按行切（NDJSON）
    buf = parts.pop();                       // 半行留到下一块
    for (const line of parts) {
      lines.push(JSON.parse(line));
      if (lines.length >= batchLines) {      // 分批回吐，主线程不拥塞
        onBatch(lines); lines = [];
        await new Promise(r => setTimeout(r));   // 让出主线程一帧
      }
    }
  }
  if (lines.length) onBatch(lines);
}
// Worker 方案：主线程零阻塞
worker.postMessage({ raw: bigText }, []);
worker.onmessage = e => render(e.data.list);   // 结果回传
```
