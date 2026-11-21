---
title: [AV-060] 视频进度条缩略图预览（sprite 图）怎么做？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-060：视频进度条缩略图预览（sprite 图）怎么做？
**答**：
- 原理：服务端预生成雪碧图（每隔 N 秒抽一帧拼成网格大图）+ VTT/JSON 索引；hover 进度条时按时间算出帧位置，`background-position` 偏移显示。
- sprite 优点：一次请求拿到全部缩略图，无逐帧请求风暴；缺点：大视频图很大，需分片 sprite（每 100 帧一张）。
- 无 sprite 兜底：动态 seek 生成——隐藏 video 设置 currentTime，等 seeked 后 drawImage 到 canvas（慢且有并发限制，仅适合短视频）。
- VTT 标准格式（webvtt thumbnail）逐条描述时间区间与 sprite 坐标，Safari 原生支持。
- 体验细节：hover 防抖、预加载相邻 sprite、retina 2x 图。

```text
WEBVTT

00:00:00.000 --> 00:00:05.000
thumbnails.jpg#xywh=0,0,160,90

00:00:05.000 --> 00:00:10.000
thumbnails.jpg#xywh=160,0,160,90

00:00:10.000 --> 00:00:15.000
thumbnails.jpg#xywh=320,0,160,90
```

```javascript
// 进度条 hover 缩略图：解析 sprite 索引 + 动态 seek 兜底
class ThumbnailPreview {
  constructor(video, spriteUrl, { interval = 5, cols = 10, tw = 160, th = 90 } = {}) {
    this.video = video; this.sprite = spriteUrl;
    Object.assign(this, { interval, cols, tw, th });
  }
  // 方案一：sprite 定位
  spriteStyleFor(time) {
    const idx = Math.floor(time / this.interval);
    const col = idx % this.cols, row = Math.floor(idx / this.cols);
    return {
      backgroundImage: `url(${this.sprite})`,
      backgroundPosition: `-${col * this.tw}px -${row * this.th}px`,
      width: this.tw + 'px', height: this.th + 'px',
    };
  }
  // 方案二：隐藏 video seek 生成（兜底，串行防抖）
  async captureAt(time) {
    const v = this.hiddenVideo ??= Object.assign(document.createElement('video'), {
      src: this.video.currentSrc, muted: true, preload: 'auto', crossOrigin: 'anonymous',
    });
    v.currentTime = time;
    await new Promise((r) => v.addEventListener('seeked', r, { once: true }));
    const c = document.createElement('canvas');
    c.width = this.tw; c.height = this.th;
    c.getContext('2d').drawImage(v, 0, 0, this.tw, this.th);
    return c.toDataURL('image/jpeg', 0.6);
  }
}
```

---

## 九、实时通信工程（AV-061 ~ AV-067）
