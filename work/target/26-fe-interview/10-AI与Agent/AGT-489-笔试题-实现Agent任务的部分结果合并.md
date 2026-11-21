---
title: [AGT-489] 笔试题——实现部分结果合并（超时/失败后聚合已完成部分+缺口标注）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-489：手写部分结果聚合：成功项合并、失败项标注、缺口对最终答案的影响声明

**需求与边界**：
- 输入：子任务结果集（done/failed/skipped）、聚合函数；输出：部分结果+缺口声明。
- 边界要求：① 成功项正常聚合；② 失败项不静默（缺口清单进最终答案）；③ 缺口对结论的影响分级（关键缺口→降级声明；边缘缺口→脚注）；④ 可续跑入口（补齐失败项后增量合并）。

**答**：
```javascript
async function mergePartial(results, { aggregate, criticalityOf }) {
  const done = results.filter(r => r.status === 'done');
  const failed = results.filter(r => r.status !== 'done');
  // 1. 成功项聚合
  const answer = await aggregate(done.map(r => r.value));
  // 2. 缺口分级
  const gaps = failed.map(f => ({
    task: f.taskId, reason: f.reason,
    critical: criticalityOf(f.taskId),   // 关键/边缘
  }));
  const criticalGaps = gaps.filter(g => g.critical);
  // 3. 缺口对结论的影响声明
  const impact = criticalGaps.length
    ? { level: 'degraded',
        note: `以下关键信息缺失，结论可能不完整：${criticalGaps
          .map(g => g.task).join('、')}`,
        position: 'header' }             // 头部显著声明
    : gaps.length
      ? { level: 'minor',
          note: `部分次要信息未获取：${gaps.map(g => g.task).join('、')}`,
          position: 'footnote' };
  return {
    answer,
    gaps,
    impact,
    resume: {                             // 可续跑入口
      failed: failed.map(f => f.taskId),
      action: '重试失败项后增量合并（不重跑成功项）' },
  };
}
// 增量合并：resume 时只跑 failed 项，
// 新结果与 done 项重新 aggregate。
```

**评分点**:
- 成功项聚合+失败项缺口清单，不静默不编造。
- 缺口分级影响声明：关键缺口头部降级声明、边缘缺口脚注。
- 续跑入口增量合并（不重跑成功项——成本意识）。
- criticalityOf 外部化（关键性由任务定义而非硬编码）。
