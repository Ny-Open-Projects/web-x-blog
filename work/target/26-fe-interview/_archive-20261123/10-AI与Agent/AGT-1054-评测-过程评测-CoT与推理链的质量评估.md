---
title: [1054] 推理链（思维链）怎么评，不只评结论
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 评测, 推理链]
type: 面试题
---

## 1054：推理链（思维链）怎么评，不只评结论

**答**：
- 推理链三查：有效性（每步从前提推得出，无跳步）、忠实性（结论确实由该链推出——链和结论矛盾即「事后编造」）、效率（步数合理，无循环空转）。
- 忠实性检测最关键：把推理链单独喂给裁判问「该结论是否由这些步骤支持」，与「直接看答案打分」分离——模型常出现「链是错的答案是对的」或反之。
- 过程评测的成本控制：只在推理型任务（数学/决策/排障）开启，事实型问答不需要。
- 追问钩子：链对答案错说明什么？——说明模型的推理链是「表演」而非真实计算过程，改 prompt 引导不如换模型或拆解任务（分步执行每步验证）。

```ts
async function evalChain(q, { chain, answer }, gold) {
  const correct = grade(answer, gold);
  const faithful = await judge('该结论是否由以下步骤必然得出？', chain, answer);
  const steps = chain.length;
  return { correct, faithful, steps,
    verdict: correct && faithful ? 'pass'
      : correct && !faithful ? 'chain_theater'    // 链是表演
      : 'fail' };
}
```
