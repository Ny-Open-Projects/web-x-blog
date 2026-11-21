---
title: [AGT-064] 反思循环（Reflection）如何实现？收敛条件怎么定？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-064：反思循环（Reflection）如何实现？收敛条件怎么定？
**答**：
- 反思 = 在「生成 → 评审 → 修订」环上跑：让模型以评审者身份对照需求清单挑毛病，产出可执行的修订意见。
- 评审必须给维度清单（完整性/事实性/格式）与输出 schema（pass + issues 列表），「再检查一遍」式提示没有效果。
- 收敛条件三选一：评审通过、达到最大轮数、两轮产出差异极小（防抖动震荡）。
- 成本高（每轮 2 次调用），只用于高质量产出场景（报告、代码、对外文案）。

```typescript
import { z } from 'zod';

const RUBRIC = `评审以下产出，逐项检查：
1. 是否覆盖了任务要求的全部要点
2. 是否存在事实或计算错误
3. 是否符合要求的输出格式
输出 JSON：{"pass": boolean, "issues": ["具体问题与修改建议"]}`;

export async function generateWithReflection(goal: string, maxRounds = 2): Promise<string> {
  let draft = await chatOnce([{ role: 'user', content: goal }]);
  for (let i = 0; i < maxRounds; i++) {
    const review = await structuredLLM(
      [{ role: 'user', content: `${RUBRIC}\n\n任务：${goal}\n\n产出：\n${draft}` }],
      z.object({ pass: z.boolean(), issues: z.array(z.string()) }),
    );
    if (review.pass) return draft;
    draft = await chatOnce([
      { role: 'user', content: goal },
      { role: 'assistant', content: draft },
      { role: 'user', content: `评审意见：\n${review.issues.map((s, j) => `${j + 1}. ${s}`).join('\n')}\n请逐条修订后输出完整新版本。` },
    ]);
  }
  return draft; // 达到上限仍带问题：返回并标记低置信，交人工复核
}
```
