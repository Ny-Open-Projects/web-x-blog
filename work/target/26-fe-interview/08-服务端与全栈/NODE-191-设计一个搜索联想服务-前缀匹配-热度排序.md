---
title: [NODE-191] 设计一个搜索联想服务（前缀匹配/热度排序）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-191：设计一个搜索联想服务（前缀匹配/热度排序）？
**答**：
- 量级决定方案：词典万级 → Redis ZSET（score=热度）内存过滤；百万级 → ES completion suggester（FST 结构）或常驻内存 Trie。
- 数据来源：搜索日志离线挖掘（query 去重 + 频次 + 转化率），热词榜 5 分钟增量更新；敏感词前置过滤（NODE-096）。
- 体验细节：纠错候选兜底（编辑距离 1，"iphoe"→"iphone"）、个性化按 uid 历史加权、曝光埋点反哺热度。
- 接口要求 P99 < 20ms：本地缓存词典快照，Redis 只做兜底。

```javascript
async function suggest(prefix, { uid } = {}) {
  const key = `suggest:${prefix[0]}`;                 // 按首字分桶
  const candidates = await redis.zrevrange(key, 0, -1); // 万级词典全量可承受
  let hits = candidates.filter((t) => t.startsWith(prefix));
  if (!hits.length) hits = fuzzyByEditDistance(prefix, candidates, 1); // 纠错兜底
  const personal = uid ? await redis.smembers(`suggest:hist:${uid}`) : [];
  hits.sort((a, b) => Number(personal.includes(b)) - Number(personal.includes(a)));
  const result = hits.slice(0, 10);
  recordSuggestHit(prefix, result[0]);                // 曝光埋点 → 反哺热度
  return result;
}
// 热度更新（离线任务）：ZINCRBY suggest:a 1 <term>；ZREMRANGEBYSCORE 清零低热词
```
