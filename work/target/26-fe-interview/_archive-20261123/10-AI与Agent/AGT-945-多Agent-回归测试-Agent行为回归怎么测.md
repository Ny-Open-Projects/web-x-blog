---
title: [945] Agent 改了 prompt 之后，怎么防止其他场景回退
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 回归]
type: 面试题
---

## 945：Agent 改了 prompt 之后，怎么防止其他场景回退

**答**：
- prompt 即代码：任何 prompt 改动必须过回归集（场景 × 断言），断言含「结果断言」（答案正确）与「行为断言」（工具调用序列、拒答边界）。
- 行为断言更容易抓坏：比如修复「过度拒答」后，回归集里「该拒答的题仍然拒答」这组断言守住另一侧边界。
- 快慢双轨：快速轨（200 条核心，5 分钟，每次提交跑）+ 慢速轨（全量 + LLM-as-judge，夜间跑），平衡反馈速度与覆盖。
- 快照对比：同一输入新旧 prompt 各跑一遍 diff 输出，人只审「变化的部分」，比全量人审省 10 倍工时。
- 追问钩子：LLM 输出不确定怎么做快照 diff？——断言「结构 + 关键事实」而非逐字，温度调 0 也只是降低不是消除波动。

```ts
const regressions = loadCases('regressions/');
for (const c of regressions) {
  const out = await agent.run(c.input);
  assert(out[c.resultKey], c.expect, c.id);          // 结果断言
  assertSeq(out.toolCalls, c.toolSeq, c.id);          // 行为断言：调用序列
}
// 快慢双轨在 CI 里按触发条件选择
const track = process.env.CI_NIGHT ? 'full' : 'core';
```

