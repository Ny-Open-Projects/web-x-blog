---
title: [AIC-676] 为什么 AI 效能指标「一旦变成考核目标就失效」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-676：为什么 AI 效能指标「一旦变成考核目标就失效」？

**答**：
- 结论先行：**这就是古德哈特定律——「当一个指标成为目标，它就不再是好指标」**。因为被考核的人会优化指标本身而非指标背后的真实价值（AIC-681 效能体系实施）。
- 在 AI 度量的表现：1) **考核「AI 使用次数」**→ 工程师开着补全无脑 Tab，次数涨了但代码没变好；2) **考核「代码行数」**→ AI 生成冗长代码，行数涨了价值没涨；3) **考核「PR 数量」**→ 拆小 PR 刷量；4) **考核「接受率」**→ 无脑接受再悄悄改回。
- 为什么会失效：指标是真实价值的「代理」，一旦有激励，人们优化代理而非价值本身——代理人问题。且 AI 让「刷指标」成本极低（生成一堆代码只要几秒）。
- 应对措施：1) **指标 + 护栏成对**：任何速度指标都配质量护栏（逃逸率/存活率），刷速度会被护栏拦下；2) **用组合指标而非单一**：北极星 + 多维护栏让作弊难度指数上升；3) **定性补充**：定期抽检 + 工程师访谈，数据之外看真实感受；4) **别用它做个人考核**：指标用于团队改进与趋势分析，一旦绑定到个人 KPI 就必然被游戏化。
- 追问钩子：为什么「指标用于团队改进」比「用于个人考核」更安全？——因为团队层面无法靠个体刷量作弊（个体刷量会被团队其他数据稀释），且团队有共同利益去改进真实效率；个人考核则直接激励个体优化数字——激励方向决定指标命运。

```typescript
type Metric = { name: string; value: number; hasGuardrail: boolean; gamed: boolean };

function assessMetricGameability(m: Metric): { safe: boolean; reason: string } {
  if (!m.hasGuardrail) return { safe: false, reason: `${m.name} 无护栏指标，易被单一优化` };
  if (m.gamed) return { safe: false, reason: `${m.name} 已观察到游戏化行为` };
  return { safe: true, reason: '有护栏且未观察到作弊' };
}

console.log(assessMetricGameability({ name: 'AI调用量', value: 100, hasGuardrail: false, gamed: false }).safe); // false
console.log(assessMetricGameability({ name: '有效交付(带存活护栏)', value: 20, hasGuardrail: true, gamed: false }).safe); // true
```
