---
title: [H5-069] Picture-in-Picture API 如何实现画中画？有哪些事件与限制？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-069：Picture-in-Picture API 如何实现画中画？有哪些事件与限制？
**答**：
- `video.requestPictureInPicture()` 让视频缩成系统级悬浮窗（最小化到其他页面/应用仍悬浮）；`document.exitPictureInPicture()` 退出。
- 触发前提：视频正在播放、用户手势触发、页面处于激活状态；一页同时只能有一个画中画窗口。
- 事件对：`enterpictureinpicture / leavepictureinpicture` 监听进出；pip 窗口内只有 `pictureInPictureElement` 暴露，外部 DOM 不可操作。
- pip 窗口可加自定义按钮：`disablePictureInPicture` 禁用入口，`navigator.mediaSession.setActionHandler` 定制播放/暂停/快进。
- 权限策略：iframe 中需要 `allow="picture-in-picture"`；"被禁自动 PiP" 由 `disablePictureInPicture` 属性控制。

```html
<video id="player" src="/media/movie.mp4" controls playsinline muted></video>
<button id="pip-btn">进入画中画</button>

<script>
  const v = document.getElementById('player');
  const btn = document.getElementById('pip-btn');

  btn.addEventListener('click', async () => {
    if (!('pictureInPictureEnabled' in document)) return alert('浏览器不支持画中画');
    if (document.pictureInPictureElement) {
      await document.exitPictureInPicture();     // 已在画中画则退出
    } else {
      try {
        await v.requestPictureInPicture();       // 必须在用户手势里调用
      } catch (err) {
        console.warn('进入失败：', err);          // 未播放或被策略拦截
      }
    }
  });

  // 进出事件：切主界面布局（如腾出空间给推荐列表）
  v.addEventListener('enterpictureinpicture', () => document.body.classList.add('pip-on'));
  v.addEventListener('leavepictureinpicture', () => document.body.classList.remove('pip-on'));

  // 尺寸变化：pip 窗口拖大拖小时回调，可用于调整字幕字号
  v.addEventListener('resize', () => {
    console.log('pip 尺寸：', v.videoWidth, 'x', v.videoHeight);
  });
</script>
```
