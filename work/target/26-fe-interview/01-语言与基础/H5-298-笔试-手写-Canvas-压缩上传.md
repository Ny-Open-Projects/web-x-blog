---
title: [H5-298] 笔试：手写 Canvas 压缩上传
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Canvas]
type: 笔试题
---

## H5-298：笔试：手写 Canvas 压缩上传

**题目**：实现 `compressUpload(file)`：图片压缩到 2MB 以内——先降分辨率（长边 ≤1280）再降质量（0.85 起步，每次 -0.1），找第一个达标组合；输出 File 对象供表单上传。

**答**：
```javascript
async function compressUpload(file, { maxBytes = 2 * 1024 * 1024, maxSide = 1280 } = {}) {
  const bitmap = await createImageBitmap(file);
  const scale = Math.min(1, maxSide / Math.max(bitmap.width, bitmap.height));
  const c = document.createElement('canvas');
  c.width = Math.round(bitmap.width * scale);
  c.height = Math.round(bitmap.height * scale);
  c.getContext('2d').drawImage(bitmap, 0, 0, c.width, c.height);

  for (let q = 0.85; q >= 0.3; q -= 0.1) {
    const blob = await new Promise(r => c.toBlob(r, 'image/jpeg', q));
    if (blob.size <= maxBytes) {
      return new File([blob], file.name.replace(/\.\w+$/, '.jpg'), { type: 'image/jpeg' });
    }
  }
  // 最低质量仍超标：再降一半分辨率递归一次
  const half = document.createElement('canvas');
  half.width = c.width / 2; half.height = c.height / 2;
  half.getContext('2d').drawImage(c, 0, 0, half.width, half.height);
  const blob = await new Promise(r => half.toBlob(r, 'image/jpeg', 0.7));
  return new File([blob], file.name, { type: 'image/jpeg' });
}

// 用法
const compressed = await compressUpload(input.files[0]);
const fd = new FormData(); fd.append('file', compressed);
await fetch('/api/upload', { method: 'POST', body: fd });
```

**评分点**：
- 两级压缩策略：先分辨率（影响观感小、省体积多）后质量
- createImageBitmap 比 Image 加载快且支持 EXIF 方向（现代浏览器）
- File 对象保留文件名（改扩展名为 jpg）
- 兜底路径：全降级仍超标时降分辨率重试，而不是死循环
