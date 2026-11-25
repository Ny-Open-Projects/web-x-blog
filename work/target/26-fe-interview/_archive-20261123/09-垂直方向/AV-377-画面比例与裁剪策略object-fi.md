---
title: [AV-377] 画面比例与裁剪策略（object-fit 的视频版）
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## AV-377：画面比例与裁剪策略（object-fit 的视频版）

**答**：
- 场景：竖屏视频在横屏容器——contain（留黑边）/cover（裁剪）/fill（拉伸变形）。
- 智能裁剪：人脸/显著性检测定焦点（服务端），cover 模式带 focus 参数（object-position）。
- 前端：video object-fit + object-position 组合，或 canvas 合成时按焦点裁剪。

```javascript
// 智能裁剪
function fitVideo(videoAR, boxAR, mode, focus = 0.5) {
  if (mode === 'contain') return { scale: 'contain', bars: boxAR > videoAR ? 'left-right' : 'top-bottom' };
  if (mode === 'cover') {
    const visibleRatio = boxAR / videoAR;              // 可见比例
    return { scale: 'cover',
      crop: { keep: visibleRatio, focus },             // 焦点保留区域
      css: `object-fit: cover; object-position: ${focus * 100}% center` };
  }
  return { scale: 'fill', note: '变形，慎用' };
}
```
