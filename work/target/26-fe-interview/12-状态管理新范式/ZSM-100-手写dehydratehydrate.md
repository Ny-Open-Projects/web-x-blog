---
title: [ZSM-100] 笔试：手写简化版 dehydrate/hydrate（缓存序列化与新鲜度恢复）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-100：手写简化版 dehydrate/hydrate（缓存序列化与新鲜度恢复）

**答**：
- dehydrate：把缓存 Map 序列化为 `{ entries: [{ key, data, ts }] }`，只序列化可 JSON 化的 data。
- hydrate：把 entries 灌回缓存；恢复时保留原 ts（新鲜度随时间迁移），不覆盖客户端已有**更新**的数据（客户端 ts 更新则跳过）。
- 说明 staleTime 在两端如何统一生效。

```javascript
export function dehydrate(cache) {
  const entries = []
  for (const [kstr, e] of cache) {
    if (e.error) continue                    // 错误态不传输
    try {
      entries.push({ key: JSON.parse(kstr), data: e.data, ts: e.ts }) // 校验可序列化
    } catch { /* 不可序列化数据跳过 */ }
  }
  return JSON.stringify({ entries })
}

export function hydrate(cache, dehydrated, staleTime = 0) {
  const { entries } = JSON.parse(dehydrated)
  for (const { key, data, ts } of entries) {
    const kstr = JSON.stringify(key)
    const local = cache.get(kstr)
    // 客户端已有更新数据则不覆盖
    if (local && local.ts >= ts) continue
    cache.set(kstr, { data, ts }) // 保留服务端时间戳
    // 新鲜度：Date.now() - ts < staleTime 的条目客户端直接复用不重取
  }
}
```

**评分点**：
- 序列化容错：错误态、不可序列化数据跳过而非抛错。
- hydrate 的「新者胜」：比较 ts 避免客户端已交互的数据被服务端旧值覆盖。
- 保留服务端 ts 使 staleTime 跨端一致（而不是 hydrate 时刷新时间戳）。
- 能口述 SSR 双端 key 必须一致，否则 hydrate 全 miss。
