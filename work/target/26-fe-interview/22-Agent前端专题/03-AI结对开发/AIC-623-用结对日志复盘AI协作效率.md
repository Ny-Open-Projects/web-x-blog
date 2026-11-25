---
title: [AIC-623] 怎么用「结对日志」复盘 AI 协作效率？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-623：怎么用「结对日志」复盘 AI 协作效率？

**答**：
- 结论先行：**没有日志的「感觉高效」是不可靠的**。结对日志把 AI 协作从「凭感觉」变成「可复盘的数据」，核心记录四类事件：任务开始/结束、AI 生成、人工干预、回滚。
- 记录什么：1) **时间**：任务起止、AI 响应时长、人工审查时长（AIC-142 ROI 价值链）；2) **产出**：生成代码行数、接受/修改/丢弃比例（AIC-516 接受率）；3) **干预**：人工介入次数与原因（幻觉/上下文不足/风格不符）；4) **结果**：7 天存活率（AIC-074）、是否返工。
- 复盘指标：1) **接受率**（直接采纳 / 总生成）——衡量 AI 产出质量；2) **干预率**（干预次数 / 轮数）——衡量 prompt 质量；3) **存活率**（7 天后仍未被改的代码比例）——衡量真实价值；4) **迭代收敛速度**（到达可验收的轮数）——衡量协作效率。
- 复盘节奏：每周看趋势而非单日波动，重点分析「低接受率任务」——是任务不适合 AI、prompt 没写好、还是上下文不足？针对性改进。
- 追问钩子：为什么「7 天存活率」比「一次通过率」更能反映协作效率？——因为一次通过可能是「看起来对但没人敢用」，7 天后仍存活说明代码真的融入了系统、经得起后续变更；存活率是「延迟满足」的真实价值指标。

```typescript
type Event = { t: number; kind: 'task'|'gen'|'intervene'|'rollback'; meta?: any };

function summarizePairLog(events: Event[]) {
  const gens = events.filter(e => e.kind === 'gen');
  const accepted = gens.filter(e => e.meta?.accepted).length;
  const interventions = events.filter(e => e.kind === 'intervene').length;
  const rollbacks = events.filter(e => e.kind === 'rollback').length;
  const tasks = events.filter(e => e.kind === 'task');
  const totalMs = tasks.length ? tasks[tasks.length - 1].t - tasks[0].t : 0;
  return {
    acceptanceRate: gens.length ? accepted / gens.length : 0,
    interventionRate: gens.length ? interventions / gens.length : 0,
    rollbackCount: rollbacks,
    avgTaskMs: tasks.length ? totalMs / Math.max(1, tasks.length - 1) : 0,
  };
}

const events: Event[] = [
  { t: 0, kind: 'task' },
  { t: 1000, kind: 'gen', meta: { accepted: true } },
  { t: 2000, kind: 'gen', meta: { accepted: false } },
  { t: 3000, kind: 'intervene', meta: { reason: 'hallucination' } },
  { t: 9000, kind: 'task' },
];
const s = summarizePairLog(events);
console.log(s.acceptanceRate === 0.5);
console.log(s.interventionRate === 0.5);
```
