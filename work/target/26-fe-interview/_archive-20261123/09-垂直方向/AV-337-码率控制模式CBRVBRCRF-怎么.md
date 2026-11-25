---
title: [AV-337] 码率控制模式：CBR/VBR/CRF 怎么选
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-337：码率控制模式：CBR/VBR/CRF 怎么选

**答**：
- CBR：码率恒定，带宽稳定但质量波动（场景切换时糊）——直播推流用。
- VBR：码率随内容波动，质量稳、平均码率低——点播/文件用。
- CRF（x264/x265）：恒定质量因子，码率不可预测——存档转码用；流媒体不可用（带宽不可控）。

```javascript
// 码率模式对比
const RATE_MODES = {
  cbr: { bitrate: '恒定 4Mbps', quality: '波动', use: '直播推流' },
  vbr: { bitrate: '均值 3Mbps 峰值 6', quality: '稳定', use: '点播' },
  crf: { bitrate: '不可预测', quality: '恒定 CRF 20', use: '转码存档' },
};
function estimateSize(mode, durationSec) {
  if (mode === 'cbr') return 4 * durationSec / 8;   // MB
  if (mode === 'vbr') return 3 * durationSec / 8;
  return null;   // crf 无法预估
}
```
