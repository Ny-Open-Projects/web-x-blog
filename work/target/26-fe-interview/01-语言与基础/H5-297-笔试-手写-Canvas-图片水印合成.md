---
title: [H5-297] 笔试：手写 Canvas 图片水印合成
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Canvas]
type: 笔试题
---

## H5-297：笔试：手写 Canvas 图片水印合成

**题目**：实现 `addWatermark(imgUrl, text)`：加载图片（限制长边 1280）→ 平铺半透明文字水印（-30° 交错）→ 导出 JPEG。要求跨域图片可用（CORS 处理），导出质量 0.8。

**答**：
```javascript
async function addWatermark(imgUrl, text) {
  const img = await loadImage(imgUrl);
  const scale = Math.min(1, 1280 / Math.max(img.width, img.height));
  const W = img.width * scale, H = img.height * scale;
  const c = document.createElement('canvas');
  c.width = W; c.height = H;
  const ctx = c.getContext('2d');
  ctx.drawImage(img, 0, 0, W, H);

  // 水印平铺层
  const tile = document.createElement('canvas');
  tile.width = 220; tile.height = 140;
  const tc = tile.getContext('2d');
  tc.translate(110, 70);
  tc.rotate(-Math.PI / 6);
  tc.font = '16px sans-serif';
  tc.fillStyle = 'rgba(0,0,0,0.12)';
  tc.textAlign = 'center';
  tc.fillText(text, 0, 0);
  ctx.fillStyle = ctx.createPattern(tile, 'repeat'); // 平铺模式
  ctx.fillRect(0, 0, W, H);

  return new Promise(r => c.toBlob(r, 'image/jpeg', 0.8));
}
function loadImage(src) {
  return new Promise((res, rej) => {
    const img = new Image();
    img.crossOrigin = 'anonymous'; // 跨域必须
    img.onload = () => res(img);
    img.onerror = rej;
    img.src = src;
  });
}
```

**评分点**：
- crossOrigin 在 src 之前设置，否则画布污染 toBlob 抛错
- 等比缩放长边限制
- 用 createPattern 平铺而非双重循环逐个画（性能与简洁）
- toBlob 异步导出 + 指定 JPEG 质量
