---
title: [XP-186] Electron 多窗口管理：窗口池与状态恢复
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-186：Electron 多窗口管理：窗口池与状态恢复

**答**：
- 多窗口：窗口池（复用 BrowserWindow 避免频繁创建销毁——创建成本 200ms+）；窗口状态持久化（位置/大小/布局恢复）。
- 实现：窗口池 acquire/release；状态保存（Bounds + 全屏状态）→ 启动恢复；多显示器场景（屏幕变化重排）。
- 内存：每窗口独立渲染进程——窗口池上限（同类型最多 3 个）。

```javascript
class WindowPool {
  constructor({ maxPerType = 3 } = {}) { this.pool = new Map(); this.max = maxPerType; }
  async acquire(type) {                                         // 获取窗口
    const pool = this.pool.get(type) ?? [];
    const idle = pool.find(w => !w.busy);
    if (idle) { idle.busy = true; return idle; }                 // 复用
    if (pool.length >= this.max) {
      const oldest = pool.sort((a, b) => a.lastUsed - b.lastUsed)[0];   // 淘汰最旧
      oldest.destroy(); pool.splice(pool.indexOf(oldest), 1);
    }
    const win = await this.createWindow(type);                    // 新建（200ms）
    pool.push(win);
    return win;
  }
  saveState(win) { win.getBounds(); }                             // 状态持久化
  restoreState(type) {                                             // 启动恢复
    const saved = store.get(`window-${type}`);
    if (saved) return { x: saved.x, y: saved.y, width: saved.width, height: saved.height };
  }
}
```
