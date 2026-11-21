---
title: [H5-276] Canvas 导出图片与压缩的质量控制
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Canvas]
type: 面试题
---

## H5-276：Canvas 导出图片与压缩的质量控制

**答**：
- 导出 API：toDataURL(type, quality)（同步、返回字符串，大图慢且占内存）与 toBlob（异步、内存友好，推荐）
- 质量-体积权衡：JPEG quality 0.7~0.85 是甜点区；PNG 适合透明与线稿，照片类用 JPEG/WebP
- 尺寸控制：导出前按目标宽高重绘到临时 canvas（双线性缩放），限制长边（如 1280px）比调 quality 更省体积
- 渐进式降级：目标体积上限（如 2MB）时循环降 quality 二分查找
- 细节：toBlob 的 MIME 决定编码器；跨域图片污染问题（同 Canvas 2D）；iOS 老版本 toBlob 偶发 bug 要兜底 toDataURL

```javascript
async function exportUnder(c, maxBytes = 2 * 1024 * 1024) {
  for (let q = 0.85; q >= 0.4; q -= 0.1) {
    const blob = await new Promise(r => c.toBlob(r, 'image/jpeg', q));
    if (blob.size <= maxBytes) return blob; // 从高往低找到第一个达标的
  }
  // 仍超标则降分辨率再试一轮
}
```
