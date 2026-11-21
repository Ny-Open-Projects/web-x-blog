---
title: [WEB-123] 全屏、屏幕方向锁与屏幕唤醒锁的 API 细节是什么？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-123：全屏、屏幕方向锁与屏幕唤醒锁的 API 细节是什么？
**答**：
- 全屏：`element.requestFullscreen()` 必须由用户手势触发，配合 `fullscreenchange` 事件同步 UI；document.exitFullscreen() 退出。
- 方向锁：`screen.orientation.lock('landscape')` 只有在全屏状态下才允许（移动端）。
- 唤醒锁：`navigator.wakeLock.request('screen')` 防止息屏，仅页面可见时可申请；切后台自动释放，回前台要重新申请——监听 visibilitychange 重取。
- 三个 API 都是用户意图驱动 + 权限管控的现代能力，滥用（保活、强制横屏）会在审核和体验上付出代价。

```javascript
// 视频页三件套：全屏 + 横屏 + 防息屏
const video = document.querySelector('video');
let wakeLock = null;

btn.onclick = async () => {                       // 用户手势内
  await video.requestFullscreen();                // 1. 全屏
  try { await screen.orientation.lock('landscape'); } catch {} // 2. 横屏（需先全屏）
  try { wakeLock = await navigator.wakeLock.request('screen'); } catch {} // 3. 防息屏
};

// 切后台唤醒锁自动释放，回前台重新申请
document.addEventListener('visibilitychange', async () => {
  if (document.visibilityState === 'visible' && wakeLock) {
    wakeLock = await navigator.wakeLock.request('screen');
  }
});
document.addEventListener('fullscreenchange', () => {
  if (!document.fullscreenElement) screen.orientation.unlock();
});
```

## 二十一、综合与演化
