---
title: [NODE-714] 数据导出与报表服务怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-714：报表服务怎么做？
**答**：
- 异步任务化：大报表异步生成（任务队列 + 进度——SCN-FIN-512 导出任务化）；生成完成通知（IM/站内——SCN-OPS-612）。
- 报表数据源：OLAP 化（报表走数仓/读模型——不压 OLTP 主库，SCN-NODE-713 投影联动）；准实时报表的 CDC（binlog → 投影——延迟可控）。
- 权限与口径：行级权限（数据权限过滤进导出——SCN-OPS-609 矩阵）、口径版本化（报表口径变更留痕——SCN-SLA-710 口径治理）、水印与审计（导出留痕——谁导出了什么）。
- 性能：流式生成（SCN-NODE-681 流式——内存守恒）、缓存（同参数报表短 TTL——重复导出去重）。
- 追问钩子：为什么报表必须走「读模型/数仓」而不是直接查主库——报表查询是重查询（全表聚合——行锁/IO 大），压主库会让 OLTP 交易抖动（报表拖垮交易——经典事故）；读模型（异步投影）隔离负载——负载隔离是报表服务的架构前提，不是优化项。

```javascript
// 异步报表任务
async function reportTask(params, user) {
  const taskId = createTask(params);                   // 任务化
  queue.add('report', { params, user, taskId });       // 队列执行
  return { taskId };
}
worker.on('report', async (job) => {
  const stream = await olap.queryStream(job.params);   // 读模型/数仓
  const file = await streamToExcel(stream, job.params.columns);
  await notifyDone(job.user, signUrl(file));           // 签名直链通知
  auditExport(job.user, job.params);                   // 导出审计
});
```
