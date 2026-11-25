---
title: [NODE-407] Node 服务的故障复盘与 SOP 沉淀如何运作？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-407：故障复盘与 SOP 沉淀
**答**:
- 无责复盘（blameless）：聚焦"系统为什么允许这个故障发生"而不是"谁改坏的"；时间线还原（告警时间/响应时间/止血动作/恢复时间，从日志与值班记录自动生成初稿）。
- 复盘产出三件：根因链（直接原因 → 深层原因 → 流程缺陷）、改进项（每项有 owner/优先级/验收标准，进跟踪看板防烂尾）、知识沉淀（Runbook 更新：这类故障怎么发现/怎么止血）。
- 指标复盘：MTTD（发现时长）/MTTR（恢复时长）趋势；改进项完成率；同类故障重复率（重复发生说明改进项没落地）。
- SOP 沉淀机制：复盘中的手动操作步骤固化为 Runbook（值班可执行）；高频手动操作自动化（脚本化/平台化）。
- 文化配套：复盘会议 48h 内开（记忆新鲜）、改善项兑现率公开（信任基础）、故障案例进新人培训（ARC-391）。
```javascript
// 复盘文档骨架
const postmortem = {
  timeline: 'auto from alerts & logs',
  rootCause: { direct: '连接池耗尽', deep: '慢查询占连接未超时', process: '无 statement_timeout 规范' },
  actionItems: [ ['DB 强制 statement_timeout=3s', 'DBA', 'P0', '配置校验进 CI'] ],
  runbookUpdates: ['api/5xx → 检查连接池等待数 → 杀慢查询 SOP'],
  metrics: { mttr: '42min', repeatRisk: '已闭环（timeout+监控）' }
};
```
