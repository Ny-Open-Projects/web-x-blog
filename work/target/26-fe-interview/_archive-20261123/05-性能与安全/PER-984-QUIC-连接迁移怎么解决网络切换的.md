---
title: [PER-984] QUIC 连接迁移怎么解决网络切换的断连问题
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-984：QUIC 连接迁移怎么解决网络切换的断连问题

**答**：
- TCP 四元组（源IP:端口）变化即断连：WiFi→蜂窝切换必然重连；QUIC 用 Connection ID 标识连接，IP 变化连接不中断。
- 收益：弱网切换场景（地铁/电梯/双网卡手机）请求不重试、页面不闪断，对长连接 IM/直播价值最大。
- 前端配合：捕获 online/offline 与 NetworkInformation.change，切换期间请求走队列暂停，恢复后复用连接立即重放。
- 限制：部分中间盒/NAT 对 QUIC 不友好，需回退 HTTP/2（Alt-Svc 协商 + fallback 监控）。

```javascript
// 网络切换期间请求队列化
let offlineQueue = [];
addEventListener('online', async () => {
  const q = offlineQueue; offlineQueue = [];
  for (const { url, init, resolve } of q) {
    try { resolve(await fetch(url, init)); } catch (e) { resolve(Promise.reject(e)); }
  }
});
addEventListener('offline', () => report({ type: 'conn-switch' }));
function fetchQ(url, init) {
  if (!navigator.onLine) return new Promise((resolve, reject) =>
    offlineQueue.push({ url, init, resolve, reject }));
  return fetch(url, init);
}
```
