---
title: [WEB-412] Origin Private File System（OPFS）是什么？什么场景用？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-412：Origin Private File System（OPFS）是什么？什么场景用？
**答**：
- OPFS 是页面/Worker 私有的文件系统（navigator.storage.getDirectory()），不走用户目录、性能接近本地文件，可同步访问（Worker 里 createSyncAccessHandle）。
- 适用：SQLite WASM 持久化、大文件本地缓存、离线编辑草稿；比 localStorage 大得多、比 IndexedDB 二进制读写快。
- 注意：仅私有无路径导出能力有限；跨标签页同步句柄有排他锁（拿不到要重试）。

```javascript
const root = await navigator.storage.getDirectory();
const fh = await root.getFileHandle('draft.json', { create: true });
const w = await fh.createWritable();
await w.write(JSON.stringify(draft)); await w.close();
// Worker 内同步: const h = await fh.createSyncAccessHandle();
console.log('OPFS=页面私有高性能文件系统');
```
