---
title: [BAS-102] visibilitychange 和 beforeunload 分别什么时候用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-102：visibilitychange 和 beforeunload 分别什么时候用？
**答**：
- visibilitychange：切后台标签/最小化时 document.hidden 变 true，用于暂停视频、停轮询、上报埋点，比 unload 可靠得多。
- beforeunload：用户即将离开时触发，配合 preventDefault 可弹离开确认（现代浏览器不显示自定义文案）；移动端不保证触发。
- 卸载阶段上报数据用 `navigator.sendBeacon`，普通异步请求会被浏览器掐断。

```javascript
document.addEventListener('visibilitychange', () => {
  if (document.hidden) video.pause();
  else video.play();
});
window.addEventListener('beforeunload', (e) => {
  if (hasUnsavedChanges) {
    e.preventDefault();     // 触发离开确认
    e.returnValue = '';
  }
});
window.addEventListener('pagehide', () => navigator.sendBeacon('/log', payload));
```
