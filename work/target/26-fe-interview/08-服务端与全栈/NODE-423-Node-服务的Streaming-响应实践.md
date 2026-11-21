---
title: [NODE-423] Node 服务的 Streaming 响应实践（SSE/NDJSON/chunked）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-423：Streaming 响应实践
**答**:
- 三种流式协议：SSE（事件语义，浏览器 EventSource 原生）、NDJSON（每行一个 JSON，程序化消费友好，AI 流式输出主流）、chunked 原始流（二进制）。选型看消费方：前端 UI 用 SSE，服务间/脚本用 NDJSON。
- 实现要点：writeHead 正确头（NODE-347 SSE 头；NDJSON 用 application/x-ndjson + no-buffering）、背压（res.write 返回 false 时暂停上游读取等 drain，NODE-010）、分块大小权衡（太小 overhead 大太大数据不新鲜——按消费节奏 flush）。
- 生命周期：数据源错误中途断流（已发部分语义——协议带结束标记或错误事件让消费方识别不完整数据）、客户端断开取消上游（NODE-422）、超时保护。
- 中间层陷阱：代理/CDN 缓冲（X-Accel-Buffering: no、禁 gzip 或流式 gzip——有些压缩实现会缓冲整包）、压缩对流式延迟的影响评估。
- 可观测：流式请求的 TTFB 与总时长分开统计（TTFB 才是流式价值指标）。
```javascript
app.get('/stream/goods', async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/x-ndjson',
    'Transfer-Encoding': 'chunked', 'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no' });
  const cur = db.stream('select * from goods');
  for await (const row of cur) {
    if (req.closed) { cur.destroy(); return; }                   // 客户端断开取消
    if (!res.write(JSON.stringify(row) + '\n'))                  // 背压
      await once(res, 'drain');
  }
  res.end();
});
```
