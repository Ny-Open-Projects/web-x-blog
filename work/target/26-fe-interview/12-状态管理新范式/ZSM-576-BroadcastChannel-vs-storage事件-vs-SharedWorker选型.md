---
title: [ZSM-576] 跨 tab 同步选型：BroadcastChannel、storage 事件、SharedWorker 怎么选
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-576：跨 tab 同步选型：BroadcastChannel、storage 事件、SharedWorker 怎么选

**答**：
- **BroadcastChannel**：同源 tab 间广播，支持任意结构化对象（不只字符串）、延迟低（不落盘）、API 简洁。首选，Safari 15.4+ / 全主流支持。局限：仅同源同浏览器实例、消息不持久（后开的 tab 收不到历史）。
- **storage 事件**：写 localStorage 时其他 tab 触发。优点兼容性最老；缺点只能传字符串（JSON 序列化开销）、写盘有延迟、本 tab 不触发（同步本 tab 与跨 tab 要走两条路）、Safari 隐私模式下不可靠。作为降级方案。
- **SharedWorker**：一个常驻 worker 被多 tab 共享，是真正的「中心节点」：持有权威状态、可做选举、可主动推送给所有连接。优点：状态收口、可执行逻辑；缺点：Safari 曾长期不支持（现支持）、调试复杂、worker 崩溃要恢复协议。
- 选型口诀：纯通知（如「有人登出了」）用 BroadcastChannel；需要中心化权威状态/复杂协议用 SharedWorker；要兼容老浏览器或需要持久化用 storage 事件。三者可组合：SharedWorker 为主干，广播做通知，localStorage 做恢复兜底。
- 追问钩子：无论哪种通道，都要处理「消息乱序/重复」——协议层加 seq 和幂等，通道层不保证有序送达。

```javascript
// 三通道统一抽象
function createChannel(name) {
  if ('BroadcastChannel' in window) {
    const ch = new BroadcastChannel(name)
    return {
      post: (msg) => ch.postMessage(msg),
      sub: (fn) => { ch.onmessage = (e) => fn(e.data); return () => (ch.onmessage = null) },
    }
  }
  // 降级：storage 事件（本 tab 写，其他 tab 收）
  const key = `__channel_${name}`
  return {
    post: (msg) => { localStorage.setItem(key, JSON.stringify({ ...msg, _n: Math.random() })) },
    sub: (fn) => {
      const onStorage = (e) => { if (e.key === key && e.newValue) fn(JSON.parse(e.newValue)) }
      window.addEventListener('storage', onStorage)
      return () => window.removeEventListener('storage', onStorage)
    },
  }
}

// SharedWorker 主干模式
// worker.js
const tabs = new Set()
onconnect = (e) => {
  const port = e.ports[0]
  tabs.add(port)
  port.onmessage = (m) => {
    if (m.data.type === 'state') broadcast({ type: 'state', payload: m.data.payload })
  }
}
function broadcast(msg) { tabs.forEach((p) => p.postMessage(msg)) }
```
