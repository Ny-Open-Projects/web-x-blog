---
title: [1148] 检索改写模块用大模型太贵，怎么蒸馏到小模型
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 蒸馏]
type: 面试题
---

## 1148：检索改写模块用大模型太贵，怎么蒸馏到小模型

**答**：
- 蒸馏路径：大模型批量生成「(上下文+query) → 改写后 query」的高质量对（5k~20k 条）→ 微调小模型 → 评估集验证改写质量与大模型的一致率（目标 90%+）→ 灰度替换。
- 数据质量决定成败：蒸馏数据要覆盖真实分布（多轮指代/口语化/混杂语言），全靠模板生成会学成「只会模板改写」；配额从线上真实 query 采样。
- 收益核算：改写是每请求必经环节，量极大；小模型延迟降 3~5 倍、成本降 10 倍以上，是蒸馏 ROI 最高的场景之一。
- 追问钩子：蒸馏后线上效果回退怎么办？——保留「回退开关」（小模型置信度低时升级大模型）+ 蒸馏版进回归集长期看护，漂移即回退。

```ts
async function distill() {
  const pairs = await sampleRealQueries(10000)
    .map(q => llmBig(rewritePrompt(q), { teach: true }));    // 大模型当老师
  const student = await fineTune('small', pairs);
  const agree = await evalAgreement(student, bigModel, rewriteEval);
  if (agree > 0.9) return rollout(student, { canary: 0.05, fallback: bigModel });
  return abort(agree);
}
```
