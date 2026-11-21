---
title: [NODE-594] Node 服务的搜索联想（suggest/纠错/热词）如何实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-594：搜索联想服务
**答**:
- 联想类型：前缀补全（completion suggester——索引化前缀查询）、热门联想（高频搜索词——热度权重）、个性化联想（用户历史/偏好——加权）、纠错联想（拼音纠错/拼写纠错——"您是不是要找"ARC-649）。
- 性能设计：联想延迟要求高（< 50ms——ES completion/前缀 Trie 内存索引——热词内存缓存）、防抖配合（ARC-383 端上 300ms 防抖 + 服务端快速响应）、限流（联想 QPS 极高——轻接口预算）。
- 内容治理：联想词过滤（敏感/违规词不入联想——词库管理）、无结果词处理（联想无结果商品——避免引导到空页）、热词运营（运营配置权重/置顶——活动词）。
- 效果闭环：联想点击率（采纳率——排序优化）、联想到转化的归因（联想词效果统计）、新词发现（用户输入新模式——词典迭代）。
- 协议：suggest 接口（q + 个性化维度 → 带类型标记的列表：补全/纠错/热词——前端区分展示）。
```javascript
// 联想服务
app.get('/suggest', async (ctx) => {
  const { kw } = ctx.query;
  const [completions, corrections, hot] = await Promise.all([
    es.suggest(kw), spell.correct(kw), hotWords.top(kw, { user: ctx.user })]);
  return merge({ completions, corrections, hot }, { personalBoost: ctx.user });  // 类型标记
});
```
