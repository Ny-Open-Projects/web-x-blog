---
title: [H5-325] 笔试：手写图片压缩为 Blob 并预览
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Canvas]
type: 笔试题
---

## H5-325：笔试：手写图片压缩为 Blob 并预览

**题目**：实现 `pickAndCompress(input)`：读取 input 选中的图片，压缩到长边 1080、质量 0.8，生成 Blob URL 预览（页面卸载时 revoke），返回 { blob, url, width, height }。注意内存释放与方向（EXIF）。

**答**：
```javascript
const objectUrls = new Set();
addEventListener('pagehide', () => objectUrls.forEach(u => URL.revokeObjectURL(u)));

async function pickAndCompress(input, { maxSide = 1080, quality = 0.8 } = {}) {
  const file = input.files[0];
  if (!file?.type.startsWith('image/')) throw new Error('请选择图片');

  const bitmap = await createImageBitmap(file); // 现代浏览器自动按 EXIF 方向解码
  const scale = Math.min(1, maxSide / Math.max(bitmap.width, bitmap.height));
  const w = Math.round(bitmap.width * scale), h = Math.round(bitmap.height * scale);
  const c = document.createElement('canvas');
  c.width = w; c.height = h;
  const ctx = c.getContext('2d');
  ctx.imageSmoothingQuality = 'high';
  ctx.drawImage(bitmap, 0, 0, w, h);
  bitmap.close(); // 释放解码内存

  const blob = await new Promise(r => c.toBlob(r, 'image/jpeg', quality));
  const url = URL.createObjectURL(blob);
  objectUrls.add(url); // 登记以便统一 revoke
  return { blob, url, width: w, height: h };
}
```

**评分点**：
- createImageBitmap 优先（比 Image 快，且现代浏览器按 EXIF 方向解码）
- toBlob 而非 toDataURL（Blob 内存友好，避免 base64 膨胀 33%）
- object URL 的 revoke 管理（登记 + pagehide 统一释放）——内存判分点
- bitmap.close() 显式释放解码位图
