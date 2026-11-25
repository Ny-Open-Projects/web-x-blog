---
title: [TST-766] 混沌实验的「自愈」如何验证：AI 判定 vs 确定性断言
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-766：混沌实验的「自愈」如何验证：AI 判定 vs 确定性断言

**答**：
- 结论：自愈验证要「确定性断言为主，AI 为辅」——恢复时间、错误率回落等硬指标用断言，AI 只判断「是否真正恢复到正确状态」这类模糊语义。
- 确定性断言可重复、可审计，是门禁依据；AI 判定用于辅助发现「指标恢复但业务语义错误」的情况。
- AI 判定要给出置信度与依据，低置信度转人工，不能直接判实验成功。
- 追问钩子：指标全绿但 AI 判定「未恢复」，信谁？

```javascript
// 自愈验证：硬断言 + AI 语义判定
function verifyRecovery({ errorRate, recoveredMs, sloMs, aiSemanticOk }) {
  const hardOk = errorRate < 0.01 && recoveredMs <= sloMs;
  return {
    hardOk,
    semanticOk: aiSemanticOk,
    passed: hardOk && aiSemanticOk !== false, // AI 明确否定则否决
  };
}
console.log(verifyRecovery({ errorRate: 0.005, recoveredMs: 800, sloMs: 1000, aiSemanticOk: false }));
// passed:false，AI 否决
```
