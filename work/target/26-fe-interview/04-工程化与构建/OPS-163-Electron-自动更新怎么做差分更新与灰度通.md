---
title: [OPS-163] Electron 自动更新怎么做？差分更新与灰度通道怎么设计？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-163：Electron 自动更新怎么做？差分更新与灰度通道怎么设计？
**答**：
- electron-updater + 更新服务器（generic provider 即可用静态文件服务）：客户端定期静默检查、下载后提示重启安装。
- 差分更新：blockmap 机制只下载差异块，百兆安装包的更新可压到几 MB，桌面用户敏感流量。
- 通道制：alpha/beta/stable 三通道，stable 永远落后 beta 两周，beta 崩溃率达标才晋升——灰度在通道间完成。
- 服务端灰度：更新清单按 machine id hash 决定是否命中放量，配合崩溃率监控自动暂停。
- 更新必须有兜底：allowDowngrade 防降级回环；强制更新场景走"关键版本号"标记，客户端按策略阻断使用旧版。

```javascript
// electron-updater：通道制 + 差分更新 + 服务端灰度
const { autoUpdater } = require('electron-updater');

autoUpdater.channel = process.env.UPDATE_CHANNEL || 'stable';   // alpha / beta / stable
autoUpdater.allowDowngrade = false;      // 防版本降级回环
autoUpdater.autoDownload = false;        // 下载前提示，尊重桌面用户掌控感

autoUpdater.on('update-available', async (info) => {
  // 服务端灰度：更新清单按 machine id hash 判断是否命中本次放量
  const hit = await window.api.checkGrayFlags(info.version);
  if (hit) await autoUpdater.downloadUpdate();   // 差分更新：只下载 blockmap 差异块
});

autoUpdater.on('update-downloaded', async () => {
  const { response } = await dialog.showMessageBox({
    message: '新版本已就绪，是否立即重启更新？',
    buttons: ['立即重启', '稍后'],
  });
  if (response === 0) autoUpdater.quitAndInstall(false, true);
});

setInterval(() => autoUpdater.checkForUpdates(), 4 * 3600 * 1000);  // 每 4h 静默检查

// 发布纪律：stable 落后 beta 两周；beta 崩溃率达标才晋升；崩溃率超阈值自动暂停放量
```
