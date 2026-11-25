---
title: [WEB-400] 存储配额怎么查？requestPersistentStorage 是干什么的？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-400：存储配额怎么查？requestPersistentStorage 是干什么的？
**答**：
- 配额查询：navigator.storage.estimate() 返回 usage/quota（通常约磁盘空闲的一定比例，Chrome 数十 GB 级）；per-origin 隔离。
- 默认存储是"best-effort"：磁盘压力下浏览器可清；requestPersistentStorage() 申请持久化（PWA 安装后更易批准），用户须保留则不清理。
- 实践：大文件缓存（视频/音频）先查配额再下、监听 quota exceeded 降级清理旧缓存。

```javascript
const { usage, quota } = await navigator.storage.estimate();
console.log('已用', (usage / 1e6).toFixed(1), 'MB / 配额', (quota / 1e9).toFixed(1), 'GB');
const persisted = await navigator.storage.persist();
if (!persisted) console.warn('压力下可能被清，重要数据要同步服务端');
```
