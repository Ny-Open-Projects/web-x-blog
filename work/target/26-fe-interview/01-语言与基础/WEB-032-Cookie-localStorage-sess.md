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
