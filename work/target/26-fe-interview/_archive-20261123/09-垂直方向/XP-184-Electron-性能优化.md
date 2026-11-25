---
title: [XP-184] Electron 性能优化：启动时间与内存
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-184：Electron 性能优化：启动时间与内存

**答**：
- 启动优化：主进程延迟加载（require 惰性）、渲染进程窗口延迟创建、V8 快照缓存；目标冷启动 < 2s。
- 内存：渲染进程多窗口（每窗口 ~100MB）→ 单窗口多视图（WebContentsView 复用进程）；GPU 缓存清理。
- 量化：主进程 require 全量依赖 800ms → 惰性加载 200ms。

```javascript
class ElectronPerf {
  lazyRequire() {                                             // 主进程惰性加载
    // BAD: const heavy = require('heavy-lib') 启动即加载（800ms）
    let _heavy = null;
    Object.defineProperty(module.exports, 'heavy', {
      get() { return _heavy ??= require('heavy-lib'); },       // 首次使用才加载
    });
  }
  sharedWebContents() {                                       // 单进程多视图
    // 多窗口 → 多渲染进程（每进程 100MB）→ 内存爆炸
    // 改用 WebContentsView：共享一个渲染进程
    const view = new WebContentsView({ webPreferences: { shared: true } });
    win.contentView.addChildView(view);                        // 复用进程
  }
}
```
