---
title: [XP-183] Electron 自动更新：electron-updater 与差分更新
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-183：Electron 自动更新：electron-updater 与差分更新

**答**：
- 题目：Electron 自动更新——electron-updater 全量/差分更新、灰度发布（按比例放量）、强制更新（关键安全修复）。
- 思路：electron-updater（checkForUpdates → download → quitAndInstall）；差分（blockmap 只下载变更块）；灰度（更新服务端按用户分桶下发版本）；强制更新（主进程阻断业务直到更新完成）。
- 评分点：更新流程；差分更新；灰度与强制。

```javascript
const { autoUpdater } = require('electron-updater');
class AppUpdater {
  setup({ force = false, grayPercent = 100 } = {}) {
    autoUpdater.on('update-downloaded', async () => {
      if (force) {                                              // 强制更新
        autoUpdater.quitAndInstall(false, true);                // 静默安装
        return;
      }
      showUpdateDialog({ onConfirm: () => autoUpdater.quitAndInstall() });   // 用户确认
    });
    this.check();
  }
  async check() {
    const update = await autoUpdater.checkForUpdates();         // 检查（服务端按灰度下发）
    if (!update) report('up-to-date');
  }
}
// 差分更新：blockmap 文件记录块 hash——只下载变更块（100MB 包 → 变更 5MB）
// 灰度：更新服务器按 userId hash 分桶 → 灰度组返回新版本 URL
```
