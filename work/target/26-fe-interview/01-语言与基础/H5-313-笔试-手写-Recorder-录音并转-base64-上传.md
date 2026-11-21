---
title: [H5-313] 笔试：手写 Recorder 录音并转 base64 上传
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, 音视频]
type: 笔试题
---

## H5-313：笔试：手写 Recorder 录音并转 base64 上传

**题目**：实现 `startRecording() / stopRecording()`：getUserMedia 麦克风 → MediaRecorder 采集 → 停止后转 base64 → POST 上传。要求：录音时长上限 60s 自动停止；停止时释放所有 tracks；错误信封返回。

**答**：
```javascript
let recorder, stream, chunks = [], autoStop;

async function startRecording() {
  try {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = new MediaRecorder(stream);
    chunks = [];
    recorder.ondataavailable = (e) => e.data.size && chunks.push(e.data);
    recorder.start(); // 不带 timeslice，stop 时一次性出数据
    autoStop = setTimeout(() => stopRecording(), 60000); // 上限保护
    return { ok: true };
  } catch (e) {
    return { ok: false, error: e.name === 'NotAllowedError' ? '权限被拒' : '无可用麦克风' };
  }
}

async function stopRecording() {
  clearTimeout(autoStop);
  if (!recorder || recorder.state === 'inactive') return { ok: false, error: '未在录音' };
  const blob = await new Promise(r => { recorder.onstop = () => r(new Blob(chunks, { type: recorder.mimeType })); recorder.stop(); });
  stream.getTracks().forEach(t => t.stop()); // 释放麦克风（重要）

  const base64 = await blobToBase64(blob);
  await fetch('/api/voice', { method: 'POST', body: JSON.stringify({ audio: base64 }) });
  return { ok: true, size: blob.size };
}
const blobToBase64 = (b) => new Promise(r => {
  const fr = new FileReader();
  fr.onload = () => r(fr.result);
  fr.readAsDataURL(b);
});
```

**评分点**：
- NotAllowedError 的用户提示分类
- 60s 自动停止保护
- stop 后必须释放 tracks（否则麦克风占用指示灯一直亮）——高频失分点
- onstop 回调里聚合 Blob；FileReader 转 base64
