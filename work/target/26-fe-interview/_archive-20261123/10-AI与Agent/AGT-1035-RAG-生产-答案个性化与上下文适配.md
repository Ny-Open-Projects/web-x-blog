---
title: [1035] 同一个问题，新人和专家要不同答案，RAG 怎么做个性化
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 个性化]
type: 面试题
---

## 1035：同一个问题，新人和专家要不同答案，RAG 怎么做个性化

**答**：
- 个性化三层：检索层（按用户画像调元数据权重——新人提升「入门文档」权重）、生成层（按用户等级适配深度与术语——新手多解释概念，专家直接给结论）、呈现层（新手展示步骤、专家展示参数表）。
- 画像来源要克制：只用显式信号（用户自报角色、历史提问深度），行为推断画像要过隐私评估。
- 个性化与缓存冲突：答案带个性化后不能按 query 直接缓存，缓存 key 加画像档位（limited 档位如 3 档，缓存仍可用）。
- 追问钩子：个性化会不会造成「信息茧房」？——会，所以每个档位的评估集都要覆盖「跨档提问」，且档位间答案事实层必须一致（只是详略不同），防止各档答案互相矛盾。

```ts
function personalize(query, user, hits) {
  const tier = user.expertise;                     // beginner | pro
  const boostHits = tier === 'beginner'
    ? reweight(hits, { meta: 'intro', boost: 1.5 }) // 检索层加权
    : hits;
  const style = tier === 'beginner'
    ? '面向新手，解释术语，分步骤' : '面向专家，直接结论，附参数表';
  return llm(prompt(query, boostHits, style));      // 生成层适配
}
```
