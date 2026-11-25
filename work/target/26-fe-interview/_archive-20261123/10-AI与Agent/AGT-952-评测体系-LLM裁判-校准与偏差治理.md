---
title: [952] 用 LLM-as-judge 打分，怎么校准才能信
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 评测, LLM裁判]
type: 面试题
---

## 952：用 LLM-as-judge 打分，怎么校准才能信

**答**：
- 裁判必须先校准：抽 50~100 条人工标注样本，对比裁判分与人工分的一致率（Cohen's kappa 或分组一致率），一致率不低于 0.75 才能用于迭代决策。
- 已知偏差要治理：位置偏差（A/B 顺序影响判断→交换顺序各评一次取均值）、长度偏差（偏爱长答案→评分标准明确「冗余扣分」）、自我偏好（裁判和被评是同一模型→换裁判模型）。
- 绝对分不可靠，相对比较更稳：打分制漂移大，两两比较 + Elo 排名更适合做版本对比。
- 追问钩子：裁判分能替代人工吗？——不能，只能「减少」人工：裁判初筛 + 人工抽检裁判的分歧样本，把人工量压缩一个数量级。

```ts
async function judgePair(a, b, rubric) {
  const [ab, ba] = await Promise.all([
    llm(judgePrompt(a, b, rubric)), llm(judgePrompt(b, a, rubric)) // 交换顺序消位置偏差
  ]);
  if (ab.winner === ba.winner) return ab.winner;         // 双向一致
  if (ab.winner === 'tie' || ba.winner === 'tie') return 'tie';
  return 'tie';                                          // 不一致按平局 + 转人工
}
```

