---
title: [NODE-460] Node 服务的容灾切换（自动化决策与执行）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-460：容灾切换自动化
**答**:
- 切换决策分级：自动切换（明确故障：健康检查全挂 + 副单元健康——秒级）、半自动（可疑故障：部分异常——系统建议 + 人工确认）、人工（区域性决策：切流影响大——预案评审后执行）。
- 切换编排：切流（DNS/网关层流量调度）→ 数据补偿（切流前 diff 补偿同步 NODE-459）→ 依赖检查（备单元依赖服务容量/状态确认）→ 验证（切后核心链路拨测）→ 公告。
- 一键预案：预案剧本化（NODE-429 Runbook 平台扩展为可执行剧本：预检 → 执行步骤 → 每步验证 → 失败自动回切），值班可一键执行（权限 + 双人确认高危）。
- 切回策略：故障单元恢复后的回切（回切也要走预案——数据反向补偿 + 灰度回切，防"恢复即事故"）。
- 演练与度量：季度真实切换演练（ARC-459）、切换耗时（MTTR 指标）、演练发现的问题闭环。
```javascript
// 切换剧本
const failoverPlaybook = playbook('unit-a-down', [
  { step: 'precheck', run: checkBackupHealth, gate: true },      // 备单元健康才继续
  { step: 'drain-sync', run: () => reconcile.diff('unit-a', 'unit-b') }, // 数据补偿
  { step: 'switch', run: () => gateway.routeUnits('unit-a', 'unit-b'), confirm: 'double' },
  { step: 'verify', run: probeCoreFlows, onFail: 'auto-rollback' },
  { step: 'notify', run: () => broadcast('已切至 unit-b') }
]);
```
