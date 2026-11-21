---
title: [WEB-184] WiFi 与 4G 网络切换时，前端要注意什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-184：WiFi 与 4G 网络切换时，前端要注意什么？
**答**：
- 切换等于网络接口与 IP 变化，所有已建立的 TCP/TLS 连接作废：WS 与 HTTP/2 多路复用连接集中断开重连，形成"切换风暴"。
- 监听 online/offline（Network Information API 只做参考），对在途请求主动 abort，避免悬挂。
- 重连要指数退避加随机抖动；多标签页场景用 Web Locks/竞态协调，避免同时打爆服务端。
- 切换期优先恢复关键路径：先恢复鉴权态，再恢复业务通道；已失败的写操作进离线同步队列。

```javascript
// 切网时的连接治理：中断在途请求 + 延迟重连
let controller = null;
async function loadFeed() {
  controller?.abort();                      // 旧请求作废
  controller = new AbortController();
  try {
    const res = await fetch('/api/feed', { signal: controller.signal });
    render(await res.json());
  } catch (e) {
    if (e.name !== 'AbortError') scheduleRetry();
  }
}
window.addEventListener('offline', () => controller?.abort());
window.addEventListener('online', () => {
  // 抖动 0.5 到 2 秒，避免切换风暴把请求同时打回源站
  setTimeout(loadFeed, 500 + Math.random() * 1500);
});
```
