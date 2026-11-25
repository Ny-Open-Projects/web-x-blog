---
title: [AGT-711] 图文混合上下文里，图片 token 远贵于文本，预算怎么分配？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-711：图文混合上下文里，图片 token 远贵于文本，预算怎么分配

**答**：
- 图片按「信息密度预算」：一张图 ≈ 1000~2000 tokens，检索命中 10 张图就爆预算；策略是图片分档——关键图（答案引用的）全量传、相关图降为缩略图+描述文本、弱相关只留标题引用。
- 动态降级：预算不够时优先保「答案必需模态」（问图表数据就保图表原图，把无关文本块压缩），按 query 意图分配预算权重。
- 计量与缓存：vision 调用结果（描述/提取）缓存复用，同一图片在同会话内不重复计费。

```javascript
function allocateBudget(candidates, budget) {
  const intentWeights = detectModality(query);     // { image: 0.6, text: 0.4 }
  const sorted = candidates.sort(byRelevance);
  let used = 0; const kept = [];
  for (const c of sorted) {
    const cost = c.kind === 'image' ? IMG_TOKENS
      : c.kind === 'thumb' ? 200 : tokenCount(c.text);
    if (used + cost > budget * intentWeights[c.kind]) {
      if (c.kind === 'image') kept.push(thumbnailize(c)); // 图片降档
      continue;
    }
    used += cost; kept.push(c);
  }
  return kept;
}
```

