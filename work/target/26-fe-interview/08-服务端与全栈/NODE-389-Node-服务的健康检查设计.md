---
title: [NODE-389] Node 服务的健康检查（liveness/readiness 深度）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-389：Node 服务的健康检查深度设计
**答**:
- 两个探针语义不同：liveness 回答"进程是否活着"（只查自检：事件循环响应、内存超限）——不查依赖！依赖故障杀进程会雪崩（重启风暴）；readiness 回答"能否接流量"（查依赖：DB/Redis 连通 + 预热完成 + 降级状态）。
- 设计细节：readiness 快速失败（依赖检查超时 < 1s，探针周期内能反馈）、检查结果缓存（1~2s，防探针高频打挂自己）、启动期 readiness false 直到预热完成（缓存回填/连接建立 NODE-375）。
- 依赖降级的语义：Redis 挂了但服务能降级运行（NODE-383）→ readiness 应保持 true（能接流量）还是 false？——能降级服务保持 true，配合指标告警；完全不可服务才 false。
- 启动深度检查：依赖就绪 + 数据迁移版本正确 + 配置加载成功（NODE-388）。
- 人工干预通道：健康状态可被运维置为"摘流"（发布/故障时主动 readiness false，NODE-351）。
```javascript
app.get('/healthz', (req, res) => res.status(eventLoopHealthy() && !oomRisk() ? 200 : 500).end()); // 自检 only
app.get('/readyz', async (req, res) => {
  if (!warmed) return res.status(503).end();                    // 预热未完成
  const deps = await checkDeps({ timeout: 800 });               // DB/Redis 连通
  const ok = deps.db || CAN_DEGRADE_WITHOUT_DB;                 // 能降级则不摘流
  res.status(ok ? 200 : 503).end();
});
```
