---
title: [H5-227] Picture-in-Picture 画中画怎么实现
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-227：Picture-in-Picture 画中画怎么实现

**答**：
- API：`video.requestPictureInPicture()` 进入、`document.exitPictureInPicture()` 退出；小窗置顶于所有应用，可拖拽
- 条件：必须是正在播放的 `<video>` 元素；需用户手势触发（按钮点击）；`disablePictureInPicture` 属性可禁用
- 事件联动：`enterpictureinpicture`/`leavepictureinpicture` 同步 UI 状态；`resize` 事件可拿到小窗尺寸
- 画中画内的自定义控制：`navigator.mediaSession.setActionHandler` 响应播放/暂停按钮
- 用途：课程页边看边做题、会议小窗；注意小窗模式里 DOM 交互不可用，只有视频画面

```javascript
pipBtn.onclick = async () => {
  if (document.pictureInPictureElement) await document.exitPictureInPicture();
  else await video.requestPictureInPicture();
};
video.addEventListener('enterpictureinpicture', () => track.classList.add('pip'));
```
