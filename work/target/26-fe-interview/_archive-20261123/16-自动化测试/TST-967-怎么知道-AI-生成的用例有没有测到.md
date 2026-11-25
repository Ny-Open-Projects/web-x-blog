---
title: [TST-967] 怎么知道 AI 生成的用例有没有测到「新东西」？如何度量覆盖率贡献？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-967：怎么知道 AI 生成的用例有没有测到「新东西」？如何度量覆盖率贡献？
**答**：
- 结论：用「增量覆盖率贡献」——对比加入 AI 用例前后的分支/行覆盖差，只看它是否触达了人工用例未覆盖的路径。
- 做法：分别采集 only-human 与 human+AI 的覆盖率，diff 出 AI 新增覆盖的行/分支数；贡献为 0 的 AI 用例视为冗余。
- 注意：覆盖率贡献高不等于价值高（可能测的是无关分支），需结合断言有效性一起看。
- 追问钩子：AI 用例让覆盖率涨了 10%，但变异测试分数没变，这说明什么？

```javascript
function coverageContribution(humanCov, withAICov) {
  const added = [...withAICov].filter(x => !humanCov.has(x));
  return {
    addedLines: added.length,
    addedBranches: added.filter(x => x.includes('branch')).length,
    contribution: +(added.length / (withAICov.size || 1)).toFixed(2),
  };
}
const human = new Set(['src/a.js:10', 'src/a.js:20']);
const withAI = new Set(['src/a.js:10', 'src/a.js:20', 'src/a.js:35:branch-true']);
console.log(coverageContribution(human, withAI));
// { addedLines:1, addedBranches:1, contribution:0.33 }
// 若 mutation score 未变 → 新增覆盖未真正验证行为，需加强断言
```
