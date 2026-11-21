---
title: [AGT-239] 多 Agent 结果聚合——多个子 Agent 结论冲突怎么处理？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-239：并行子 Agent 返回的结论冲突时，聚合层怎么处理？

**答**:
- 聚合前先结构化对齐：把各子结果映射到统一 schema（结论/依据/置信度/覆盖范围），冲突检测才有抓手——自由文本聚合是冲突不可见的第一原因。
- 冲突处置阶梯：证据可判（一方有硬数据另一方没有→按证据强度）→ 置信度加权（都有依据→按专业领域分工加权，如安全域信安全 Agent）→ 升级仲裁（仍冲突→追加"验证子任务"复查关键分歧点，或人审）。
- 冲突不掩盖：聚合结果中保留"已解决的冲突"记录（哪两方冲突、怎么裁的、依据）——下游与用户有权知道结论的确定性程度；不可判定时输出"存在分歧+各方观点"而不是强行拍板。
- 预防优于解决：冲突多数源于子任务边界重叠（两个 Agent 各答一半）或信息不同步——分解阶段明确各自范围与共享事实（AGT-232），能消除大半冲突。

```javascript
function aggregate(results) {
  const aligned = results.map(toSchema);        // 结构化对齐
  const conflicts = detectConflicts(aligned);   // 按字段比对
  const resolved = conflicts.map(c =>
    byEvidence(c) || byDomainWeight(c)
    || escalate(c));                            // 阶梯处置
  return {
    conclusion: merge(aligned, resolved),
    audit: resolved.map(c => ({                 // 冲突留痕
      between: [c.a.agent, c.b.agent],
      resolution: c.how, basis: c.basis })),
  };
}
```
