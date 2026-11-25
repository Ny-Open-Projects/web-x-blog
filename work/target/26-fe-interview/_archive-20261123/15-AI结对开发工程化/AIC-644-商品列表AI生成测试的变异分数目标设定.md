---
title: [AIC-644] 商品列表的 AI 生成测试，变异分数该定多少？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-644：商品列表的 AI 生成测试，变异分数该定多少？

**答**：
- 结论先行：**变异分数（mutation score）不是越高越好，要按「模块风险 × 测试成本」定目标**——核心购买链路定 80%+，边角展示逻辑 60% 即可；盲目追 100% 会被无意义的等价变异体拖垮（AIC-238 变异测试）。
- 变异分数是什么：故意改坏源码（变异体，如把 `>` 改成 `>=`），看测试能不能发现；发现率 = 变异分数。它比行覆盖率更真实——覆盖率只看代码有没有被执行，变异分数看测试有没有真正断言行为。
- AI 测试的典型问题：AI 爱写弱断言（`expect(x).toBeDefined()`），行覆盖率很高但变异分数很低——杀不死任何变异体（AIC-232 弱断言 / AIC-413）。所以 AI 生成测试后，变异分数是照妖镜。
- 定目标的依据：1) **模块风险**：支付/库存 > 列表展示；2) **变更频率**：常改的模块值得高变异分数；3) **成本**：变异测试运行慢，全仓每次跑不现实——只对核心模块跑，或夜间定时跑。
- 追问钩子：为什么「变异分数」比「行覆盖率」更适合评估 AI 生成的测试？——因为 AI 特别擅长生成「让覆盖率好看」的测试（把每个分支都执行一遍），但断言软弱；覆盖率会被这种「广而不深」的测试骗过，变异分数必须从行为上杀死变异体，骗不过去。

```typescript
type ModuleRisk = { name: string; risk: 'high'|'medium'|'low'; changeFreq: number };

function mutationTarget(m: ModuleRisk): number {
  const base = m.risk === 'high' ? 80 : m.risk === 'medium' ? 65 : 50;
  // 高频变更模块 +10，封顶 90（不追 100，避免等价变异体）
  return Math.min(90, base + (m.changeFreq > 10 ? 10 : 0));
}

console.log(mutationTarget({ name: 'checkout', risk: 'high', changeFreq: 20 })); // 90
console.log(mutationTarget({ name: 'list-display', risk: 'low', changeFreq: 2 })); // 50
console.log(mutationTarget({ name: 'cart', risk: 'medium', changeFreq: 1 })); // 65
```
