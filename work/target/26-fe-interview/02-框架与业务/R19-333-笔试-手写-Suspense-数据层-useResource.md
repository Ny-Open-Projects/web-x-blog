---
title: [R19-333] 笔试：手写 Suspense 数据层 useResource（promise 缓存 + 失效）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-333：笔试：手写 Suspense 数据层 useResource
**题**：实现 `useResource(fetcher, key)`：key→promise 的模块级缓存（同 key 并发共享一个 promise）；返回 use(promise) 的值；提供 invalidate(key) 清缓存使下次渲染重新取数；组件卸载不清缓存（跨组件共享）。

```javascript
const cache = new Map()
export function invalidate(key) { cache.delete(key) }
export function useResource(fetcher, key) {
  let entry = cache.get(key)
  if (!entry) {
    entry = fetcher(key).then(
      v => (entry.status = 'ok', entry.value = v),
      e => (entry.status = 'err', entry.reason = e)
    ).then(() => entry)
    entry = Object.assign(entry, { status: 'pending' })
    cache.set(key, entry)
  }
  if (entry.status === 'pending') throw entry
  if (entry.status === 'err') throw entry.reason
  return entry.value
}
// 组件内：
// const goods = useResource(id => fetchGoods(id), `goods:${id}`)
```
**评分点**：
- key 去重共享 promise。
- 三态挂到 entry（pending/ok/err），resolve 后不再 throw。
- invalidate 清缓存触发重新取数（配合 key 变化或强制刷新）。
- 模块级缓存的生命周期说明（SPA 内持久，需失效策略）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-72fec032-d07c-4dd9-9621-fbd08fb0e092-cwd'; fi
exit "$__zcode_status"
