---
title: [NODE-628] Node 服务的异步任务取消与超时（进行中任务的取消协议）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-628：异步任务取消与超时
**答**:
- 取消协议：任务可取消声明（任务类型声明可取消性——已开始的部分可逆（批处理：已处理批次保留））、取消请求（任务中心发起 → 取消信号到 worker（标志位/AbortSignal——任务内部协作式检查））、取消语义（部分完成状态：completed N/M——产物按需保留或回滚）。
- 超时协议：任务级超时（总时长超限——软超时告警/硬超时强杀）、步骤超时（单步超时——重试或跳过策略）、超时后的清理（资源释放/状态标记——不悬挂 NODE-581）。
- 实现：协作式取消（任务代码定期检查 cancel 信号——process.on / AbortSignal——外部强杀不可靠）、取消传播（任务内下游调用带 signal——级联取消 NODE-422）、取消幂等（重复取消/取消已完成任务——幂等语义）。
- 边界：不可取消段（事务中途——完成事务再取消——取消点设计在事务边界）、产物清理（取消后产物删除策略）。
- 观测：取消成功率/取消延迟（请求到实际停止——协作式检查粒度）、超时率（任务配置合理性）。
```javascript
// 协作式取消
async function runTask(job, signal) {
  for (const batch of batches) {
    if (signal.aborted) { await markPartiallyDone(job, { done: batch.index }); return 'cancelled'; }
    await processBatch(batch, { signal });                       // 内部调用也传 signal
  }
}
// 取消入口：taskCenter.cancel(taskId) → signal.dispatch → 任务检查点响应
```
