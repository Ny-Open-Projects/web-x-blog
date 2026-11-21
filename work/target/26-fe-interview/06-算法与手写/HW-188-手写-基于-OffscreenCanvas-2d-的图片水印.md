---
title: [HW-188] 手写批量图片水印——Worker 内 OffscreenCanvas 平铺水印 + 内存回收 + 批量进度
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：批量加水印（相册导出）：Worker + OffscreenCanvas（主线程零卡顿）——drawImage 原图 → 平铺绘制水印（pattern 平铺或坐标循环）→ convertToBlob 回传；ImageBitmap transfer 零拷贝 + close() 回收；批量回压（并发 2）与进度。

```javascript
// worker.js
self.onmessage = ({ data: { bitmap, wm, id } }) => {      // bitmap transfer 传入
  const canvas = new OffscreenCanvas(bitmap.width, bitmap.height);
  const ctx = canvas.getContext('2d');
  ctx.drawImage(bitmap, 0, 0);
  ctx.globalAlpha = 0.3;
  ctx.rotate(-20 * Math.PI / 180);
  ctx.font = 'bold 32px sans-serif';
  ctx.fillStyle = '#fff';
  const diag = Math.sqrt(bitmap.width ** 2 + bitmap.height ** 2);
  for (let x = -diag / 2; x < diag; x += 260)             // 旋转平铺：覆盖对角线全幅
    for (let y = -diag / 2; y < diag; y += 160) ctx.fillText(wm, x, y);
  ctx.rotate(20 * Math.PI / 180);                          // 恢复旋转（不影响后续）
  canvas.convertToBlob({ type: 'image/jpeg', quality: 0.85 })
    .then((blob) => { self.postMessage({ id, blob }); bitmap.close(); });   // 位图立即回收
};
// 主线程：回压并发 2（HW-145 同款）+ 进度 + revokeObjectURL
// 平铺水印的覆盖性：按对角线长度计算平铺范围（旋转后矩形不覆盖边角——对角线保证全幅）
```

**评分点**：
- Worker + OffscreenCanvas 主线程零卡顿；transfer 零拷贝 + bitmap.close() 回收。
- 平铺水印的对角线范围计算（旋转后覆盖全幅）。
- 回压并发 + 批量进度。
- convertToBlob 质量参数（jpeg 0.85 平衡体积）。
