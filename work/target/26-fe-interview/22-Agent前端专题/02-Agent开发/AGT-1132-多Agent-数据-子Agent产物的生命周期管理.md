---
title: [1132] 子 Agent 产出的中间产物（diff/草稿/检索结果）怎么管理
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 数据]
type: 面试题
---

## 1132：子 Agent 产出的中间产物（diff/草稿/检索结果）怎么管理

**答**：
- 生命周期：产物分级——最终产物长期留存（供审计与复用）、关键中间产物保留一个复盘期（7~30 天）、临时产物（草稿迭代）会话结束即清理；分级规则进资产策略而不是各 Agent 自定。
- 存储形态：产物进对象存储 + 元数据入索引（谁产、何时、属于哪个任务、被谁引用），引用计数决定「想删但还被引用」的延迟删除。
- 产物复用：相似任务的中间产物（如同一库的检索结果）按内容 hash 复用，避免重复劳动——中间产物不是垃圾，是缓存。
- 追问钩子：产物里有敏感数据怎么办？——产物入库前过同一套 DLP（与输出防线同级），存储按密级分区，清理任务也要清理敏感分区。

```ts
async function saveArtifact(art, { tier }) {
  const safe = await dlp.scan(art.content);       // 入库前 DLP
  const id = await store.put(safe, { acl: tierAcl(tier) });
  meta.add({ id, task: ctx.taskId, by: ctx.agent, refs: 0, tier,
    expireAt: tierTtl(tier) });                   // 分级 TTL
  return id;
}
async function gc() {
  const expired = await meta.expired();
  for (const m of expired) if (m.refs === 0) await store.del(m.id); // 引用计数
}
```

