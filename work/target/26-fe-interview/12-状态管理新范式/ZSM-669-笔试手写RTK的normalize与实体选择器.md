---
title: [ZSM-669] 笔试：手写 createEntityAdapter（归一化 CRUD + 排序 selector）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-669：手写 createEntityAdapter（归一化 CRUD + 排序 selector）
**答**：实现 `createEntityAdapter({ selectId, sortComparer })` 返回 adapter + 状态形状 `{ ids, entities }`：1) `addOne(state, entity)`：插入并按 sortComparer 重排 ids；2) `updateOne(state, { id, changes })`：patch 合并后重排；3) `removeOne/removeAll/setAll`；4) `upsertMany`：存在更新不存在插入（批量一次重排）；5) `getSelectors(stateFn)`：selectById/selectAll/selectTotal；6) 附用例：验证排序维护与 upsertMany 原子性。

```javascript
function createEntityAdapter({ selectId = (e) => e.id, sortComparer = null } = {}) {
  function reSort(state) {
    if (sortComparer) state.ids.sort((a, b) => sortComparer(state.entities[a], state.entities[b]))
    return state
  }

  const adapter = {
    getInitialState(extra = {}) {
      return { ids: [], entities: {}, ...extra }
    },
    addOne(state, entity) {
      const id = selectId(entity)
      if (!state.entities[id]) state.ids.push(id)
      state.entities[id] = entity
      return reSort(state)
    },
    setAll(state, entities) {
      state.ids = entities.map(selectId)
      state.entities = Object.fromEntries(entities.map((e) => [selectId(e), e]))
      return reSort(state)
    },
    updateOne(state, { id, changes }) {
      const cur = state.entities[id]
      if (!cur) return state
      state.entities[id] = { ...cur, ...changes }   // 不可变 patch
      return reSort(state)                          // 更新后重排
    },
    removeOne(state, id) {
      delete state.entities[id]
      state.ids = state.ids.filter((i) => i !== id)
      return state
    },
    removeAll(state) { state.ids = []; state.entities = {}; return state },
    upsertMany(state, entities) {
      // 批量：一次重排（原子性）
      entities.forEach((e) => {
        const id = selectId(e)
        if (state.entities[id]) state.entities[id] = { ...state.entities[id], ...e }
        else { state.entities[id] = e; state.ids.push(id) }
      })
      return reSort(state)
    },
    getSelectors(stateFn) {
      return {
        selectIds: (s) => stateFn(s).ids,
        selectEntities: (s) => stateFn(s).entities,
        selectAll: (s) => stateFn(s).ids.map((id) => stateFn(s).entities[id]),
        selectTotal: (s) => stateFn(s).ids.length,
        selectById: (s, id) => stateFn(s).entities[id],
      }
    },
  }
  return adapter
}

// 用例
const adapter = createEntityAdapter({
  sortComparer: (a, b) => b.score - a.score,   // 分数降序
})
let state = adapter.getInitialState({ loading: 'idle' })

state = adapter.addOne(state, { id: 'a', score: 10 })
state = adapter.addOne(state, { id: 'b', score: 30 })
state = adapter.addOne(state, { id: 'c', score: 20 })
console.log(state.ids)                                  // ['b','c','a']：降序
state = adapter.updateOne(state, { id: 'a', changes: { score: 99 } })
console.log(state.ids)                                  // ['a','b','c']：更新后重排
state = adapter.upsertMany(state, [{ id: 'd', score: 50 }, { id: 'b', score: 40 }])
console.log(state.ids)                                  // ['a','d','b','c']：一次重排

const sel = adapter.getSelectors((s) => s)
console.log(sel.selectById(state, 'c'))                 // { id: 'c', score: 20 }
console.log(sel.selectTotal(state))                     // 4
```
**评分点**：
- ids/entities 双结构维护（删除/更新同步 ids）
- sortComparer 在插入与更新后自动重排
- upsertMany 批量单次重排（原子性，省 N-1 轮通知）
- getSelectors 生成完整查询集（引用稳定依赖双结构）
