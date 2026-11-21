---
title: [H5-257] Background Sync 是什么：弱网补发请求
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-257：Background Sync 是什么：弱网补发请求

**答**：
- 语义：注册一个「网络恢复后」的任务——即使页面已关闭，浏览器也会在联网时唤醒 SW 执行 sync 事件
- 典型场景：弱网下发的消息先存 IndexedDB，sync 到达后补发；相当于浏览器代管的离线队列
- API：主线程 `swRegistration.sync.register('send-msg')`；SW 里 `sync` 事件处理 + `event.waitUntil`
- 局限：Chrome 支持较好，Safari/Firefox 支持有限——关键业务不要只依赖它，页面存活时先尝试直接发送
- 升级版 Periodic Sync：定期唤醒（如每小时同步），仅安装后的 PWA 且系统裁量，浏览器控制频率不可信任

```javascript
// 主线程：弱网先存后发
await idbPut('outbox', msg);
await registration.sync.register('send-msg');
// SW
self.addEventListener('sync', (e) => {
  if (e.tag === 'send-msg') {
    e.waitUntil(idbAll('outbox').then(msgs =>
      Promise.all(msgs.map(m => fetch('/api/msg', { method: 'POST', body: JSON.stringify(m) })
        .then(() => idbDelete('outbox', m.id)))));
  }
});
```
