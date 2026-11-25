---
title: [NODE-758] 笔试题——实现推荐网关（多路召回 + 配额 + 重排）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-758：手写推荐网关

**需求与边界**：
- 需求：推荐三段管线（SCN-NODE-659）——① 多路召回并行（每路超时+配额——部分成功）；② 合并去重 + 精排；③ 重排（多样性打散——同店铺限流）；④ traceId 贯穿（曝光归因——SCN-联想-807）。
- 边界：① 全路失败冷启动兜底（热门兜底——SCN-NODE-832）；② 配额占比声明（每路候选上限）；③ 精排服务的失败降级（按召回分粗排——精排挂退化为粗排结果）。

**答**：
```javascript
async function recommend(user, ctx) {
  const recalls = await Promise.allSettled([
    call('hot', user, { timeout: 50, quota: 200 }),    // 每路超时 + 配额
    call('cf', user, { timeout: 80, quota: 200 }),
    call('vec', user, { timeout: 100, quota: 300 }),
  ]);
  let candidates = mergeDedup(recalls.map(orEmpty));   // 部分成功合并（SCN-NODE-729）
  if (!candidates.length) candidates = hotFallback();  // 冷启动兜底（SCN-NODE-659）
  let ranked;
  try { ranked = await rank(candidates.slice(0, 500), { timeout: 100 }); }
  catch { ranked = coarseRank(candidates); }           // 精排挂退化粗排（降级链）
  return rerank(ranked, { diversity: { maxPerShop: 3 }, traceId: ctx.traceId });   // 打散 + 归因
}
```

**评分点**:
- 多路并行配额（超时+quota——SCN-NODE-659 部分成功）。
- 精排失败退化粗排（降级链——结果不空）。
- 冷启动热门兜底（SCN-NODE-832 对应）。
- traceId 贯穿重排（曝光归因闭环——SCN-联想-807）。
