---
title: [AV-044] 美颜/滤镜的处理管线怎么搭？Canvas 和 WebGL 各自怎么做？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-044：美颜/滤镜的处理管线怎么搭？Canvas 和 WebGL 各自怎么做？
**答**：
- 通用管线：video（源）→ 处理器（Canvas2D 或 WebGL）→ canvas.captureStream() 生成新 MediaStream → replaceTrack 推出去。
- Canvas2D 简单滤镜：`ctx.filter = 'blur(2px) brightness(1.1) saturate(1.2)'` 一行搞定；美颜思路 = 轻微高斯模糊 + 提亮 + 饱和度。
- WebGL 方案：YUV/RGB 上传纹理，fragment shader 做磨皮（双边滤波）、锐化、LUT 调色，性能可跑 1080p30；人像分割用 MediaPipe/TFLite 模型输出 mask 再合成。
- 帧率控制：requestAnimationFrame 驱动绘制，注意处理 video 的 readyState 与视频宽高同步。
- 代价提示：处理链增加 20~100ms 延迟与 GPU 占用；移动端 Canvas2D 会掉帧，美颜尽量 WebGL。

```javascript
// Canvas2D 滤镜 + captureStream 管线
class BeautyPipeline {
  constructor(videoEl, { fps = 30 } = {}) {
    this.video = videoEl;
    this.canvas = document.createElement('canvas');
    this.canvas.width = 1280; this.canvas.height = 720;
    this.ctx = this.canvas.getContext('2d');
    this.stream = this.canvas.captureStream(fps); // 输出流
    const loop = () => {
      if (this.video.readyState >= 2) {
        this.ctx.filter = 'blur(1.5px) brightness(1.08) saturate(1.15)'; // 轻美颜
        this.ctx.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height);
        this.ctx.filter = 'none';
      }
      this.raf = requestAnimationFrame(loop);
    };
    loop();
  }
  get track() { return this.stream.getVideoTracks()[0]; }
  destroy() { cancelAnimationFrame(this.raf); this.track.stop(); }
}
// 推流时替换
const beauty = new BeautyPipeline(localVideoEl);
await videoSender.replaceTrack(beauty.track);
```
