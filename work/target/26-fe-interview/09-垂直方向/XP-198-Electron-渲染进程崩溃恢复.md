---
title: [XP-198] Electron 渲染进程崩溃恢复：窗口重建与状态恢复
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-198：Electron 渲染进程崩溃恢复：窗口重建与状态恢复

**答**：
- 题目：渲染进程崩溃（OOM/渲染器异常）——崩溃检测（render-process-gone）→ 窗口重建 → 状态恢复（路由/表单数据）。
- 思路：render-process-gone 事件 → 重建 BrowserWindow → 渲染进程恢复（路由栈从主进程缓存恢复 + 表单数据定期快照）。
- 评分点：崩溃监听；窗口重建；状态恢复。

```javascript
class CrashRecovery {
  constructor() {
    app.on('render-process-gone', async (e, contents, details) => {
      if (details.reason === 'clean-exit') return;                  // 正常退出不恢复
      fire('renderer-crash', { reason: details.reason });           // 上报
      await this.rebuildWindow(contents);                            // 重建
    });
  }
  async rebuildWindow(crashedContents) {
    const state = this.windowStates.get(crashedContents);            // 恢复状态（主进程缓存）
    const newWin = await this.createWindow(state?.route);             // 重建窗口
    if (state?.formData) newWin.webContents.send('restore-form', state.formData);   // 表单恢复
  }
}
// 表单数据定期快照：渲染进程 setInterval(() => ipc.send('form-snapshot', formData), 10000)
```
