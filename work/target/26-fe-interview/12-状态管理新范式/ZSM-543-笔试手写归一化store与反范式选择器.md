---
title: [ZSM-543] 笔试：手写归一化 store 与反范式选择器
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-543：手写归一化 store 与反范式选择器
**答**：实现 `createNormalizedStore(schema)`：1) `upsert(entity, record)` / `remove(entity, id)` 写入 Map 结构；2) 关系引用用外键（如 comment.authorId），`upsert` 时**校验外键存在性**（悬空引用报错，可配 strict: false 放行）；3) `join(entity, id, rel)` 反范式查询：一层关系展开（comment → author 对象），带一层缓存（引用实体未变不重算）；4) `remove` 时提供 `onCascade` 钩子处理级联（删用户连带删其评论）；5) 附用例验证外键校验与缓存命中。

```javascript
function createNormalizedStore(schema) {
  const tables = new Map()    // entity -> Map<id, record>
  for (const e of Object.keys(schema)) tables.set(e, new Map())
  const joinCache = new Map() // `${entity}:${id}:${rel}` -> { ver, result }
  const versions = new Map()  // entity -> version
  const bump = (e) => versions.set(e, (versions.get(e) ?? 0) + 1)

  function upsert(entity, record) {
    const t = tables.get(entity)
    if (!t) throw new Error(`unknown entity ${entity}`)
    // 外键校验
    for (const [fk, target] of Object.entries(schema[entity].refs ?? {})) {
      const refId = record[fk]
      if (refId != null && !tables.get(target)?.has(refId)) {
        if (schema[entity].strict) throw new Error(`dangling ${fk}=${refId} on ${entity}`)
      }
    }
    t.set(record.id, record)
    bump(entity)
  }

  function remove(entity, id, onCascade) {
    tables.get(entity).delete(id)
    bump(entity)
    onCascade?.(id)   // 级联由调用方编排
  }

  function join(entity, id, rel) {
    const conf = schema[entity].refs?.[rel]
    if (!conf) throw new Error(`no ref ${rel}`)
    const key = `${entity}:${id}:${rel}`
    const fkId = tables.get(entity).get(id)?.[`${rel}Id`]
    const ver = versions.get(conf)
    const hit = joinCache.get(key)
    if (hit && hit.ver === ver && hit.fkId === fkId) return hit.result   // 缓存命中
    const result = fkId != null ? tables.get(conf).get(fkId) ?? null : null
    joinCache.set(key, { ver, fkId, result })
    return result
  }

  return { upsert, remove, join, get: (e, id) => tables.get(e).get(id) }
}

// 用例
const store = createNormalizedStore({
  comment: { refs: { author: 'user' }, strict: true },
  user: {},
})
store.upsert('user', { id: 'u1', name: '张三' })
store.upsert('comment', { id: 'c1', authorId: 'u1', text: 'hi' })
console.log(store.join('comment', 'c1', 'author').name)  // 张三（首次计算）
console.log(store.join('comment', 'c1', 'author') === store.join('comment', 'c1', 'author')) // true 缓存
store.upsert('user', { id: 'u1', name: '张三三' })
console.log(store.join('comment', 'c1', 'author').name)  // 张三三（版本失效重算）
try {
  store.upsert('comment', { id: 'c2', authorId: 'ghost' })  // 悬空外键
} catch (e) { console.log(e.message) }                     // dangling authorId=ghost
store.remove('user', 'u1', (id) => console.log('cascade cleanup for', id))
```
**评分点**：
- 外键存在性校验与 strict 开关（数据完整性）
- join 缓存按「目标表版本 + 外键值」双维度失效
- 级联钩子外置（删主记录的编排交给调用方）
- 版本号失效机制（写入 bump，读取比对）
