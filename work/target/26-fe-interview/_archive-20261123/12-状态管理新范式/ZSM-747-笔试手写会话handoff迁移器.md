---
title: [ZSM-747] 笔试：手写会话 handoff 迁移器（分级恢复 + 所有权转移 + 双活防御）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-747：手写会话 handoff 迁移器（分级恢复 + 所有权转移 + 双活防御）
**需求**：实现 `createHandoff()`：1) `export()`：会话快照 `{ schemaVersion, takenAt, route, position, draft }`（位置类/草稿类标记 transferable: 'auto'|'confirm'）；2) `import(snap, { confirm })`：按 transferable 分级恢复——auto 直接应用、confirm 经确认回调通过才应用；过期（5min）与版本不符走 migrate/拒绝；3) 所有权：import 后写 `ownerDevice`，源端 `saveDraft` 检查 ownership 被转移则拒绝并清空本地草稿（防双活）；4) 附用例：分级恢复 + 双活拦截。

```javascript
const SCHEMA = 2
const TTL = 5 * 60000

function createHandoff({ now = Date.now, confirmFn } = {}) {
  let ownerDevice = 'self'
  const drafts = new Map()     // key -> draft 内容

  function export() {
    return {
      schemaVersion: SCHEMA,
      takenAt: now(),
      ownerDevice,
      items: [
        { kind: 'route', value: '/docs/123', transferable: 'auto' },
        { kind: 'position', value: { anchorId: 'para-7', ratio: 0.3 }, transferable: 'auto' },
        { kind: 'draft', key: 'comment', value: drafts.get('comment') ?? null, transferable: 'confirm' },
      ],
    }
  }

  async function importSnap(snap) {
    if (now() - snap.takenAt > TTL) throw new Error('HANDOFF_EXPIRED')
    if (snap.schemaVersion !== SCHEMA) snap = migrate(snap)
    const applied = { auto: [], pending: [] }
    for (const item of snap.items) {
      if (item.transferable === 'auto') {
        applyItem(item)
        applied.auto.push(item.kind)
      } else {
        const ok = await confirmFn?.(item)
        if (ok) { applyItem(item); applied.auto.push(item.kind) }
        else applied.pending.push(item.kind)      // 用户拒绝：不应用
      }
    }
    // 所有权转移：源端写操作将被拒
    ownerDevice = snap.ownerDevice === 'self' ? 'target' : snap.ownerDevice
    return applied
  }

  function applyItem(item) {
    if (item.kind === 'draft' && item.value) drafts.set(item.key, item.value)
    // route/position 由调用方渲染层消费（此处记录）
    if (item.kind === 'route' || item.kind === 'position') appliedTarget = item.value
  }

  let appliedTarget = null

  function saveDraft(key, value, fromDevice) {
    if (ownerDevice !== fromDevice) {
      // 双活防御：所有权已转移
      drafts.delete(key)                           // 清空本地草稿
      return { ok: false, reason: 'SESSION_TAKEN_OVER' }
    }
    drafts.set(key, value)
    return { ok: true }
  }

  function migrate(snap) {
    // v1 → v2：items 结构扁平化
    if (snap.schemaVersion === 1) {
      return { ...snap, schemaVersion: 2, items: snap.context?.items ?? [] }
    }
    return snap
  }

  return { export, import: importSnap, saveDraft, get ownerDevice() { return ownerDevice }, get target() { return appliedTarget } }
}

// 用例
let t = 0
const h = createHandoff({ now: () => t, confirmFn: async (item) => item.kind === 'draft' })
h.saveDraft('comment', '未完成的评论…', 'self')

const snap = h.export()
t += 1000
const applied = await h.importSnap(snap)
console.log(applied)                            // { auto: ['route','position'], pending: [] }（draft 经确认后也 auto）
console.log(h.target)                           // { anchorId: 'para-7', ratio: 0.3 }

// 双活防御：源端再保存被拒
const r = h.saveDraft('comment', '源端继续写…', 'self')
console.log(r)                                  // { ok: false, reason: 'SESSION_TAKEN_OVER' }

// 过期拒绝
const old = { ...snap, takenAt: t - 600000 }
try { await h.importSnap(old) } catch (e) { console.log(e.message) }   // HANDOFF_EXPIRED
```
**评分点**：
- transferable 分级（auto 直接恢复 / confirm 经确认）
- TTL 过期与版本 migrate 链
- 所有权转移 + 源端 save 拦截（双活防御，清本地草稿）
- applyItem 记录渲染层消费目标（协议与渲染解耦）
