---
title: [XP-033] Electron 的进程模型是怎样的（主进程/渲染进程/Utility）？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-033：Electron 的进程模型是怎样的（主进程/渲染进程/Utility）？
**答**：
- **主进程**（main）：Node 环境，管理应用生命周期、窗口、原生 API、系统托盘；**全局唯一**，是所有渲染进程的父进程。
- **渲染进程**（renderer）：每个 BrowserWindow/BrowserView/`<webview>` 一个独立 Chromium 渲染进程，跑页面 UI；默认无 Node 能力（安全考虑）。
- **Utility Process**（utilityProcess 模块）：Node 子进程，用于在不污染主进程的情况下跑重活（如 LSP、文件索引、ffmpeg）。
- **GPU 进程/网络服务**：Chromium 基础设施进程，开发者一般不直接操作。
- 关键认知：主进程卡 = 全部窗口卡（菜单/窗口管理失灵）；渲染进程卡 = 单窗口卡；崩溃隔离由进程边界保证。

```text
electron-app 进程树（tasklist / ps 视角）
electron（主进程 main.ts：app、BrowserWindow、ipcMain、托盘、全局快捷键）
├── renderer（窗口 A 的 Chromium 渲染进程：index.html + preload.cjs）
├── renderer（窗口 B 的渲染进程）
├── utility-process（utilityProcess.fork('worker.cjs')：重 CPU 任务、文件索引）
├── GPU Process（合成与光栅化，所有窗口共享）
└── Network Service（网络栈，独立进程）

// main.ts —— 进程模型骨架
import { app, BrowserWindow, utilityProcess } from 'electron';
app.whenReady().then(() => {
  const win = new BrowserWindow({ webPreferences: { preload: path.join(__dirname, 'preload.cjs') } });
  win.loadFile('index.html');                                   // 独立渲染进程
  const util = utilityProcess.fork(path.join(__dirname, 'worker.cjs'));
  util.postMessage({ task: 'index', dir: '/docs' });            // 重活放 Utility，防主进程阻塞
});
```
