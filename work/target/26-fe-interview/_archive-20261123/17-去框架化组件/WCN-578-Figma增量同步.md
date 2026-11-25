---
title: [WCN-578] Figma Variables → 平台 token 的「增量同步」：设计稿改一个颜色，如何精准更新受影响组件？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-578：Figma Variables → 平台 token 的「增量同步」：设计稿改一个颜色，如何精准更新受影响组件？

**答**：
- 结论：同步按「设计变量 → 语义 token → 消费组件」的反向依赖图，只更新变更变量影响的 token 与组件。
- 每次同步做 diff（变量 id → 新值），命中变更的变量查反向图得到受影响 token 清单。
- 只重新生成这些 token 的 CSS 变量与依赖它们的组件主题包，避免全量重编。
- 追问：设计稿新增变量但代码未消费怎么办？（答：标记为「待采用」，不生成产物，仅提示）

```javascript
function incrementalSync(prevVars, nextVars, reverseGraph) {
  const changed = Object.keys(nextVars).filter(k => prevVars[k] !== nextVars[k]);
  const affectedTokens = new Set(), affectedComps = new Set();
  for (const v of changed) {
    const tokens = reverseGraph.variableToToken.get(v) || [];
    tokens.forEach(t => { affectedTokens.add(t); (reverseGraph.tokenToComp.get(t) || []).forEach(c => affectedComps.add(c)); });
  }
  return { changed, tokens: [...affectedTokens], components: [...affectedComps] };
}
```
