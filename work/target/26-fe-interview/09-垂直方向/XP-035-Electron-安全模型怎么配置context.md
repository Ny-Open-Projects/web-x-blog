---
title: [XP-035] Electron 安全模型怎么配置？contextIsolation 与 nodeIntegration 如何取舍？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-035：Electron 安全模型怎么配置？contextIsolation 与 nodeIntegration 如何取舍？
**答**：
- 黄金配置：**`contextIsolation: true`（默认）+ `nodeIntegration: false` + `sandbox: true`**，preload 是唯一通道，页面永远不直接摸 Node。
- 放弃 `nodeIntegration: true` 的理由：渲染进程一旦被 XSS/加载第三方页面，等于拿到整台机器的 Node 权限（fs/child_process/RCE）。
- 配套措施：禁 `nodeIntegrationInWorker`、`webSecurity` 不许关、限制 `will-navigate`/`setWindowOpenHandler`（防导航劫持）、加载远程内容必须 CSP、`session.setPermissionRequestHandler` 管权限弹窗。
- 校验习惯：所有 ipcMain.handle 校验 senderFrame.origin；不 `eval` 任何远程输入；shell.openExternal 仅放行 https。
- 历史教训：Node 任意版本漏洞都会经由 nodeIntegration 放大成桌面端 RCE，社区安全公告反复强调。

```javascript
// 安全基线配置（main.ts）
const win = new BrowserWindow({
  webPreferences: {
    contextIsolation: true,     // 必开：preload 与页面上下文隔离
    nodeIntegration: false,     // 必关：渲染进程无 Node
    sandbox: true,              // 沙箱渲染进程，即使 preload 漏洞也被限制
    preload: path.join(__dirname, 'preload.cjs'),
    webviewTag: false,          // 不需要就关掉
  },
});

// 防导航劫持与外链
win.webContents.setWindowOpenHandler(({ url }) => {
  if (url.startsWith('https://')) shell.openExternal(url); // 外链交给系统浏览器
  return { action: 'deny' };
});
win.webContents.on('will-navigate', (e, url) => {
  if (!url.startsWith('https://app.example.com')) e.preventDefault();
});

// CSP（index.html 头部）：
// <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; object-src 'none'">
// 权限收口：
session.defaultSession.setPermissionRequestHandler((wc, permission, cb) =>
  cb(permission === 'clipboard-read' && wc.frame.url.includes('app.example.com')));
```
