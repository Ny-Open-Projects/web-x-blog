---
title: [RBL-100] 笔试：手写文件监听器（防抖 + glob 过滤 + 变更分类）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-100：笔试：手写文件监听器（防抖 + glob 过滤 + 变更分类）
**题目**：实现 watchFiles(paths, cb)：1) 对目录树递归建立 mtime 快照；2) 轮询对比发现 added/changed/removed 三类变更；3) 支持 ignore glob（如 node_modules/**）；4) 变更事件防抖 100ms 批量回调（参数为 [{type, file}]）；5) 停止监听 stop()。

```javascript
const fs = require('fs'), path = require('path');

function watchFiles(paths, cb, { ignore = [], interval = 500, debounce = 100 } = {}) {
  let snapshot = new Map();   // file -> mtimeMs
  let timer = null, poll = null, stopped = false;
  let pending = [];           // 防抖批

  const ignored = (f) => ignore.some(g =>
    f.includes(g.replace(/\*\*/g, '').replace(/\/$/, '')));

  function scan(dir, acc) {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (ignored(p)) continue;
      if (e.isDirectory()) scan(p, acc);
      else acc.set(p, fs.statSync(p).mtimeMs);
    }
  }
  function tick() {
    if (stopped) return;
    const now = new Map();
    scan(paths, now);
    const events = [];
    for (const [f, mt] of now)
      if (!snapshot.has(f)) events.push({ type: 'added', file: f });
      else if (snapshot.get(f) !== mt) events.push({ type: 'changed', file: f });
    for (const f of snapshot.keys())
      if (!now.has(f)) events.push({ type: 'removed', file: f });
    snapshot = now;
    if (events.length) {
      pending.push(...events);
      clearTimeout(timer);
      timer = setTimeout(() => { cb(pending); pending = []; }, debounce);
    }
  }
  poll = setInterval(tick, interval);
  return { stop() { stopped = true; clearInterval(poll); clearTimeout(timer); } };
}
module.exports = { watchFiles };
```
**评分点**：
- 快照对比产生三类事件（added/changed/removed 全覆盖）。
- ignore 过滤在扫描阶段剪枝（不只过滤结果）。
- 防抖批量回调（编辑器保存风暴合并）。
- stop 释放定时器（资源清理）。
- 能指出生产用 fs.watch/inotify/chokidar 而非轮询，轮询是简化实现。
