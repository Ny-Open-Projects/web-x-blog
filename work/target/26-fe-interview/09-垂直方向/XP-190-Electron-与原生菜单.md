---
title: [XP-190] Electron 与原生菜单：应用菜单与上下文菜单
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-190：Electron 与原生菜单：应用菜单与上下文菜单

**答**：
- 题目：Electron 菜单——应用菜单（macOS 顶部菜单栏/Windows 窗口菜单）、右键上下文菜单（自定义）、菜单与快捷键绑定。
- 思路：Menu.setApplicationMenu（应用级，macOS 必须）；webContents.on context-menu（右键事件 → 自定义菜单）；accelerator 绑定快捷键。
- 评分点：应用菜单；上下文菜单；快捷键绑定。

```javascript
const { Menu, MenuItem } = require('electron');
function setupAppMenu(win) {                                     // 应用菜单
  const template = [
    { label: '文件', submenu: [
      { label: '新建', accelerator: 'CmdOrCtrl+N', click: () => win.webContents.send('menu', 'new') },
      { type: 'separator' },
      { label: '退出', role: 'quit' },
    ] },
    { label: '编辑', role: 'editMenu' },                          // 角色菜单（复制粘贴等）
  ];
  Menu.setApplicationMenu(Menu.buildFromTemplate(template));      // macOS 必须
}
win.webContents.on('context-menu', (e, params) => {              // 右键菜单
  const menu = new Menu();
  if (params.isEditable) {
    menu.append(new MenuItem({ label: '粘贴', role: 'paste' }));
  }
  if (params.selectionText) {
    menu.append(new MenuItem({ label: '复制', role: 'copy' }));
  }
  menu.popup();
});
```
