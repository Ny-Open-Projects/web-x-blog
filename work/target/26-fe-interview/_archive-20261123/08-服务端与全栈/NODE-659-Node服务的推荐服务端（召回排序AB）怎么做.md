---
title: [NODE-659] 推荐服务端（召回/排序/实验）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-659：推荐服务端怎么做？
**答**：
- 三段管线：召回（多路——热门/协同/向量相似，各路几百候选）→ 排序（模型打分——精排几百到几十）→ 重排（打散/多样性/业务规则——同店铺限流）。
- Node 的角色：推荐网关（并发调多路召回——并行聚合，SCN-NODE-644 BFF 模式）、特征拼装、AB 分流（SCN-ENG-296 分流器复用）、结果缓存（同用户短 TTL——滑动刷新）。
- 实时特征：用户最近行为（点击流 → Redis 特征队列——实时性）；特征缺失的降级（冷启动——热门兜底，SCN-NODE-832 冷启动同构）。
- 实验闭环：曝光/点击埋点回流（traceId 贯穿——SCN-SUG-807 归因）、实验指标看板（SCN-OPS-252 对冲指标）。
- 追问钩子：为什么推荐网关的「多路召回并行 + 配额」是关键设计——各路召回服务（向量检索/协同）性能差异大，无配额时慢路拖整链（BFF 串联放大）；每路超时+配额（超时路降级为空——其余路补足），并配各路配额占比——部分成功模式在推荐场景的必然性（总要有东西给用户看）。

```javascript
const [hot, cf, vec] = await Promise.allSettled([
  recallHot(user, { timeout: 50, quota: 200 }),
  recallCF(user, { timeout: 80, quota: 200 }),
  recallVec(user, { timeout: 100, quota: 200 }),
]);
const candidates = mergeDedup([hot, cf, vec].map(orEmpty));   // 合并去重
const ranked = await rank(candidates.slice(0, 500), features);
return rerank(ranked.slice(0, 30), { diversity: true });
```
