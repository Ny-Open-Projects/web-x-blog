---
title: [NODE-330] Node 服务的健康探针设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-330：Node 服务的健康探针设计？
**答**:
- 双探针：liveness（进程活着，只查 ELU/内存，不查依赖）与 readiness（可服务，查依赖：DB ping/Redis ping/下游连通）——K8s 区分使用（NODE-184）。
- readiness 失败 → 摘流不重启；liveness 失败 → 重启容器。探针误判的代价不对称——依赖抖动不应触发 liveness 重启。
- 返回内容：水位指标（ELU/RSS/队列长）+ 依赖状态明细——网关限流决策输入（NODE-249）。
- 探针自身保护：/health 不打日志、无鉴权、超短超时——探针风暴防护。

```javascript
app.get('/healthz', (ctx) => {   // liveness：轻
  const elu = eventLoopUtilization().utilization;
  ctx.status = elu > 0.95 ? 503 : 200;
  ctx.body = { elu };
});
app.get('/ready', async (ctx) => {   // readiness：查依赖
  const checks = await Promise.allSettled([db.query('SELECT 1'), redis.ping(), pingDownstream()]);
  const failed = checks.filter(c => c.status === 'rejected');
  ctx.status = failed.length ? 503 : 200;
  ctx.body = { deps: checks.map((c, i) => ({ name: DEPS[i], ok: c.status === 'fulfilled' })) };
});
```
