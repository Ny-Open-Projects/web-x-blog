---
title: [ZSM-629] invalidateQueries 的失效传播：标记怎么精确命中 Query
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-629：invalidateQueries 的失效传播：标记怎么精确命中 Query

**答**：
- invalidateQueries 三步：1) 用过滤器（key 前缀匹配 / predicate 函数 / 精确 key）在 QueryCache 里找到目标 Query 集合；2) 给每个 Query 打 `state.isInvalidated = true`（标脏）；3) 对**有活跃 observer** 的 Query 立即触发 refetch；没有 observer 的只留标记，等下次挂载时被 shouldFetchOnMount 命中。
- key 匹配规则：前缀匹配——`invalidateQueries({ queryKey: ['todos'] })` 命中 `['todos', 1]`、`['todos', 'list', {page: 2}]` 全部；`exact: true` 才只匹配完全相等。数组元素按 hash 规则序列化比较（对象键序无关）。
- 失效粒度选择：变更多个相关视图时倾向**大前缀失效**（简单可靠）+ 依赖各自 staleTime 控制频率；性能敏感场景用 `predicate: (q) => q.queryKey[0] === 'todos' && q.state.data?.page === 2` 做运行时精确命中。
- `refetchQueries` vs `invalidateQueries`：前者不管 stale 直接拉，后者先标脏再按 refetchType 拉——`refetchType: 'none'` 只标脏不拉（等挂载时拉，适合后台预失效）。
- 追问钩子：invalidate 不会清除 data——旧数据保留用于渲染（后台刷新），「清空重来」要用 `removeQueries` 或 `resetQueries`。

```javascript
// 失效传播骨架
function invalidateQueries(client, filters = {}, options = {}) {
  const cache = client.getQueryCache()
  const matched = cache.findAll(filters)   // 前缀匹配 / predicate / exact

  const promises = []
  for (const query of matched) {
    query.state.isInvalidated = true       // ① 标脏（data 保留）
    if (query.observers.length > 0) {      // ② 有订阅者：立即拉
      const refetchType = options.refetchType ?? 'active'
      if (refetchType !== 'none') {
        promises.push(query.fetch({ cancelRefetch: options.cancelRefetch ?? true }))
      }
    }
    // ③ 无订阅者：标记留置，挂载时 shouldFetchOnMount 命中
  }
  return Promise.all(promises)
}

// 过滤器实现要点
function findAll({ queryKey, exact, predicate }) {
  return [...this.queries.values()].filter((q) => {
    if (queryKey && !partialMatchKey(q.queryKey, queryKey, exact)) return false
    if (predicate && !predicate(q)) return false
    return true
  })
}
function partialMatchKey(a, b, exact) {
  if (!exact && Array.isArray(a) && Array.isArray(b)) {
    return b.every((item, i) => partialMatchKey(a[i], item))
  }
  return JSON.stringify(hash(a)) === JSON.stringify(hash(b))   // hashKey 序列化（键排序）
}

// 用例
await queryClient.invalidateQueries({ queryKey: ['todos'] })          // 全部 todos 失效
await queryClient.invalidateQueries({ queryKey: ['todos', id] })      // 某条失效
await queryClient.invalidateQueries({ queryKey: ['todos'], refetchType: 'none' })  // 只标脏
```
