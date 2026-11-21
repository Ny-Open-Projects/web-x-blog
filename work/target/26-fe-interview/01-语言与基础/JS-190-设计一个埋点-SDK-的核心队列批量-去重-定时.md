---
title: [JS-190] 设计一个埋点 SDK 的核心队列？批量、去重、定时冲刷、失败重试怎么实现？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-190：设计一个埋点 SDK 的核心队列？批量、去重、定时冲刷、失败重试怎么实现？

**答**：
- 核心是缓冲队列：track() 只入队不上报，达到 maxBatch 或 flushInterval 定时触发冲刷；页面隐藏/卸载时用 sendBeacon 强制冲刷（visibilitychange 时机优于 unload）。
- 去重：对"事件+载荷"做 hash，去重窗口内同 hash 只发一次（防连点、防重复 PV）。
- 失败重试：失败批次塞回队头 + 指数退避重发；超过 maxRetry 计入死信丢弃，防止队列无限膨胀。
- 持久化：未上报队列落 localStorage，页面刷新后恢复，丢数率大幅降低；同时设容量上限。
- 通道优先级：sendBeacon（不阻塞卸载）→ fetch keepalive（POST 可带更多头）双通道。

```javascript
// 1. 埋点队列：批量 + 去重 + 定时冲刷 + 重试 + 持久化
function createTracker({ endpoint, maxBatch = 20, interval = 5000, maxRetry = 3 } = {}) {
  const DEDUP_WINDOW = 1000;
  const dedup = new Map();                          // hash -> lastTs
  let queue = loadQueue();                          // 刷新后恢复
  let retryCount = 0;

  function track(event, props = {}) {
    const hash = event + JSON.stringify(props);
    const now = Date.now();
    if (dedup.has(hash) && now - dedup.get(hash) < DEDUP_WINDOW) return; // 窗口内去重
    dedup.set(hash, now);
    queue.push({ event, props, ts: now, _retry: 0 });
    saveQueue();
    if (queue.length >= maxBatch) flush();          // 攒够一批立即发
  }

  async function flush(useBeacon = false) {
    if (!queue.length) return;
    const batch = queue;
    queue = [];                                     // 先摘下队列，失败再塞回，避免重试时重复
    const body = JSON.stringify({ events: batch, sentAt: Date.now() });
    if (useBeacon && navigator.sendBeacon?.(endpoint, body)) {
      saveQueue(); return;                          // 卸载场景：sendBeacon 即视为成功
    }
    try {
      const resp = await fetch(endpoint, { method: 'POST', body, keepalive: true });
      if (!resp.ok) throw new Error('HTTP ' + resp.status);
      retryCount = 0; saveQueue();
    } catch (e) {
      if (batch[0]._retry >= maxRetry) {            // 超过上限：死信丢弃
        saveQueue();
        return;
      }
      batch.forEach((it) => it._retry++);
      queue = [...batch, ...queue];                 // 失败批次塞回队头
      const backoff = Math.min(1000 * 2 ** ++retryCount, 30_000);
      setTimeout(() => flush(), backoff);           // 指数退避重试
    }
  }

  function saveQueue() {
    try { localStorage.setItem('__tk', JSON.stringify(queue.slice(-200))); } catch {}
  }
  function loadQueue() {
    try { return JSON.parse(localStorage.getItem('__tk') || '[]'); } catch { return []; }
  }

  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') flush(true); // 离开页面：sendBeacon 兜底
  });
  const timer = setInterval(() => flush(), interval);       // 定时冲刷
  return { track, flush, destroy: () => clearInterval(timer) };
}

// 2. 使用
const tracker = createTracker({ endpoint: '/collect', maxBatch: 10, interval: 3000 });
tracker.track('pv', { page: '/home' });
tracker.track('click', { target: 'buy-btn' });
tracker.track('click', { target: 'buy-btn' });    // 窗口内被去重，只发一条
```
