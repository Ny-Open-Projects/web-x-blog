---
title: [AGT-254] LLM-as-judge——用模型评模型有哪些坑？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-254：用 LLM 当裁判评 Agent 输出，怎么用才可靠？

**答**:
- judge 的系统性偏差：位置偏差（偏好某个位置的答案——A/B 对比时要交换顺序取平均）、长度偏差（偏好长答案——rubric 里显式惩罚冗长）、自我偏好（偏好自己模型的风格——judge 与被评模型最好异源）、谄媚（顺着 prompt 里的暗示给分——评测 prompt 要中立无暗示）。
- 提升可靠性的手段：结构化 rubric（逐维度 1~5 分+评分依据，禁止整体一个分）、few-shot 锚定（给评分示例校准尺度）、多 judge 投票（3 个异源 judge 取中位）、人工校准集（固定 50~100 条人工标注样本，定期测 judge 与人的一致率，低于阈值就重校准）。
- 使用边界：judge 适合"相关性/风格/结构"这类主观维度；事实性判断不可靠（judge 自己会幻觉）——事实校验走程序化断言（引用存在性/数字比对），不交给 judge。
- 成本与抖动：judge 也是调用（有成本有方差）——同一样本多次评（temperature=0 仍有波动），关键评测取 2~3 次平均；评测预算单列。

```javascript
async function judge(sample, rubric) {
  const [a, b] = shuffle([sample.output, sample.baseline]); // 防位置偏差
  const r1 = await judgeLLM({ rubric, a, b, fewshot: rubric.examples });
  const r2 = await judgeLLM({ rubric, a: b, b: a, fewshot: rubric.examples });
  return mergeSwapped(r1, r2);     // 交换顺序取均值
}
// 校准：每月跑人工集，judge-human 一致率 < 0.85 → 修 rubric
// 事实类 → 不用 judge，走程序化断言
```
