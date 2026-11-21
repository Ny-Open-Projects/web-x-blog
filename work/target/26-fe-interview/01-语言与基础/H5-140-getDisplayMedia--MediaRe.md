---
title: [H5-140] getDisplayMedia + MediaRecorder 屏幕录制的全流程？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-140：getDisplayMedia + MediaRecorder 屏幕录制的全流程？
**答**：
- 流程：`getDisplayMedia({video, audio})` 拿屏幕流（用户在系统弹层选屏幕/窗口/标签页，网页无选择权）→ `new MediaRecorder(stream, {mimeType})` → `ondataavailable` 收 chunk → `onstop` 合成 Blob → `createObjectURL` 触发下载。
- mimeType 用 `isTypeSupported` 探测降级（vp9 → vp8 → 默认），`start(timeslice)` 定时分片防内存峰值与崩溃丢全部数据。
- 必须监听 `track.onended`：用户随时可能点浏览器自带的"停止共享"，Web 应用不感知这个 UI。
- 必须**用户手势触发**；Safari 支持 `video/mp4` 优先，其余多为 webm；只能录屏音频（audio: true 表示尝试采集系统声音，能否勾选由浏览器决定）。

```html
<button id="rec">开始录屏</button>
<a id="dl" hidden>下载录像</a>
<script>
const pickMime = () =>
  ['video/webm;codecs=vp9,opus', 'video/webm;codecs=vp8,opus', 'video/webm']
    .find((t) => MediaRecorder.isTypeSupported(t)) || '';

document.getElementById('rec').onclick = async function () {
  // 用户在系统弹层里选"整个屏幕 / 窗口 / 标签页"，网页拿不到选择权
  const stream = await navigator.mediaDevices.getDisplayMedia({
    video: { frameRate: 30 },
    audio: true,          // 尝试采集系统声音，能否勾选由浏览器与用户决定
  });
  const chunks = [];
  const rec = new MediaRecorder(stream, {
    mimeType: pickMime(),
    videoBitsPerSecond: 5e6,
  });
  rec.ondataavailable = (e) => { if (e.data.size) chunks.push(e.data); };
  rec.onstop = () => {
    const blob = new Blob(chunks, { type: rec.mimeType });
    const a = document.getElementById('dl');
    a.href = URL.createObjectURL(blob);
    a.download = 'screen.' + (rec.mimeType.includes('mp4') ? 'mp4' : 'webm');
    a.hidden = false;
  };
  // 关键：用户随时可能点浏览器自带的"停止共享"按钮 —— 只能靠 track 事件感知
  stream.getVideoTracks()[0].onended = () => {
    if (rec.state !== 'inactive') rec.stop();
  };
  rec.start(1000);        // 每秒落一个 chunk：防内存峰值，崩溃时不丢全部
  this.textContent = '停止';
  this.onclick = () => rec.state !== 'inactive' && rec.stop();
};
</script>
```
