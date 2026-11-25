---
title: [TST-976] 笔试：手写「AI 用例可靠性分级器」，综合多指标输出等级与门禁策略
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-976：笔试：手写「AI 用例可靠性分级器」，综合多指标输出等级与门禁策略
**答**：
- 需求：实现 gradeUseCase(metrics, thresholds)，metrics = { flakeRate, validity, survival, mutationScore }。
- 规则：L1 需四项全部优于严格阈值；L2 需 flakeRate/validity 达标；L3 只需 flakeRate 可接受；否则 L4。输出 { level, policy, reasons }。
- 边界：任一指标缺失降级处理（按 L4 + reason）；threshold 缺省用内置默认值。

```javascript
function gradeUseCase(m, t = {}) {
  const d = { flake: 0.01, validity: 0.95, survival: 0.9, mutation: 0.6,
    l2Flake: 0.03, l2Validity: 0.85, l3Flake: 0.08, ...t };
  const missing = ['flakeRate','validity','survival','mutationScore'].filter(k => m[k] == null);
  if (missing.length) return { level: 4, policy: '隔离观察', reasons: missing.map(k => `缺失 ${k}`) };
  const reasons = [];
  const l1 = m.flakeRate <= d.flake && m.validity >= d.validity &&
    m.survival >= d.survival && m.mutationScore >= d.mutation;
  const l2 = m.flakeRate <= d.l2Flake && m.validity >= d.l2Validity;
  const l3 = m.flakeRate <= d.l3Flake;
  const level = l1 ? 1 : l2 ? 2 : l3 ? 3 : 4;
  if (level > 1) reasons.push(`flakeRate=${m.flakeRate} 未达更严阈值`);
  return { level, policy: ['阻塞门禁','普通门禁','建议级','隔离观察'][level - 1], reasons };
}
console.log(gradeUseCase({ flakeRate: 0.02, validity: 0.9, survival: 0.88, mutationScore: 0.7 }).level);
// 2
```
**评分点**：
- L1/L2/L3/L4 判定条件正确，四项全优才 L1。
- 指标缺失降级为 L4 并列出 reasons。
- 支持自定义 thresholds，缺省用内置默认值。
- 输出 level/policy/reasons，可直接接入门禁。
