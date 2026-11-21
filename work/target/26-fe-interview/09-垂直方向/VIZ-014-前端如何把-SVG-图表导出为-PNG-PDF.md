---
title: [VIZ-014] 前端如何把 SVG 图表导出为 PNG/PDF？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-014：前端如何把 SVG 图表导出为 PNG/PDF？
**答**：PNG 路线：`XMLSerializer` 序列化 SVG → 包成 Blob → `Image` 加载（SVG 无跨域污染问题）→ 画到 canvas（按 DPR 放大）→ `toBlob`。PDF 路线：PNG 结果喂给 jsPDF 的 `addImage`，或走浏览器打印的"另存为 PDF"。三个坑：**字体**必须内联（style 里嵌 base64 woff2 或转 outline），**外链图片**必须转 dataURL 否则画不出来，**canvas 污染**——SVG 里如果引用了外域 image 且未 CORS 放行，toBlob 会抛 SecurityError。

```javascript
// SVG -> PNG：serialize 成 Blob -> Image -> canvas 绘制 -> toBlob
async function svgToPng(svgEl, scale = 2) {
  const xml = new XMLSerializer().serializeToString(svgEl);
  const url = URL.createObjectURL(new Blob([xml], { type: 'image/svg+xml;charset=utf-8' }));
  const img = new Image();
  await new Promise((ok, err) => { img.onload = ok; img.onerror = err; img.src = url; });
  const { width, height } = svgEl.viewBox.baseVal;
  const canvas = Object.assign(document.createElement('canvas'), {
    width: width * scale, height: height * scale,
  });
  const ctx = canvas.getContext('2d');
  ctx.scale(scale, scale); // 放大导出保证清晰
  ctx.drawImage(img, 0, 0);
  URL.revokeObjectURL(url);
  return new Promise(ok => canvas.toBlob(ok, 'image/png'));
}
// 注意：字体与外链图片需内联为 base64，否则导出缺字/缺图
// PDF：import jsPDF 后 pdf.addImage(pngDataUrl, 'PNG', 0, 0, width, height)
```

---

## 三、Canvas 深入（VIZ-015 ~ VIZ-021）
