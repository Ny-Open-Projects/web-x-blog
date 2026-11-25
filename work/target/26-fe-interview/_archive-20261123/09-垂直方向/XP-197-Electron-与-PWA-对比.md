---
title: [XP-197] Electron 与 PWA 对比：桌面应用的两种路径
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-197：Electron 与 PWA 对比：桌面应用的两种路径

**答**：
- Electron vs PWA：Electron 完全控制（Node/系统集成/多窗口）但体积大（~150MB）/内存高；PWA（浏览器安装）轻量（~5MB）但受浏览器沙箱限制。
- 选型：需要文件系统深度操作/系统托盘/原生菜单 → Electron；Web 应用增强（离线/推送/快捷方式）→ PWA。
- 混合路径：Web 版 PWA 先行 → 需求驱动升级 Electron（业务代码复用）。

```javascript
const electronVsPwa = {
  electron: { size: '~150MB', memory: '高（独立 Chromium）',
    capabilities: ['Node.js', '文件系统', '系统托盘', '原生菜单', '多窗口', 'Native addon'],
    fit: 'IDE/重桌面工具（VS Code/Figma Desktop）' },
  pwa: { size: '~5MB', memory: '低（浏览器内）',
    capabilities: ['离线（Service Worker）', '推送', '快捷方式', '文件系统访问（File System Access API，受限）'],
    fit: 'Web 应用增强（Notion/Twitter 桌面版）' },
  migration: 'Web 版 → PWA（加 manifest/SW）→ Electron（加 Node 层）——业务代码复用率 > 90%',
  decision: '文件系统深度操作/多窗口/原生模块 → Electron；否则 PWA 够用',
};
```
