---
title: [1176] LLM 裁判和人工评审意见不一致，怎么办系统化
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 评测]
type: 面试题
---

## 1176：LLM 裁判和人工评审意见不一致，怎么办系统化

**答**：
- 分歧是信号不是麻烦：分歧率高的样本类别 = 裁判能力边界或规范模糊处，每周分析分歧聚类，输出「裁判改进项」或「规范澄清项」。
- 仲裁机制：分歧样本进仲裁队列（资深评审终裁），裁决结果回写——既校准裁判（下轮训练/调 prompt 用裁决样本），又让规范长出判例。
- 一致率指标分层：总体一致率、分意图一致率（某些意图裁判特别弱要显式暴露）、漂移监控（一致率周环比下降=裁判或规范变了）。
- 追问钩子：分歧要不要「让裁判投票」解决？——双裁判投票只是提高方差利用率，不解决系统性偏差；价值在于「分歧检测」本身（不一致才送人工），而不是靠投票得出真理。

```ts
async function adjudicate(cases) {
  const disputes = [];
  for (const c of cases) {
    const [llm, human] = await Promise.all([judge(c), humanScore(c)]);
    if (llm.verdict !== human.verdict) disputes.push({ c, llm, human });
  }
  const ruled = await seniorReview(disputes);       // 终裁
  judgeCalibrate(ruled);                            // 回写校准裁判
  spec.addCases(ruled);                             // 规范长判例
  return { rate: disputes.length / cases.length, byIntent: groupRate(disputes) };
}
```
