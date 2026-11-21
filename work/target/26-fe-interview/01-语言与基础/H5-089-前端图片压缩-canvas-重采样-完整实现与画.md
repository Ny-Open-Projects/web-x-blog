---
title: [H5-089] 前端图片压缩（canvas 重采样）完整实现与画质要点。
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-089：前端图片压缩（canvas 重采样）完整实现与画质要点。
**答**：
- 主流程：解码（createImageBitmap 优于 Image+FileReader）→ 计算目标尺寸（限制最长边或面积）→ canvas 绘制 → `toBlob(jpeg, quality)`。
- 重采样质量问题：canvas 的 drawImage 在大幅缩小时会丢细节（欠采样），用**多级半倍缩放**（每次缩小 ≤ 1/2）近似高质量重采样。
- 格式策略：透明图保 png/webp（`image/webp` 支持度高、体积小），照片用 jpeg；导出前对 jpeg 铺白底。
- EXIF 方向：createImageBitmap 传 `imageOrientation: 'from-image'` 或依赖现代浏览器默认纠正，避免旋转 90 度的老 bug。
- 参数建议：最长边 1280~1920、quality 0.8 起步；用 `blob.size` 与原文件比较，压不小就回退原图。

```javascript
async function compressImage(file, { maxSide = 1600, quality = 0.8, type = 'image/jpeg' } = {}) {
  // 1) 解码：from-image 纠正 EXIF 旋转
  const bmp = await createImageBitmap(file, { imageOrientation: 'from-image' });

  // 2) 目标尺寸：只缩不放
  const scale = Math.min(1, maxSide / Math.max(bmp.width, bmp.height));
  let w = Math.round(bmp.width * scale);
  let h = Math.round(bmp.height * scale);

  // 3) 多级半倍缩放：比一步到位更少摩尔纹与锯齿
  let src = bmp;
  while (src.width > w * 2) {
    const half = document.createElement('canvas');
    half.width = Math.max(1, Math.floor(src.width / 2));
    half.height = Math.max(1, Math.floor(src.height / 2));
    half.getContext('2d').drawImage(src, 0, 0, half.width, half.height);
    src = half;
  }

  // 4) 最终画布：jpeg 铺白底防透明区变黑
  const cv = document.createElement('canvas');
  cv.width = w; cv.height = h;
  const ctx = cv.getContext('2d');
  if (type === 'image/jpeg') {
    ctx.fillStyle = '#fff';
    ctx.fillRect(0, 0, w, h);
  }
  ctx.imageSmoothingQuality = 'high';
  ctx.drawImage(src, 0, 0, w, h);

  // 5) 导出，压不赢原图就回退
  const blob = await new Promise(r => cv.toBlob(r, type, quality));
  if (!blob || blob.size >= file.size) return { blob: file, reused: true };

  return {
    blob,
    reused: false,
    file: new File([blob], file.name.replace(/\.\w+$/, '.jpg'), { type }),
  };
}

// 使用：上传前压缩
input.addEventListener('change', async () => {
  const { blob, file } = await compressImage(input.files[0]);
  console.log(`原始 ${input.files[0].size} -> 压缩后 ${blob.size}`);
  const fd = new FormData();
  fd.append('img', file ?? input.files[0]);
});
```
