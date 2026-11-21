---
title: [H5-306] 笔试：手写 Worker 图片解码器
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Worker]
type: 笔试题
---

## H5-306：笔试：手写 Worker 图片解码器

**题目**：主线程把图片 Blob 发给 Worker，Worker 解码后返回压缩缩略图（长边 200px）的 ImageBitmap（零拷贝）。要求 Worker 内用 createImageBitmap 完成缩放。

**答**：
```javascript
// worker.js
self.onmessage = async ({ data }) => {
  try {
    const src = await createImageBitmap(data.blob);
    const scale = Math.min(1, 200 / Math.max(src.width, src.height));
    const w = Math.round(src.width * scale), h = Math.round(src.height * scale);
    const oc = new OffscreenCanvas(w, h);
    const ctx = oc.getContext('2d');
    ctx.imageSmoothingQuality = 'high';
    ctx.drawImage(src, 0, 0, w, h);
    const thumb = await createImageBitmap(oc);          // OffscreenCanvas → ImageBitmap
    self.postMessage({ ok: true, thumb, w, h }, [thumb]); // transfer 零拷贝回传
    src.close();
  } catch (e) {
    self.postMessage({ ok: false, error: e.message });
  }
};
// main.js
const worker = new Worker('worker.js');
async function makeThumb(file) {
  return new Promise((resolve, reject) => {
    worker.onmessage = ({ data }) => data.ok ? resolve(data) : reject(new Error(data.error));
    worker.postMessage({ blob: file }); // Blob 可结构化克隆
  });
}
```

**评分点**：
- 解码缩放全在 Worker（不占主线程）——任务架构正确
- OffscreenCanvas 在 Worker 中创建并绘制
- ImageBitmap 用 transfer 列表回传（零拷贝），漏了 transfer 也能工作但丢分
- 错误信封 { ok, data|error }；src.close() 释放解码内存
