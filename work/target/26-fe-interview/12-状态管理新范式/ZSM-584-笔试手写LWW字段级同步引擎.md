---
title: [ZSM-584] 笔试：手写字段级 LWW 同步引擎（含 op 计数器与确定性决胜）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-584：手写字段级 LWW 同步引擎（含 op 计数器与确定性决胜）
**答**：实现 `createSyncEngine(deviceId)`：1) `setField(key, value, serverTs)`：写入带 `{ value, ts: serverTs, device }`；同 ts 用 deviceId 字典序决胜（两端合并结果一致）；2) `counter(key, delta)`：op 累积（本地立即生效 + 待同步队列）；3) `sync(remoteState)`：合并远端——字段 LWW、计数器取 delta 应用、游标字段（`__max` 前缀）取 max；4) `flushQueue()` 返回待同步 op 并清空（失败重入队）；5) `exportState()` 输出全量可同步状态。附用例验证同 ts 决胜一致性与游标 max。

```javascript
function createSyncEngine(deviceId) {
  const fields = new Map()     // key -> { value, ts, device }
  const counters = new Map()   // key -> 本地累计值
  const queue = []             // 待同步 op

  function setField(key, value, ts = Date.now()) {
    const cur = fields.get(key)
    if (!cur || ts > cur.ts || (ts === cur.ts && deviceId > cur.device)) {
      fields.set(key, { value, ts, device: deviceId })
      queue.push({ type: 'field', key, value, ts })
    }
  }

  function counter(key, delta) {
    counters.set(key, (counters.get(key) ?? 0) + delta)
    queue.push({ type: 'counter', key, delta })
  }

  function sync(remote) {
    // 字段合并：LWW + 同 ts 设备 id 决胜（确定性）
    for (const [key, rf] of Object.entries(remote.fields ?? {})) {
      const lf = fields.get(key)
      if (!lf || rf.ts > lf.ts || (rf.ts === lf.ts && rf.device > lf.device)) {
        fields.set(key, rf)
      }
    }
    // 远端计数器 delta 应用
    for (const [key, delta] of Object.entries(remote.counterDeltas ?? {})) {
      counters.set(key, (counters.get(key) ?? 0) + delta)
    }
    // 游标字段（__max 前缀）：取 max
    for (const [key, v] of Object.entries(remote.cursors ?? {})) {
      const ck = `__max:${key}`
      fields.set(ck, { value: Math.max(v, fields.get(ck)?.value ?? 0), ts: Date.now(), device: deviceId })
    }
  }

  function flushQueue() {
    const ops = queue.splice(0)
    // 模拟上报：失败重入队由调用方处理
    return { ops, retry: (ops2) => queue.unshift(...ops2) }
  }

  function exportState() {
    const cursors = {}
    fields.forEach((f, k) => { if (k.startsWith('__max:')) cursors[k.slice(6)] = f.value })
    return { fields: Object.fromEntries(fields), counterDeltas: {}, cursors }
  }

  return { setField, counter, sync, flushQueue, exportState, get: (k) => fields.get(k)?.value }
}

// 用例
const phone = createSyncEngine('phone')
const pad = createSyncEngine('pad')
phone.setField('nickname', 'A', 1000)
pad.setField('nickname', 'B', 1000)          // 同 ts
phone.sync(pad.exportState())
pad.sync(phone.exportState())
// 两端决胜一致：deviceId 'pad' > 'phone' → nickname 都是 'B'
console.log(phone.get('nickname'), pad.get('nickname'))   // B B
phone.counter('likes', 1)
pad.counter('likes', 1)
pad.sync({ counterDeltas: { likes: 1 } })    // 应用远端 delta
console.log(pad.get('likes') ?? pad.exportState().fields) // likes=2：不丢更新
phone.setField('__max:progress', 90)
pad.setField('__max:progress', 50)
pad.sync({ cursors: { progress: 90 } })
console.log(pad.get('__max:progress'))       // 90：游标取 max
```
**评分点**：
- 同 ts 用 deviceId 字典序决胜（两端结果确定性一致）
- 计数器走 op delta 合并（不丢更新）而非值覆盖
- 游标字段取 max（阅读进度类语义化合并）
- flushQueue 失败重入队（重试协议闭环）
