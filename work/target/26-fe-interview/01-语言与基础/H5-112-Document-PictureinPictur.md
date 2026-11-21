---
title: [H5-112] Document Picture-in-Picture 与视频画中画的区别是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-112：Document Picture-in-Picture 与视频画中画的区别是什么？
**答**：
- 视频 PiP（H5-069）悬浮窗里**只有 video 元素**；Document PiP 打开一个可承载**任意 HTML** 的迷你窗口（自绘字幕、控制面板、白板批注）。
- 用法：`documentPictureInPicture.requestWindow({ width, height })` 返回新 window → 把元素 move 过去（appendChild 即移动节点）→ 关闭时搬回原容器。
- 新窗口继承 opener 的样式表需手动 copyStyleSheets（旧实现）或复制 style 标签；事件与主窗口同一个 JS 上下文。
- 仅 Chrome/Edge 桌面版支持，需用户手势；窗口关闭触发 `pagehide`/`windowClose` 时机要做元素归还。
- 典型用途：会议软件的悬浮参会者列表、带自定义字幕样式的播放器、跟随播放的控制条。

```html
<div id="player-ui">
  <video src="/media/lesson.mp4" controls muted playsinline></video>
  <div class="captions">默认字幕区域</div>
  <button id="doc-pip">字幕画中画</button>
</div>

<script>
  const ui = document.getElementById('player-ui');
  const captions = ui.querySelector('.captions');
  let pipWin = null;

  document.getElementById('doc-pip').addEventListener('click', async () => {
    if (!('documentPictureInPicture' in window)) return alert('仅 Chromium 桌面版支持');

    if (pipWin) return pipWin.close();

    // 1) 请求迷你窗口（需用户手势内调用）
    pipWin = await documentPictureInPicture.requestWindow({ width: 360, height: 120 });

    // 2) 同步样式：把主文档样式表克隆进新窗口
    [...document.styleSheets].forEach((sheet) => {
      try {
        const style = pipWin.document.createElement('style');
        style.textContent = [...sheet.cssRules].map(r => r.cssText).join('\n');
        pipWin.document.head.append(style);
      } catch {}                       // 跨域样式表跳过
    });

    // 3) 移动节点：appendChild 即 move，事件绑定不丢
    pipWin.document.body.append(captions);

    // 4) 窗口被用户关闭时把元素搬回来
    pipWin.addEventListener('pagehide', () => {
      ui.querySelector('video').after(captions);
      pipWin = null;
    });
  });
</script>
```
