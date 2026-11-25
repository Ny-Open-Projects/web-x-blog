---
title: [AGT-093] 回归评测流水线怎么搭（prompt 改动自动跑评测集）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-093：回归评测流水线怎么搭（prompt 改动自动跑评测集）？
**答**：
- prompt/模型/参数任何改动都自动跑评测：PR 级 CI job 出对比报告，通过率下降超阈值即阻断合并。
- 基线管理：main 分支定期跑并落基线文件；PR 结果与基线 diff，明确列出哪些用例变好/变坏。
- 成本控制：分级执行（PR 跑 20 条冒烟集、nightly 跑全量）、结果缓存（相同输入 hash 复用）、并发限流。
- 报告落到 PR comment：让改 prompt 的人看到具体用例的输出变化，而不只是一个通过率数字。

```yaml
# .github/workflows/eval.yml —— prompt 改动触发回归评测
name: eval-regression
on:
  pull_request:
    paths:
      - 'prompts/**'
      - 'evals/**'
jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
      - run: npm run eval -- --suite smoke --baseline main   # 冒烟集 20 条，快速反馈
      - run: npm run eval:report                             # 生成报告并发布 PR comment
```

```typescript
import { z } from 'zod';

// 对比基线，超阈值阻断
interface EvalResult { caseId: string; pass: boolean }

export async function compareWithBaseline(current: EvalResult[], baseline: EvalResult[]) {
  const base = new Map(baseline.map((r) => [r.caseId, r]));
  const regressions = current.filter((r) => {
    const b = base.get(r.caseId);
    return b?.pass && !r.pass;                               // 基线通过、本次失败 = 回归
  }).map((r) => r.caseId);
  const rate = (rs: EvalResult[]) => rs.filter((r) => r.pass).length / rs.length;
  const passRate = rate(current), baseRate = rate(baseline);
  const report = { passRate, baseRate, regressions };
  if (passRate < baseRate - 0.02) {                          // 允许 2% 波动
    throw new Error(`评测回归：${(baseRate * 100).toFixed(1)}% -> ${(passRate * 100).toFixed(1)}%，阻断合并`);
  }
  return report;
}
```
