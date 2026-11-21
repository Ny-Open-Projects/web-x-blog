---
title: [MFW-303] Data Cache 的自建后端（Redis 化 revalidateTag）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-303：Data Cache 私有化

**答**:
- 动机：托管缓存（Vercel）不可用/成本/合规——自建 fetch 缓存后端（Redis），语义对齐 revalidateTag
- 实现：自定义 cache handler（Next 暴露接口）：get/set 按生成的缓存 key 写 Redis（值含 tags 集合与时间戳）；revalidateTag → 扫 tag 索引（ZSET tag→keys）删成员并 bump 代纪（key 内嵌代纪，代纪不符即 miss——免全扫）
- 正确性要点：代纪（generation）机制让失效 O(1)（不删值只换代——旧值自然过期被代纪拒之门外）；跨实例时钟用 Redis TIME 为准
- 取舍：自建后端 = 接管正确性责任（竞态/时钟/容量）——收益是控制力与成本，代价是一条必须长期维护的子系统

```javascript
// 自定义 handler 核心：代纪失效
async function revalidateTag(tag) {
  await redis.incr(`gen:${tag}`)                    // O(1) 换代
}
async function get(key, { tags }) {
  const rec = await redis.get(`c:${key}`)
  for (const t of tags) if (await genOf(t) !== rec.gens[t]) return null   // 代纪不符 = 失效
  return rec.data
}
```
