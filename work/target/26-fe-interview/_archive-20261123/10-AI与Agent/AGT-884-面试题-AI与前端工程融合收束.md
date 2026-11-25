---
title: [AGT-884] 把 AI 与前端工程的融合收束成一张图（写码/评审/测试/运维/流程五环），核心原则是什么？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-884：把 AI 与前端工程的融合收束成一张图（写码/评审/测试/运维/流程五环），核心原则是什么

**答**：
- 五环：写码（AI 结对+模板锁定+边界 rules）、评审（AI 机械面+人语义面+置信分级）、测试（AI 补覆盖+变异验证质量+人保验收）、运维（自动归因+分级自愈+禁区明确）、流程（CI 门禁对 AI 产出同权+契约驱动+知识沉淀）。
- 核心原则三条：① AI 产出的质量责任仍归人（责任不转移）；② 确定性强的事交给程序（codemod/lint/schema），AI 只处理语义层——能用规则的不用模型；③ 一切 AI 产出可观测可回滚（标记/归因/台账），黑盒产出不进主干。
- 判断融合成熟度：看「AI 产出的事故率」与「团队对 AI 产出的默认信任度」——好的融合是"默认信任但有门禁兜底"，坏的融合是"要么盲信要么全人工复审"。

```javascript
const FUSION = {
  write: ['pair', 'template', 'rules'],
  review: { ai: 'mechanical', human: 'semantic', gating: 'confidence' },
  test: { ai: 'coverage', verify: 'mutation', human: 'acceptance' },
  ops: { levels: ['auto-reversible', 'draft-human', 'human-only'] },
  flow: { ci: 'same-gate', contract: 'single-source' },
};
const PRINCIPLES = ['责任归人', '规则优先于模型', '产出可观测可回滚'];
function maturity() {
  return { incidentRate: aiIncidentRate(),
    trust: defaultTrustLevel() };   // 默认信任+门禁兜底=成熟
}
```

