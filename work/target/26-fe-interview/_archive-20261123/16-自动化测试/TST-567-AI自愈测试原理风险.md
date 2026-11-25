---
title: [TST-567] AI 自愈测试（self-healing）的原理与风险
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-567：AI 自愈测试（self-healing）的原理与风险

**答**：
- 结论：自愈 = 元素定位失败时，用多属性（文本/语义/结构/视觉）相似度重新匹配候选元素并生成新定位器；风险是「 healed 到错误元素」导致假阳性。
- 做法：定位失败时给候选打分（多属性加权），超过阈值才采用；新定位器进入「待审队列」人工确认后入库；记录每次 healing 与变更 diff 供审计。
- 追问钩子：自愈会不会掩盖真实 UI bug（元素本该消失）？——会；所以自愈必须区分「定位器变更」与「功能变更」，对结构/文本大幅变化的 healing 强制人工确认，而非静默通过。

```javascript
// 自愈候选打分：多属性加权，超阈值才采用
function healLocator(failed, candidates, domSnapshot) {
  const weight = { text: 0.5, role: 0.3, structure: 0.2 };
  const scored = candidates.map(c => ({
    c, score: (c.textMatch || 0) * weight.text + (c.roleMatch || 0) * weight.role
      + (c.structMatch || 0) * weight.structure,
  })).sort((a, b) => b.score - a.score);
  const best = scored[0];
  return best && best.score >= 0.8
    ? { healed: true, locator: best.c.locator, score: best.score, needReview: best.score < 0.95 }
    : { healed: false };
}
```
