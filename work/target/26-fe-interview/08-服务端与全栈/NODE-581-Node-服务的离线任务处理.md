---
title: [NODE-581] Node 服务的离线任务（用户不可在线等待的作业）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-581：离线任务设计
**答**:
- 场景：批量导入/报表生成/数据修复/视频转码——用户提交后不等结果（任务中心轮询 ARC-576）。任务模型：提交（参数快照——重放一致）、执行（Worker 池——并发/优先级/资源隔离 NODE-418）、状态（进度可查询/ETA）、产物（文件/数据——签名 URL 下载）。
- 提交协议：任务参数校验（提交时验证——防运行时才失败）、预检（轻量前置检查：范围行数/权限——快速失败）、任务幂等（提交键防重复提交——ARC-481）。
- 执行可靠性：任务超时（长时间运行任务 checkpoint——可续跑）、失败重试（可重试错误自动重试——确定性失败进死信）、资源保护（大任务限流——不挤占在线服务 NODE-418 独立池）。
- 产物管理：产物生命周期（TTL 自动清理——存储成本）、产物校验（完整性/水印）。
- 观测：任务成功率/执行时长分布/队列深度——任务中心健康看板。
```javascript
// 任务提交与执行
app.post('/tasks/export', async (ctx) => {
  await precheck(ctx.body);                                      // 轻量预检
  const id = await taskQueue.add('export', ctx.body, { idempotencyKey: ctx.idem });
  return { taskId: id, eta: estimate(ctx.body) };                // ETA 预估
});
worker.process('export', withCheckpoint(async (job) => {         // 可续跑
  const rows = await streamExport(job.data, { resume: job.progress });
  return uploadArtifact(rows, { watermark: job.userId, ttl: '24h' });
}));
```
