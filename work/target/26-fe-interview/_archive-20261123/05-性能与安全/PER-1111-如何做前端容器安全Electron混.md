---
title: [PER-1111] 如何做"前端容器安全"（Electron/混合 App 的 Web 层）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1111：如何做"前端容器安全"（Electron/混合 App 的 Web 层）

**答**：
- Electron：禁 nodeIntegration（渲染进程无 Node 权限）、contextIsolation 开启、preload 白名单桥接。
- 远程内容：加载远程页面必须 sandbox + CSP，禁在主进程直接执行来自渲染层的命令（IPC 参数校验）。
- 混合 App：WebView 的 file 域访问禁用（防本地文件窃取）、URL 白名单（防任意远程页加载进容器获得 Bridge 权限）。
- 更新链：Electron 自动更新走签名校验，防更新通道投毒。

```javascript
// Electron 安全配置基线
new BrowserWindow({
  webPreferences: {
    nodeIntegration: false,
    contextIsolation: true,
    sandbox: true,
    preload: path.join(__dirname, 'preload.js'),     // 白名单桥
  },
});
// preload.js:
contextBridge.exposeInMainWorld('appAPI', {
  readFile: (p) => ipcRenderer.invoke('read-file', p),  // 主进程校验路径
});
// 主进程 IPC 校验：
ipcMain.handle('read-file', (e, p) => {
  const safe = path.resolve(ALLOW_DIR, p);
  if (!safe.startsWith(ALLOW_DIR)) throw new Error('路径越界');
  return fs.promises.readFile(safe);
});
```
