---
title: [AGT-895] 手写 reviewFlow：置信分级（阻塞/建议）、人工焦点区、采纳校准、误报降级？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-895：手写 reviewFlow：置信分级（阻塞/建议）、人工焦点区、采纳校准、误报降级

**需求与边界**：
- 实现 aiReviewFlow(pr)。
- 边界要求：① confidence ≥0.9 进 blocking（合并阻断），其余进 suggestions；② 人工焦点区=AI 无法覆盖的语义风险点（业务逻辑变更/架构文件）；③ 开发者对意见的 adopt/reject 信号累计，reject 率 >70% 的检查规则自动降级为建议；④ 输出评审面板数据结构。

**答**：
```javascript
async function aiReviewFlow(pr, { calib }) {
  const issues = await aiReview(pr);
  const grouped = {
    blocking: issues.filter(i => i.confidence >= 0.9),
    suggestions: issues.filter(i => i.confidence < 0.9),
  };
  const focus = pr.diff.files
    .filter(f => f.kind === 'business-logic' || f.path.startsWith('arch/'))
    .map(f => ({ file: f.path, why: '语义风险，AI 不覆盖' }));
  for (const i of issues) {                        // 校准挂钩
    i.onFeedback = (adopt) => calib.record(i.rule, adopt);
  }
  const demote = calib.rules().filter(r =>
    r.rejectRate > 0.7).map(r => ({ rule: r.id,
      action: '降级为建议' }));                    // 误报降级
  return { ...grouped, focus, demote };
}
```

**评分点**:
- 置信分级明确（≥0.9 阻塞，其余建议不抢注意力）。
- 人工焦点区按语义风险划定（AI 不越界）。
- 采纳信号校准+误报规则自动降级（误报治理闭环）。

