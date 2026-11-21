---
title: [OPT-112] Electron 应用的性能优化有哪些抓手？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-112：Electron 应用的性能优化有哪些抓手？

**答**：
- Electron 是多进程架构：主进程（Node）+ 渲染进程（Chromium）；性能三大坑：**重活压进主进程**（阻塞 IPC 与窗口管理）、渲染进程塞满全局依赖、原生模块同步调用。
- 抓手一：**进程职责拆分**——CPU 密集任务进 `UtilityProcess`/隐藏渲染进程，主进程只做窗口与 IPC 路由；抓手二：渲染进程按页面懒加载与代码分割（同 Web 规则）。
- 抓手三：**预加载脚本（preload）最小化**——contextBridge 只暴露必要 API，别把整个 fs 挂进渲染层；抓手四：原生模块用 N-API 异步接口，避免阻塞事件循环。
- 启动优化：延迟 require 重依赖、`ready` 前不做 IO、窗口先 show 再加载（`show: false` + `ready-to-show`）。

```javascript
// 一一对应：Electron 主进程/预加载/渲染层的职责拆分
// main.js —— 主进程：只做窗口与路由，重活交给 UtilityProcess
const { app, BrowserWindow, ipcMain, UtilityProcess } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    show: false,                    // 白屏优化：先不显示
    webPreferences: { preload: path.join(__dirname, 'preload.js'), sandbox: true },
  });
  win.once('ready-to-show', () => win.show()); // 内容就绪再展示，避免白屏
  win.loadFile('index.html');
  return win;
}

ipcMain.handle('parse-huge-file', async (e, filePath) => {
  // 反例：主进程直接 fs.readFileSync 同步解析 -> 全部窗口卡死
  // 正解：UtilityProcess（Node 子进程）处理，主进程零阻塞
  const worker = UtilityProcess.fork(path.join(__dirname, 'parser.js'));
  return new Promise((resolve, reject) => {
    worker.on('message', (msg) => (msg.ok ? resolve(msg.data) : reject(new Error(msg.error))));
    worker.postMessage({ filePath });
  });
});
app.whenReady().then(createWindow);

// parser.js —— UtilityProcess 入口：重活在这
const fs = require('fs');
process.parentPort.on('message', (e) => {
  try {
    const raw = fs.readFileSync(e.data.filePath, 'utf8'); // 子进程里同步无妨
    process.parentPort.postMessage({ ok: true, data: JSON.parse(raw).length });
  } catch (err) {
    process.parentPort.postMessage({ ok: false, error: err.message });
  }
});

// preload.js —— contextBridge 最小暴露面
const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('api', {
  parseHugeFile: (p) => ipcRenderer.invoke('parse-huge-file', p),
  // 反例：exposeInMainWorld('fs', require('fs')) —— 安全与性能双输
});

// 渲染层：await window.api.parseHugeFile('/data/big.json')，全程无阻塞
```
