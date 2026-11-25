---
title: [AGT-526] AI 问答的结果缓存怎么做（精确缓存→语义缓存的前端视角）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-526：AI 问答的结果缓存怎么做（精确缓存→语义缓存的前端视角）

**答**：
- 两级缓存：精确缓存（相同 prompt+参数+模型版本 → hash 键）与语义缓存（向量相似度 > 阈值命中，返回时标注"来自相似问题"）。
- 前端职责是「展示命中透明度」与「失效策略」：命中缓存的回答标注"秒答"，语义命中给出原问题让用户判断相关性；带时效知识的回答不缓存或短 TTL。
- 缓存键必须包含提示词版本与知识库版本，知识库更新后旧缓存自动失效。

```javascript
function cacheKey(req) {
  return hash([req.promptNorm, req.model, req.promptVer,
    req.kbVersion, JSON.stringify(req.params)].join('|'));
}
async function ask(q) {
  const exact = await cache.get(cacheKey(normalize(q)));
  if (exact) return { ...exact, fromCache: 'exact' };
  const sem = await vectorCache.search(embed(q), 0.92);  // 语义缓存
  if (sem) return { ...sem.answer, fromCache: 'similar',
    originQ: sem.question };   // UI 标注原问题
  return fresh(q);
}
```

