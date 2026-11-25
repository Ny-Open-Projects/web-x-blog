---
title: [H5-076] 大图如何用 toBlob 导出？质量参数与分块策略怎么选？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-076：大图如何用 toBlob 导出？质量参数与分块策略怎么选？
**答**：
- `canvas.toBlob(cb, type, quality)`：异步、不阻塞主线程大字符串（对比 `toDataURL` 的同步 base64，大图容易卡死页面）。
- `quality` 只对 `image/jpeg`、`image/webp` 生效（0~1），对 png 无意义；jpeg 没有透明通道，导出前铺白底，否则透明区变黑。
- 大图内存爆炸对策：分块绘制到小画布再逐块导出上传（配合分片上传），或导出前 `drawImage` 缩到目标尺寸（重采样）。
- iOS Safari 对 canvas 有面积上限（约 16M 像素级别），超限绘制直接空白，导出前必须检测 `ctx.getImageData` 是否可用。
- 落地链路：`toBlob` → `URL.createObjectURL` 触发下载，或直接进 `FormData` 上传；用完记得 `revokeObjectURL`。

```html
<canvas id="export-cv" width="1200" height="800"></canvas>
<button id="save">导出 JPEG</button>

<script>
  const cv = document.getElementById('export-cv');
  const ctx = cv.getContext('2d');

  // 铺白底防透明区变黑，再画内容
  ctx.fillStyle = '#fff';
  ctx.fillRect(0, 0, cv.width, cv.height);
  ctx.fillStyle = 'teal';
  ctx.fillRect(100, 100, 400, 300);

  document.getElementById('save').addEventListener('click', () => {
    // 0.92 是画质/体积的经验平衡点；png 场景 quality 传不传都行
    cv.toBlob((blob) => {
      if (!blob) return alert('导出失败：可能超出设备 canvas 面积上限');
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `snapshot-${Date.now()}.jpg`;
      a.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000); // 及时释放
    }, 'image/jpeg', 0.92);
  });

  // 超大图分块导出：每块 1080 高，逐块切片上传
  async function exportSlices(cv, sliceH = 1080) {
    const parts = [];
    for (let y = 0; y < cv.height; y += sliceH) {
      const h = Math.min(sliceH, cv.height - y);
      const piece = document.createElement('canvas');
      piece.width = cv.width;
      piece.height = h;
      piece.getContext('2d').drawImage(cv, 0, -y);  // 平移取样
      const blob = await new Promise(r => piece.toBlob(r, 'image/jpeg', 0.9));
      parts.push(blob);
    }
    return parts;                                    // 交给分片上传逻辑
  }
</script>
```
