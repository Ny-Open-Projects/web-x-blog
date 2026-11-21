---
title: [XP-037] Electron 多窗口管理怎么做？窗口之间如何通信？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-037：Electron 多窗口管理怎么做？窗口之间如何通信？
**答**：
- 用 **WindowManager 统一管理**：创建、焦点、生命周期、按 key 复用（单例窗口如"设置"）、`getAllWindows()` 遍历广播。
- 窗口间通信三条路：① 经主进程中转（通用但主进程是瓶颈）；② **MessagePort 直连**（`postMessage` 把 port 转给两个渲染进程，点对点、不经主进程，适合高频大数据）；③ 共享状态走主进程 + 变更广播（保持单一数据源）。
- 关闭策略：`close` 事件拦截做确认/保存；macOS 惯例关窗不退应用（`window-all-closed` 区分平台）。
- 崩溃隔离：一个窗口渲染进程崩不影响其它窗口，监听 `render-process-gone` 重建窗口并恢复状态（状态快照存主进程）。

```javascript
// main.ts —— WindowManager + 两种窗口通信
class WindowManager {
  #wins = new Map();
  open(key, options, url) {
    if (this.#wins.has(key)) { this.#wins.get(key).focus(); return this.#wins.get(key); } // 单例复用
    const win = new BrowserWindow(options);
    this.#wins.set(key, win);
    win.on('closed', () => this.#wins.delete(key));
    win.loadURL(url);
    return win;
  }
  broadcast(channel, payload) {
    for (const w of BrowserWindow.getAllWindows()) w.webContents.send(channel, payload);
  }
}
// 路径1：经主进程转发
ipcMain.on('win:forward', (e, { to, channel, data }) =>
  wm.#wins.get(to)?.webContents.send(channel, data));

// 路径2：MessagePort 直连（高频场景：编辑器 A ↔ 预览窗 B）
ipcMain.on('peer:connect', (e) => {
  const p2 = new MessageChannelMain();
  e.senderFrame.postMessage('peer:init', null, [p2.port1]);       // 给请求方
  BrowserWindow.getAllWindows().find((w) => w.webContents !== e.sender)
    ?.webContents.postMessage('peer:init', null, [p2.port2]);     // 给对端
});
// renderer：window.onmessage = ({ ports }) => ports[0].onmessage = (m) => apply(m.data);
```
