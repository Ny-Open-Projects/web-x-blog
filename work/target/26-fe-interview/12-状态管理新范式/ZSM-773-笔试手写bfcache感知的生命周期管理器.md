---
title: [ZSM-773] 笔试：手写 bfcache 感知生命周期管理器（冻结恢复 + 会话校验）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-773：手写 bfcache 感知生命周期管理器（冻结恢复 + 会话校验 + 不阻断缓存）
**答**：实现 `createBfcacheManager({ hooks })`：1) `pagehide(persisted)` 冻结钩子：执行注册的 cleanup（flush/断连/暂停）——**不注册 unload**（保住 bfcache 资格）；2) `pageshow(persisted=true)` 恢复钩子：依次执行 hooks.onRestore（重连/追平/revalidate），并做**会话校验**（校验失败触发 onSessionInvalid）；3) 恢复去重：pageshow 可能在非 bfcache 恢复（persisted=false）时不执行恢复逻辑；4) `bfcacheEligible()`：静态自查（有无 unload 监听/未断的 WS——用于 dev 警告）；5) 附用例：冻结→恢复链执行与持久标志区分。

```javascript
function createBfcacheManager({ hooks = {}, checkSession } = {}) {
  const cleanups = []
  const restoreHooks = []
  const listeners = new Set()

  function onFreeze(fn) { cleanups.push(fn) }        // pagehide persisted=true
  function onRestore(fn) { restoreHooks.push(fn) }   // pageshow persisted=true

  function attach() {
    // 只用 pagehide/pageshow：不碰 unload（保 bfcache）
    window.addEventListener('pagehide', async (e) => {
      if (!e.persisted) return                     // 真关闭：交给浏览器默认
      notify('freeze')
      for (const fn of cleanups) {
        try { await fn() } catch (err) { console.error('[bfcache freeze]', err) }
      }
    })
    window.addEventListener('pageshow', async (e) => {
      if (!e.persisted) return                     // 非 bfcache 恢复（首次/普通后退）：跳过
      notify('restore')
      // 会话校验：冻结期间可能已登出
      if (checkSession) {
        const valid = await checkSession().catch(() => false)
        if (!valid) { hooks.onSessionInvalid?.(); return }
      }
      for (const fn of restoreHooks) {
        try { await fn() } catch (err) { console.error('[bfcache restore]', err) }
      }
    })
  }

  function bfcacheEligible() {
    // 静态自查：dev 警告用
    const issues = []
    if (typeof wsClient !== 'undefined' && wsClient.isConnected?.()) issues.push('ws-not-closed-on-freeze')
    if (window.__hasUnloadListener) issues.push('unload-listener-registered')
    return { eligible: issues.length === 0, issues }
  }

  function notify(kind) { listeners.forEach((fn) => fn(kind)) }

  return { onFreeze, onRestore, attach, bfcacheEligible, subscribe: (fn) => (listeners.add(fn), () => listeners.delete(fn)) }
}

// 用例（jsdom 模拟）
const events = []
const mgr = createBfcacheManager({
  hooks: { onSessionInvalid: () => events.push('session-invalid') },
  checkSession: async () => true,
})
mgr.onFreeze(() => events.push('flush-queue'))
mgr.onFreeze(() => events.push('close-ws'))
mgr.onRestore(() => events.push('reconnect-ws'))
mgr.onRestore(() => events.push('revalidate'))
mgr.attach()
mgr.subscribe((kind) => events.push(`event:${kind}`))

// 模拟冻结
const freezeEvt = new Event('pagehide')
Object.defineProperty(freezeEvt, 'persisted', { value: true })
window.dispatchEvent(freezeEvt)
await new Promise((r) => setTimeout(r, 10))
console.log(events)
// ['event:freeze', 'flush-queue', 'close-ws']：冻结钩子链

// 模拟 bfcache 恢复
const showEvt = new Event('pageshow')
Object.defineProperty(showEvt, 'persisted', { value: true })
window.dispatchEvent(showEvt)
await new Promise((r) => setTimeout(r, 10))
console.log(events.at(-2), events.at(-1))   // 'event:restore' 'revalidate'（链尾）

// 非 bfcache 恢复：不执行
const normalEvt = new Event('pageshow')
Object.defineProperty(normalEvt, 'persisted', { value: false })
window.dispatchEvent(normalEvt)
console.log(events.filter((e) => e === 'event:restore').length)   // 1：未重复执行
```
**评分点**：
- 只用 pagehide/pageshow（不碰 unload，保 bfcache 资格）
- persisted 标志区分（真恢复 vs 普通导航）
- 恢复前会话校验（冻结期间登出的防御）
- 钩子链错误隔离（单钩子失败不影响其他）
