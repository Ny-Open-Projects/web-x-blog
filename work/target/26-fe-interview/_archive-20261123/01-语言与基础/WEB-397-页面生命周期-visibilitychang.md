---
title: [WEB-397] 页面生命周期：visibilitychange、pagehide、freeze、discard 分别是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-397：页面生命周期：visibilitychange、pagehide、freeze、discard 分别是什么？
**答**：
- hidden（visibilitychange）：切后台/锁屏，停轮询、上报状态、存草稿；这是最可靠的"用户离开"信号。
- pagehide：页面可能进入 bfcache 或关闭，替代 unload 做最终上报（sendBeacon）。
- freeze/discard：浏览器省内存冻结或丢弃后台页（事件为 freeze/resume、document.wasDiscarded），恢复时要重建状态。

```javascript
document.addEventListener('visibilitychange', () => {
  if (document.hidden) { pausePoll(); saveDraft(); }
  else resumePoll();
});
window.addEventListener('pagehide', () => navigator.sendBeacon('/log', blob));
if (document.wasDiscarded) restore();  // 页面曾被 discard
console.log('告别 unload：hidden/pagehide 才可靠');
```
