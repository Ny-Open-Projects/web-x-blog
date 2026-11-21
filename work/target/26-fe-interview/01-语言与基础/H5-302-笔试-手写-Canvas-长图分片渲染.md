---
title: [H5-302] 笔试：手写 Canvas 长图分片渲染
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, Canvas]
type: 笔试题
---

## H5-302：笔试：手写 Canvas 长图分片渲染

**题目**：一张 20000px 高的长图（已切成 20 张 1000px 分片），实现视口内可见分片加载渲染：滚动时只 drawImage 可见区间分片，分片图片懒加载缓存，未加载完成的分片画占位。

**答**：
```javascript
function longImageViewer(canvas, baseUrl, total = 20, sliceH = 1000) {
  const ctx = canvas.getContext('2d');
  const cache = new Map(); // idx -> ImageBitmap|null(加载中)
  let offsetY = 0;

  async function loadSlice(i) {
    if (cache.has(i)) return cache.get(i);
    cache.set(i, null); // 占位标记
    const bmp = await createImageBitmap(await fetch(`${baseUrl}/slice-${i}.jpg`).then(r => r.blob()));
    cache.set(i, bmp);
    return bmp;
  }
  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const first = Math.floor(offsetY / sliceH);
    const last = Math.min(total - 1, Math.floor((offsetY + canvas.height) / sliceH));
    for (let i = first; i <= last; i++) {
      const bmp = cache.get(i);
      const y = i * sliceH - offsetY;
      if (bmp) ctx.drawImage(bmp, 0, y);
      else { loadSlice(i); ctx.fillStyle = '#f0f0f0'; ctx.fillRect(0, y, canvas.width, sliceH); }
    }
    // 清理远端缓存（保留前后 3 片），控内存
    for (const idx of cache.keys()) {
      if (idx < first - 3 || idx > last + 3) { cache.get(idx)?.close?.(); cache.delete(idx); }
    }
  }
  canvas.parentElement.addEventListener('scroll', () => { offsetY = canvas.parentElement.scrollTop; render(); }, { passive: true });
  render();
}
```

**评分点**：
- 可见区间计算：offsetY/sliceH 得首片，视口底得末片——只画可见
- 加载中的占位（null 标记防重复请求）
- LRU 式缓存清理（close() 释放 bitmap 内存）
- scroll passive + 只在滚动回调重绘
