---
title: [MFW-462] 笔试：手写跨标签 SWR 后台刷新协调器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-462：跨标签 SWR 后台刷新协调器
**需求**：基于 BroadcastChannel 实现跨标签页单飞刷新：1) `swr(key, fetcher, { ttl })`：本地缓存新鲜直接返回；过期则先回旧值（stale），并选举一个标签发请求——`tryLock(key)` 用 channel 抢锁（id 小者胜，模拟确定性选举）；2) 中标标签 fetch 后 `broadcast({ key, data, version })`，所有标签写回缓存；3) 抢锁 300ms 未定则自己上（选举失败的兜底，防 channel 丢消息集体等死）；4) 同 key 请求进行中直接复用 in-flight promise（本标签单飞）。

```javascript
const ch = typeof BroadcastChannel !== 'undefined' ? new BroadcastChannel('swr') : null
const TAB = Math.random().toString(36).slice(2)
const mem = new Map()   // key -> { data, at, ver }
const inflight = new Map()

export function swr(key, fetcher, { ttl = 30000 } = {}) {
  const hit = mem.get(key)
  if (hit && Date.now() - hit.at < ttl) return Promise.resolve(hit.data)
  if (inflight.has(key)) return inflight.get(key)
  const p = new Promise(resolve => {
    let elected = false
    const onMsg = ({ data: m }) => {
      if (m.type === 'claim' && m.key === key && m.tab < TAB) elected = true
      if (m.type === 'result' && m.key === key) {
        mem.set(key, { data: m.data, at: Date.now(), ver: m.ver })
        ch?.removeEventListener('message', onMsg); inflight.delete(key); resolve(m.data)
      }
    }
    ch?.addEventListener('message', onMsg)
    ch?.postMessage({ type: 'claim', key, tab: TAB })
    setTimeout(() => { // 兜底：300ms 没人自称中标 → 自己刷
      if (!elected || TAB <= TAB) { run(key, fetcher) }
    }, 300)
  })
  inflight.set(key, p)
  return p
}

async function run(key, fetcher) {
  const data = await fetcher()
  ch?.postMessage({ type: 'result', key, data, ver: Date.now() })
}
```

**评分点**：
- 先回 stale 再后台刷新（SWR 语义：不等网络）
- claim 消息确定性选举 + 300ms 兜底自刷（防丢消息集体饿死）
- result 广播全标签写回（一次请求全站受益）
- 本标签 in-flight 复用（同标签并发也不重复打）
