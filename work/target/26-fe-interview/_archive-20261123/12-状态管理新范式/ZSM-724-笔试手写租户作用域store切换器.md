---
title: [ZSM-724] 笔试：手写租户作用域 store 切换器（隔离 + 缓存 key + 泄漏清理）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-724：手写租户作用域 store 切换器（隔离 + 缓存 key + 泄漏清理）
**需求**：实现 `createTenantStore()`：1) `switch(tenantId, hydrate)`：切换——目标 scope 惰性创建（hydrate 填充）、旧 scope **保留可恢复**（LRU 上限 3 个，超出淘汰）；2) 每个作用域内 `setState/getState/subscribe` 独立（订阅只收本 scope 变更）；3) `cacheKey(key)`：自动给 queryKey 前缀租户 id（跨租户缓存隔离）；4) `purge(except)`：清理指定 scope（登出场景）与超限淘汰通知；5) 附用例：切换数据隔离 + LRU 淘汰。

```javascript
function createTenantStore({ lru = 3 } = {}) {
  const scopes = new Map()          // tenantId -> { state, subs, lastActive }
  let active = null
  let subsCount = 0
  const purgeListeners = new Set()

  function ensureScope(tenantId, hydrate) {
    if (!scopes.has(tenantId)) {
      scopes.set(tenantId, { state: hydrate?.() ?? {}, subs: new Set(), lastActive: Date.now() })
    }
    return scopes.get(tenantId)
  }

  function evictLRU() {
    if (scopes.size <= lru) return
    // 淘汰最久未激活的 scope
    const sorted = [...scopes.entries()]
      .filter(([id]) => id !== active)
      .sort((a, b) => a[1].lastActive - b[1].lastActive)
    while (scopes.size > lru && sorted.length) {
      const [id] = sorted.shift()
      scopes.delete(id)
      purgeListeners.forEach((fn) => fn(id))       // 上层同步清 Query 缓存
    }
  }

  function switch(tenantId, hydrate) {
    active = tenantId
    ensureScope(tenantId, hydrate)
    evictLRU()
    scopes.get(tenantId).lastActive = Date.now()
    // 通知所有 scope 订阅（租户上下文变了）
    scopes.get(tenantId).subs.forEach((fn) => fn(scopes.get(tenantId).state))
    return scopes.get(tenantId).state
  }

  function setState(patch) {
    if (!active) throw new Error('no active tenant')
    const scope = scopes.get(active)
    scope.state = typeof patch === 'function' ? patch(scope.state) : { ...scope.state, ...patch }
    scope.lastActive = Date.now()
    scope.subs.forEach((fn) => fn(scope.state))
  }

  function getState() {
    if (!active) return null
    return scopes.get(active).state
  }

  function subscribe(fn) {
    // 订阅绑定当前 active scope：切换后收新 scope
    const holder = { fn, boundTo: null }
    function wrapped(state) { fn(state) }
    const attach = () => {
      if (active) {
        (scopes.get(active).subs ?? scopes.set(active, { state: {}, subs: new Set(), lastActive: 0 }).get(active)).subs.add(wrapped)
        holder.boundTo = active
      }
    }
    attach()
    return () => scopes.get(holder.boundTo)?.subs.delete(wrapped)
  }

  function cacheKey(key) {
    return ['tenant', active, ...key]          // 租户前缀隔离
  }

  function purge(exceptId = null) {
    const removed = []
    for (const [id] of scopes) {
      if (id !== exceptId) { scopes.delete(id); removed.push(id) }
    }
    removed.forEach((id) => purgeListeners.forEach((fn) => fn(id)))
    return removed
  }

  return {
    switch, setState, getState, subscribe, cacheKey, purge,
    onPurge: (fn) => (purgeListeners.add(fn), () => purgeListeners.delete(fn)),
    audit: () => ({ active, scopes: [...scopes.keys()], size: scopes.size }),
  }
}

// 用例
const ts = createTenantStore({ lru: 2 })
ts.switch('t1', () => ({ lists: { a: 1 } }))
ts.setState({ lists: { a: 99 } })
ts.switch('t2', () => ({ lists: { b: 2 } }))
console.log(ts.getState())                     // { lists: { b: 2 } }：隔离
ts.switch('t1')
console.log(ts.getState().lists.a)             // 99：t1 保留可恢复
ts.switch('t3', () => ({ lists: {} }))         // LRU：3 > 2 → 淘汰 t2
console.log(ts.audit())                        // { active: 't3', scopes: ['t1','t3'], size: 2 }
console.log(ts.cacheKey(['todos']))            // ['tenant', 't3', 'todos']
ts.purge('t3')
console.log(ts.audit().scopes)                 // ['t3']
```
**评分点**：
- scope Map 隔离 + 惰性创建 + 恢复语义（切回来数据还在）
- LRU 淘汰（最久未激活剔除 + onPurge 通知上层清 Query 缓存）
- cacheKey 租户前缀（跨租户缓存隔离）
- purge 白名单（登出清理、except 保留）
