---
title: [XP-036] Electron 中重任务应该放在主进程还是渲染进程？如何分工？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-036：Electron 中重任务应该放在主进程还是渲染进程？如何分工？
**答**：
- 原则：**主进程只做轻协调**（窗口、生命周期、IPC 路由、托盘），因为它阻塞会影响所有窗口；重 CPU（压缩、解析、索引、图像处理）放 **Utility Process** 或渲染进程的 Web Worker。
- 分工矩阵：文件 IO 大量数据 → utility；纯计算不碰 Node API → renderer Web Worker；需要 Node + CPU → utilityProcess（Node 子进程）。
- 通信成本意识：大 Buffer 跨进程传输有拷贝成本，能传文件路径就不传内容，或用 SharedArrayBuffer/MessagePort 直连。
- 兜底观测：主进程加 event loop lag 监控，超阈值告警；utility 崩溃由主进程守护重启。
- 与浏览器认知对齐：渲染进程内阻塞同样掉帧，Worker 不解决"需要访问 DOM"的重活——那要靠虚拟化与增量渲染。

```javascript
// 重任务调度：utilityProcess 承担 Node 重活，renderer Worker 承担纯计算
// main.ts
const util = utilityProcess.fork('worker.cjs');
const taskMap = new Map();
ipcMain.handle('zip:create', (e, { id, files }) => {
  util.postMessage({ type: 'zip:create', id, files });       // 主进程只转发，不干活
  return 'accepted';
});
util.on('message', ({ type, id, result }) => {               // 结果回投窗口
  const win = BrowserWindow.getAllWindows().find((w) => w.webContents);
  taskMap.get(id)?.(result);
  win?.webContents.send('zip:done', { id, result });
});

// worker.cjs（Utility 进程，有 Node 能力）
process.parentPort.on('message', async ({ data }) => {
  if (data.type === 'zip:create') {
    const buf = await zipInWorkerNode(data.files);            // 压缩在子进程完成
    process.parentPort.postMessage({ type: 'zip:done', id: data.id, result: buf.length });
  }
});

// renderer：纯 CPU 且不需要 Node 的任务（如 JSON 大解析）直接 Web Worker
const w = new Worker(new URL('./parse.worker.ts', import.meta.url), { type: 'module' });
w.postMessage(bigJsonText); // 主线程不卡
```
