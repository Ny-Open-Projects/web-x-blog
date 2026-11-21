---
title: [ZSM-102] 解释 SWR 名字里的 stale-while-revalidate 策略，一次完整请求生命周期发生了什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-102：解释 SWR 名字里的 stale-while-revalidate 策略，一次完整请求生命周期发生了什么？
**答**：
- 它借用了 HTTP Cache-Control 的 `stale-while-revalidate` 响应头语义：缓存过期后不阻塞用户，先吐旧值，同时在后台拉新值，新值到了再静默替换。
- 生命周期：组件挂载 → 读 key 对应缓存 → 有缓存立即渲染旧 data（state 为 revalidating）→ 发起 revalidate（去重窗口内的重复请求直接复用）→ 响应落地用深比较（结构共享）决定是否触发重渲染 → 缓存更新并广播给所有订阅该 key 的组件。
- 没有缓存时才真正 isLoading，所以「首屏 loading」和「二次进入闪 loading」被天然区分开。
- 追问钩子：这个策略的代价是可能短暂展示过期数据，对价格、库存这类强一致数据要配 `revalidateIfStale: true` + 短 dedupingInterval，甚至禁用缓存兜底。

```javascript
// 伪代码：SWR 内核的取数决策
async function fetchFor(key) {
  const cacheItem = cache.get(key)
  if (cacheItem && !isStale(cacheItem)) return cacheItem.data  // 新鲜：直接用
  if (cacheItem) emit({ data: cacheItem.data, isValidating: true }) // 吐旧值
  if (inflight.has(key)) return inflight.get(key)              // 请求去重
  const p = fetcher(key).then(data => {
    if (!shallowEqual(data, cacheItem?.data)) emit({ data })   // 结构共享防抖渲染
    cache.set(key, { data, ts: Date.now() })
    inflight.delete(key)
    return data
  })
  inflight.set(key, p)
  return p
}
```
