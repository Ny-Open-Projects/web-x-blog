---
title: [XP-104] Electron 多窗口的性能怎么治理？共享进程怎么设计？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-104：Electron 多窗口的性能怎么治理？共享进程怎么设计？
**答**：
- 成本认知：每个 BrowserWindow 独立渲染进程（几十 MB 起），多窗口+多 webview 会让内存与 GPU 翻倍；治理三方向——**窗口复用、进程共享、按需创建**。
- 窗口复用：功能相近的弹窗类窗口合并为单实例多视图（切换 URL/状态而非新建）；隐藏代替销毁要配合释放重资源（视频/大列表），显示时恢复。
- **utilityProcess 共享**：重计算（数据索引、文件解析、压缩）从各窗口抽离到 utilityProcess（独立 Node 进程，主进程管理），窗口间经主进程转发或 MessagePort 直连，避免每个窗口各自起 Node 重活。
- 渲染进程间通信：主进程做 hub（广播节流），或 `MessageChannelMain` 建 port 直连降主进程压力；大数据（文件句柄/Buffer）走 structured clone 一次性传递。
- 治理指标：窗口数 × 内存基线监控、GPU 进程崩溃率、主进程事件循环阻塞时长；`backgroundThrottling` 按窗口场景开关（后台窗口可降帧）。

```javascript
// main/windows.js —— 窗口复用 + utilityProcess 共享计算
import { BrowserWindow, utilityProcess, MessageChannelMain } from 'electron';

// 1) 弹窗类窗口单实例复用：按 role 取窗，隐藏不销毁
const windowPool = new Map();
function getWindow(role) {
  if (windowPool.has(role)) return windowPool.get(role);
  const win = new BrowserWindow({
    show: false,
    webPreferences: { preload: PRELOAD, sandbox: true, nodeIntegration: false },
  });
  win.on('close', (e) => {                 // 关闭改隐藏：复用实例
    if (!app.isQuitting) { e.preventDefault(); win.hide(); releaseHeavy(win); }
  });
  windowPool.set(role, win);
  return win;
}
function releaseHeavy(win) { win.webContents.send('page:pause'); } // 停视频/大列表

// 2) utilityProcess：重计算抽离，多窗口共享一个 worker
const worker = utilityProcess.fork(path.join(__dirname, 'worker/indexer.js'));
ipcMain.handle('index:search', async (_e, q) => {
  const { port1, port2 } = new MessageChannelMain();   // port 直连：主进程只做接线
  worker.postMessage({ type: 'search', q, port: port2 }, [port2]);
  return new Promise((resolve) => { port1.once('message', (m) => { resolve(m.data); port1.close(); }); });
});

// 3) 广播节流：主进程 hub 聚合后再分发，防多窗口风暴
const broadcast = throttle((channel, payload) =>
  BrowserWindow.getAllWindows().forEach((w) => w.webContents.send(channel, payload)), 100);
// 监控：每窗口内存基线 + GPU 崩溃率 + 主进程 loop lag（口径进 XP-135 平台）
```
