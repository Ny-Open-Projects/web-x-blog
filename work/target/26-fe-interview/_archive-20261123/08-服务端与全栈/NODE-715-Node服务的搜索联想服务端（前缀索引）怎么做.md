---
title: [NODE-715] 搜索联想服务端（前缀索引/热词）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-715：联想服务端怎么做？
**答**：
- 前缀索引：Trie/Redis 有序集（ZSET prefix 索引——前缀查询 O(logN)）+ 分词前缀（拼音/首字母——SCN-联想-811 三层匹配的服务端实现）。
- 热词机制：实时热度统计（搜索日志 → 滑窗计数——爆发检测，SCN-联想-843）→ 热词池（TTL 衰减）。
- 缓存策略：热门前缀预计算（幂律——Top 前缀缓存，SCN-联想-834 成本模型）+ 冷前缀实时查。
- 接口设计：低延迟要求（P99 < 80ms——SCN-联想-810 预算）、限流（1 字符不请求——SCN-联想-809）、个性化（用户历史本地+服务端合并——隐私分层）。
- 追问钩子：为什么联想服务的「热门前缀预计算」是成本核心——搜索前缀分布幂律（Top 20% 前缀占 80% 流量）；预计算成缓存后，实时索引查询只剩长尾——按流量分布优化（缓存热、实时冷）是联想服务 QPS 成本差 10× 的原因——通用模式：幂律流量分层处理。

```javascript
// 前缀索引（ZSET）
await redis.zadd(`sug:${prefix}`, score, word);        // 词 → 前缀索引
const sug = await redis.zrevrange(`sug:${q}`, 0, 9);   // 前缀查询
// 热度统计（滑窗爆发）
await redis.hincrby('hot:count', q, 1);                // 计数
if (burstDetected(q)) promoteHot(q);                   // 爆发提升热词
```
