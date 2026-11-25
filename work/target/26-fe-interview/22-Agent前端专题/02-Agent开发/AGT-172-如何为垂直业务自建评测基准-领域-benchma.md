---
title: [AGT-172] 如何为垂直业务自建评测基准（领域 benchmark）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-172：如何为垂直业务自建评测基准（领域 benchmark）？
**答**：
- 自建基准的四类题目配比：真实分布题（线上抽样，最代表性）、边界题（人工设计的难例/易混淆例）、对抗题（注入/诱导，来自红队积累）、回归题（每次线上事故沉淀一题——事故永远会复发，基准要能接住）。
- 评分器分层：可程序判分（SQL 可执行且结果一致、代码过测试）优先；规则判分（关键词/引用存在性）次之；LLM judge 打分（配 rubric 与双 judge 一致性校验）兜底。
- 防污染与防过拟合：评测集与训练集来源隔离、评测题哈希入黑名单禁止出现在 few-shot/prompt、定期换血（保留金丝雀题监测 judge 漂移）。
- 运营指标：基准与线上负反馈的相关性是唯一有效性证明——每月校准一次，相关性掉了说明基准脱离真实分布，要重新采样。

```typescript
// 领域基准：题目分层 + 分层判分 + 相关性校准
import { z } from 'zod';

const Case = z.object({
  id: z.string(), tier: z.enum(['online', 'edge', 'adversarial', 'regression']),
  input: z.string(), expectation: z.unknown(),
  scorer: z.enum(['program', 'rule', 'judge']), rubric: z.string().optional(),
  incidentRef: z.string().nullable().default(null),          // 回归题关联线上事故
});
type Case = z.infer<typeof Case>;

export async function runBenchmark(model: string, cases: Case[]) {
  const results = [];
  for (const c of cases) {
    const output = await callModel(model, c.input);
    const score = c.scorer === 'program' ? await programScore(output, c.expectation)
      : c.scorer === 'rule' ? ruleScore(output, c.expectation)
      : await judgeScore(output, c.input, c.rubric!);
    results.push({ id: c.id, tier: c.tier, score });
  }
  const byTier = groupAvg(results);                          // 分层报告：对抗题与回归题单独看
  if ((byTier.regression ?? 1) < 0.95) alert('历史事故回归题出现退步');
  return { byTier, results };
}

// 有效性校准：基准分与线上负反馈率的相关性
export async function calibrateBenchmark(benchmarkRuns: { version: string; score: number }[], prod: Map<string, number>) {
  const xs = benchmarkRuns.map((r) => r.score), ys = benchmarkRuns.map((r) => prod.get(r.version) ?? 0);
  const corr = pearson(xs, ys);
  if (corr > -0.6) alert(`基准与线上负反馈相关性弱（r=${corr.toFixed(2)}），需重新采样真实分布`); // 分数高应负反馈低
  return corr;
}
async function callModel(m: string, i: string) { void m; void i; return ''; }
async function programScore(o: unknown, e: unknown) { void o; void e; return 1; }
function ruleScore(o: unknown, e: unknown) { void o; void e; return 1; }
async function judgeScore(o: string, i: string, rubric: string) { void o; void i; void rubric; return 0.9; }
function groupAvg(rs: { tier: string; score: number }[]) {
  return Object.fromEntries([...new Set(rs.map((r) => r.tier))].map((t) => [t, rs.filter((r) => r.tier === t).reduce((s, r) => s + r.score, 0) / rs.filter((r) => r.tier === t).length]));
}
function pearson(xs: number[], ys: number[]) { void xs; void ys; return -0.8; }
const alert = (m: string) => console.error(m);
```
