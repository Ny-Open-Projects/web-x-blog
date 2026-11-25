---
title: [H5-339] 移动端页面生命周期：visibility 与 Page Lifecycle 实战
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 浏览器架构]
type: 面试题
---

## H5-339：移动端页面生命周期：visibility 与 Page Lifecycle 实战

**答**：
- 移动端关键状态序列：切后台 → hidden（rAF 停、定时器节流）→ freeze（冻结）→ 切回 → resume/resume → visible；用户离开页面可能永远不回来（直接被杀）
- 可靠的「离开」信号是 pagehide（不是 unload——移动端 unload 不可靠且阻止 bfcache）；保活上报/持久化都挂在 pagehide + visibilitychange hidden
- Page Lifecycle API：freeze/resume 事件用于「冻结前持久化、恢复后校准数据」；discarded 状态（pageWasDiscarded）用于检测页面被丢弃后恢复
- 计时统计注意：页面在后台的时长不应计入使用时长；onhidden/onvisible 记录时间戳分段计算
- iOS 特殊性：切后台一段时间 rAF/定时器完全暂停，恢复时计时器一次性补发或跳过——长任务用绝对时间调度

```javascript
// 生命周期上报 + 使用时长统计
let activeStart = Date.now(), totalActive = 0;
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'hidden') {
    totalActive += Date.now() - activeStart;
    navigator.sendBeacon('/api/mon/lc', JSON.stringify({ totalActive, evt: 'hidden' }));
  } else activeStart = Date.now();
});
addEventListener('pagehide', () => {           // 可靠的最终信号
  navigator.sendBeacon('/api/mon/lc', JSON.stringify({
    totalActive: totalActive + (Date.now() - activeStart), evt: 'exit',
  }));
});
// 冻结/恢复
document.addEventListener('freeze', persistDraft);
document.addEventListener('resume', () => { recalibrateTimers(); });
```
