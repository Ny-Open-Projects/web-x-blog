---
title: [AV-182] MSE buffer 堆积导致内存爆炸的复盘案例。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-182：MSE buffer 堆积导致内存爆炸的复盘案例。（高频）
**答**：
- 现象：直播页开 1 小时后崩溃（iOS 更明显），内存曲线只涨不跌。
- 根因：直播场景 appendBuffer 只进不出，没人做旧 buffer 清理；叠加同页 3 路隐藏预览流。
- 定位：performance.memory 采样 + video.buffered 区间可视化（总时长持续增长）。
- 修复：直播滑动窗口清理（保留播放点前后 30s，sourceBuffer.remove）；隐藏预览流降频或惰性加载。
- 沉淀：buffer 水位管理组件化 + 上线内存告警（buffered 总时长 > 60s 报警）。

```javascript
// 直播 buffer 滑动窗口清理
async function trimLiveBuffer(video, sourceBuffer, keepSec = 30) {
  const buf = video.buffered;
  if (buf.length === 0) return;
  const end = buf.end(buf.length - 1);
  const cutBefore = video.currentTime - keepSec;
  if (buf.start(0) < cutBefore) {
    try {
      sourceBuffer.remove(buf.start(0), cutBefore);  // updateend 后内存实际释放
    } catch (e) {
      report({ level: 'warn', msg: 'buffer trim failed', err: String(e) });
    }
  }
  if (end - video.currentTime > 120) {
    video.currentTime = end - 3;                     // 追帧 buffer 超长直播要拉回边缘
  }
}
// setInterval(() => trimLiveBuffer(video, sb), 10_000)
```
