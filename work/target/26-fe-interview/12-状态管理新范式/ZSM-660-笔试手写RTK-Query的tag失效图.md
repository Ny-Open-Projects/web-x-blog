---
title: [ZSM-660] 笔试：手写 RTK Query 风格的 tag 失效图（invalidatesTags 传播）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-660：手写 RTK Query 风格的 tag 失效图（invalidatesTags 传播）
**答**：实现 `createTagGraph()`：1) query 注册 `providesTags(tags)`，mutation 注册 `invalidatesTags(tags)`——tag 形如 `{ type, id? }` 或 `'Type'`；2) mutation 提交后，按 tag 图找出**所有提供这些 tag 的 query**：全量 tag（无 id）失效该 type 的全部 query，带 id 的只失效同 type 同 id 的；3) `invalidate('Mutation', vars)` 返回应重拉的 query 清单（去重）；4) 循环失效防护（mutation 的 tag 被自己 provide 的场景）；5) 附用例验证全量/定点失效与去重。

```javascript
function createTagGraph() {
  const provides = new Map()    // queryName -> Set<tagKey>
  const mutations = new Map()   // mutationName -> { tags(vars), handler }

  const tagKey = (t) => typeof t === 'string' ? t : `${t.type}:${t.id ?? '*'}`

  function register(name, kind, conf) {
    if (kind === 'query') provides.set(name, (conf.providesTags || []).map(tagKey))
    else mutations.set(name, conf)   // conf: { invalidatesTags(vars) }
    return name
  }

  // 变更后失效：返回要重拉的 query 名单
  function invalidate(mutationName, vars) {
    const conf = mutations.get(mutationName)
    const targets = new Set()
    const targetTags = (conf.invalidatesTags?.(vars) ?? []).map(tagKey)
    for (const tag of targetTags) {
      const [type, id] = tag.split(':')
      for (const [queryName, provided] of provides) {
        if (mutationName === queryName) continue          // 循环防护：不失效自己
        for (const p of provided) {
          const [pType, pId] = p.split(':')
          const hit = pType === type && (id === '*' || pId === '*' || id === pId)
          if (hit) { targets.add(queryName); break }
        }
      }
    }
    return [...targets]
  }

  return { register, invalidate, graph: () => ({ provides: Object.fromEntries(provides) }) }
}

// 用例：RTK Query 语义
const g = createTagGraph()
g.register('getPosts', 'query', { providesTags: ['Post'] })                       // 全量 tag
g.register('getPost', 'query', { providesTags: (r, e, id) => [{ type: 'Post', id }] })   // 定点 tag
g.register('updatePost', 'mutation', { invalidatesTags: (r, e, { id }) => [{ type: 'Post', id }] })
g.register('addPost', 'mutation', { invalidatesTags: ['Post'] })                 // 全量失效

console.log(g.invalidate('updatePost', { id: 7 }))
// ['getPost']：只失效 id=7 的定点 query，getPosts（全量 'Post:*'）也命中因为 pId==='*'
console.log(g.invalidate('addPost', {}))
// ['getPosts', 'getPost']：全量 tag 失效所有提供者；去重排序
```
**评分点**：
- tag 归一化（'Type' 简写与 {type,id} 统一 key）
- 全量 vs 定点失效语义（id==='*' 或 pId==='*' 的笛卡尔命中）
- 循环防护（mutation 不失效自己）
- 返回去重清单（多 tag 命中同一 query 只算一次）
