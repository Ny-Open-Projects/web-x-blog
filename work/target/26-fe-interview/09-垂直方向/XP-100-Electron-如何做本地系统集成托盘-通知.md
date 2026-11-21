---
title: [XP-100] Electron 如何做本地系统集成？托盘、通知、文件关联？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-100：Electron 如何做本地系统集成？托盘、通知、文件关联？
**答**：
- 托盘（Tray）：常驻图标 + 上下文菜单（显示主窗口/快捷任务/退出）；注意 macOS 菜单栏图标模板图（`setTemplateImage`）与 Windows 托盘闪烁处理；点击行为平台差异分派。
- 通知：用系统原生 `new Notification()`（走系统通知中心），别用渲染进程 HTML 模拟；点击通知跳转对应窗口/会话需要携带 payload 回传主进程路由。
- 文件/URL 关联：打包配置（electron-builder `fileAssociations`/`protocols`）注册文件类型与协议，运行时经 `open-file`/`open-url` 事件（macOS）与 `process.argv`（Windows 二次启动）接收，统一路由到主窗口处理。
- 其它集成：开机自启（`app.setLoginItemSettings`）、全局快捷键（`globalShortcut`，注意冲突与用户可关）、剪贴板、`shell.openPath/showItemInFolder`。
- 平台差异收口：所有系统能力经 `platform/` 适配层封装，渲染进程永远只调统一 IPC 接口（权限申请与能力探测也在此层，风格对齐 XP-070）。

```javascript
// main/integration.js —— 托盘 + 通知 + 文件关联 统一集成层
import { app, Tray, Menu, Notification, shell } from 'electron';

let tray;
function initTray(mainWindow) {
  tray = new Tray(iconFor(process.platform));              // mac 用 Template 图标自动适配
  tray.setToolTip('MyApp');
  tray.setContextMenu(Menu.buildFromTemplate([
    { label: '打开主窗口', click: () => showWindow(mainWindow) },
    { label: '开始同步', click: () => ipcSend('sync:start') },
    { type: 'separator' },
    { label: '退出', click: () => { app.quit(); } },
  ]));
  // mac: 点击图标弹菜单；win/linux: 点击直接开窗
  tray.on('click', () => process.platform === 'darwin' ? tray.popUpContextMenu()
                                                        : showWindow(mainWindow));
}

function notify(payload) {                                  // 系统原生通知
  if (!Notification.isSupported()) return;
  const n = new Notification({ title: payload.title, body: payload.body });
  n.on('click', () => routeTo(payload));                    // 点击跳转：主进程统一路由
  n.show();
}

// 文件关联：electron-builder.yml 配 fileAssociations 与 protocols（见下）
app.on('open-file', (e, path) => {                          // macOS：已启动实例
  e.preventDefault(); routeToFile(path);
});
app.on('second-instance', (_e, argv) => {                   // Windows/Linux：二次启动带参
  const file = argv.find(a => /\.(myext|mypkg)$/.test(a));
  if (file) routeToFile(file);
  showWindow(mainWindow);
});
const gotLock = app.requestSingleInstanceLock();            // 单实例锁：二次启动转发参数
if (!gotLock) app.quit();
// electron-builder.yml 片段：
// fileAssociations: [ { ext: myext, name: MyApp Document, role: Editor } ]
// protocols: [ { name: MyApp Deep Link, schemes: [myapp] } ]   // myapp:// 协议深链
```
