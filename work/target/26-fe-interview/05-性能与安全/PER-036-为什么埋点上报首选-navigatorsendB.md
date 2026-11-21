---
title: [PER-036] 为什么埋点上报首选 navigator.sendBeacon？降级方案是什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-036：为什么埋点上报首选 navigator.sendBeacon？降级方案是什么？

**答**：
- `sendBeacon` 由浏览器保证在页面**卸载后仍能可靠发出**，不阻塞 unload，适合"离开页面"这类必丢场景。
- `fetch/XHR` 在页面卸载时会被取消，除非 `fetch` 加 `keepalive: true`（这就是标准降级方案）。
- 上报体一般用 Blob 指定 `application/json`；注意 sendBeacon 队列有总量限制（约 64KB），大批量要分片。
- 传统兜底还有创建 Image 的 GET 打点，但现在主要用于极老浏览器。

```javascript
function report(data) {
  const url = 'https://log.example.com/api/collect';
  const payload = JSON.stringify({ ...data, ts: Date.now() });
  if (navigator.sendBeacon) {
    // 页面卸载时也能可靠发出，且不会阻塞卸载流程
    navigator.sendBeacon(url, new Blob([payload], { type: 'application/json' }));
  } else {
    // 降级：fetch keepalive，卸载后请求仍会继续完成
    fetch(url, { method: 'POST', body: payload, keepalive: true }).catch(() => {});
  }
}
```
