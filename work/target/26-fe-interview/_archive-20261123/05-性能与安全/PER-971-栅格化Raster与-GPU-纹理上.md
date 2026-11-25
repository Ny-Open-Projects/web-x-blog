---
title: [PER-971] 栅格化（Raster）与 GPU 纹理上传的成本怎么控制
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-971：栅格化（Raster）与 GPU 纹理上传的成本怎么控制

**答**：
- 栅格化是把绘制记录转成位图：软件栅格（CPU 线程池）或 GPU 栅格；分辨率提升（如 DPR 3、动画中"每帧重栅格"）成本线性放大。
- 上传：栅格结果作为纹理上传 GPU，首次上传/失效重传是大层卡顿主因。
- 控制手段：减小层面积（裁剪溢出）、避免动画中触发重绘（只动 transform/opacity 不触发 Paint）、慎用大尺寸 blur/阴影（重栅格热点）。
- 验证：DevTools Layers 面板看 paint 计数与每层内存；Performance 面板找 Rasterize 段时长。

```javascript
// 大阴影触发的重绘热点检测
function shadowPaintCost(el) {
  const r = el.getBoundingClientRect();
  const s = getComputedStyle(el);
  const blur = parseFloat(s.boxShadow.match(/(\d+)px/) ? s.boxShadow.split(' ')[3] : 0) || 20;
  const area = (r.width + blur * 4) * (r.height + blur * 4);  // 模糊扩散 4 倍
  return { paintAreaKB: Math.round(area * 4 / 1024),
    advice: area > 2_000_000 ? '阴影面积过大，改用预渲染贴图或缩小 blur' : 'ok' };
}
```
