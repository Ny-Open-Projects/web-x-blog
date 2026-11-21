---
title: [ARC-115] Electron 桌面端架构如何设计（主进程/渲染进程/IPC/安全策略）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-115：Electron 桌面端架构如何设计（主进程/渲染进程/IPC/安全策略）？
**答**：
- 进程模型：主进程管窗口、托盘、自动更新、系统能力与全局状态；渲染进程每窗口一个，跑 UI；重 CPU 任务（大文件解析、加密）再开 utilityProcess/子进程，不阻塞渲染。
- IPC 治理：渲染进程不直接碰 Node（contextIsolation: true、nodeIntegration: false），preload 用 contextBridge 暴露白名单 API；IPC handler 按模块注册并校验入参，禁止 `ipcRenderer.send('eval', code)` 这类通用通道。
- 安全清单：禁 remote 模块、CSP 收紧、webview 开 sandbox、加载内容校验协议（只允许 app:// 与白名单 https）、依赖供应链审计。
- 发布链路：自动更新（全量+差量）、崩溃采集（main + renderer 分开上报）、多窗口状态恢复。

```typescript
// preload.ts：唯一的安全暴露面
import { contextBridge, ipcRenderer } from 'electron';

const ALLOWED_CHANNELS = ['file:open', 'file:save', 'app:update', 'db:query'] as const;
type AllowedChannel = (typeof ALLOWED_CHANNELS)[number];

contextBridge.exposeInMainWorld('desktop', {
  invoke: (channel: AllowedChannel, payload: unknown) => {
    if (!ALLOWED_CHANNELS.includes(channel)) {          // 1. 通道白名单
      return Promise.reject(new Error(`channel not allowed: ${channel}`));
    }
    return ipcRenderer.invoke(channel, payload);        // 2. invoke 模式（有回执）
  },
});
// main.ts：handler 按模块注册 + 入参校验
// ipcMain.handle('db:query', async (_e, q: QueryInput) => {
//   parseWithZod(QuerySchema, q);          // 渲染进程输入不可信，一律校验
//   return db.run(q);                      // 重计算走 utilityProcess，不占渲染进程
// });
// 渲染进程 webPreferences：{ contextIsolation: true, nodeIntegration: false, sandbox: true }
```
