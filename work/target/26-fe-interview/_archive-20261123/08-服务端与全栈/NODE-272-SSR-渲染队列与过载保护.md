---
title: [NODE-272] SSR 渲染队列与过载保护？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-272：SSR 渲染队列与过载保护？
**答**:
- 问题：SSR 是 CPU 密集，瞬时流量超容量 → 全部请求变慢（雪崩）——必须主动限流。
- 队列策略：并发渲染上限（进程内信号量）+ 排队上限（队列长度）——超限直接降级 CSR（快速失败优于排队等待）。
- 队列长度权衡：排队增加 P95 但保住吞吐；实时类页面（秒杀）宁可降级不排队。
- 配合摘流：健康探针带饱和度（NODE-249），网关把流量导向空闲实例。

```javascript
import PQueue from 'p-queue';
const renderQueue = new PQueue({ concurrency: os.cpus().length * 2 });
app.get('*', async (req, res) => {
  if (renderQueue.size > 100) return serveFallbackShell(res);    // 队列超限：快速降级
  const critical = isCriticalPage(req.path);                     // 秒杀页：不排队
  if (!critical && renderQueue.size > 20 && renderQueue.pending > 4) 
    return serveFallbackShell(res);
  await renderQueue.add(() => renderAndPipe(req, res));
});
```
