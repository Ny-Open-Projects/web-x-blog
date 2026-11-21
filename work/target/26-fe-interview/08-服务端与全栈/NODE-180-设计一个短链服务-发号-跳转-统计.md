---
title: [NODE-180] 设计一个短链服务（发号/跳转/统计）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-180：设计一个短链服务（发号/跳转/统计）？
**答**：
- 与 NODE-071 互补，本题聚焦**跳转链路性能与统计**：发号用号段模式（一次取 1000 个号，DB 压力降千倍）；跳转走本地 LRU → Redis 两级，302 保持可统计。
- 301 vs 302：301 浏览器永久缓存不再回源（统计丢失），需要统计选 302。
- 统计异步化：跳转路径只做 302 + 投递统计事件，绝不同步写库；PV/UV（HyperLogLog 去重）/来源/时段离线聚合。
- 防刷：同 IP+code 窗口去重；黑名单域名在创建时校验（防短链跳钓鱼）。

```javascript
async function shorten(longUrl) {
  assertSafeDomain(longUrl);                        // 黑名单域名校验
  const id = await idSegment.next();                // 号段模式批量取号
  const code = base62(id);                          // 62 进制紧凑编码
  await redis.set(`u:${code}`, longUrl);
  localLRU.set(code, longUrl);                      // 本地 LRU 二级
  return { code, url: `https://s.example.com/${code}` };
}

app.get('/:code', async (ctx) => {
  const url = localLRU.get(ctx.params.code) ?? await redis.get(`u:${ctx.params.code}`);
  if (!url) ctx.throw(404);
  ctx.status = 302;                                 // 302 保留统计能力
  ctx.set('location', url);
  statsQueue.add('hit', {                           // 统计异步化，不挡跳转
    code: ctx.params.code, referer: ctx.get('referer'),
    ua: ctx.get('user-agent'), ip: ctx.ip,
  }, { removeOnComplete: 1000 });
});
// 统计聚合：PV 计数器 + UV 用 PFADD/PFCOUNT（HyperLogLog，12KB 扛亿级去重）
```
