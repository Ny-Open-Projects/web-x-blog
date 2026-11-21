---
title: [NODE-630] Node 服务的异步任务幂等与断点续跑（任务可靠性闭环）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-630：任务幂等与断点续跑
**答**:
- 可靠性三支柱：幂等（任务重跑安全——输入快照 + 操作幂等键 ARC-481）、断点（进度持久化——checkpoint：已完成批次记录，续跑从断点 NODE-583）、对账（任务产物 vs 输入的对账——完成度验证）。
- 断点设计：checkpoint 粒度（批次/文件/分页——自然断点：事务边界处存）、恢复语义（从 checkpoint 继续 vs 从头重跑（幂等下等价）——按幂等强度选）、跨实例恢复（实例崩溃 → 任务重新调度到其他实例——断点在共享存储（任务表/Redis））。
- 幂等实现：任务输入快照（参数版本化——重跑输入一致）、操作幂等键（任务 ID + 步骤 + 批次——派生键 NODE-476）、产物幂等（产物存在即跳过——hash 校验）。
- 失败分类处理：瞬时（重试）、确定性（死信）、资源类（限流等待）——分类重试策略 NODE-391。
- 观测：断点续跑率/重跑成本（幂等下重跑的浪费度量）、任务完成度对账差异。
```javascript
// 断点续跑框架
async function run(job) {
  const cp = await checkpoint.load(job.id);                      // { doneBatches }
  for (const [i, batch] of batches.entries()) {
    if (i < cp.done) continue;                                   // 断点跳过
    await process(batch, { idemKey: `${job.id}:${i}` });         // 派生幂等键
    await checkpoint.save(job.id, { done: i + 1 });              // 每批保存
  }
  await verify(job);                                             // 产物对账
}
```
