---
title: [919] 元数据过滤条件一多，检索质量反而掉怎么办
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 元数据]
type: 面试题
---

## 919：元数据过滤条件一多，检索质量反而掉怎么办

**答**：
- 过滤条件组合爆炸的根因：把「用户能感知的意图」直接翻译成硬 filter。用户说「去年的政策」不一定要硬过滤年份，时间应作为排序信号而非过滤信号。
- 生产规则：权限类（部门/密级）必须硬过滤；偏好类（语言、时间、产品线）走软过滤——先硬过滤保底，再对软条件做加权重排。
- filter 字段设计：高基数字段（用户 ID）不要进索引 filter，改用租户前缀路由；低基数字段（部门、语言）建 doc_values 加速。
- 追问钩子：软过滤怎么实现？——boost 函数按满足的软条件加分，等价于在相关性上叠加业务偏好，避免「过滤后空结果」。

```ts
function buildQuery(q, pref) {
  const must = permFilter(pref.user);            // 硬：权限，必选
  const should = [];
  if (pref.lang) should.push({ term: { lang: pref.lang, boost: 2 } });   // 软：语言
  if (pref.recency) should.push({ range: { publishedAt: { gte: pref.recency, boost: 1.5 } } });
  return { bool: { must, should: [...should, { knn: embed(q) }] }, // 软条件仅加权
    min_should: 0 };
}
```

