---
title: [HW-137] 手写大 JSON 流式解析——Worker 内分块解析 + 进度上报 + 结构回调（不全量驻内存）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：50MB JSON 用 JSON.parse 一次解析 = 主线程卡 2~5s + 双倍内存峰值。Worker 内流式方案：按字节块读取（File.slice / fetch reader）→ 增量解析顶层元素（JSON Lines 最简单；标准 JSON 用括号深度扫描切顶层元素）→ 每解析出一个元素回调主线程（进度 + 数据），不全量驻内存。

```javascript
// worker.js：JSON Lines 流式解析（行分隔场景最实用）
self.onmessage = ({ data }) => {
  const { url } = data;
  (async () => {
    const res = await fetch(url);
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buf = '', count = 0;
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      buf += decoder.decode(value, { stream: true });
      const lines = buf.split('\n');
      buf = lines.pop();                          // 最后一段可能不完整：留到下块
      const batch = [];
      for (const line of lines) {
        if (line.trim()) { batch.push(JSON.parse(line)); count++; }
      }
      if (batch.length >= 1000) {
        self.postMessage({ type: 'batch', items: batch, count });   // 分批回传（不驻内存）
      }
    }
    if (buf.trim()) self.postMessage({ type: 'batch', items: [JSON.parse(buf)], count: ++count });
    self.postMessage({ type: 'done', count });
  })();
};
// 主线程：Worker 分批接收 → 增量渲染/入库，峰值内存 = 一批大小而非 50MB 全量
// 进度：count / 总行数（或 response header 的 Content-Length 估算）
// 标准单 JSON（非 Lines）：Worker 内做括号深度扫描切顶层元素——复杂度高，工程上优先推动接口改 JSON Lines
```

**评分点**：
- 流式分块 + 增量解析（split 留尾巴处理不完整行的边界正确）。
- 分批回传不全量驻内存（峰值内存 = 批大小）——本题核心。
- 进度上报（count + Content-Length 估算）。
- 能说出"标准 JSON 流式解析复杂，推动 JSON Lines 是工程正解"。
