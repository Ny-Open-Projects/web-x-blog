---
title: [ZSM-554] Redux DevTools 通信协议的关键消息类型有哪些
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-554：Redux DevTools 通信协议的关键消息类型有哪些

**答**：
- 协议本质：扩展页面与页面 JS 之间通过 `window.postMessage` / 注入 bridge 通信，约定一组 `msg.type` 消息。应用侧核心消息：`START`（连接建立，要求上报初始状态）、`ACTION`（面板 dispatch 一个 action 要求应用执行）、`DISPATCH`（面板命令）、`STATE`（应用上报状态）。
- `DISPATCH` 的常见 payload：`JUMP_TO_STATE`（时间旅行跳转——应用收到后 setState 到 msg.state）、`RESET`、`ROLLBACK`、`COMMIT`、`PAUSE_RECORDING`。理解这组消息就能自己给任意状态库接 DevTools。
- 自定义实例：`__REDUX_DEVTOOLS_EXTENSION__.connect({ name, features })` 返回的 connection 上 `send(action, state)` 推时间线、`subscribe` 收面板消息——Zustand/Jotai 的官方 devtools 中间件都只是这层协议的封装。
- 监控点：`LIFTED_STORE` 概念——扩展自己维护一份「动作序列账本」，面板展示的时间线是 action 流而非状态流，状态是按需 lift 出来的，所以大状态库要注意 send 的 payload 体积。
- 追问钩子：`import { composeWithDevTools }` 与 enhancer 的关系；多 store 用 `name` 区分实例。

```javascript
// 给任意状态库接 Redux DevTools（协议层骨架）
function connectDevTools(store, name = 'MyStore') {
  const ext = window.__REDUX_DEVTOOLS_EXTENSION__
  if (!ext) return
  const conn = ext.connect({ name })

  // 应用 → 面板：每次变更上报
  const origSet = store.setState
  store.setState = (p, r, actionName) => {
    origSet(p, r, actionName)
    conn.send({ type: actionName ?? 'setState', payload: null }, store.getState())
  }

  // 面板 → 应用：处理关键 DISPATCH
  conn.subscribe((msg) => {
    if (msg.type !== 'DISPATCH') return
    switch (msg.payload?.type) {
      case 'JUMP_TO_STATE':
      case 'ROLLBACK':
      case 'COMMIT':
        if (msg.state) store.setState(JSON.parse(msg.state), true)  // replace 整体写回
        break
      case 'RESET':
        store.setState(store.getInitialState?.() ?? {}, true)
        break
      case 'PAUSE_RECORDING':
        store.__paused = msg.payload.status === 'START'
        break
    }
  })
  conn.send({ type: '@@INIT' }, store.getState())   // 初始化上报
}
```
