---
title: [AV-006] I 帧、P 帧、B 帧和 GOP 分别是什么？对播放体验有什么影响？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-006：I 帧、P 帧、B 帧和 GOP 分别是什么？对播放体验有什么影响？
**答**：
- I 帧（帧内编码）自含完整画面；P 帧参考前面的帧做运动补偿；B 帧双向参考，压缩率最高但增加延迟与解码复杂度。
- GOP = 两个 I 帧之间的帧序列；丢包/花屏会持续到下一个 I 帧才恢复，这就是"花屏要到关键帧才好"的原因。
- 直播出画、seek、切清晰度都必须对齐 I 帧，否则黑屏/花屏；因此直播分片切点必须落在 I 帧上。
- B 帧在实时通信（WebRTC）中默认禁用——它引入显示顺序与解码顺序的重排延迟。
- 工程要点：转码服务设置固定 GOP（如 2s）并对齐各清晰度，保证 ABR 无缝切换。

```javascript
// 从 fMP4/TS 解析角度模拟：seek 时定位最近关键帧的逻辑
const segments = [
  { url: 'seg-0.ts', start: 0, hasKeyframe: true },
  { url: 'seg-1.ts', start: 2, hasKeyframe: true },
  { url: 'seg-2.ts', start: 4, hasKeyframe: false }, // 中途分片以 P 帧开场
  { url: 'seg-3.ts', start: 6, hasKeyframe: true },
];

function findSeekTarget(seekTime) {
  // 从目标时间向前找最近的关键帧起点，避免从 P 帧开始解码导致花屏
  for (let i = segments.length - 1; i >= 0; i--) {
    if (segments[i].start <= seekTime && segments[i].hasKeyframe) {
      return segments[i];
    }
  }
  return segments[0];
}
console.log('seek 到 5s 应从', findSeekTarget(5)); // seg-3 start=6? 不，回退到 seg-3 之前的 seg-2 无 I 帧，命中 seg-1
console.log('seek 到 1s 应从', findSeekTarget(1)); // seg-0

// 切清晰度也必须等待 IDR 帧：用 appendBuffer 前校验新分片首帧类型
function canSwitchNow(newFragmentInfo) {
  return newFragmentInfo.firstFrameType === 'IDR';
}
```
