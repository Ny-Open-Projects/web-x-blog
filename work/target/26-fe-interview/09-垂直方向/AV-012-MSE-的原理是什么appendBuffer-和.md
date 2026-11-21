---
title: [AV-012] MSE 的原理是什么？appendBuffer 和 SourceBuffer 怎么用？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-012：MSE 的原理是什么？appendBuffer 和 SourceBuffer 怎么用？（高频压轴）
**答**：
- MSE 允许 JS 向 video 喂入媒体数据：`MediaSource` 挂到 `video.src`（需 URL.createObjectURL），内部包含多个 `SourceBuffer`（每条轨道一个）。
- JS 只负责"取数据 + appendBuffer"，真正的 demux/decode 由浏览器 C++ 层完成——所以 MSE 输入必须是浏览器支持的封装（fMP4/WebM）。
- 标准流程：createObjectURL → addSourceBuffer(mimeType) → fetch 分片 → appendBuffer → updateend 续传 → endOfStream 结束。
- 常见坑：append 时 SourceBuffer 正在 updating 会抛错；数据时间戳乱序会报 decode error；必须 `removeBuffer` 清理旧数据防内存膨胀。
- hls.js/flv.js 的本质都是：JS demux（TS/FLV → fMP4）+ MSE 喂流。

```javascript
// 最小可用 MSE 播放器：顺序追加 fMP4 分片
async function playWithMSE(video, segUrls, mime = 'video/mp4; codecs="avc1.64001f,mp4a.40.2"') {
  const ms = new MediaSource();
  video.src = URL.createObjectURL(ms);
  await new Promise((r) => (ms.addEventListener('sourceopen', r, { once: true })));

  const sb = ms.addSourceBuffer(mime);
  sb.mode = 'sequence'; // 按追加顺序排时间戳，简单可靠
  const queue = [];

  const append = (buf) => {
    if (sb.updating) { queue.push(buf); return; }
    try { sb.appendBuffer(buf); } catch (e) { console.error('append 失败', e); }
  };
  sb.addEventListener('updateend', () => {
    if (queue.length) append(queue.shift());
    else if (video.buffered.length) video.play();
  });

  for (const url of segUrls) {
    const buf = await (await fetch(url)).arrayBuffer();
    append(new Uint8Array(buf));
  }
  sb.addEventListener('updateend', function done() {
    if (!sb.updating && !queue.length) ms.endOfStream();
    sb.removeEventListener('updateend', done);
  });
}
```
