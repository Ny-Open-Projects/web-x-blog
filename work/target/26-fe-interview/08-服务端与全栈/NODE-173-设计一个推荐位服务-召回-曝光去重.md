---
title: [NODE-173] 设计一个推荐位服务（召回/曝光去重）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-173：设计一个推荐位服务（召回/曝光去重）？
**答**：
- 工程链路：候选池（离线任务更新进 Redis Set）→ 在线召回 → 粗排（规则/模型分数）→ **曝光去重** → 批量取详情 → 展示埋点回流。
- 曝光去重：按用户按天记 Set（`exposed:{uid}:{day}`）；亿级规模换 BloomFilter（120MB 内存扛 1 亿 id，1% 误判换 10 倍内存节省）。
- 召回与排序分离：服务端只管工程层（去重、补位、降级），排序模型离线训练在线打分。
- 闭环：曝光/点击埋点回流 → 离线任务更新候选池与权重 → 次日生效。

```javascript
async function recommend(uid, { scene, size = 10 } = {}) {
  const [pool, exposed] = await Promise.all([
    redis.smembers(`rec:pool:${scene}`),             // 离线更新的候选池
    redis.smembers(`exposed:${uid}:${dayKey()}`),    // 当日已曝光
  ]);
  const items = pool
    .filter((id) => !exposed.includes(id))           // 曝光去重
    .sort(() => Math.random() - 0.5)                 // 粗排：随机占位，接模型时替换
    .slice(0, size);
  await redis.sadd(`exposed:${uid}:${dayKey()}`, ...items); // 预记曝光
  await redis.expire(`exposed:${uid}:${dayKey()}`, 86_400);
  return hydrate(items);                             // 批量取详情（NODE-048 聚合）
}
// 补位：去重后不足 size → 用热度榜兜底补齐；降级：召回失败直接返回热度榜
```
