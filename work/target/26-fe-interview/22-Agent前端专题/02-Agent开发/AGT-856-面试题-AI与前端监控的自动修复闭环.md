---
title: [AGT-856] 报错自动归因之后，哪些修复可以自动执行、哪些必须人工？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-856：报错自动归因之后，哪些修复可以自动执行、哪些必须人工

**答**：
- 分级自动化：L1 自动执行（配置类修复：降级开关打开/CDN 回切/feature flag 关闭——已有预案且可逆）；L2 自动起草人工确认（代码修复 PR/回滚脚本）；L3 纯人工（架构级问题）。判断标准：可逆性×影响面×预案成熟度。
- 自动执行的安全阀：同类自动动作有频率上限（24h 内最多 2 次，防抖动循环）、执行前后快照、一键撤销。
- 演进：L2 的采纳率高的修复模式沉淀为 L1（预案化），让闭环逐步升级。

```javascript
const AUTO_LEVELS = {
  L1: { actions: ['toggleFlag', 'cdnRollback'], maxPerDay: 2 },
  L2: { actions: ['draftFixPR', 'rollbackScript'], needHuman: true },
  L3: { hint: true },
};
async function respond(issue, attribution) {
  const level = pickLevel(attribution, AUTO_LEVELS);
  if (level === 'L1' && countToday(level) < 2)
    return executeReversible(attribution.action, { snapshot: true,
      undoable: true });
  if (level === 'L2') return draftForReview(attribution);
  return pageEngineer(attribution);
}
```

