---
title: [NODE-757] 笔试题——实现搜索联想服务端查询器（前缀索引 + 分层缓存）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-757：手写联想查询

**需求与边界**：
- 需求：联想查询器（SCN-NODE-715）——① 热门前缀缓存命中（幂律分层——SCN-联想-834）；② 冷前缀走 ZSET 实时查；③ 限流（1 字符不查——SCN-联想-809）；④ 个性化合并（用户历史 + 全局——SCN-联想-808 隐私分层）。
- 边界：① 查询规范化（trim/小写/全角——SCN-联想-695 normalize）；② 空结果降级（纠错/品类兜底——SCN-联想-832 降级链服务端版）；③ P99 预算（80ms——超预算降级静态热词）。

**答**：
```javascript
async function suggest(q, user, { budget = 80 } = {}) {
  const norm = normalize(q);                           // 规范化（SCN-联想-695）
  if (norm.length < 2) return [];                      // 1 字符不查（SCN-联想-809）
  if (hotPrefixCache.has(norm)) return hotPrefixCache.get(norm);   // 热前缀缓存（幂律分层）
  const deadline = Date.now() + budget;
  const [global, personal] = await Promise.all([
    zrevrangeTimeout(`sug:${norm}`, 10, deadline),     // 冷前缀实时查（带超时）
    userHistory(user, norm),                           // 用户历史（本地+服务端合并）
  ]);
  if (!global.length && deadline - Date.now() > 20)    // 空结果降级链
    return fallbackChain(norm);                        // 纠错 → 品类（SCN-联想-832）
  return dedupeMerge(personal, global);                // 个性化合并（SCN-联想-808）
}
```

**评分点**:
- 幂律分层缓存（热前缀预计算——SCN-联想-834 成本模型）。
- 限流前置（1 字符不查）+ 查询规范化。
- 空结果降级链（服务端兜底——SCN-联想-832 对应）。
- deadline 预算（超时降级——SCN-联想-810 性能预算服务端版）。
