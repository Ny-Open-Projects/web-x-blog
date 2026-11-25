---
title: [XP-194] Electron 应用生命周期：单实例锁与退出清理
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-194：Electron 应用生命周期：单实例锁与退出清理

**答**：
- 题目：Electron 应用生命周期——单实例锁（requestSingleInstanceLock）、退出清理（关闭前保存状态/清理临时文件）、崩溃恢复。
- 思路：requestSingleInstanceLock（第二实例唤醒第一实例）；before-quit 生命周期（异步清理）；崩溃恢复（临时文件检测）。
- 评分点：单实例锁；异步清理；崩溃恢复。

```javascript
const gotLock = app.requestSingleInstanceLock();                 // 单实例锁
if (!gotLock) { app.quit(); } else {
  app.on('second-instance', (e, argv) => {                        // 第二实例唤醒
    win.show();                                                    // 聚焦已有窗口
    const deepLink = argv.find(a => a.startsWith('app://'));        // 处理深链
    if (deepLink) handleDeepLink(deepLink);
  });
}
app.on('before-quit', async (e) => {                              // 退出清理
  if (cleanupPending) { e.preventDefault(); await doCleanup(); app.exit(0); }
});
app.on('will-quit', async (e) => {                                 // 异步清理
  e.preventDefault();
  await db.close();                                                 // 关库
  await tempFiles.clean();                                           // 清临时文件
  app.exit(0);
});
```
