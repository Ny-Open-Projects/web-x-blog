---
title: [ZSM-687] 笔试：手写秒杀活动状态引擎（phase 派生 + 库存门禁 + 请求去抖）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-687：手写秒杀活动状态引擎（phase 派生 + 库存门禁 + 请求去抖）
**答**：实现 `createSeckillEngine(activity)`：1) `phase(nowOffset)`：'upcoming'|'active'|'ended' 由活动窗口派生（服务端口径时间）；2) `trySubmit(userId)`：门禁链——phase 必须 active、每人限购 1（本地参与标记）、库存 > 0、请求在途不允许重复（去重锁）；门禁失败返回结构化原因不发起请求；3) `submit` 成功后本地扣库存 + 标记参与；失败（服务端拒绝）区分「已抢完/重复参与/限流」；4) `reset()`；5) 附用例：门禁链逐项验证与并发去重。

```javascript
function createSeckillEngine(activity, { now = () => Date.now() } = {}) {
  let stock = activity.stock
  const participants = new Set()
  let inFlight = false
  const log = []

  function phase(t = now()) {
    return t < activity.startAt ? 'upcoming' : t < activity.endAt ? 'active' : 'ended'
  }

  function trySubmit(userId) {
    const p = phase()
    // 门禁链：顺序短路
    if (p !== 'active') return { ok: false, code: `PHASE_${p.toUpperCase()}` }
    if (participants.has(userId)) return { ok: false, code: 'ALREADY_JOINED' }
    if (stock <= 0) return { ok: false, code: 'SOLD_OUT' }
    if (inFlight) return { ok: false, code: 'IN_FLIGHT' }       // 去重锁

    inFlight = true
    return {
      ok: true,
      exec: async () => {
        try {
          const res = await api.seckill(activity.id, userId)
          if (res.code === 'SOLD_OUT') { stock = 0; return { ok: false, code: 'SOLD_OUT' } }
          if (res.code === 'DUPLICATE') { participants.add(userId); return { ok: false, code: 'ALREADY_JOINED' } }
          if (res.code === 'RATE_LIMITED') return { ok: false, code: 'RATE_LIMITED' }
          // 成功：本地扣减 + 标记
          stock--
          participants.add(userId)
          log.push({ userId, ts: now(), stockLeft: stock })
          return { ok: true, order: res.order }
        } finally {
          inFlight = false        // 释放去重锁
        }
      },
    }
  }

  function reset() {
    stock = activity.stock
    participants.clear()
    inFlight = false
    log.length = 0
  }

  return {
    phase, trySubmit, reset,
    state: () => ({ stock, participants: [...participants], inFlight }),
    log: () => log,
  }
}

// 用例
const fixedNow = activity_start = 1000
let t = 2000     // active 窗口内
const engine = createSeckillEngine(
  { id: 's1', stock: 2, startAt: 1000, endAt: 3000 },
  { now: () => t }
)
console.log(engine.phase())                      // 'active'
const r1 = engine.trySubmit('u1')
console.log(r1.ok)                               // true
r1.exec().then((res) => {
  console.log(res.ok, engine.state().stock)      // true 1
  const r2 = engine.trySubmit('u1')              // 重复参与
  console.log(r2.code)                           // 'ALREADY_JOINED'
  const r3 = engine.trySubmit('u2')
  r3.exec().then(() => {
    console.log(engine.state().stock)            // 0
    console.log(engine.trySubmit('u3').code)     // 'SOLD_OUT'
    t = 4000
    console.log(engine.phase())                  // 'ended'
    console.log(engine.trySubmit('u3').code)     // 'PHASE_ENDED'
  })
})
```
**评分点**：
- phase 纯派生（时间窗口比较，不存储状态）
- 门禁链顺序短路（phase→参与→库存→在途锁）
- 去重锁的 finally 释放（异常也解锁）
- 服务端拒绝码的本地状态同步（SOLD_OUT 扣 0、DUPLICATE 补标记）
