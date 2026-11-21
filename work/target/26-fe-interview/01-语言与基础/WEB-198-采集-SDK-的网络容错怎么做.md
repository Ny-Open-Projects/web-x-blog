---
title: [WEB-198] 采集 SDK 的网络容错怎么做？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-198：采集 SDK 的网络容错怎么做？
**答**：
- 上报通道优先级：sendBeacon（页面卸载不丢）→ keepalive fetch → 普通请求队列；失败进本地持久队列（IndexedDB/localStorage）。
- 重试策略：指数退避带上限；按事件优先级决定丢弃顺序——性能数据可丢，错误数据必达。
- 防雪崩：上报本身要限流采样，故障时自动降低上报频率；批量合并减少请求数。
- 数据一致性：每条带上 sessionId 与序列号，服务端可去重与排序。

```javascript
// SDK 容错：sendBeacon 失败转持久队列，退避重试
const queue = {
  async push(event) {
    const ok = navigator.sendBeacon('/collect', JSON.stringify(event));
    if (!ok) await db.put('retryQueue', { id: crypto.randomUUID(), event }); // 页面关闭前的兜底
  },
};
async function drainRetryQueue() {
  const items = await db.getAll('retryQueue');
  let delay = 1000;
  for (const it of items) {
    try {
      const res = await fetch('/collect', { method: 'POST', keepalive: true, body: JSON.stringify(it.event) });
      if (res.ok) await db.delete('retryQueue', it.id);
      else throw new Error('retry later');
    } catch {
      delay = Math.min(delay * 2, 60000);      // 指数退避，上限 60 秒
      setTimeout(drainRetryQueue, delay);
      return;
    }
  }
}
window.addEventListener('online', drainRetryQueue);  // 网络恢复后自动补传
```
