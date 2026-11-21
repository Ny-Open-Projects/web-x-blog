---
title: [H5-273] 移动端图片上传的方向：EXIF 旋转问题
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 移动端]
type: 面试题
---

## H5-273：移动端图片上传的方向：EXIF 旋转问题

**答**：
- 现象：竖拍照片在某些浏览器/服务器显示横放——相机的像素矩阵永远是横向的，方向信息存在 EXIF Orientation 标记里
- 浏览器差异：现代浏览器 img 标签默认按 EXIF 方向渲染（image-orientation: from-image），但 canvas drawImage、上传后的服务端处理可能不认 EXIF
- 彻底方案：上传前用 canvas 重绘一次（按真实方向），生成「物理方向正确」的图片再传，服务端不再依赖 EXIF
- 读取 EXIF：用 exifr 这类库解析 Orientation 字段（1~8），据此旋转绘制
- 顺带优化：重绘时一起做压缩与尺寸限制，一次 canvas 操作解决方向+体积两个问题

```javascript
async function fixOrientation(file) {
  const exif = await exifr.orientation(file); // 1~8
  const img = await createImageBitmap(file);
  const rot = { 3: 180, 6: 90, 8: 270 }[exif] || 0;
  const c = document.createElement('canvas');
  if (rot === 90 || rot === 270) { c.width = img.height; c.height = img.width; }
  else { c.width = img.width; c.height = img.height; }
  const ctx = c.getContext('2d');
  ctx.translate(c.width / 2, c.height / 2);
  ctx.rotate(rot * Math.PI / 180);
  ctx.drawImage(img, -img.width / 2, -img.height / 2);
  return c.toDataURL('image/jpeg', 0.85);
}
```
