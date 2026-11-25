---
title: [XP-182] Electron 安全加固：contextIsolation 与 CSP
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-182：Electron 安全加固：contextIsolation 与 CSP

**答**：
- 题目：Electron 安全清单——contextIsolation/sandbox/nodeIntegration 关闭、CSP 严格、远程内容隔离（webview/iframe）、协议白名单。
- 思路：BrowserWindow webPreferences { contextIsolation: true, sandbox: true, nodeIntegration: false }；CSP 限制脚本源；will-navigate 拦截外部导航。
- 评分点：webPreferences 三项；CSP；导航拦截。

```javascript
const win = new BrowserWindow({
  webPreferences: {
    contextIsolation: true,                                    // 上下文隔离（必须）
    sandbox: true,                                              // 沙箱（必须）
    nodeIntegration: false,                                     // 禁 Node（必须）
    preload: path.join(__dirname, 'preload.js'),                // 安全桥
  },
});
// CSP（session 级）
session.defaultSession.webRequest.onHeadersReceived((details, cb) => {
  cb({ responseHeaders: { ...details.responseHeaders,
    'Content-Security-Policy': ["default-src 'self'; script-src 'self'"] } });
});
// 导航拦截（防远程内容逃逸）
win.webContents.on('will-navigate', (e, url) => {
  if (!url.startsWith('file://') && !ALLOWED_HOSTS.some(h => url.includes(h)))
    e.preventDefault();                                          // 阻断外部导航
});
```
