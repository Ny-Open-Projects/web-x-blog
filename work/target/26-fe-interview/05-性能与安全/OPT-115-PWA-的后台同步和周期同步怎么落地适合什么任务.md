---
title: [OPT-115] PWA 的后台同步和周期同步怎么落地？适合什么任务？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-115：PWA 的后台同步和周期同步怎么落地？适合什么任务？

**答**：
- **Background Sync**（`sync` 事件）：用户关页面后，浏览器在网络恢复时唤醒 SW 执行任务——离线发出的表单/聊天消息在恢复后自动补发，是"离线优先"的闭环。
- **Periodic Background Sync**：定期唤醒（浏览器自定频率，通常受 PWA 安装与使用频次影响），适合内容预热、离线数据更新，不能当定时闹钟用。
- 限制要背：Chrome 限定已安装 PWA 且 HTTPS、iOS Safari 两者都缺（iOS 用推送通知替代部分场景）；同步任务没有 UI 权限，失败要重试设计。
- 与 OPT-028/029 的缓存策略衔接：sync 补发的是**写请求**队列，cache-first 管的是**读请求**。

```javascript
// 一一对应：后台同步注册 + SW 内补发队列 + 周期同步预热
// main.js —— 发消息失败入队并注册 sync
async function sendMessage(msg) {
  try {
    await fetch('/api/messages', { method: 'POST', body: JSON.stringify(msg) });
  } catch {
    const db = await openDb('outbox');
    await db.put('messages', { id: crypto.randomUUID(), msg, ts: Date.now() });
    const reg = await navigator.serviceWorker.ready;
    // 注册后台同步：网络恢复时浏览器自动触发 SW 的 sync 事件
    await reg.sync.register('outbox-sync');
  }
}

// sw.js —— sync 事件里补发
self.addEventListener('sync', (event) => {
  if (event.tag === 'outbox-sync') {
    event.waitUntil(flushOutbox()); // waitUntil：任务完成前 SW 不被杀
  }
});
async function flushOutbox() {
  const db = await openDb('outbox');
  const items = await db.getAll('messages');
  for (const it of items) {
    try {
      await fetch('/api/messages', { method: 'POST', body: JSON.stringify(it.msg) });
      await db.delete('messages', it.id); // 成功才出队，失败留着下次
    } catch { break; } // 仍离线：整体退出，等下一次 sync
  }
}

// 周期同步：已安装的 PWA 定期预热内容
self.addEventListener('periodicsync', (event) => {
  if (event.tag === 'content-refresh') {
    event.waitUntil((async () => {
      const cache = await caches.open('news-v1');
      await cache.addAll(['/api/top-stories']); // 用户打开前就绪
    })());
  }
});
// 注册周期同步（必须已安装 PWA，频率浏览器自定）：
// const reg = await navigator.serviceWorker.ready;
// if ('periodicSync' in reg) {
//   const status = await navigator.permissions.query({ name: 'periodic-background-sync' });
//   if (status.state === 'granted') await reg.periodicSync.register('content-refresh', { minInterval: 12 * 3600 * 1000 });
// }
```
