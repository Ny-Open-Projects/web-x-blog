---
title: [AIC-262] 高峰期多个 PR 抢 CI 资源，AI 如何做合并调度（merge queue 优化）？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-262：高峰期多个 PR 抢 CI 资源，AI 如何做合并调度（merge queue 优化）？
**答**：
- 按风险排序：低风险小 PR 优先过队列（快速周转），高风险大 PR 集中资源深验。
- 预测验证范围：AI 按 diff 预测「最小必要验证集」（受影响测试子集），缩短排队时间。
- 冲突预测：PR 间文件重叠预测，有冲突的串行合并避免二次排队。
- 全量兜底：合并前最终态仍跑全量门禁——提速不降标准。

```javascript
function mergeQueue(prs: PR[]) {
  const sorted = prs.sort(byRiskAndAge);
  for (const p of sorted) {
    p.verifySet = predictAffectedTests(p);      // 最小验证集
    p.conflictWith = prs.filter(q => overlap(p.files, q.files) > 0.3);
  }
  return { finalGate: '全量验证不变', fastLane: sorted.filter(p => p.risk === 'low') };
}
r
```
