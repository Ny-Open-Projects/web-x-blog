---
title: [R19-121] Electron + React 的架构要点？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-121：Electron + React 的架构要点？
**答**：
- 三层：主进程（Node 能力：文件、系统）、preload（contextBridge 桥）、渲染进程（React UI）。
- 安全底线：contextIsolation: true、nodeIntegration: false，渲染进程只能通过 preload 暴露的白名单 IPC 与系统交互。
- IPC 用 invoke/handle 的请求-响应模式，preload 返回清理函数让 React effect 无缝订阅事件。
- React 层面与 Web 复用度高，平台差异收敛到 api 层，便于未来迁移 Tauri 或纯 Web。

```jsx
// Electron + React：主进程 Node、渲染进程 React、preload 桥接
// preload.cjs —— contextBridge 暴露受限 IPC，绝不直接开 nodeIntegration
// const { contextBridge, ipcRenderer } = require('electron');
//
// contextBridge.exposeInMainWorld('api', {
//   readConfig: () => ipcRenderer.invoke('config:read'),
//   saveFile: (content) => ipcRenderer.invoke('file:save', content),
//   onUpdaterEvent: (cb) => {
//     const listener = (_, data) => cb(data);
//     ipcRenderer.on('updater', listener);
//     return () => ipcRenderer.removeListener('updater', listener);  // 返回清理函数
//   },
// });

// 渲染进程 React 组件安全消费
import { useEffect, useState } from 'react';

function UpdaterBanner() {
  const [status, setStatus] = useState('idle');
  useEffect(() => window.api.onUpdaterEvent(setStatus), []);   // cleanup 由 effect 自动调用
  if (status !== 'available') return null;
  return <button onClick={() => window.api.invokeUpdate()}>更新可用，立即安装</button>;
}
// 安全清单：contextIsolation: true、nodeIntegration: false、IPC 参数在主进程校验
```
