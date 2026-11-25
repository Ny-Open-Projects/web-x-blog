---
title: [H5-387] 笔试：手写移动端图片压缩上传工具
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 笔试题, 文件]
type: 笔试题
---

## H5-387：笔试：手写移动端图片压缩上传工具

**答**：实现 `uploadImage(file)`：① 校验真实类型（读文件头魔数：JPEG FF D8 FF / PNG 89 50 4E 47），伪装后缀直接拒绝；② 压缩：createImageBitmap（EXIF 方向 from-image）→ 最长边缩到 1280 → JPEG quality 0.8，输出 <200KB 为目标，超过则循环降 quality（0.8→0.6→0.4，最低 0.4）；③ EXIF 修正由 imageOrientation 选项承担；④ 进度回调：压缩完成 30%、上传进度 30~100%；⑤ 上传失败重试 1 次。写出核心实现。

```javascript
async function readMagic(file) {
  const head = new Uint8Array(await file.slice(0, 8).arrayBuffer());
  if (head[0] === 0xFF && head[1] === 0xD8) return 'image/jpeg';
  if (head[0] === 0x89 && head[1] === 0x50) return 'image/png';
  return null;
}

async function uploadImage(file, { onProgress } = {}) {
  const realType = await readMagic(file);
  if (!realType) throw new Error('unsupported type');
  onProgress?.(0);

  const bmp = await createImageBitmap(file, { imageOrientation: 'from-image' });
  const scale = Math.min(1, 1280 / Math.max(bmp.width, bmp.height));
  const off = new OffscreenCanvas(bmp.width * scale, bmp.height * scale);
  off.getContext('2d').drawImage(bmp, 0, 0, off.width, off.height);
  bmp.close();

  let blob, quality = 0.8;
  do {
    blob = await off.convertToBlob({ type: 'image/jpeg', quality });
    if (blob.size <= 200 * 1024) break;
    quality -= 0.2;
  } while (quality >= 0.4);
  onProgress?.(30);

  const fd = new FormData();
  fd.append('file', blob, 'photo.jpg');
  const send = () => new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/upload');
    xhr.upload.onprogress = (e) => onProgress?.(30 + Math.round(e.loaded / e.total * 70));
    xhr.onload = () => xhr.status < 400 ? resolve(JSON.parse(xhr.responseText)) : reject(new Error(xhr.statusText));
    xhr.onerror = () => reject(new Error('network'));
    xhr.send(fd);
  });
  try { return await send(); }
  catch { return await send(); }                      // 重试 1 次
}
```

**评分点**：
- 魔数校验真实类型（JPEG/PNG 特征字节），防后缀伪装
- EXIF 方向修正 + 缩放解码一体（createImageBitmap）
- 质量循环降级逼近目标体积且有下限
- 进度分段（压缩 30% + 上传 70%）+ 上传重试
