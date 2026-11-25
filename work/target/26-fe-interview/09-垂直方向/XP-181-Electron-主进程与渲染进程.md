---
title: [XP-181] Electron 主进程与渲染进程：职责边界与 IPC
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-181：Electron 主进程与渲染进程：职责边界与 IPC

**答**：
- Electron 双进程：主进程（Node.js：文件系统/系统 API/窗口管理）+ 渲染进程（Chromium：UI）——IPC 通信（ipcMain/ipcRenderer）。
- 安全边界：渲染进程不信任（contextIsolation: true）——渲染进程通过 preload 暴露白名单 API（contextBridge），不直接暴露 Node 能力。
- IPC 模式：invoke/handle（Promise 请求响应）、send/on（单向推送）。

```javascript
// preload.js（安全桥）
const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('desktopAPI', {
  readFile: (path) => ipcRenderer.invoke('fs:read', path),     // 白名单暴露
  saveFile: (path, data) => ipcRenderer.invoke('fs:write', path, data),
  onMenuAction: (cb) => ipcRenderer.on('menu', (e, action) => cb(action)),
});
// main.js
ipcMain.handle('fs:read', async (e, path) => {                 // 主进程处理
  assertInAllowedDir(path);                                     // 路径白名单校验（防目录穿越）
  return fs.promises.readFile(path, 'utf-8');
});
// 渲染进程：window.desktopAPI.readFile('/data/config.json')——无 Node 权限
```
