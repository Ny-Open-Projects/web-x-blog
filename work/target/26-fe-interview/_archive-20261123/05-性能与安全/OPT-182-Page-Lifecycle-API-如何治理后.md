---
title: [OPT-182] Page Lifecycle API 如何治理"后台 tab"的资源占用？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-182：Page Lifecycle API 如何治理"后台 tab"的资源占用？

**答**：
- 用户一开几十个 tab，你的页面在后台仍跑定时器/轮询/动画，白耗 CPU 与电量。Page Lifecycle 提供标准信号：`visibilitychange`（可见性）、`freeze`（浏览器冻结）、`resume`（解冻）、`resumer`（被丢弃恢复）。
- 策略：hidden 即暂停（轮询、动画、视频、canvas 循环）；`freeze` 时做最终持久化（IndexedDB 写盘）并停止一切活动；页面被 discard（丢弃）后由 `pageshow persisted` 或重新加载恢复。
- 前台恢复钩子：`resume`/visibility 恢复时刷新过期数据 + 恢复计时器，保证"回来看到的是新的"。
- 注意 `visibilitychange` 在 Safari 老版本的兼容，用 Page Lifecycle polyfill 统一。

```javascript
// 一一对应：基于 Page Lifecycle 的后台资源治理
const app = {
  timers: [],
  pause() {   // 后台：全部暂停
    this.timers.forEach(clearInterval); this.timers = [];
    videoEl?.pause();
    rafActive = false;              // rAF 循环读到 false 自然退出
  },
  resume() {  // 回前台：恢复 + 刷新过期数据
    this.timers.push(setInterval(pollNotifications, 30_000));
    rafActive = true;
    requestAnimationFrame(renderLoop);
    refreshIfStale();               // 数据新鲜度检查
  },
};

document.addEventListener('visibilitychange', () => {
  document.hidden ? app.pause() : app.resume();
});

// freeze：浏览器即将冻结（移动端省电），机会做最终持久化
document.addEventListener('freeze', () => {
  idbSet('app-state', { draft: currentDraft, at: Date.now() });  // 必须是异步 API
});

document.addEventListener('resume', () => app.resume());

// 被系统 discard（丢弃）后重开：从持久化状态恢复
if (navigator.userActivation && performance.getEntriesByType('navigation')[0]?.type === 'back_forward') {
  idbGet('app-state').then(restoreState);
}

// 自动暂停能力也适用于 WebSocket：hidden 60s 主动断开省电
let wsIdleTimer;
document.addEventListener('visibilitychange', () => {
  if (document.hidden) wsIdleTimer = setTimeout(() => ws.close(), 60_000);
  else { clearTimeout(wsIdleTimer); ensureWsConnected(); }
});
```
