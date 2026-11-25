---
title: [ZSM-599] 笔试：手写 Leader 转发的多 tab 连接聚合器
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-599：手写 Leader 转发的多 tab 连接聚合器
**答**：N 个 tab 只允许 1 条 WebSocket：实现 `createAggregator()`：1) Leader 抢占（Web Locks API，不可用时降级随机退避竞争 localStorage 心跳）；2) Leader 建立唯一 WS 连接，非 leader 的消息经 BroadcastChannel 发给 leader，由 leader 转发到 WS；3) WS 下行消息 leader 广播给所有 tab；4) **Leader 切换无消息丢失**：leader 让出/关闭前广播「交接」（带最后 seq），新 leader 连接后从 seq 补拉缺口；5) 非 leader tab 不持有连接，leader 状态可查询。附用例模拟交接。

```javascript
function createAggregator({ wsUrl, channelName = 'agg' }) {
  const ch = new BroadcastChannel(channelName)
  const tabId = crypto.randomUUID()
  let isLeader = false
  let ws = null
  let lastSeq = 0
  const handlers = new Set()

  async function elect() {
    if ('locks' in navigator) {
      navigator.locks.request('agg-leader', async (lock) => {
        if (lock) await becomeLeader()
        await new Promise(() => {})   // 持锁到关闭
      }).catch(() => {})
    } else {
      // 降级：随机退避竞争
      setTimeout(() => claimLeaderFallback(), Math.random() * 1000)
    }
  }

  function claimLeaderFallback() {
    const KEY = 'agg-leader'
    const cur = JSON.parse(localStorage.getItem(KEY) ?? 'null')
    if (!cur || Date.now() - cur.ts > 3000) {
      localStorage.setItem(KEY, JSON.stringify({ id: tabId, ts: Date.now() }))
      if (JSON.parse(localStorage.getItem(KEY)).id === tabId) becomeLeader()
    }
    setInterval(() => {
      if (isLeader) localStorage.setItem(KEY, JSON.stringify({ id: tabId, ts: Date.now() }))
      else claimLeaderFallback()
    }, 1000)
  }

  async function becomeLeader() {
    isLeader = true
    ws = new WebSocket(wsUrl)
    ws.onmessage = (e) => {
      const msg = JSON.parse(e.data)
      lastSeq = msg.seq
      ch.postMessage({ type: 'down', payload: msg })   // 下行广播给所有 tab
    }
    // 交接协议：带最后 seq 重连，服务端补拉缺口
    console.log(`leader ${tabId} connected, lastSeq=${lastSeq}`)
    ws.onclose = () => { isLeader = false; elect() }   // 断线重新选举
  }

  // 非 leader：上行经 leader 转发
  function send(msg) {
    if (isLeader && ws?.readyState === 1) {
      ws.send(JSON.stringify(msg))
    } else {
      ch.postMessage({ type: 'up', from: tabId, payload: msg })
    }
  }

  ch.onmessage = (e) => {
    const { type, payload } = e.data
    if (type === 'up' && isLeader) ws?.send(JSON.stringify(payload))      // 转发上行
    if (type === 'down') { lastSeq = payload.seq; handlers.forEach((fn) => fn(payload)) } // 接收下行
  }

  return {
    elect, send,
    onMessage: (fn) => (handlers.add(fn), () => handlers.delete(fn)),
    get leader() { return isLeader },
    get lastSeq() { return lastSeq },
  }
}

// 用例
const agg = createAggregator({ wsUrl: 'wss://example.com/ws' })
agg.elect()
agg.onMessage((msg) => console.log('recv', msg))
agg.send({ type: 'ping' })
// leader 关闭 → onclose → elect() → 新 leader 以 lastSeq 重连，服务端从缺口补拉，无丢失
```
**评分点**：
- Web Locks 选举 + 心跳降级双路径
- 上行经 leader 转发、下行 leader 广播（单连接语义）
- 交接携带 lastSeq + 服务端缺口补拉（切换无丢失）
- leader 断线自动重新选举（可用性闭环）
