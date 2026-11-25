---
title: [ZSM-592] Yjs 接入协同编辑状态：Y.Map/Y.Text 与 React 状态的边界
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-592：Yjs 接入协同编辑状态：Y.Map/Y.Text 与 React 状态的边界

**答**：
- 分界原则：**协同字段放 Yjs 类型，本地态放普通 store**。Y.Map（结构化字段）、Y.Array（列表）、Y.Text（富文本）是多端并发收敛的；「谁正在选中哪段」（ephemeral 态）放 Awareness（广播但不需要持久收敛）。
- React 接线：Yjs 不是响应式的——用 `observe`/`observeDeep` 监听变更，把最新值写进一个普通 store（zustand/atom）供组件订阅；或者用 `useSyncExternalStore` 包一层。注意事务批处理：`doc.transact()` 里多次修改只触发一次 observe，防止高频重渲。
- 权威方向：不要把 Yjs 的值「复制两份」当普通状态改——所有修改走 Y 类型 API（`ymap.set`、`ytext.insert`），普通 store 只是投影只读；双向同步会打架。
- 离线与持久化：`y-websocket` provider 断网时本地缓冲，重连自动 diff 同步；持久化用 `y-indexeddb`（本地快照），服务端用 Yjs 的 update 二进制增量存。
- 追问钩子：Yjs 的 update 是二进制 op 流（可合并、可压缩），存储体积远小于全文快照；`encodeStateAsUpdate` 做快照导出、`applyUpdate` 做恢复——回放/审计能力强。

```javascript
import * as Y from 'yjs'
import { WebsocketProvider } from 'y-websocket'
import { create } from 'zustand'

const doc = new Y.Doc()
const provider = new WebsocketProvider('wss://sync.example.com', 'doc-1', doc)

// 协同数据结构
const ymeta = doc.getMap('meta')       // { title, status }
const ytodo = doc.getArray('todos')    // 协同列表
const awareness = provider.awareness   // ephemeral：光标/选区

// 投影 store：Yjs → React
const useDoc = create((set) => ({ title: '', todos: [] }))

doc.observeDeep((events) => {
  useDoc.setState({
    title: ymeta.get('title') ?? '',
    todos: ytodo.toArray().map((t) => t.toJSON()),
  })
})

// 所有修改走 Y API
export const actions = {
  setTitle(title) {
    doc.transact(() => { ymeta.set('title', title) })   // 事务：一次广播
  },
  addTodo(text) {
    doc.transact(() => {
      ytodo.push([{ id: crypto.randomUUID(), text, done: false }])
    })
  },
  toggleTodo(id) {
    const i = ytodo.toArray().findIndex((t) => t.id === id)
    doc.transact(() => ytodo.get(i).set('done', !ytodo.get(i).get('done')))
  },
}

// 本地光标（不需要收敛，只广播）
export function setCursor(anchor, head) {
  awareness.setLocalStateField('cursor', { anchor, head, user: currentUser })
}
```
