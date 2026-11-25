---
title: [ZSM-578] 笔试：手写多 tab 状态同步协议（含加入握手与乱序处理）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-578：手写多 tab 状态同步协议（含加入握手与乱序处理）
**答**：基于 BroadcastChannel 实现完整同步协议：1) 新 tab 加入时发 `hello`，已存在 tab 应答 `welcome(携带当前状态+最新 seq)`——新 tab 等待 300ms 取「seq 最大的 welcome」（防多个 tab 各自应答）；2) 变更广播带 `seq`（每 tab 本地递增 + 源 tabId），接收方按 `{tabId, seq}` 去重（乱序/重复消息）；3) `sync(tabId, uptoSeq)` 重同步请求：接收方发现 seq 缺口时要求源 tab 重发全量状态；4) leave 时广播；5) 附用例模拟两 tab 交互。

```javascript
function createSyncProtocol(store, { joinTimeout = 300 } = {}) {
  const tabId = crypto.randomUUID()
  const ch = new BroadcastChannel('sync')
  const seen = new Set()        // `${tabId}:${seq}` 已处理
  let localSeq = 0
  let state = { ...store.initial }

  ch.onmessage = (e) => handle(e.data)

  function post(type, payload = {}) {
    ch.postMessage({ type, from: tabId, ...payload })
  }

  function handle(msg) {
    if (msg.from === tabId) return
    switch (msg.type) {
      case 'hello':
        post('welcome', { state, seq: localSeq })
        break
      case 'welcome': {
        // 取 seq 最大的 welcome（防应答竞争）
        if (!pendingWelcome || msg.seq > pendingWelcome.seq) pendingWelcome = msg
        break
      }
      case 'change': {
        const key = `${msg.from}:${msg.seq}`
        if (seen.has(key)) return        // 重复消息去重
        seen.add(key)
        if (msg.baseSeq !== localSeq && msg.baseSeq > localSeq) {
          // 疑似漏消息：请求重同步
          post('resync', { to: msg.from })
          return
        }
        applyChange(msg.patch)
        break
      }
      case 'resync':
        if (msg.to === tabId) post('snapshot', { state, seq: localSeq })
        break
      case 'snapshot':
        if (msg.seq >= localSeq) { state = msg.state; localSeq = msg.seq }
        break
      case 'leave':
        break
    }
  }

  let pendingWelcome = null
  function join() {
    post('hello')
    return new Promise((resolve) => {
      setTimeout(() => {
        if (pendingWelcome) {
          state = pendingWelcome.state
          localSeq = pendingWelcome.seq
        }   // 无应答：自己是第一个 tab，用初始状态
        resolve(state)
      }, joinTimeout)
    })
  }

  function applyChange(patch) {
    state = typeof patch === 'function' ? patch(state) : { ...state, ...patch }
    localSeq++
  }

  function update(patch) {
    const prevSeq = localSeq
    applyChange(patch)
    post('change', { patch, seq: localSeq, baseSeq: prevSeq })
  }

  function leave() { post('leave') }

  return { join, update, getState: () => state, tabId, leave }
}

// 用例（模拟两个 tab 的消息交错）
const tabA = createSyncProtocol({ initial: { count: 0 } })
const tabB = createSyncProtocol({ initial: { count: 0 } })
tabA.join()
tabB.join()                        // hello/welcome 握手
tabB.update({ count: 5 })          // change 广播
console.log(tabB.getState())       // { count: 5 }
// tabA 处理 change 后 state.count === 5（真实环境经 ch.onmessage 同步）
```
**评分点**：
- 加入握手 + 300ms 竞争窗取最大 seq welcome（防多应答不一致）
- `{tabId, seq}` 消息去重（乱序与重复消息防御）
- 缺口检测触发 resync（baseSeq 比对，全量快照兜底）
- 生命周期消息（hello/welcome/leave）完整
