---
title: [H5-262] 文件系统访问 API：showOpenFilePicker 能做什么
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-262：文件系统访问 API：showOpenFilePicker 能做什么

**答**：
- File System Access API：让 Web 直接读写本地文件与目录（用户授权后），能力接近原生
- 三组 API：showOpenFilePicker（选文件拿 FileSystemFileHandle）、showSaveFilePicker（另存）、showDirectoryPicker（目录句柄，可遍历递归读写）
- 与传统 input file 的区别：拿到的是「句柄」——可以重复读写、保存修改，而不是一次性只读副本
- 持久化句柄：handle 可存 IndexedDB，下次打开免重新选择（需 `queryPermission/requestPermission` 重新授权）
- 兼容降级：Firefox/Safari 不支持时降级 input[type=file] + Blob 下载；IDE 类 Web 应用（VS Code Web、Photoshop Web）是典型用户

```javascript
const [handle] = await showOpenFilePicker({ types: [{ accept: { 'text/plain': ['.md'] } }] });
const file = await handle.getFile();
const writable = await handle.createWritable();
await writable.write(fileText.toUpperCase());
await writable.close(); // 直接保存回原文件，无需再下载
```
