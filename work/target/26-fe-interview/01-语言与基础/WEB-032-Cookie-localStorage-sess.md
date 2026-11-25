---
title: [WEB-032] Cookie、localStorage、sessionStorage、IndexedDB 如何选型？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-032：Cookie、localStorage、sessionStorage、IndexedDB 如何选型？
**答**：
- Cookie：需要随请求自动发给服务器的身份信息（session id、追踪），体积 4KB，每次请求都带上要注意膨胀。
- localStorage：同源持久化的小型配置与状态（主题、语言、UI 偏好）。
- sessionStorage：会话期临时数据（表单草稿、一次性流程状态）。
- IndexedDB：大容量结构化数据（离线缓存、消息记录、媒体文件），异步事务型，容量可达数百 MB 以上。
- 安全红线：XSS 能读 localStorage，凭证类要么 HttpOnly Cookie，要么配合严格的 XSS 防护。

```javascript
// IndexedDB 基本用法：异步打开、建索引、增查
function openDB() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open('chat-db', 1);
    req.onupgradeneeded = () => {
      const db = req.result;
      if (!db.objectStoreNames.contains('messages')) {
        const store = db.createObjectStore('messages', { keyPath: 'id', autoIncrement: true });
        store.createIndex('by_chat', 'chatId'); // 按 chatId 建索引
      }
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

const db = await openDB();

// 写入（事务）
function addMessage(msg) {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('messages', 'readwrite');
    tx.objectStore('messages').add(msg);
    tx.oncomplete = resolve;
    tx.onerror = () => reject(tx.error);
  });
}
await addMessage({ chatId: 1, text: 'hello', time: Date.now() });

// 按索引查询
function messagesOf(chatId) {
  return new Promise((resolve) => {
    db.transaction('messages').objectStore('messages').index('by_chat').getAll(chatId).onsuccess = (e) =>
      resolve(e.target.result);
  });
}
console.log(await messagesOf(1));
```

## 追问（补充）

**追问**：

1. Cookie 每次请求都携带，怎么避免拖慢首屏？ → 静态资源放独立 CDN 域名不带 Cookie，主域 Cookie 用 Path 与 SameSite 收窄范围，控制体积在 4KB 内。
2. localStorage 是同步 API，大量写入有什么代价？ → 阻塞主线程，序列化大对象会掉帧甚至卡死，大容量结构化数据应换 IndexedDB 的异步事务。
3. sessionStorage 在刷新与新建标签时的表现？ → 刷新保留，同源新标签默认不共享，`window.open` 或复制标签页会复制一份副本，容易误以为「跨标签共享」。
