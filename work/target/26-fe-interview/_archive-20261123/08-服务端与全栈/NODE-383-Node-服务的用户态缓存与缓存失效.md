---
title: [NODE-383] Node 服务的用户态（session/权限/购物车）缓存策略如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-383：用户态缓存策略
**答**:
- 三类用户态特征不同：session（高频读、失效即时性要求中——踢出延迟可容忍秒级）、权限（读极高频、变更要求准实时——ARC-223）、购物车（读写都频繁、要持久不丢）。
- session：Redis 主存（TTL + 续期滑动），内存微缓存 1~3s（高 QPS 会话校验降 Redis 压力，NODE-353）；踢出 = 删 Redis key，微缓存容忍短暂窗口。
- 权限：Redis 缓存 + 变更主动失效（Pub/Sub 广播，NODE-353）；版本号机制（用户权限版本号，变更 +1，请求带版本比对旧版失效——比全删精准）。
- 购物车：Redis 为主（hash 结构 skuId→qty），异步落库（防 Redis 故障丢数据）；Redis 不可用时降级直读 DB（性能降级但不丢）。
- 通用红线：用户态缓存 key 必须带用户维度（防串户，ARC-428）；敏感字段（支付密码哈希）不进缓存。
```javascript
// 权限版本号失效
async function getPerms(uid) {
  const ver = await redis.get(`perm:ver:${uid}`) ?? '0';        // 当前版本
  const cached = await redis.get(`perm:${uid}:${ver}`);          // 版本化 key
  if (cached) return JSON.parse(cached);
  const perms = await db.loadPerms(uid);
  await redis.set(`perm:${uid}:${ver}`, JSON.stringify(perms), 'EX', 300);
  return perms;
}
// 变更：await redis.incr(`perm:ver:${uid}`)  → 旧版本 key 自然过期，精准失效
```
