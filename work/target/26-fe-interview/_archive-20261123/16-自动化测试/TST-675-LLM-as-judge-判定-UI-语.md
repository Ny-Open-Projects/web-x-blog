---
title: [TST-675] LLM-as-judge 判定 UI 语义正确性怎么做？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-675：LLM-as-judge 判定 UI 语义正确性怎么做？

**答**：
- 结论：把截图 + DOM 文本 + 验收要点一起喂给多模态模型，让它按 rubric 打分而非自由发挥。
- rubric 拆成可判定项：文案存在、状态正确、层级合理；每项给 0/1 与证据。
- 低置信度或模型分歧时转人工，结果回流作 few-shot。
- 追问钩子：模型对「好看」这类主观项判断不稳，你怎么处理？

```javascript
function judgeRubric(visionResult, rubric) {
  const items = rubric.map(r => ({
    id: r.id,
    pass: visionResult.evidence.some(e => e.includes(r.keyword)),
    evidence: visionResult.evidence.filter(e => e.includes(r.keyword)),
  }));
  const conf = visionResult.confidence;
  return {
    items,
    pass: items.every(i => i.pass),
    needHuman: conf < 0.7,
  };
}
```
