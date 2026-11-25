---
title: [NODE-821] 笔试题——实现 BFF 流式合并（多下游 SSE → 单响应流）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-821：手写流式合并

**需求与边界**：
- 需求：多下游流式合并（SCN-NODE-821）——① 多 SSE 下游合并为单响应流（分段标记——客户端区分来源）；② 顺序语义（按完成顺序流——慢下游不阻塞快下游，SCN-NODE-821 并发）；③ 背压（客户端慢——SCN-NODE-636）；④ 断开传播（客户端断开 abort 所有下游——SCN-NODE-744）。
- 边界：① 下游失败的分段处理（某流失败——该段标记失败不中断其他——部分成功流式版，SCN-NODE-729）；② 段间分隔协议（NDJSON——每行 JSON 带来源）；③ 内存守恒（流式不缓存全量——SCN-NODE-681）。

**答**：
```javascript
app.get('/stream/combine', async (req, res) => {
  res.setHeader('Content-Type', 'application/x-ndjson');
  const abort = new AbortController();
  req.on('close', () => abort.abort());                // 断开传播（SCN-NODE-744）
  const streams = ['news', 'alerts', 'chat'].map(async (src) => {
    const upstream = await downstreamSSE(src, { signal: abort.signal });
    for await (const chunk of upstream) {
      if (res.destroyed) break;                        // 客户端断开（背压语义）
      res.write(JSON.stringify({ src, data: chunk }) + '\n');   // NDJSON 分段（来源标记）
    }
  });
  await Promise.allSettled(streams);                   // 部分成功（某流失败不中断——SCN-NODE-729）
  res.end();
});
```

**评分点**:
- NDJSON 分段协议（来源标记——客户端区分）。
- 并发流互不阻塞（完成顺序流式——SCN-NODE-821）。
- 部分成功流式版（某流失败标记不中断——SCN-NODE-729）。
- 断开传播 + 背压（SCN-NODE-744/636）。
