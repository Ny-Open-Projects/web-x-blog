---
title: [ARC-282] 灰度期间的 CDN 与缓存一致性如何保证？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-282：灰度期间的 CDN 与缓存一致性如何保证？
**答**：
- 核心问题：灰度决策发生在 HTML 层（ARC-276），但 HTML 被 CDN/浏览器缓存后，灰度比例会"漂移"（缓存里的旧版本持续返回）。
- 方案：HTML 不做长缓存——CDN 层用**短 TTL（如 30~60s）+ 缓存 key 不含灰度因子**，比例变化最多延迟一个 TTL 生效；版本内部产物（js/css）immutable 长缓存不受影响。
- 更彻底：把灰度决策放**边缘计算**（Cloudflare Workers/边缘节点按请求实时决策），HTML 每次请求边缘动态生成，比例实时生效。
- 一致性校验：定时抽样边缘节点返回的版本分布，与配置比例对比（对账 ARC-279），发现漂移告警并主动刷新缓存（软清除）。

```typescript
// 边缘函数灰度（每次请求实时决策）
export default {
  async fetch(req, env) {
    const uid = getCookie(req, 'uid');
    const v = bucket(uid, env.grayRatio);                    // 环境变量存比例，改配置即时生效
    const html = await env.ASSETS.fetch(`/builds/${v}/index.html`);
    return new Response(html.body, { headers: { 'Cache-Control': 'private, no-store',
      'Set-Cookie': `__build=${v}` } });                     // 浏览器端也不缓存 HTML，保持灰度实时性
  },
};
// 对账：cron 抽样 50 个边缘节点 → 版本分布 vs grayRatio → 偏差 > 5% → purgeCache()
```
