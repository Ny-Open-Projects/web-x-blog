---
title: [AGT-714] 图文问答的评测怎么做（图文一致性/数值准确/引用正确）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-714：图文问答的评测怎么做（图文一致性/数值准确/引用正确）

**答**：
- 三类判据：数值准确性（图表读数与金标容差比对，程序可判）、要素完整性（回答是否覆盖图中关键要素，vision judge 辅助）、引用正确性（引用的图/页码/时间戳是否真的支撑该答案，程序校验引用存在性+judge 校验支撑性）。
- 幻觉专项：让模型描述不存在于图中的内容（编造数据）是最大风险，评测集要有"图中没有问XX"类陷阱用例。
- 评测成本控制：vision judge 调用贵，程序判据（数值/引用存在性）优先，judge 只做抽样与最终仲裁。

```javascript
const MM_EVAL = {
  numeric: (gold, out) => tolerance(gold.value, out.value),   // 程序判
  citation: (gold, out) => citesExist(out.citations) &&
    judgeSupport(out.answer, out.citations),                   // 混合判
  hallucination: (case) => case.trap && mentionsAbsent(case, case.absent),
};
function evalMultimodal(cases, run) {
  return cases.map(c => {
    const checker = MM_EVAL[c.kind] ?? visionJudge;
    return { case: c.id, score: checker(c.golden, run[c.id]) };
  });
}
```

