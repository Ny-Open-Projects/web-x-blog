---
title: [ALG-151] 接口要下发一个 80MB 的 JSON（NDJSON 逐行格式），`JSON.parse` 整体解析会oom卡死。如何流式解析？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-151：接口要下发一个 80MB 的 JSON（NDJSON 逐行格式），`JSON.parse` 整体解析会oom卡死。如何流式解析？
**答**：用 `response.body.getReader()` 分块读流：每块用 `TextDecoder({ stream: true })` 解码（处理多字节字符跨块），拼接进缓冲区；每凑到完整一行（NDJSON 以换行分隔）立即 `JSON.parse` 并回调消费，缓冲区只保留残余片段，内存占用恒定。整体 O(n)，峰值内存 O(单条记录 + 一个 chunk)。

```javascript
async function parseNDJSONStream(response, onRecord) {
  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buf = '';
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    buf += decoder.decode(value, { stream: true }); // stream: true 处理跨块多字节字符
    let idx;
    // 每凑到一条完整行立即解析回调，内存只保留残余片段
    while ((idx = buf.indexOf('\n')) >= 0) {
      const line = buf.slice(0, idx).trim();
      buf = buf.slice(idx + 1);
      if (line) onRecord(JSON.parse(line)); // 逐条消费，不攒全量
    }
  }
  if (buf.trim()) onRecord(JSON.parse(buf)); // 收尾最后一条（无换行结尾）
}
// parseNDJSONStream(await fetch('/api/logs'), r => appendRow(r))
```
