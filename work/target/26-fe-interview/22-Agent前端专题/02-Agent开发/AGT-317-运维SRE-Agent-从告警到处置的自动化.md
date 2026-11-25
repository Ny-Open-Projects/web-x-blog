---
title: [AGT-317] 运维 SRE Agent——告警诊断与处置自动化的边界？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-317：SRE Agent（告警聚合→根因分析→处置建议）怎么设计？

**答**:
- 管线：告警聚合降噪（风暴去重、关联聚合——一次故障的 500 条告警聚成 3 个事件）、根因假设（基于拓扑/变更关联/历史相似故障的 RAG+推理，输出"假设+证据链"而非唯一结论）、处置建议（Runbook 检索匹配+操作建议分级）。
- 自动化边界：只读诊断全自动（查指标/日志/trace）；变更类操作（重启/扩容/回滚）人审或 Runbook 预授权（白名单内自动+外白名单人审，AGT-286）；涉及资金的交易相关操作永不自动。
- 假设呈现：根因分析输出"假设列表+各假设证据+验证方法"而不是单结论——运维场景过度自信的单一结论会误导处置；验证类操作（灰度观察）优先于变更类操作。
- 学习闭环：每次故障的"假设→实际根因"对比入知识库（诊断准确率持续提升）；误诊断样本进评测集（AGT-257）。

```javascript
async function sreDiagnose(incident) {
  const events = aggregateAlerts(incident);       // 聚合降噪
  const hyps = await rootCause(events, {          // 假设+证据链
    topology, recentChanges, similarCases: rag(incident) });
  return hyps.map(h => ({
    ...h, action: runbookMatch(h),                // 处置建议分级
    auto: RUNBOOK_WHITELIST.includes(h.action),   // 白名单自动
  }));
  // 变更操作默认人审；验证类优先于变更类。
}
```
