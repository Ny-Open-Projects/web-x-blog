---
title: [NODE-427] Node 服务依赖图与服务画像（自动化生成）如何建设？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-427：服务依赖图与服务画像
**答**:
- 依赖图自动生成：从 trace 的 span 父子关系聚合（caller → callee 边 + QPS/P99/错误率标注），定时（小时级）重算——文档手画的依赖图必然过时，trace 是事实源。
- 服务画像卡：每个服务一页（owner/SLA/依赖/被依赖/容量水位/最近事故/仓库与 Runbook 链接），从多源数据自动聚合（trace/指标/发布记录/oncall 工单）。
- 影响面分析：改服务 X 前查"谁依赖 X"（下游清单 + 各依赖方的关键程度）——变更评审（ARC-187）自动生成影响面附件。
- 治理应用：孤岛服务识别（无人依赖且无流量的服务 → 下线评估）、环依赖检测（调用环告警）、单点依赖（某服务被 20 个服务依赖 → 它的变更要冻结期）。
- 与架构评审联动：新服务立项自动挂到依赖图（服务注册表：新建服务必须登记 owner/分级/依赖声明）。
```javascript
// 从 trace 聚合依赖边
async function buildDepGraph(window = '1h') {
  const edges = await traceAgg.groupBy(['caller.service', 'callee.service'], {
    metrics: { qps: count, p99: p99(duration), err: rate(status >= 500) } });
  return { edges: edges.filter(e => e.qps > 0.1),              // 过滤噪音边
           critical: edges.filter(e => e.err > 0.01 || e.p99 > 500) };
}
// 画像：{ svc, owner, tier, deps, dependents, sla, lastIncident, runbook }
```
