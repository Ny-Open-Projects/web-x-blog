---
title: [AIC-821] AI 质量工程和传统 QA 的本质差异在哪？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-821：AI 质量工程和传统 QA 的本质差异在哪？
**答**：
- 传统 QA 断言是**确定性的**（输入 → 期望输出，assert equal）；AI 输出是**概率性的**，同一个 prompt 两次结果不同，所以质量从「通过/失败」变成「分布与概率」——要看通过率、置信区间、分位数，而不是一次结果。
- 测试对象变了：除了代码，还要测 **prompt、模型版本、上下文组装逻辑、工具调用链**；代码没变但模型升级或 prompt 改一个词就会导致质量漂移（AIC-816）。
- 评估标准本身难定义：很多任务（摘要质量、代码风格）没有唯一正确答案，需要 **golden 集 + 裁判模型 + 人工抽检** 组合评估，评估器自身也要被评估。
- 反馈闭环更长：线上问题要先转成评测用例（回归守卫 AIC-830），才能进入门禁防止复发——QA 从「发布前把关」变成「持续运行的飞轮」。
- 追问钩子：能说出「传统 QA 测确定性代码，AI QE 测概率性系统 + 评估器本身」的候选人，抓住了本质而非照搬传统测试流程。

```typescript
// 传统断言：确定性
function traditionalTest(result: string) {
  return result === 'expected'; // 非黑即白
}

// AI 质量评估：概率性 + 多次采样 + 分位数
async function aiQualityTest(prompt: string, n = 20) {
  const scores: number[] = [];
  for (let i = 0; i < n; i++) {
    const res = await model.chat(prompt);
    scores.push(await evaluator.score(res)); // 评估器本身也可能是模型
  }
  scores.sort((a, b) => a - b);
  return {
    passRate: scores.filter(s => s >= 0.8).length / n,
    p50: scores[Math.floor(n * 0.5)],
    p10: scores[Math.floor(n * 0.1)],   // 关注最差情况，而非平均
    mean: +(scores.reduce((a, b) => a + b, 0) / n).toFixed(3),
  };
}
// 结论写法：passRate ≥ 0.9 且 p10 ≥ 0.6 才算通过（带置信区间）
```
