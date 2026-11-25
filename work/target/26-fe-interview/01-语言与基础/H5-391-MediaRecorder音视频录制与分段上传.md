---
title: [H5-391] MediaRecorder：音视频录制与分段上传实战
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 多媒体]
type: 面试题
---

## H5-391：MediaRecorder：音视频录制与分段上传实战

**答**：
- 录制链路：getUserMedia 拿 MediaStream → MediaRecorder 编码（ mimeType webm/vp8 或 iOS 支持的 mp4）→ ondataavailable 收 chunk → 上传/存储
- 移动端关键坑：mimeType 支持差异大（iOS 14.3 前不支持 MediaRecorder），用 isTypeSupported 探测选格式；分段录制 timeslice 定时出 chunk 可边录边传（直播/长录场景）
- 内存控制：长录制全量 blob 攒内存会爆——分片即传（服务端拼接）或定时 flush 到 IndexedDB；录制暂停/恢复用 pause/resume 保持同一文件时间轴
- 音频录制场景（语音消息）：AudioWorklet/AnalyserNode 做音量检测（波形 UI）+ 自动停止（静音判定）；iOS 录音与播放同时进行需 audio session 配置（桥解决）
- 权限与生命周期：录制中切后台 iOS 会自动中断（可接 interruption 事件），录制结束必须 stop + track.stop 释放

```javascript
const stream = await navigator.mediaDevices.getUserMedia({ audio: true, video: false });
const mime = MediaRecorder.isTypeSupported('video/webm;codecs=vp8') ? 'video/webm;codecs=vp8'
  : MediaRecorder.isTypeSupported('video/mp4') ? 'video/mp4' : '';
const rec = new MediaRecorder(stream, mime ? { mimeType: mime } : undefined);
rec.ondataavailable = async ({ data }) => {
  await uploadChunk(data);                 // timeslice 边录边传
};
rec.start(2000);                           // 每 2s 出一个 chunk
rec.onstop = () => stream.getTracks().forEach(t => t.stop());
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'hidden' && rec.state === 'recording') rec.pause();
});
```
