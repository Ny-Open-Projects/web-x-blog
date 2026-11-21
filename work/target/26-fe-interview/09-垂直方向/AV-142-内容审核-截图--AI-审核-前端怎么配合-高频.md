---
title: [AV-142] 内容审核（截图 + AI 审核）前端怎么配合？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-142：内容审核（截图 + AI 审核）前端怎么配合？（高频）
**答**：
- 审核主体在服务端/云端（推流旁路截图 → AI 模型 → 人工复审队列），前端做"即时反馈与止损"。
- 前端可做：开播前封面预检（video → canvas → 上传 AI 接口）、审核状态轮询展示（正常/复审中/已封禁）。
- 推流端预检：开播前自检封面与首帧，命中敏感直接拦截，减少"开播即封"的差体验。
- 实时止损：服务端下发"流违规"事件 → 前端立即下播并展示原因，截图证据按合规要求留存。
- 灰度与误杀：审核结果带置信度，低置信度走"限流不封禁"，必须给申诉通道。

```javascript
// 本地抽帧送审：封面预检
async function precheckCover(videoEl, token) {
  const canvas = document.createElement('canvas');
  canvas.width = videoEl.videoWidth;
  canvas.height = videoEl.videoHeight;
  canvas.getContext('2d').drawImage(videoEl, 0, 0);      // 抓当前帧
  const blob = await new Promise((r) => canvas.toBlob(r, 'image/jpeg', 0.8));
  const form = new FormData();
  form.append('image', blob, 'cover.jpg');
  const res = await fetch('/api/moderation/image', {
    method: 'POST',
    headers: { Authorization: `Bearer ${token}` },
    body: form,
  });
  const { label, confidence } = await res.json();        // label: pass | review | block
  if (label === 'block' && confidence > 0.9) {
    toast('封面包含违规内容，请更换后再开播');            // 开播前拦截
    return false;
  }
  return true;                                           // review 档放行但进入异步复审
}
```
