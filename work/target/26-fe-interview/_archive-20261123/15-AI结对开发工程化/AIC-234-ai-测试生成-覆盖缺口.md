---
title: [AIC-234] 如何让 AI 针对「覆盖率盲区」定向生成测试而不是重复生成已有用例？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-234：如何让 AI 针对「覆盖率盲区」定向生成测试而不是重复生成已有用例？
**答**：
- 输入覆盖报告的未覆盖行/分支数据，让 AI 按「未覆盖分支清单」逐条出用例。
- 提供既有测试文件，明确要求不重复既有场景。
- 对分支级覆盖（branch coverage）而非行级：AI 更容易理解分支语义。
- 生成后复跑覆盖验证增量，未提升的用例判为无效并删除。

```javascript
async function fillCoverageGaps(srcFile: string) {
  const cov = await coverage(srcFile);            // istanbul/v8 数据
  const gaps = cov.uncoveredBranches;             // 分支级缺口
  const existing = readTestFile(srcFile);
  const tests = await llm(`未覆盖分支：${JSON.stringify(gaps)}
既有用例（不得重复）：${existing}
只为这些缺口生成用例。`);
  const delta = await rerunCoverage(srcFile, tests);
  return delta.newBranchCovered > 0 ? tests : null; // 无效即弃
}
r
```
