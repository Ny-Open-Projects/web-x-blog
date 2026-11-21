---
title: [AIC-254] PR 自动评审如何做风险分级，让不同风险走不同流程？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-254：PR 自动评审如何做风险分级，让不同风险走不同流程？
**答**：
- 风险特征输入：diff 规模、涉及模块（核心/边缘）、测试覆盖变化、是否动配置/依赖。
- 分级输出：低风险自动通过（附摘要）、中风险正常评审、高风险加人 + AI 深审报告。
- 分级要可解释：给出每个因子的贡献，避免黑盒分级引发争议。
- 高风险定义校准：定期回看「漏网的高风险 PR」和「被误判高风险的低风险 PR」。

```javascript
function riskScore(pr: PR) {
  const s =
    pr.lines > 500 ? 3 : pr.lines > 100 ? 1 : 0 +
    (touchesCore(pr.files) ? 4 : 0) +
    (touchesDepsOrConfig(pr.files) ? 3 : 0) +
    (pr.coverDelta < 0 ? 2 : 0);
  return { score: s, level: s >= 6 ? 'high' : s >= 3 ? 'mid' : 'low',
           factors: explain(pr) };
}
r
```
