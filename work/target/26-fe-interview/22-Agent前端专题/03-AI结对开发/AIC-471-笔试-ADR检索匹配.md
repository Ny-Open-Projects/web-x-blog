---
title: [AIC-471] 笔试：实现变更与 ADR 的相关度匹配。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-471：笔试：实现变更与 ADR 的相关度匹配。
**答**：ADR `[{id, modules[], status}]`（status: accepted/deprecated），变更 `changedModules[]`。相关 = 模块交集非空且 status=accepted。输出相关 ADR 列表（按交集大小降序）与 deprecated 命中提示（变更涉及已废弃决策需人工确认）。

```javascript
function matchADR(adrs, changedModules) {
  const cm = new Set(changedModules);
  const hits = [], deprecatedHits = [];
  for (const a of adrs) {
    const inter = a.modules.filter(m => cm.has(m));
    if (!inter.length) continue;
    (a.status === 'accepted' ? hits : deprecatedHits)
      .push({ id: a.id, inter });
  }
  hits.sort((x, y) => y.inter.length - x.inter.length);
  return { related: hits, deprecatedConfirm: deprecatedHits };
}
console.log(matchADR([
  { id: 'ADR-1', modules: ['state', 'hooks'], status: 'accepted' },
  { id: 'ADR-9', modules: ['state'], status: 'deprecated' },
], ['state', 'pages'])); // related [ADR-1]；deprecatedConfirm [ADR-9]

```

**评分点**：
- 废弃 ADR 不进相关列表但单独提示——容易漏的考点。
- 交集大小排序（最相关优先）。
- 空交集/空变更返回空。
- 输出带交集模块清单（可解释）。
