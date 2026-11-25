---
title: [ZSM-696] 笔试：手写在场状态 presence 引擎（TTL 清理 + 节流广播 + idle 分级）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-696：手写在场状态 presence 引擎（TTL 清理 + 节流广播 + idle 分级）
**答**：实现 `createPresence()`：1) `update(partial)`：本地状态更新 + 节流广播（30ms 合并，只发最终值）；2) `receive(peer)`：远端成员状态合并（同用户只保留最新，lastSeen 取 max）；3) `snapshot()`：活跃/空闲/僵尸三级过滤——active（idle 内）、idle（超 idle 未超 ttl，灰显）、移除（超 ttl）；4) `leave()` 广播 + 本地清除；5) 定时巡检（interval）驱动分级变化并通知；6) 附用例：节流合并、僵尸清理与分级变化通知。

```javascript
function createPresence({ broadcast, idleMs = 5000, ttlMs = 10000, notify } = {}) {
  const me = { id: 'self', data: {}, dirty: false }
  const peers = new Map()       // userId -> { data, lastSeen, level }
  let throttle = null

  function update(partial) {
    me.data = { ...me.data, ...partial }
    me.dirty = true
    clearTimeout(throttle)
    throttle = setTimeout(() => {   // 30ms 节流：只发最终值
      if (!me.dirty) return
      me.dirty = false
      broadcast({ type: 'update', id: me.id, data: me.data, ts: Date.now() })
    }, 30)
  }

  function receive({ id, data, ts }) {
    if (id === me.id) return
    const p = peers.get(id) ?? { data: {}, lastSeen: 0, level: 'active' }
    // 同用户合并：只保留最新（数据新者胜 + lastSeen 取 max）
    if (ts >= p.lastSeen) p.data = data
    p.lastSeen = Math.max(p.lastSeen, ts)
    p.level = 'active'
    peers.set(id, p)
    notify?.(snapshot())
  }

  function leave() {
    broadcast({ type: 'leave', id: me.id })
    peers.clear()                   // 本地清除
    notify?.(snapshot())
  }

  function snapshot(now = Date.now()) {
    const out = { active: [], idle: [], removed: [] }
    for (const [id, p] of peers) {
      const age = now - p.lastSeen
      const newLevel = age <= idleMs ? 'active' : age <= ttlMs ? 'idle' : 'removed'
      if (newLevel !== p.level) { p.level = newLevel; notify?.(snapshot(now)) }   // 分级变化通知
      if (newLevel === 'removed') peers.delete(id)
      else out[newLevel].push({ id, ...p.data })
    }
    return out
  }

  // 定时巡检：驱动分级变化
  const timer = setInterval(() => snapshot(), 1000)

  function destroy() { clearInterval(timer); clearTimeout(throttle); leave() }

  return { update, receive, leave, snapshot, destroy }
}

// 用例（虚拟时钟）
let t = Date.now()
const events = []
const p = createPresence({
  broadcast: (m) => events.push(m),
  idleMs: 5000, ttlMs: 10000,
  notify: (s) => events.push({ type: 'notify', active: s.active.length, idle: s.idle.length }),
})
// 节流合并
p.update({ cursor: 1 })
p.update({ cursor: 2 })
p.update({ cursor: 3 })
setTimeout(() => console.log(events.filter((e) => e.type === 'update').length), 50)  // 1：只发最终值

// 远端接收 + 分级
p.receive({ id: 'u1', data: { cursor: 5 }, ts: t })
p.receive({ id: 'u1', data: { cursor: 9 }, ts: t + 100 })   // 新数据胜出
console.log(p.snapshot(t).active.length)      // 1
console.log(p.snapshot(t + 6000).idle.length) // 1：超 idle 灰显
console.log(p.snapshot(t + 11000).active.length + p.snapshot(t + 11000).idle.length)  // 0：超 ttl 移除
p.destroy()
```
**评分点**：
- 节流广播只发最终值（30ms 合并，dirty 标志）
- 同用户合并语义（数据新者胜 + lastSeen max）
- 三级分级（active/idle/removed）与变化通知
- 定时巡检 + destroy 清理（interval 不泄漏）
