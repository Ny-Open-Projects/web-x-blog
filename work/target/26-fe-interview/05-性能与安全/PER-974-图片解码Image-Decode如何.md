---
title: [PER-974] 图片解码（Image Decode）如何成为隐形卡顿源
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-974：图片解码（Image Decode）如何成为隐形卡顿源

**答**：
- 大图从网络到上屏还需解码：JPEG/AVIF 解码发生在主线程或合成线程，超大图（>2000px）解码可达数十 ms。
- 触发点：懒加载图片进入视口瞬间解码 → 快速滚动时的卡顿；切换 src 的轮播图首帧延迟。
- 治理：img decoding="async"；用 createImageBitmap 在 Worker 预解码；LCP 大图务必提前 fetch 并预留尺寸。
- 深水：WebP/AVIF 解码耗时高于 JPEG，移动低端机注意权衡压缩收益与解码成本。

```javascript
// 预解码大图：Worker + createImageBitmap
const worker = new Worker('decoder.js');
function preloadBitmap(url) {
  return new Promise(resolve => {
    worker.postMessage(url);
    worker.onmessage = e => resolve(e.data);   // 转回 ImageBitmap
  });
}
// decoder.js:
self.onmessage = async e => {
  const res = await fetch(e.data);
  const blob = await res.blob();
  const bmp = await createImageBitmap(blob);   // 解码完成
  self.postMessage(bmp, [bmp]);                // transfer 零拷贝
};
// HTML：<img decoding="async" fetchpriority="high">
```
