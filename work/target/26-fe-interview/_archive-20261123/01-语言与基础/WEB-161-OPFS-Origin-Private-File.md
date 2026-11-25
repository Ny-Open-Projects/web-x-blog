---
title: [WEB-161] OPFS（Origin Private File System）是什么？解决什么问题？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-161：OPFS（Origin Private File System）是什么？解决什么问题？
**答**：
- OPFS 是源私有的文件系统：路径不可枚举、不与用户文件混用，配额走标准 Storage 体系，storage.getDirectory() 拿根目录。
- 亮点是同步访问句柄 createSyncAccessHandle()：只能在 Worker 里用，对文件做同步读写，性能远超 Web 上的异步 API。
- 主线程只能用异步 createWritable()；两者覆盖"后台高性能计算"与"前台轻量存文件"两个场景。
- 典型应用：SQLite-WASM 的持久化后端（官方推荐就是 OPFS），让浏览器里跑数据库性能可用；也用于大模型文件、视频帧处理。

```javascript
// OPFS 基本读写（主线程异步 API）
const root = await navigator.storage.getDirectory();
const fileHandle = await root.getFileHandle('page-count.json', { create: true });
const writable = await fileHandle.createWritable();
await writable.write(JSON.stringify({ visits: 42 }));
await writable.close();
const blob = await fileHandle.getFile();
console.log(JSON.parse(await blob.text()).visits); // 42

// Worker 里的高性能同步句柄（SQLite-WASM 的用法，仅 Worker 可用）
// const fh = await root.getFileHandle('db.sqlite', { create: true });
// const access = await fh.createSyncAccessHandle();
// access.write(buf, { at: offset }); access.flush(); access.read(buf, { at: offset });
```
