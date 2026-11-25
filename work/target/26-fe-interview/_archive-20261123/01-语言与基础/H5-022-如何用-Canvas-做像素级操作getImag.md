---
title: [H5-022] 如何用 Canvas 做像素级操作？getImageData 有什么坑？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-022：如何用 Canvas 做像素级操作？getImageData 有什么坑？
**答**：
- `ctx.getImageData(x, y, w, h)` 拿到 ImageData，`data` 是 Uint8ClampedArray，每 4 个字节一个像素（RGBA）。
- 修改后 `ctx.putImageData` 写回，可实现滤镜（灰度/反色）、抠图等效果。
- 坑一：画布一旦绘制过跨域图片（未设 CORS）就"被污染"，getImageData 直接抛 SecurityError。
- 坑二：getImageData 开销大（回读 GPU 数据），不要每帧调用；处理大图放 Worker。

```html
<canvas id="gray" width="200" height="200"></canvas>

<script>
  const canvas = document.getElementById('gray');
  const ctx = canvas.getContext('2d');

  const img = new Image();
  img.crossOrigin = 'anonymous'; // 图片来自 CDN 时必须，否则画布被污染
  img.onload = () => {
    ctx.drawImage(img, 0, 0, 200, 200);

    const imageData = ctx.getImageData(0, 0, 200, 200); // RGBA 字节数组
    const d = imageData.data;
    for (let i = 0; i < d.length; i += 4) {
      // 灰度化：按人眼感知加权
      const gray = 0.299 * d[i] + 0.587 * d[i + 1] + 0.114 * d[i + 2];
      d[i] = d[i + 1] = d[i + 2] = gray; // alpha d[i+3] 不动
    }
    ctx.putImageData(imageData, 0, 0); // 写回画布
  };
  img.src = 'https://cdn.example.com/photo.jpg';
</script>
```
