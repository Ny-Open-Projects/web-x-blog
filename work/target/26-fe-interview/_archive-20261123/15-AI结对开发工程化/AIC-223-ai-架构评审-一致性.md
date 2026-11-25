---
title: [AIC-223] 新代码与仓库既有模式不一致（比如 90% 的页面用 Server Actions，新代码却在手写 API route），AI 如何帮忙发现？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-223：新代码与仓库既有模式不一致（比如 90% 的页面用 Server Actions，新代码却在手写 API route），AI 如何帮忙发现？
**答**：
- 让 AI 先统计仓库既有模式（抽样归纳），再对照新变更给出偏离度报告。
- 把「主流模式」写成事实基线而非规范：AI 报告偏离时不带对错判断，留给人类决定是演进还是纠偏。
- 输出要含证据：同类文件举例（路径 + 行号），避免 AI 空口断言。
- 偏离度进趋势：新模式采纳率本身就是架构演进的观测指标。

```javascript
async function patternDeviation(changedFiles: string[]) {
  const baseline = await sampleExistingPatterns('src/pages'); // 抽样归纳
  const report = await llm(`既有模式：${JSON.stringify(baseline)}
变更文件：${changedFiles}。找出与主流模式的偏离点，每条附同类对照文件路径。`);
  return report; // [{ file, deviation, mainstreamExample }]
}
r
```
