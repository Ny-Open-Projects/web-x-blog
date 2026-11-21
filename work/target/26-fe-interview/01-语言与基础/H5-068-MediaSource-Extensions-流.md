---
title: [H5-068] MediaSource Extensions 流式播放的基本模型是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-068：MediaSource Extensions 流式播放的基本模型是什么？
**答**：
- MSE 让 JS 把媒体数据**分块喂给** `<video>`：`video.src = URL.createObjectURL(mediaSource)`，取代一次性 src 下载。
- 核心对象链：`MediaSource` → `SourceBuffer`（每种编解码/类型一个）→ `appendBuffer(ArrayBuffer)` 追加媒体段。
- 典型流程：addSourceBuffer 声明 `video/mp4; codecs="avc1..."` → fetch 流式拉取 fMP4 分片 → appendBuffer → `updateend` 后继续 → `endOfStream()` 收尾。
- 应用场景：HLS/DASH 播放器（hls.js、dash.js 的底层）、边下边播、直播延迟优化、广告拼接（多 SourceBuffer 切换）。
- 现状与替代：MSE 兼容性最好但只能处理"浏览器认识的编码"；新的 **Managed MediaSource（MSE in Workers）** 与 **WebCodecs** 正在补低延迟与精细控制两块短板。

```javascript
// MSE 最小可用示例：把两段 fMP4 分片拼成一段可播视频
async function streamPlay(video, segmentUrls) {
  const ms = new MediaSource();
  video.src = URL.createObjectURL(ms);           // 关键：blob 协议接管 src

  await new Promise(res => ms.addEventListener('sourceopen', res, { once: true }));

  const sb = ms.addSourceBuffer('video/mp4; codecs="avc1.64001f"');

  for (const url of segmentUrls) {
    const buf = await fetch(url).then(r => r.arrayBuffer());
    await new Promise(res => {
      sb.addEventListener('updateend', res, { once: true });
      sb.appendBuffer(buf);                      // 喂给解码管线
    });
  }

  ms.endOfStream();                              // 全部就绪，时长可计算
  await video.play();
}

// 分片之间允许用户 seek：MSE 维护了时间轴，buffered 反映已拼装的区间
streamPlay(document.querySelector('video'), [
  '/media/init.mp4',       // 初始化段：moov 头
  '/media/seg-1.m4s',      // 0-4s
  '/media/seg-2.m4s',      // 4-8s
]);
```
