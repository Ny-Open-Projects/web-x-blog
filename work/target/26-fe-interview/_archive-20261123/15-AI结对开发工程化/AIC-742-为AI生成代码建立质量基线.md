---
title: [AIC-742] 如何为 AI 生成代码建立可度量的质量基线
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-742：如何为 AI 生成代码建立可度量的质量基线

**答**：
- 结论先行：质量基线 = 「在给定评测集上，AI 代码应达到的最低质量水位」；没有基线就无法判断某次生成是变好还是变坏，也无法发现模型静默升级带来的退化。
- 基线内容：correctness（评测集通过率）、安全（红线漏洞数）、可维护性（复杂度阈值）、测试覆盖（分支覆盖率）、成本（单任务平均 token）；每项定「红线值 + 目标值」。
- 建立方式：跑一批代表性任务取 P50 作为基线，P90 作为目标；基线要版本化，每次模型/规则变更重测。
- 追问钩子：为什么用 P50 而非均值做基线？——均值易被极端离群任务拉偏，P50 更代表「典型表现」，适合做稳定水位。

```javascript
// 质量基线：用 P50 设红线、P90 设目标
function buildBaseline(samples) {
  const sorted = [...samples].sort((a, b) => a - b);
  const pct = p => sorted[Math.floor((sorted.length - 1) * p)];
  return { red: pct(0.5), target: pct(0.9), n: samples.length };
}
function judge(value, base) {
  if (value < base.red) return 'below-redline';
  if (value >= base.target) return 'excellent';
  return 'acceptable';
}
const base = buildBaseline([0.6, 0.7, 0.72, 0.8, 0.95]);
console.log(base.red === 0.72 && base.target === 0.95); // true
console.log(judge(0.65, base)); // below-redline
```
