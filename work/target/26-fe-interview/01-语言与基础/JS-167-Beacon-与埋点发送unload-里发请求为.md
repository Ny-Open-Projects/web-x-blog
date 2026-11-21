---
title: [JS-167] Beacon 与埋点发送？unload 里发请求为什么不可靠？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-167：Beacon 与埋点发送？unload 里发请求为什么不可靠？

**答**：
- unload/pagehide 里的异步 fetch 会被浏览器直接取消；同步 XHR 阻塞卸载且已被废弃。
- `navigator.sendBeacon(url, data)`：浏览器保证页面关闭后仍「尽力送达」，异步、不阻塞、不占主线程。
- 限制：只支持 POST、不能读响应、不能带自定义 header、单个请求上限约 64KB。
- 降级链：sendBeacon → fetch keepalive（同样可跨页面存活）→ 同步 XHR（最后手段）。
- 冲刷时机用 visibilitychange 的 hidden，比 unload 可靠（移动端 unload 经常不触发）。

```javascript
class BeaconTracker {
  constructor(url) {
    this.url = url;
    this.queue = [];
    // 页面隐藏即冲刷：比 unload 可靠（移动端 unload 常不触发，bfcache 场景也不走 unload）
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') this.flush(true);
    });
  }
  track(event, props = {}) {
    this.queue.push({ event, props, ts: Date.now() });
    if (this.queue.length >= 10) this.flush();    // 攒批：满 10 条先发一批
  }
  flush(useBeacon = false) {
    if (!this.queue.length) return;
    const body = JSON.stringify(this.queue);
    if (useBeacon && navigator.sendBeacon) {
      // Blob 指定类型才会以 application/json 发送，字符串默认是 text/plain
      navigator.sendBeacon(this.url, new Blob([body], { type: 'application/json' }));
    } else {
      // 降级：keepalive 让 fetch 在页面关闭后仍可能送达（上限 64KB）
      fetch(this.url, {
        method: 'POST',
        body,
        headers: { 'Content-Type': 'application/json' },
        keepalive: true,
      }).catch(() => { /* 上报失败静默，绝不影响主流程 */ });
    }
    this.queue = [];
  }
}
const beacon = new BeaconTracker('/api/track');
beacon.track('page_view', { path: location.pathname });
```
