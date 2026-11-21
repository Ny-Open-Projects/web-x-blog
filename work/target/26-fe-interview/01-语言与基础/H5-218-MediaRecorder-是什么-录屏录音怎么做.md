---
title: [H5-218] MediaRecorder 是什么，录屏录音怎么做
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 音视频]
type: 面试题
---

## H5-218：MediaRecorder 是什么，录屏录音怎么做

**答**：
- MediaRecorder：把 MediaStream（摄像头/麦克风/屏幕）实时编码为视频/音频文件，不需要服务端转码
- 录屏组合拳：`getDisplayMedia`（屏幕流）+ MediaRecorder → webm 文件；录麦克风则用 `getUserMedia`
- 关键参数：mimeType（video/webm;codecs=vp9 优先，降级 vp8）、videoBitsPerSecond 控制码率
- 事件流：start → dataavailable（分片）→ stop；分片收集后拼 Blob 下载
- 兼容与坑：Safari 不支持 vp9、录屏必须用户主动触发选择屏幕；停止前最后一帧可能丢失（补 flush 逻辑）

```javascript
const stream = await navigator.mediaDevices.getDisplayMedia({ video: true });
const rec = new MediaRecorder(stream, { mimeType: 'video/webm;codecs=vp9', videoBitsPerSecond: 5e6 });
const chunks = [];
rec.ondataavailable = e => chunks.push(e.data);
rec.onstop = () => download(new Blob(chunks, { type: 'video/webm' }), 'rec.webm');
rec.start(1000); // 每秒出一个分片，便于断流恢复
stream.getVideoTracks()[0].onended = () => rec.stop(); // 用户点"停止共享"
```
