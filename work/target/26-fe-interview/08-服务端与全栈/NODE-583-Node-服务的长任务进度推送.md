---
title: [NODE-583] Node 服务的长任务进度推送（实时进度协议）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-583：长任务进度推送
**答**:
- 进度协议：任务进度事件（done/total/stage/eta——阶段化进度：解析 30% → 校验 20% → 写入 50%）、进度持久化（任务表进度字段——断线重连可查）、推送（WS/SSE 订阅 taskId——NODE-416/347）。
- 进度语义：真实进度 vs 阶段进度（总行数已知按行、未知按阶段权重——ETA 计算方式声明）、进度节流（高频更新合并——1s 一次推送防消息洪泛）、倒退防护（重试导致进度回退——单调性约束或重置语义声明）。
- 完成/失败推送：终态事件（成功产物链接/失败原因——任务中心消费 ARC-576）、多端同步（其他端任务状态同步 ARC-500）。
- 容错：推送链路挂 → 轮询兜底（任务状态接口——双通道 ARC-416 降级链）、进度丢失（checkpoint 恢复——从断点继续进度）。
- 观测：进度推送延迟/ETA 准确度（预估 vs 实际——ETA 算法校准数据）。
```javascript
// 进度推送
worker.on('progress', throttle(async (p) => {
  await taskRepo.setProgress(jobId, p);                          // 持久化（可查可恢复）
  await publish(`task:${jobId}`, { ...p, eta: calcEta(p) });    // 推送订阅者
}, 1000));
```
