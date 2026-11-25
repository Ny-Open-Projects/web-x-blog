---
title: [XP-188] Electron 系统集成：托盘/通知/全局快捷键
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-188：Electron 系统集成：托盘/通知/全局快捷键

**答**：
- 题目：Electron 系统集成——系统托盘（菜单/图标/点击事件）、系统通知（Notification API）、全局快捷键（注册/冲突处理）。
- 思路：Tray（托盘图标+菜单）；Notification（系统通知，点击深链）；globalShortcut（全局快捷键，冲突时捕获失败降级）。
- 评分点：托盘菜单；通知点击深链；快捷键冲突。

```javascript
const { Tray, Menu, Notification, globalShortcut } = require('electron');
class SystemIntegration {
  setupTray(win) {                                              // 托盘
    this.tray = new Tray(trayIcon);
    this.tray.setContextMenu(Menu.buildFromTemplate([
      { label: '打开主窗口', click: () => win.show() },
      { label: '退出', click: () => app.quit() },
    ]));
    this.tray.on('click', () => win.show());
  }
  notify(title, body, deepLink) {                               // 系统通知
    const n = new Notification({ title, body });
    n.on('click', () => { win.show(); win.webContents.send('deep-link', deepLink); });
    n.show();
  }
  registerShortcut(accelerator, cb) {                            // 全局快捷键
    try {
      globalShortcut.register(accelerator, cb);                   // 冲突时抛错
    } catch {                                                     // 冲突：降级为应用内快捷键
      report('shortcut-conflict', { accelerator });
    }
  }
}
```
