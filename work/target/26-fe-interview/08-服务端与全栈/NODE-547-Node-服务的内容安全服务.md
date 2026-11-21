---
title: [NODE-547] Node 服务的内容安全（机审接入/人审队列）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-547：内容安全服务
**答**:
- 机审链路：内容接入（发布事件 → 机审任务）→ 审核引擎（文本/图片/视频——供应商 API + 自研规则叠加 NODE-425 多供应商路由）→ 决策（通过/拒绝/疑似——疑似进人审）。
- 人审队列：优先级队列（风险分级：疑似高风险先审——队列策略）、审核工作台协议（内容 + 上下文 + 历史记录 + 快捷操作）、审核时效（队列积压告警——时效 SLA）、审核一致性（抽查复核——审核质量指标）。
- 决策应用：状态机联动（ARC-608 审核状态流——机审通过自动放行/疑似挂起）、申诉回流（用户申诉 → 复审队列 + 误判反馈——审核引擎迭代数据）。
- 性能与顺序：发布时同步 or 异步审（同步：首屏延迟高——异步先挂"审核中"ARC-608；高风控内容同步预审——分级）、批量内容（批量上传——批量审核任务）。
- 治理：审核规则版本化（规则变更审计——误杀率变化归因）、供应商切换演练（机审供应商故障的降级：全量人审或延迟发布）。
```javascript
// 机审编排
async function moderate(content) {
  const r = await Promise.race([
    vendors.best().check(content), timeout(2000)]);
  if (r.verdict === 'pass') return publish(content);             // 直接过
  if (r.verdict === 'reject') return reject(content, r.reason);
  await humanQueue.push({ content, priority: r.risk });          // 疑似进人审
  return publish(content, { state: 'pending-review' });
}
```
