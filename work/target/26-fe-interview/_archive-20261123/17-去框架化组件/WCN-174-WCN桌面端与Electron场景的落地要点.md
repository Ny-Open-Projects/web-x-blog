---
title: [WCN-174] WCN 在桌面端 / Electron 场景的落地要点：与 Web 版本如何共享组件？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-174：WCN 在桌面端 / Electron 场景的落地要点：与 Web 版本如何共享组件？

**答**：
- 优势场景：Electron 多进程多窗口（BrowserWindow 各自渲染），组件以 CDN/npm 共享天然跨窗口；WCN 无框架绑定让主界面（React）、托盘面板（vanilla）、设置页（Vue）共享同一套组件。
- 落地要点一：产物分发走本地 npm 包（离线可用，不依赖 CDN），version 锁定进主进程 package.json。
- 要点二：桌面特有交互——窗口拖拽区（-webkit-app-region）、系统主题（nativeTheme）、右键菜单：组件事件 → preload bridge；组件保持事件声明式（同 Hybrid 模式 WCN-161）。
- 要点三：多窗口主题同步：主窗口切换主题 → IPC 广播 → 各窗口更新 data-theme（token 级联自动生效）。
- 要点四：性能：窗口多、常驻久——启用 WCN-169 的内存纪律；影子树渲染量大的组件（表格）用实例池。
- 与 Web 版差异收敛：desktop-only 组件放独立包，共享 core 保持 95%+ 复用率。

```javascript
// preload：组件事件桥接（Electron）
contextBridge.exposeInMainWorld('acmeBridge', {
  onThemeChange: (cb) => ipcRenderer.on('theme-change', (e, t) => cb(t)),
  openContextMenu: (menu) => ipcRenderer.send('context-menu', menu),
});
// 组件层（与 Web 共用 core）：
// this.dispatchEvent(new CustomEvent('wc-native-request', { detail: { action: 'context-menu', menu } }))
// Electron 适配器监听后调用 window.acmeBridge.openContextMenu(menu)
```
