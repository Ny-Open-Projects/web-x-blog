---
title: [H5-201] OffscreenCanvas 是什么，怎么做到主线程零开销
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Canvas]
type: 面试题
---

## H5-201：OffscreenCanvas 是什么，怎么做到主线程零开销

**答**：
- OffscreenCanvas：在 Worker 里创建的画布，绘制、合成、编码全部脱离主线程，主线程只收结果
- 两种用法：Worker 里 `new OffscreenCanvas(w, h)` 直接画；主线程 canvas 调 `transferControlToOffscreen()` 把控制权交给 Worker
- 典型场景：图片滤镜批处理、视频逐帧标注、大图水印——这些在主线程做会卡掉交互
- 通信成本：纹理/位图用 `transferToImageBitmap()` + transferable 传递，避免拷贝
- 兼容注意：Safari 较晚支持，需要 feature detect 降级到主线程绘制

```javascript
// worker.js
onmessage = ({ data: { bitmap } }) => {
  const oc = new OffscreenCanvas(bitmap.width, bitmap.height);
  const ctx = oc.getContext('2d');
  ctx.filter = 'grayscale(1)';
  ctx.drawImage(bitmap, 0, 0);
  postMessage(oc.transferToImageBitmap(), [ ]);
};
// main.js
const worker = new Worker('worker.js');
worker.onmessage = ({ data }) => canvas.getContext('2d').drawImage(data, 0, 0);
worker.postMessage({ bitmap: img }, [ ]);
```
