---
title: [TST-619] AI 时代测试架构师的角色会发生什么变化？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-619：AI 时代测试架构师的角色会发生什么变化？

**答**：
- 结论：从「写测试的人」转向「定义质量标准与守卫机制的人」——AI 负责产量，架构师负责判据。
- 被放大：质量策略设计、AI 产出验证、风险建模；被弱化：样板用例编写、机械维护。
- 新增职责：AI 生成物的可信度评级、测试知识库治理、人机协作的门禁设计。
- 追问钩子：AI 一天生成 1000 个用例，你怎么防止「测试通胀」掩盖真实风险？

```javascript
function trustGate(generated, { maxFlakyRate = 0.05, minMutation = 0.6 } = {}) {
  return generated.filter(t => {
    const ok = t.flakyRate <= maxFlakyRate && t.mutationScore >= minMutation;
    if (!ok) t.reason = t.flakyRate > maxFlakyRate ? 'flaky' : 'weak-assert';
    return ok;
  });
}
console.log(trustGate([{ id: 1, flakyRate: 0.01, mutationScore: 0.8 }]).length);
```
