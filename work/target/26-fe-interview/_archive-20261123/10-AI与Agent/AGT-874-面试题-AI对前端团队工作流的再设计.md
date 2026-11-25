---
title: [AGT-874] 引入 AI 后，前端团队的工作流（需求→开发→测试→发布）哪些环节值得重排？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-874：引入 AI 后，前端团队的工作流（需求→开发→测试→发布）哪些环节值得重排

**答**：
- 真正改变的环节：开发（AI 结对，评审从"找错"转向"看设计"）、测试（AI 补覆盖面，人保验收路径）、文档/埋点/i18n（从手工劳动变审核劳动）、排障（归因提速）。不变的：需求理解/技术方案/架构决策——AI 越强，人的价值越往上游走。
- 重排原则：把「人的时间」从机械劳动转移到 AI 做不好的地方（需求澄清/取舍决策/AI 产出审核的抽查制度）；新流程要有度量（每环节 AI 参与度与质量指标）。
- 反面模式：为用 AI 而用 AI（文档生成后没人看/测试生成后没人维护）——每个 AI 环节必须有消费者与维护者。

```javascript
const WORKFLOW_V2 = {
  design: { owner: 'human', note: 'AI 越强人越往上游' },
  code: { ai: 'pair', review: 'design-focus' },
  test: { ai: 'coverage', human: 'acceptance-path' },
  docs: { ai: 'draft', owner: 'must-have-reader' }, // 有消费者才行
};
function auditWorkflow() {
  return Object.entries(WORKFLOW_V2).every(([k, v]) =>
    v.ai ? hasConsumer(k) && hasMaintainer(k) : true);
}
```

