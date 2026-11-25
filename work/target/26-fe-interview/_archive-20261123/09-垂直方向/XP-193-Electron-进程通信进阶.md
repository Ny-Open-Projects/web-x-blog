---
title: [XP-193] Electron 进程通信进阶：MessagePort 与 Utility Process
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-193：Electron 进程通信进阶：MessagePort 与 Utility Process

**答**：
- IPC 进阶：MessagePort（渲染进程间直连，不经主进程中转——降低主进程负担）；Utility Process（独立 Node 进程跑重任务，不阻塞主进程）。
- MessagePort：window.postMessage 通道对——渲染 A ↔ 渲染 B 直连（主进程只做端口传递）。
- Utility Process：Electron 21+，独立 Node 进程——CPU 密集任务（DB/加密/解析）隔离。

```javascript
// MessagePort：渲染进程直连
// main.js（只传递端口）
ipcMain.on('port-request', (e) => {
  const other = getWindowB().webContents;
  const { port1, port2 } = new MessageChannelMain();
  e.sender.postMessage('port', null, [port1]);                     // 渲染 A 拿 port1
  other.postMessage('port', null, [port2]);                         // 渲染 B 拿 port2
});
// 渲染 A ↔ B 直连（不经主进程）——主进程零负担
// Utility Process：CPU 密集隔离
const utility = new UtilityProcess(path.join(__dirname, 'heavy-worker.js'));
utility.postMessage({ op: 'parse-large-file', path });             // 主进程发任务
utility.on('message', (result) => broadcastToRenderer(result));     // 结果回渲染
```
