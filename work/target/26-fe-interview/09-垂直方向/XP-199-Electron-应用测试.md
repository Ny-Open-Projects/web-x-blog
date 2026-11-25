---
title: [XP-199] Electron 应用测试：主进程单测与渲染进程 E2E
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-199：Electron 应用测试：主进程单测与渲染进程 E2E

**答**：
- 题目：Electron 测试——主进程单元测试（mock electron 模块）、渲染进程 E2E（Playwright Electron 支持）、IPC 集成测试。
- 思路：主进程单测：mock electron（app/BrowserWindow）+ 纯逻辑抽离；E2E：Playwright _electron.launch → 操作窗口断言；IPC 测试：真 IPC 通道跑集成。
- 评分点：electron mock；Playwright E2E；IPC 集成。

```javascript
// 主进程单测（mock electron）
jest.mock('electron', () => ({
  app: { getPath: jest.fn().mockReturnValue('/tmp'), on: jest.fn() },
  BrowserWindow: jest.fn().mockImplementation(() => ({ loadURL: jest.fn(), show: jest.fn() })),
  ipcMain: { handle: jest.fn(), on: jest.fn() },
}));
import { assertSafePath } from '../main/fs-guard';                  // 纯逻辑测试
it('rejects path escape', () => {
  expect(() => assertSafePath('/etc/passwd')).toThrow('path-escape');
});
// Playwright E2E
import { _electron as electron } from 'playwright';
const app = await electron.launch({ args: ['main.js'] });            // 启动应用
const win = await app.firstWindow();
await win.click('#open-file');                                       // 操作 UI
await expect(win.locator('.content')).toContainText('loaded');        // 断言
```
