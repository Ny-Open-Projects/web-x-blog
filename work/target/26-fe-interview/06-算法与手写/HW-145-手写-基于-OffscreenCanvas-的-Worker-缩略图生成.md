---
title: [HW-145] 手写 Worker 缩略图生成——OffscreenCanvas 解码缩放 + 回压队列 + 主线程占位
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：批量图片缩略图（上传列表/相册）：解码+缩放挪 Worker（OffscreenCanvas，PER-290），主线程只挂占位与替换结果；回压队列（HW-270 模式）防 50 张图同时解码打爆 Worker 内存；失败降级（原图直出）。

```javascript
// worker.js
self.onmessage = ({ data }) => {
  const { bitmap, width, height, id } = data;             // ImageBitmap 用 transfer 传入（零拷贝）
  const canvas = new OffscreenCanvas(width, height);
  const ctx = canvas.getContext('2d');
  ctx.drawImage(bitmap, 0, 0, width, height);             // 解码后位图直接缩放（无 DOM 依赖）
  const blob = canvas.convertToBlob({ type: 'image/webp', quality: 0.8 });
  self.postMessage({ id, blob });
};
// 主线程
class ThumbGenerator {
  #pool = []; #active = 0; #max = 2;                      // 回压：同时最多 2 张解码
  constructor(onThumb) { this.onThumb = onThumb; }
  async add(file, el) {
    el.style.background = 'var(--img-placeholder)';       // 占位（防 CLS，PER-220）
    this.#pool.push({ file, el });
    this.#drain();
  }
  #drain() {
    while (this.#active < this.#max && this.#pool.length) {
      const { file, el } = this.#pool.shift();
      this.#active++;
      (async () => {
        try {
          const bitmap = await createImageBitmap(file, { resizeWidth: 200, resizeQuality: 'medium' });
          const w = 200, h = Math.round(bitmap.height * 200 / bitmap.width);
          const worker = await this.#getWorker();
          worker.onmessage = ({ data }) => {
            const url = URL.createObjectURL(data.blob);
            el.src = url; el.onload = () => URL.revokeObjectURL(url);   // 用后即弃（PER-280）
            bitmap.close();
          };
          worker.postMessage({ bitmap, width: w, height: h, id: 0 }, [bitmap]);   // transfer
        } catch {
          el.src = URL.createObjectURL(file);             // 降级：原图直出
        } finally {
          this.#active--; this.#drain();
        }
      })();
    }
  }
  #getWorker() { this.#worker ??= new Worker('thumb.worker.js'); return Promise.resolve(this.#worker); }
}
```

**评分点**：
- OffscreenCanvas + ImageBitmap transfer 零拷贝；convertToBlob 回传。
- 回压并发 2（解码是内存大户，50 张并发打爆 Worker）。
- 占位防 CLS + revokeObjectURL 用后即弃 + bitmap.close() 释放。
- 失败降级原图直出（缩略图失败不阻塞业务）。
