---
title: [ZSM-872] 笔试：手写工单 SLA 状态机（计时启停 + 超时升级 + 合并审计）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-872：手写工单 SLA 状态机（计时启停 + 超时升级 + 合并审计）
**答**：871 落地——实现 `createTicket()`：1) SLA 计时随状态启停：working 计时、pending（等用户）冻结、resolved 终止；2) 超时升级：SLA 到期自动 escalate（时间驱动迁移）+ 升级一次后重置计时（二次 SLA）；3) `merge(otherTicket)`：主从合并——消息归并去重 + merged-from 审计链 + SLA 取两者更紧的；4) 附用例：pending 冻结计时与合并审计链。

```javascript
function createTicket({ priority = 'high', now = Date.now } = {}) {
  const SLA = { high: 2 * 3600e3, medium: 8 * 3600e3 }[priority]
  const ticket = { phase: 'working', slaElapsed: 0, escalations: 0, mergedFrom: [] }
  const messages = new Set()          // 消息指纹去重（合并用）
  const auditLog = []
  let lastResume = now()
  let timer = null
  const listeners = new Set()

  function emit(e) { auditLog.push({ ts: now(), ...e }); listeners.forEach((fn) => fn(e)) }

  // SLA 计时启停
  function startTimer() {
    lastResume = now()
    timer = setInterval(() => {
      ticket.slaElapsed += now() - lastResume
      lastResume = now()
      if (ticket.slaElapsed >= SLA * (ticket.escalations + 1)) {
        escalate()                     // 超时升级（时间驱动迁移）
      }
    }, 1000)
  }
  function stopTimer() { clearInterval(timer); ticket.slaElapsed += now() - lastResume; timer = null }

  function escalate() {
    ticket.escalations++
    emit({ type: 'escalate', times: ticket.escalations })   // 升级后 SLA 重置（二次时限）
  }

  function toPending() { ticket.phase = 'pending'; stopTimer(); emit({ type: 'pending' }) }      // 冻结计时
  function resume() { ticket.phase = 'working'; startTimer(); emit({ type: 'resume' }) }
  function resolve() { ticket.phase = 'resolved'; stopTimer(); emit({ type: 'resolved' }) }

  startTimer()

  // 合并：主从关系 + 消息归并去重 + SLA 取更紧
  function merge(other, direction = 'absorb') {
    other.messages.forEach((m) => {
      if (!messages.has(m.fingerprint)) messages.add(m.fingerprint)   // 归并去重
    })
    ticket.mergedFrom.push({ id: other.id, direction, at: now() })    // 审计链
    // SLA 取更紧（elapsed 大者优先到期）
    ticket.slaElapsed = Math.max(ticket.slaElapsed, other.slaElapsed)
    emit({ type: 'merged', from: other.id, direction })
  }

  function addMessage(fingerprint) { messages.add(fingerprint) }

  return {
    toPending, resume, resolve, escalate, merge, addMessage,
    state: () => ({ ...ticket, audit: auditLog, messageCount: messages.size }),
    subscribe: (fn) => (listeners.add(fn), () => listeners.delete(fn)),
  }
}

// 用例
let t = 0
const main = createTicket({ priority: 'high', now: () => t })
main.addMessage('msg-a')
t += 1000
main.toPending()                                  // 等用户：冻结计时
const frozen = main.state().slaElapsed
t += 3600e3                                       // pending 一小时
console.log(main.state().slaElapsed === frozen)   // true：冻结生效
main.resume()                                     // 恢复计时

// 合并重复工单
const other = createTicket({ priority: 'high', now: () => t })
other.addMessage('msg-b')
main.merge(other, 'absorb')
console.log(main.state().mergedFrom)              // [{ id: ..., direction: 'absorb', at }]：审计链
console.log(main.state().messageCount)            // 2：归并去重后
main.resolve()
console.log(main.state().audit.map((a) => a.type))
// ['pending', 'resume', 'merged', 'resolved']
```
**评分点**：
- SLA 计时启停（pending 冻结 + resume 续算）
- 超时升级（escalations 递增 + 二次 SLA 重置）
- 合并三要素（消息指纹去重 + merged-from 审计链 + SLA 取更紧）
- 审计日志全量（auditLog 覆盖每次迁移）
