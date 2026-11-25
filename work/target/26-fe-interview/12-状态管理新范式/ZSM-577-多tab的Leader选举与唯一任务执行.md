---
title: [ZSM-577] 多 tab 的 Leader 选举：为什么需要以及怎么实现
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-577：多 tab 的 Leader 选举：为什么需要以及怎么实现

**答**：
- 为什么需要：轮询/心跳/WebSocket 连接这类「全局唯一任务」如果每个 tab 都做，请求翻 N 倍（服务端压力）、连接数暴涨；消息 toast、本地通知也该只有一个 tab 负责。Leader 选举让多 tab 表现得像一个应用。
- 简单实现（Web Locks API）：`navigator.locks.request('leader', ...)`——浏览器保证同源互斥锁，抢到锁的 tab 是 leader，锁释放（tab 关闭）时其他 tab 自动竞争，这是最干净的方案。
- 降级实现：心跳 + 抢占——leader 定期写 `leader: { id, ts }` 到 localStorage（或 BroadcastChannel 心跳）；其他 tab 每次心跳检查，超过 3s 没心跳就尝试接管（写自己的 id 并确认写入成功）。竞态用「写前读、写后验证」处理。
- Leader 职责设计：只保留「全局副作用」（网络轮询、通知、缓存刷新），状态本身仍每 tab 各自持有 + 通过变更广播保持一致；leader 崩溃时其他 tab 无缝接管，业务无感。
- 追问钩子：Web Locks 的锁是「同源同 profile」的，跨浏览器 profile/隐私窗口各自有 leader——多端同步还是要靠服务端。

```javascript
// 方案一：Web Locks（首选）
async function electLeader(onBecomeLeader, onLoseLeader) {
  while (true) {
    try {
      await navigator.locks.request('app-leader', async (lock) => {
        if (!lock) return   // 竞争失败，稍后重试
        console.log('I am leader')
        onBecomeLeader()
        await new Promise(() => {})   // 永不 resolve：持有锁直到 tab 关闭
      })
    } catch (e) { /* 锁被释放（关闭）会抛 AbortError */ }
    onLoseLeader()
    await new Promise((r) => setTimeout(r, 1000))   // 重新竞争
  }
}

// 方案二：心跳抢占（降级）
function electLeaderFallback(tabId) {
  const KEY = 'app-leader'
  const alive = () => {
    const l = JSON.parse(localStorage.getItem(KEY) ?? 'null')
    return l && Date.now() - l.ts < 3000
  }
  let isLeader = !alive()
  if (isLeader) localStorage.setItem(KEY, JSON.stringify({ id: tabId, ts: Date.now() }))
  setInterval(() => {
    if (isLeader) {
      localStorage.setItem(KEY, JSON.stringify({ id: tabId, ts: Date.now() }))
    } else if (!alive()) {
      // 抢占：写后验证
      localStorage.setItem(KEY, JSON.stringify({ id: tabId, ts: Date.now() }))
      if (JSON.parse(localStorage.getItem(KEY)).id === tabId) isLeader = true
    }
  }, 1000)
  return () => isLeader
}
```
