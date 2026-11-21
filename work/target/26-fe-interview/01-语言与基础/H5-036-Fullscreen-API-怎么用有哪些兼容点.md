---
title: [H5-036] Fullscreen API 怎么用？有哪些兼容点？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-036：Fullscreen API 怎么用？有哪些兼容点？
**答**：
- 进入：`el.requestFullscreen()`，退出：`document.exitFullscreen()`；`document.fullscreenElement` 判断当前状态。
- 必须由用户手势触发；`fullscreenchange` 事件监听状态切换，用来调整 UI 布局。
- 全屏元素只有自己是可见的，兄弟元素被隐藏，需要全屏容器而不是单个按钮。
- 旧 WebKit 需要 `webkitRequestFullscreen` 前缀；iOS Safari 对 iPhone 不支持元素全屏，视频要用 `playsinline`/`webkitEnterFullscreen` 特判。

```javascript
const stage = document.querySelector('.player');

async function toggleFullscreen(el) {
  if (document.fullscreenElement) {
    await document.exitFullscreen();
    return;
  }
  try {
    await el.requestFullscreen();
  } catch (e) {
    // 旧 Safari 兜底
    if (el.webkitRequestFullscreen) el.webkitRequestFullscreen();
  }
}

document.addEventListener('fullscreenchange', () => {
  const on = !!document.fullscreenElement;
  document.body.classList.toggle('is-fullscreen', on);
  // 全屏时隐藏无关 UI、把控制条固定在底部
});

// 全屏时的默认黑底由元素背景决定
// CSS: .player:fullscreen { background: #000; width: 100%; }
```
