---
title: [AGT-655] 单个 LLM judge 有偏（偏爱长答案/爱自己的风格），多评委体系怎么搭？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-655：单个 LLM judge 有偏（偏爱长答案/爱自己的风格），多评委体系怎么搭

**答**：
- 异构评委：不同家族的模型当 judge（避免同源偏好）+ 规则评委（格式/长度/引用校验），评委各自独立打分。
- 一致性协议：评委分歧小（分差 ≤1）取均值；分歧大触发仲裁（更强模型或人工）；仲裁样本自动进「judge 校准集」，用于持续测量各评委偏差。
- 已知偏差要显式修正：位置偏差（对比评测中 A/B 顺序）用双序翻转；长度偏好做长度归一分析；自我偏好用跨家族评委规避。

```javascript
async function judgedByPanel(case, rubric) {
  const scores = await Promise.all(JUDGES.map(j =>
    j.score(case, rubric, { order: Math.random() > 0.5 ? 'AB' : 'BA' })));
  const spread = Math.max(...scores) - Math.min(...scores);
  if (spread <= 1) return { score: avg(scores), agreement: 'high' };
  const arb = await ARBITER.score(case, rubric);   // 仲裁
  calibPool.add({ case, scores, arb });            // 进校准集
  return { score: arb.score, agreement: 'arbitrated' };
}
```

