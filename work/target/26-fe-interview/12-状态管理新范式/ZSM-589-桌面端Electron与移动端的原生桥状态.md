---
title: [ZSM-589] 桌面端（Electron）与移动端的原生桥状态同步要点
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-589：桌面端（Electron）与移动端的原生桥状态同步要点

**答**：
- Electron 特殊性：多窗口（BrowserWindow）+ 主进程（Node）三态。状态归属判断：**业务状态放主进程或共享 store 包**，渲染进程订阅 IPC 推送；不要把状态存渲染进程（窗口关闭即丢）。
- Electron 同步通道：主进程是天然中心——`ipcMain.handle`（request/response）+ `webContents.send`（主动推送）；状态变更主进程广播到所有窗口，窗口发起的变更经 handle 校验后写主进程 store 再广播，天然没有回环（消息都过主进程中转）。
- 移动端原生桥要点（延续 ZSM-579）：桥消息序列化开销大、不可高频；持久化状态（登录态、设置）以 native 存储为准（Keychain/MMKV），WebView 只持有会话投影。
- 通用原则：**原生层持有「长期事实」，前端层持有「会话态」**——同步方向是 native → web 单向推事实 + web → native 提交意图（经白名单），两端各自建模，不做全状态镜像。
- 追问钩子：窗口/页面崩溃恢复——Election 渲染进程 reload 后要向主进程「请求当前状态快照」（ready 握手重放），这套协议在所有跨端场景（WebView/iframe/多窗口）通用。

```javascript
// Electron 主进程：中心 store + 广播
const { ipcMain } = require('electron')
const state = { user: null, settings: {} }
const windows = []

function broadcast(changedKeys) {
  windows.forEach((w) => w.webContents.send('state:changed', {
    state, changedKeys, version: ++version,
  }))
}

ipcMain.handle('state:mutate', (e, { patch, baseVersion }) => {
  if (baseVersion !== version) return { ok: false, reason: 'stale', state, version }  // 版本校验
  Object.assign(state, patch)
  broadcast(Object.keys(patch))
  return { ok: true, version }
})

// 渲染进程
ipcRenderer.on('state:changed', (_e, { state, changedKeys }) => {
  store.setState(state)          // 主进程权威
})

async function mutate(patch) {
  const res = await ipcRenderer.invoke('state:mutate', { patch, baseVersion: version })
  if (!res.ok) store.setState(res.state)   // stale：以主进程为准
}

// 渲染进程启动：ready 握手请求快照
ipcRenderer.invoke('state:snapshot').then((snap) => store.setState(snap))
```
