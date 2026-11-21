---
title: [H5-137] 画布内容如何导出为 PNG/JPG/SVG 与裁剪选区？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-137：画布内容如何导出为 PNG/JPG/SVG 与裁剪选区？
**答**：
- 位图导出用 `canvas.toBlob(type, quality)`（异步、内存友好）；JPG 无透明通道，导出前先铺白底否则黑底；高分屏导出注意 dpr。
- 裁剪选区：`drawImage` 从主画布按"源矩形（乘 dpr）→ 目标矩形"拷贝到新 canvas。
- SVG 导出是"数据/渲染分离"的红利：数据模型是矢量，直接把场景序列化成 `<svg>` 字符串，无损缩放且可二次编辑。
- 大坑：画过跨域图片的 canvas 被污染，`toBlob` 抛 SecurityError——图片加 `crossOrigin='anonymous'` 且服务端允许 CORS。

```javascript
// 1) 位图导出 + 裁剪选区
const dpr = devicePixelRatio || 1;
async function exportPNG(rect) {
  const out = document.createElement('canvas');
  out.width = rect ? rect.w : canvas.width;
  out.height = rect ? rect.h : canvas.height;
  const c = out.getContext('2d');
  if (rect) {
    // 裁剪：从主画布拷贝源区域（源坐标要乘 dpr 回到物理像素）
    c.drawImage(canvas, rect.x * dpr, rect.y * dpr, rect.w * dpr, rect.h * dpr,
                0, 0, rect.w, rect.h);
  } else {
    c.drawImage(canvas, 0, 0);
  }
  return new Promise((res) => out.toBlob(res, 'image/png'));
}
async function exportJPG() {
  const out = document.createElement('canvas');
  out.width = canvas.width; out.height = canvas.height;
  const c = out.getContext('2d');
  c.fillStyle = '#fff'; c.fillRect(0, 0, out.width, out.height); // JPG 无透明，先铺底
  c.drawImage(canvas, 0, 0);
  return new Promise((res) => out.toBlob(res, 'image/jpeg', 0.85));
}

// 2) SVG 导出：数据模型是矢量，直接序列化（数据/渲染分离的红利）
function exportSVG(scene) {
  const body = scene.map((s) =>
    `<rect x="${s.x}" y="${s.y}" width="${s.w}" height="${s.h}" fill="${s.fill}"/>`
  ).join('');
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 320">${body}</svg>`;
}

// 3) 下载触发：createObjectURL + a[download]，用完 revoke
function download(blob, name) {
  const url = URL.createObjectURL(blob);
  const a = Object.assign(document.createElement('a'), { href: url, download: name });
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 0);
}

// 坑：画过跨域图片的 canvas 已"污染"，toBlob 抛 SecurityError；
// 解法：img.crossOrigin = 'anonymous' + 服务端返回 CORS 头
```
